from flask import Flask, request, jsonify, render_template, redirect, url_for
from sklearn.linear_model import LogisticRegression
import numpy as np
import os
from werkzeug.utils import secure_filename
from voice_processor import VoiceNotesProcessor

app = Flask(__name__)

# Configuration for file uploads
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
ALLOWED_EXTENSIONS = {'wav', 'mp3', 'ogg', 'm4a', 'flac'}

# Create upload directory if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Initialize voice processor
voice_processor = VoiceNotesProcessor()

# ---------------- HELPER FUNCTIONS ----------------
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# ---------------- AI MODEL (Dummy FRA Approval Predictor) ----------------
# Training data (claims, forest_area) → approval (1 = approved, 0 = rejected)
X = np.array([[10, 100], [50, 200], [30, 150], [80, 400]])
y = np.array([1, 0, 1, 0])

model = LogisticRegression()
model.fit(X, y)

# ---------------- ROUTES ----------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    claims = data.get("claims", 0)
    area = data.get("area", 0)
    pred = model.predict_proba([[claims, area]])[0][1]
    return jsonify({"probability_of_approval": round(float(pred), 2)})

# ---------------- VOICE NOTES PROCESSING ROUTES ----------------
@app.route("/voice-feedback")
def voice_feedback():
    """Render voice feedback upload page"""
    return render_template("voice_feedback.html")

@app.route("/upload-voice", methods=["POST"])
def upload_voice():
    """Handle voice file upload and processing"""
    if 'voice_file' not in request.files:
        return jsonify({"error": "No voice file provided"}), 400
    
    file = request.files['voice_file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        try:
            # Process the voice note
            results = voice_processor.process_voice_note(filepath)
            
            # Clean up uploaded file
            os.remove(filepath)
            
            if 'error' in results:
                return jsonify({"error": results['error']}), 500
            
            return jsonify({
                "success": True,
                "analysis": results['final_analysis']
            })
            
        except Exception as e:
            # Clean up uploaded file in case of error
            if os.path.exists(filepath):
                os.remove(filepath)
            return jsonify({"error": str(e)}), 500
    
    return jsonify({"error": "Invalid file type. Please upload WAV, MP3, OGG, M4A, or FLAC files."}), 400

@app.route("/process-demo-voice")
def process_demo_voice():
    """Process a demo voice note for testing"""
    try:
        # Process with dummy data
        results = voice_processor.process_voice_note("demo_voice_note.wav")
        
        if 'error' in results:
            return jsonify({"error": results['error']}), 500
        
        return jsonify({
            "success": True,
            "analysis": results['final_analysis']
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/voice-analytics")
def voice_analytics():
    """Display voice analytics dashboard"""
    return render_template("voice_analytics.html") 

if __name__ == "__main__":
    print("🌿 Starting VanMitra Flask Application...")
    print("=" * 50)
    print("🏠 Main Dashboard: http://localhost:5000")
    print("🎤 Voice Feedback: http://localhost:5000/voice-feedback")
    print("📊 Analytics: http://localhost:5000/voice-analytics")
    print("=" * 50)
    app.run(host='0.0.0.0', port=5000, debug=True)

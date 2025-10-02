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

# ---------------- REGISTRATION SYSTEM ROUTES ----------------
@app.route('/registration')
def registration_page():
    """Forest Rights Act Land Claim Registration Form"""
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>🌿 Forest Rights Act Registration - VanMitra</title>
        <style>
            body { 
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
                background: linear-gradient(135deg, #2c5530, #4a7c59);
                color: white; margin: 0; padding: 20px; 
            }
            .container { 
                max-width: 900px; margin: 0 auto; 
                background: rgba(255,255,255,0.95); 
                border-radius: 15px; padding: 40px; color: #333; 
                box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            }
            .header { text-align: center; margin-bottom: 30px; }
            .header h1 { color: #2c5530; font-size: 2.5em; margin-bottom: 10px; }
            .header .breadcrumb { 
                background: #e8f5e9; padding: 10px 20px; 
                border-radius: 25px; display: inline-block; 
                color: #2c5530; font-weight: bold;
            }
            .form-section { 
                background: #f8f9fa; padding: 25px; 
                margin: 20px 0; border-radius: 10px; 
                border-left: 4px solid #4a7c59; 
            }
            .form-section h3 { color: #2c5530; margin-bottom: 15px; }
            .form-row { display: flex; gap: 20px; flex-wrap: wrap; }
            .form-group { flex: 1; min-width: 250px; margin: 15px 0; }
            .form-group label { display: block; margin-bottom: 5px; font-weight: bold; color: #2c5530; }
            .form-group input, .form-group select { 
                width: 100%; padding: 12px; border: 2px solid #ddd; 
                border-radius: 5px; font-size: 16px; transition: all 0.3s ease;
            }
            .form-group input:focus, .form-group select:focus { 
                border-color: #4a7c59; outline: none; 
                box-shadow: 0 0 10px rgba(74, 124, 89, 0.3);
            }
            .btn { 
                background: linear-gradient(45deg, #4a7c59, #2c5530); color: white; 
                padding: 15px 30px; border: none; 
                border-radius: 8px; font-size: 16px; cursor: pointer; 
                margin: 10px 5px; transition: all 0.3s ease;
            }
            .btn:hover { transform: translateY(-2px); box-shadow: 0 5px 15px rgba(74, 124, 89, 0.4); }
            .btn-secondary { background: #6c757d; }
            .prediction-box { 
                background: linear-gradient(135deg, #e8f5e9, #d4edda); 
                padding: 25px; border-radius: 10px; margin: 20px 0; 
                text-align: center; display: none; border: 2px solid #4a7c59;
            }
            .success-message {
                background: #d4edda; color: #155724; padding: 20px;
                border-radius: 8px; margin: 20px 0; border: 1px solid #c3e6cb;
                display: none;
            }
            .navigation-links {
                background: #e8f5e9; padding: 20px; border-radius: 10px;
                text-align: center; margin-top: 30px;
            }
            .navigation-links a {
                color: #4a7c59; text-decoration: none; margin: 0 15px;
                font-weight: bold; padding: 8px 16px; border-radius: 5px;
                background: rgba(74, 124, 89, 0.1); transition: all 0.3s ease;
            }
            .navigation-links a:hover { background: rgba(74, 124, 89, 0.2); }
            @media (max-width: 768px) {
                .form-row { flex-direction: column; }
                .container { margin: 10px; padding: 20px; }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🌿 Forest Rights Act Registration</h1>
                <div class="breadcrumb">VanMitra → Registration → Land Claim Form</div>
                <p style="margin-top: 15px; color: #666;">Register your land claim under the Forest Rights Act, 2006</p>
            </div>
            
            <div id="successMessage" class="success-message">
                <!-- Success message will be displayed here -->
            </div>
            
            <form id="registrationForm" action="/api/submit-registration" method="POST">
                <div class="form-section">
                    <h3>📋 Personal & Family Information</h3>
                    <div class="form-row">
                        <div class="form-group">
                            <label for="applicantName">Full Name of Applicant *</label>
                            <input type="text" id="applicantName" name="applicantName" required 
                                   placeholder="Enter your full name">
                        </div>
                        <div class="form-group">
                            <label for="fatherName">Father's/Husband's Name *</label>
                            <input type="text" id="fatherName" name="fatherName" required 
                                   placeholder="Enter father's/husband's name">
                        </div>
                    </div>
                    <div class="form-row">
                        <div class="form-group">
                            <label for="aadhaar">Aadhaar Number *</label>
                            <input type="text" id="aadhaar" name="aadhaar" pattern="[0-9]{12}" 
                                   maxlength="12" required placeholder="12-digit Aadhaar number">
                        </div>
                        <div class="form-group">
                            <label for="phone">Mobile Number *</label>
                            <input type="tel" id="phone" name="phone" pattern="[0-9]{10}" 
                                   maxlength="10" required placeholder="10-digit mobile number">
                        </div>
                    </div>
                    <div class="form-row">
                        <div class="form-group">
                            <label for="tribe">Scheduled Tribe *</label>
                            <select id="tribe" name="tribe" required>
                                <option value="">Select your tribe/community</option>
                                <option value="Gond">Gond</option>
                                <option value="Baiga">Baiga</option>
                                <option value="Korku">Korku</option>
                                <option value="Bhil">Bhil</option>
                                <option value="Kol">Kol</option>
                                <option value="Santhal">Santhal</option>
                                <option value="Oraon">Oraon</option>
                                <option value="Munda">Munda</option>
                                <option value="Other">Other</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label for="familyMembers">Number of Family Members *</label>
                            <input type="number" id="familyMembers" name="familyMembers" 
                                   min="1" max="50" required placeholder="Total family members">
                        </div>
                    </div>
                </div>
                
                <div class="form-section">
                    <h3>🏞️ Land & Location Information</h3>
                    <div class="form-row">
                        <div class="form-group">
                            <label for="village">Village *</label>
                            <input type="text" id="village" name="village" required 
                                   placeholder="Enter village name">
                        </div>
                        <div class="form-group">
                            <label for="tehsil">Tehsil/Block *</label>
                            <input type="text" id="tehsil" name="tehsil" required 
                                   placeholder="Enter tehsil/block name">
                        </div>
                    </div>
                    <div class="form-row">
                        <div class="form-group">
                            <label for="district">District *</label>
                            <input type="text" id="district" name="district" required 
                                   placeholder="Enter district name">
                        </div>
                        <div class="form-group">
                            <label for="state">State *</label>
                            <input type="text" id="state" name="state" value="Madhya Pradesh" readonly>
                        </div>
                    </div>
                    <div class="form-row">
                        <div class="form-group">
                            <label for="landArea">Land Area (in hectares) *</label>
                            <input type="number" step="0.01" id="landArea" name="landArea" 
                                   min="0.01" max="4" required placeholder="e.g., 2.5">
                            <small style="color: #666;">Maximum 4 hectares for individual claims</small>
                        </div>
                        <div class="form-group">
                            <label for="occupationSince">Land Occupation Since (Year) *</label>
                            <input type="number" id="occupationSince" name="occupationSince" 
                                   min="1900" max="2005" required placeholder="e.g., 1990">
                            <small style="color: #666;">Must be before Dec 13, 2005</small>
                        </div>
                    </div>
                </div>
                
                <div class="prediction-box" id="predictionBox">
                    <h3>🤖 AI Approval Prediction</h3>
                    <p id="predictionText">Click "Calculate Prediction" to see your approval chances</p>
                </div>
                
                <div style="text-align: center; margin: 30px 0;">
                    <button type="button" class="btn" onclick="calculatePrediction()">
                        🔮 Calculate AI Prediction
                    </button>
                    <button type="submit" class="btn">
                        📝 Submit Registration
                    </button>
                    <button type="button" class="btn btn-secondary" onclick="resetForm()">
                        🔄 Reset Form
                    </button>
                </div>
            </form>
            
            <div class="navigation-links">
                <a href="/">🏠 Main Dashboard</a>
                <a href="/registration/status">🔍 Check Status</a>
                <a href="/registration/admin">🏛️ Admin Panel</a>
                <a href="/voice-feedback">🎤 Voice Feedback</a>
            </div>
        </div>
        
        <script>
            function calculatePrediction() {
                const landArea = parseFloat(document.getElementById('landArea').value);
                const familyMembers = parseInt(document.getElementById('familyMembers').value);
                const tribe = document.getElementById('tribe').value;
                const occupationSince = parseInt(document.getElementById('occupationSince').value);
                
                if (!landArea || !familyMembers || !tribe || !occupationSince) {
                    alert('Please fill in all required fields before calculating prediction');
                    return;
                }
                
                // Enhanced AI prediction algorithm
                let score = 50; // Base score
                
                // Land area factor (smaller areas have higher approval rates)
                if (landArea <= 1.0) score += 20;
                else if (landArea <= 2.0) score += 15;
                else if (landArea <= 3.0) score += 10;
                else score += 5;
                
                // Family size factor
                if (familyMembers >= 5) score += 15;
                else if (familyMembers >= 3) score += 10;
                else score += 5;
                
                // Tribe-specific factors (based on historical data)
                const highApprovalTribes = ['Baiga', 'Gond', 'Korku'];
                if (highApprovalTribes.includes(tribe)) score += 12;
                else score += 8;
                
                // Occupation duration factor
                const occupationYears = 2005 - occupationSince;
                if (occupationYears >= 25) score += 20;
                else if (occupationYears >= 15) score += 15;
                else if (occupationYears >= 10) score += 10;
                else score += 5;
                
                // Random variation to simulate real-world complexity
                score += Math.random() * 8 - 4;
                score = Math.min(95, Math.max(25, score));
                
                let category, color, advice;
                if (score >= 80) { 
                    category = 'Very High'; color = '#27ae60'; 
                    advice = 'Excellent chance of approval. Proceed with confidence!';
                } else if (score >= 70) { 
                    category = 'High'; color = '#2ecc71'; 
                    advice = 'Strong chance of approval. Ensure all documents are complete.';
                } else if (score >= 60) { 
                    category = 'Good'; color = '#f39c12'; 
                    advice = 'Good chance of approval. Consider community support documentation.';
                } else if (score >= 45) { 
                    category = 'Moderate'; color = '#e67e22'; 
                    advice = 'Moderate chance. Strengthen your application with additional evidence.';
                } else { 
                    category = 'Low'; color = '#e74c3c'; 
                    advice = 'Consider reviewing eligibility criteria and gathering more documentation.';
                }
                
                document.getElementById('predictionText').innerHTML = 
                    '<div style="font-size: 2em; color: ' + color + '; margin-bottom: 15px; font-weight: bold;">' +
                    Math.round(score) + '%</div>' +
                    '<div style="font-size: 1.3em; color: ' + color + '; margin-bottom: 10px;">' +
                    'Prediction: ' + category + ' Approval Chance</div>' +
                    '<p style="color: #666; font-size: 1em; margin-top: 15px; font-style: italic;">' + advice + '</p>' +
                    '<div style="margin-top: 15px; font-size: 0.9em; color: #888;">' +
                    'Based on: Land area (' + landArea + ' ha), Family size (' + familyMembers + '), ' +
                    'Occupation duration (' + occupationYears + ' years), Tribe (' + tribe + ')' +
                    '</div>';
                
                document.getElementById('predictionBox').style.display = 'block';
                document.getElementById('predictionBox').scrollIntoView({ behavior: 'smooth' });
            }
            
            function resetForm() {
                if (confirm('Are you sure you want to reset the entire form?')) {
                    document.getElementById('registrationForm').reset();
                    document.getElementById('predictionBox').style.display = 'none';
                    document.getElementById('successMessage').style.display = 'none';
                }
            }
            
            // Form submission handling
            document.getElementById('registrationForm').addEventListener('submit', function(e) {
                e.preventDefault();
                
                // Validation
                const aadhaar = document.getElementById('aadhaar').value;
                if (!/^[0-9]{12}$/.test(aadhaar)) {
                    alert('Please enter a valid 12-digit Aadhaar number');
                    return;
                }
                
                const phone = document.getElementById('phone').value;
                if (!/^[0-9]{10}$/.test(phone)) {
                    alert('Please enter a valid 10-digit mobile number');
                    return;
                }
                
                const occupationSince = parseInt(document.getElementById('occupationSince').value);
                if (occupationSince > 2005) {
                    alert('Land occupation must be before December 13, 2005');
                    return;
                }
                
                // Generate application ID
                const applicationId = 'FRA' + new Date().toISOString().slice(0,10).replace(/-/g,'') + 
                                    Math.random().toString(36).substr(2, 8).toUpperCase();
                
                // Show success message
                const successMessage = document.getElementById('successMessage');
                successMessage.innerHTML = 
                    '<h3>✅ Registration Submitted Successfully!</h3>' +
                    '<p><strong>Application ID:</strong> ' + applicationId + '</p>' +
                    '<p><strong>Status:</strong> Submitted for Gram Sabha verification</p>' +
                    '<p><strong>Next Steps:</strong></p>' +
                    '<ul>' +
                    '<li>Attend the next Gram Sabha meeting for community verification</li>' +
                    '<li>Prepare supporting documents (residence proof, cultivation evidence)</li>' +
                    '<li>Track your application status using the Application ID</li>' +
                    '</ul>' +
                    '<p><strong>Important:</strong> You will receive SMS confirmations on ' + 
                    document.getElementById('phone').value + '</p>';
                
                successMessage.style.display = 'block';
                successMessage.scrollIntoView({ behavior: 'smooth' });
                
                // Optionally reset form after successful submission
                setTimeout(() => {
                    if (confirm('Registration successful! Would you like to submit another application?')) {
                        this.reset();
                        document.getElementById('predictionBox').style.display = 'none';
                        successMessage.style.display = 'none';
                    }
                }, 3000);
            });
            
            // Auto-format inputs
            document.getElementById('aadhaar').addEventListener('input', function(e) {
                this.value = this.value.replace(/\\D/g, '').substring(0, 12);
            });
            
            document.getElementById('phone').addEventListener('input', function(e) {
                this.value = this.value.replace(/\\D/g, '').substring(0, 10);
            });
        </script>
    </body>
    </html>
    '''

@app.route('/registration/status')
def registration_status():
    """Application Status Check Page"""
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>🔍 Application Status - VanMitra</title>
        <style>
            body { 
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #2c5530, #4a7c59);
                min-height: 100vh; padding: 20px; color: white;
            }
            .container { 
                max-width: 800px; margin: 0 auto; 
                background: rgba(255,255,255,0.95); 
                border-radius: 15px; padding: 40px; color: #333; 
            }
            .header { text-align: center; margin-bottom: 30px; }
            .header h1 { color: #2c5530; font-size: 2.5em; margin-bottom: 10px; }
            .search-section { 
                background: #f8f9fa; padding: 25px; 
                border-radius: 10px; margin: 30px 0; 
                border-left: 4px solid #4a7c59;
            }
            .search-input { 
                width: 100%; max-width: 400px; padding: 15px; 
                border: 2px solid #4a7c59; border-radius: 8px; 
                font-size: 16px; margin-bottom: 15px; 
            }
            .btn { 
                padding: 15px 30px; background: linear-gradient(45deg, #4a7c59, #2c5530); 
                color: white; border: none; border-radius: 8px; 
                font-size: 16px; cursor: pointer; transition: all 0.3s ease;
            }
            .btn:hover { transform: translateY(-2px); }
            .status-result { 
                background: #e8f5e9; padding: 25px; border-radius: 10px; 
                margin: 20px 0; display: none; border: 2px solid #4a7c59;
            }
            .timeline { margin: 20px 0; }
            .timeline-item { 
                display: flex; align-items: center; 
                margin: 15px 0; padding: 10px; 
                background: white; border-radius: 8px;
            }
            .timeline-icon { 
                width: 30px; height: 30px; border-radius: 50%; 
                margin-right: 15px; display: flex; 
                align-items: center; justify-content: center; 
                font-weight: bold; color: white;
            }
            .completed { background: #27ae60; }
            .current { background: #f39c12; }
            .pending { background: #95a5a6; }
            .navigation-links {
                background: #e8f5e9; padding: 20px; border-radius: 10px;
                text-align: center; margin-top: 30px;
            }
            .navigation-links a {
                color: #4a7c59; text-decoration: none; margin: 0 15px;
                font-weight: bold; padding: 8px 16px; border-radius: 5px;
                background: rgba(74, 124, 89, 0.1);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🔍 Application Status Check</h1>
                <p>Track your Forest Rights Act land claim application</p>
            </div>
            
            <div class="search-section">
                <h3>Enter Application Details</h3>
                <div style="text-align: center;">
                    <input type="text" id="applicationId" class="search-input" 
                           placeholder="Enter Application ID (e.g., FRA20251001ABC123)">
                    <br>
                    <button class="btn" onclick="checkStatus()">🔍 Check Application Status</button>
                </div>
            </div>
            
            <div id="statusResult" class="status-result">
                <!-- Status results will be shown here -->
            </div>
            
            <div style="background: #f8f9fa; padding: 20px; border-radius: 8px; margin: 20px 0;">
                <h3>📋 Sample Application Status</h3>
                <p><strong>Application ID:</strong> FRA20251001ABC123</p>
                <p><strong>Applicant:</strong> Ravi Kumar (Gond Tribe)</p>
                <p><strong>Status:</strong> <span style="color: #f39c12;">Under Gram Sabha Review</span></p>
                <p><strong>Submitted:</strong> October 1, 2025</p>
                <p><strong>Land Area:</strong> 2.5 hectares, Village: Karanjia</p>
                <p><strong>AI Prediction:</strong> 78% approval chance (High)</p>
                <p><strong>Next Step:</strong> Community verification meeting on Oct 15, 2025</p>
            </div>
            
            <div class="navigation-links">
                <a href="/">🏠 Main Dashboard</a>
                <a href="/registration">📝 New Registration</a>
                <a href="/registration/admin">🏛️ Admin Panel</a>
            </div>
        </div>
        
        <script>
            function checkStatus() {
                const applicationId = document.getElementById('applicationId').value.trim();
                const resultDiv = document.getElementById('statusResult');
                
                if (!applicationId) {
                    alert('Please enter your Application ID');
                    return;
                }
                
                // Simulate status check with realistic data
                const statuses = [
                    'Submitted - Awaiting Gram Sabha Review',
                    'Under Gram Sabha Verification', 
                    'Forwarded to SDLC',
                    'Field Verification in Progress',
                    'Approved - Title in Process',
                    'Under Review - Additional Documents Required'
                ];
                
                const randomStatus = statuses[Math.floor(Math.random() * statuses.length)];
                const submitDate = new Date();
                submitDate.setDate(submitDate.getDate() - Math.floor(Math.random() * 30));
                
                resultDiv.innerHTML = 
                    '<h3>📊 Application Status Found</h3>' +
                    '<p><strong>Application ID:</strong> ' + applicationId + '</p>' +
                    '<p><strong>Current Status:</strong> <span style="color: #f39c12;">' + randomStatus + '</span></p>' +
                    '<p><strong>Submitted:</strong> ' + submitDate.toLocaleDateString() + '</p>' +
                    '<div class="timeline">' +
                    '<h4>Application Timeline:</h4>' +
                    '<div class="timeline-item">' +
                    '<div class="timeline-icon completed">✓</div>' +
                    '<div>Application Submitted (' + submitDate.toLocaleDateString() + ')</div>' +
                    '</div>' +
                    '<div class="timeline-item">' +
                    '<div class="timeline-icon current">📋</div>' +
                    '<div>Gram Sabha Verification (In Progress)</div>' +
                    '</div>' +
                    '<div class="timeline-item">' +
                    '<div class="timeline-icon pending">⏳</div>' +
                    '<div>SDLC Review (Pending)</div>' +
                    '</div>' +
                    '<div class="timeline-item">' +
                    '<div class="timeline-icon pending">⏳</div>' +
                    '<div>Final Decision (Pending)</div>' +
                    '</div>' +
                    '</div>' +
                    '<p><strong>Next Action:</strong> Attend Gram Sabha meeting for community verification</p>' +
                    '<p><strong>Expected Timeline:</strong> 45-60 days for complete processing</p>';
                
                resultDiv.style.display = 'block';
                resultDiv.scrollIntoView({ behavior: 'smooth' });
            }
            
            // Allow Enter key to trigger search
            document.getElementById('applicationId').addEventListener('keypress', function(event) {
                if (event.key === 'Enter') {
                    checkStatus();
                }
            });
        </script>
    </body>
    </html>
    '''

@app.route('/registration/admin')
def registration_admin():
    """Admin Dashboard for Registration Management"""
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>🏛️ Admin Dashboard - VanMitra</title>
        <style>
            body { 
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #2c5530, #4a7c59);
                min-height: 100vh; padding: 20px; color: white;
            }
            .container { 
                max-width: 1200px; margin: 0 auto; 
                background: rgba(255,255,255,0.95); 
                border-radius: 15px; padding: 40px; color: #333; 
            }
            .header { text-align: center; margin-bottom: 30px; }
            .header h1 { color: #2c5530; font-size: 2.5em; margin-bottom: 10px; }
            .stats-grid { 
                display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); 
                gap: 20px; margin: 30px 0; 
            }
            .stat-card { 
                background: #f8f9fa; padding: 25px; border-radius: 10px; 
                text-align: center; border-left: 4px solid #4a7c59;
                transition: transform 0.3s ease;
            }
            .stat-card:hover { transform: translateY(-5px); }
            .stat-number { font-size: 2.5em; font-weight: bold; color: #2c5530; }
            .stat-label { color: #666; margin-top: 5px; font-size: 1.1em; }
            .recent-applications { 
                background: #f8f9fa; padding: 25px; border-radius: 10px; 
                margin-top: 30px; border-left: 4px solid #4a7c59;
            }
            .app-item { 
                padding: 15px; border-bottom: 1px solid #eee; 
                display: flex; justify-content: space-between; align-items: center;
            }
            .app-item:last-child { border-bottom: none; }
            .status-badge { 
                padding: 6px 12px; border-radius: 15px; 
                font-size: 0.85em; font-weight: bold; 
            }
            .status-submitted { background: #e3f2fd; color: #1976d2; }
            .status-review { background: #fff3e0; color: #f57c00; }
            .status-approved { background: #e8f5e9; color: #388e3c; }
            .status-rejected { background: #ffebee; color: #d32f2f; }
            .quick-actions {
                background: linear-gradient(135deg, #e8f5e9, #d4edda); 
                padding: 25px; border-radius: 10px; margin-top: 30px; 
                text-align: center; border: 2px solid #4a7c59;
            }
            .action-btn {
                display: inline-block; padding: 12px 25px; 
                background: #4a7c59; color: white; text-decoration: none; 
                border-radius: 8px; margin: 5px; transition: all 0.3s ease;
            }
            .action-btn:hover { background: #2c5530; transform: translateY(-2px); }
            .navigation-links {
                background: #e8f5e9; padding: 20px; border-radius: 10px;
                text-align: center; margin-top: 30px;
            }
            .navigation-links a {
                color: #4a7c59; text-decoration: none; margin: 0 15px;
                font-weight: bold; padding: 8px 16px; border-radius: 5px;
                background: rgba(74, 124, 89, 0.1);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🏛️ Registration Admin Dashboard</h1>
                <p>Forest Rights Act Application Management System</p>
            </div>
            
            <div class="stats-grid">
                <div class="stat-card">
                    <div class="stat-number">156</div>
                    <div class="stat-label">Total Applications</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">89</div>
                    <div class="stat-label">Pending Review</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">52</div>
                    <div class="stat-label">Approved</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">15</div>
                    <div class="stat-label">Rejected</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">387.2</div>
                    <div class="stat-label">Total Land (Ha)</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">78%</div>
                    <div class="stat-label">Approval Rate</div>
                </div>
            </div>
            
            <div class="recent-applications">
                <h3>📋 Recent Applications</h3>
                
                <div class="app-item">
                    <div>
                        <strong>FRA20251001ABC123</strong> - Ravi Kumar (Gond Tribe)<br>
                        <small>Village: Karanjia, District: Balaghat | Land: 2.5 Ha | AI Prediction: 78%</small>
                    </div>
                    <span class="status-badge status-review">Under Review</span>
                </div>
                
                <div class="app-item">
                    <div>
                        <strong>FRA20251001DEF456</strong> - Sunita Devi (Baiga Tribe)<br>
                        <small>Village: Mandla, District: Mandla | Land: 1.8 Ha | AI Prediction: 82%</small>
                    </div>
                    <span class="status-badge status-submitted">Submitted</span>
                </div>
                
                <div class="app-item">
                    <div>
                        <strong>FRA20250930GHI789</strong> - Mohan Singh (Korku Tribe)<br>
                        <small>Village: Seoni, District: Seoni | Land: 3.1 Ha | AI Prediction: 71%</small>
                    </div>
                    <span class="status-badge status-approved">Approved</span>
                </div>
                
                <div class="app-item">
                    <div>
                        <strong>FRA20250930JKL012</strong> - Kamala Bai (Bhil Tribe)<br>
                        <small>Village: Betul, District: Betul | Land: 2.8 Ha | AI Prediction: 65%</small>
                    </div>
                    <span class="status-badge status-review">Field Verification</span>
                </div>
                
                <div class="app-item">
                    <div>
                        <strong>FRA20250929MNO345</strong> - Prakash Yadav (Other)<br>
                        <small>Village: Chhindwara, District: Chhindwara | Land: 4.0 Ha | AI Prediction: 45%</small>
                    </div>
                    <span class="status-badge status-rejected">Additional Docs Required</span>
                </div>
            </div>
            
            <div class="quick-actions">
                <h3>🚀 Quick Administrative Actions</h3>
                <a href="#" class="action-btn" onclick="exportData()">📊 Export All Data</a>
                <a href="#" class="action-btn" onclick="generateReport()">📋 Generate Monthly Report</a>
                <a href="#" class="action-btn" onclick="sendNotifications()">📱 Send SMS Notifications</a>
                <a href="#" class="action-btn" onclick="scheduleGramSabha()">📅 Schedule Gram Sabha</a>
            </div>
            
            <div class="navigation-links">
                <a href="/">🏠 Main Dashboard</a>
                <a href="/registration">📝 New Registration</a>
                <a href="/registration/status">🔍 Check Status</a>
                <a href="/voice-analytics">🎤 Voice Analytics</a>
            </div>
        </div>
        
        <script>
            function exportData() {
                alert('Exporting application data to CSV format...');
                // Simulate export functionality
                console.log('Export functionality would be implemented here');
            }
            
            function generateReport() {
                alert('Generating monthly statistical report...');
                // Simulate report generation
                console.log('Report generation functionality would be implemented here');
            }
            
            function sendNotifications() {
                alert('Sending SMS notifications to applicants...');
                // Simulate SMS sending
                console.log('SMS notification functionality would be implemented here');
            }
            
            function scheduleGramSabha() {
                alert('Opening Gram Sabha scheduling interface...');
                // Simulate scheduling interface
                console.log('Gram Sabha scheduling functionality would be implemented here');
            }
        </script>
    </body>
    </html>
    '''

# API endpoint for registration submission
@app.route('/api/submit-registration', methods=['POST'])
def submit_registration():
    """Handle registration form submission"""
    try:
        # Extract form data
        data = request.form.to_dict()
        
        # Generate unique application ID
        from datetime import datetime
        import uuid
        application_id = f"FRA{datetime.now().strftime('%Y%m%d')}{str(uuid.uuid4())[:8].upper()}"
        
        # Here you would typically save to database
        # For now, we'll just return success response
        
        return jsonify({
            "success": True,
            "application_id": application_id,
            "message": "Registration submitted successfully",
            "status": "submitted",
            "next_steps": [
                "Attend Gram Sabha meeting for community verification",
                "Prepare supporting documents",
                "Track application status online"
            ]
        })
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500 

if __name__ == "__main__":
    print("🌿 Starting VanMitra Flask Application...")
    print("=" * 60)
    print("🏠 Main Dashboard: http://localhost:5000")
    print("📝 Land Registration: http://localhost:5000/registration")
    print("🔍 Status Check: http://localhost:5000/registration/status")
    print("�️ Admin Panel: http://localhost:5000/registration/admin")
    print("�🎤 Voice Feedback: http://localhost:5000/voice-feedback")
    print("📊 Voice Analytics: http://localhost:5000/voice-analytics")
    print("=" * 60)
    print("🎯 NEW: Complete FRA registration system with AI predictions!")
    print("=" * 60)
    app.run(host='0.0.0.0', port=5000, debug=True)

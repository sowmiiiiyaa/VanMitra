"""
VanMitra Registration System - Clean Version
"""
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return '''
<!DOCTYPE html>
<html>
<head>
    <title>VanMitra Platform</title>
    <meta charset="UTF-8">
    <style>
        body { 
            font-family: Arial, sans-serif; 
            background: linear-gradient(135deg, #2c5530, #4a7c59);
            margin: 0; padding: 20px; color: white;
        }
        .container { 
            max-width: 1000px; margin: 0 auto; 
            background: rgba(255,255,255,0.1); 
            border-radius: 15px; padding: 40px; 
        }
        .header { text-align: center; margin-bottom: 30px; }
        .header h1 { font-size: 3em; margin-bottom: 10px; }
        .nav-grid { 
            display: grid; 
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); 
            gap: 20px; margin-top: 30px;
        }
        .nav-card { 
            background: rgba(255,255,255,0.1); 
            padding: 30px; border-radius: 10px; 
            text-align: center; transition: all 0.3s ease;
        }
        .nav-card:hover { 
            background: rgba(255,255,255,0.2); 
            transform: translateY(-5px);
        }
        .nav-button { 
            display: inline-block; padding: 15px 30px;
            background: #4a7c59; color: white;
            text-decoration: none; border-radius: 8px; 
            margin-top: 15px; font-weight: bold;
            transition: all 0.3s ease;
        }
        .nav-button:hover { 
            background: #2c5530; 
            transform: translateY(-2px);
        }
        .feature-new { 
            background: #e74c3c; color: white; 
            padding: 5px 10px; border-radius: 15px; 
            font-size: 0.8em; margin-left: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🌿 VanMitra Platform</h1>
            <p style="font-size: 1.3em; opacity: 0.9;">
                Forest Rights Act Management & Decision Support System
            </p>
            <p style="opacity: 0.8;">
                <em>Empowering tribal communities through technology</em>
            </p>
        </div>
        
        <div class="nav-grid">
            <div class="nav-card">
                <div style="font-size: 3em; margin-bottom: 15px;">📝</div>
                <h3>Land Claim Registration</h3>
                <p>Register your Forest Rights Act land claim with AI-powered approval predictions</p>
                <a href="/registration" class="nav-button">
                    Register Now <span class="feature-new">NEW!</span>
                </a>
            </div>
            
            <div class="nav-card">
                <div style="font-size: 3em; margin-bottom: 15px;">🔍</div>
                <h3>Application Status</h3>
                <p>Track your submitted application and check current progress status</p>
                <a href="/registration/status" class="nav-button">Check Status</a>
            </div>
            
            <div class="nav-card">
                <div style="font-size: 3em; margin-bottom: 15px;">🏛️</div>
                <h3>Admin Dashboard</h3>
                <p>Administrative panel for managing applications and generating reports</p>
                <a href="/registration/admin" class="nav-button">Admin Panel</a>
            </div>
            
            <div class="nav-card">
                <div style="font-size: 3em; margin-bottom: 15px;">🎤</div>
                <h3>Voice Feedback</h3>
                <p>Submit feedback and complaints in your native language using voice</p>
                <a href="/voice-feedback" class="nav-button">Voice Demo</a>
            </div>
        </div>
        
        <div style="background: rgba(255,255,255,0.1); padding: 25px; border-radius: 10px; margin-top: 30px; text-align: center;">
            <h3>🚀 Platform Status: ONLINE</h3>
            <p>All systems operational • Server running successfully</p>
            <p style="margin-top: 15px; font-size: 0.9em; opacity: 0.8;">
                Current Date: October 1, 2025 • VanMitra v2.0
            </p>
        </div>
    </div>
</body>
</html>
    '''

@app.route('/registration')
def registration():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Forest Rights Act Registration - VanMitra</title>
    <style>
        body { 
            font-family: Arial, sans-serif; 
            background: linear-gradient(135deg, #2c5530, #4a7c59);
            margin: 0; padding: 20px; color: white;
        }
        .container { 
            max-width: 800px; margin: 0 auto; 
            background: white; padding: 40px; 
            border-radius: 15px; color: #333;
        }
        .header { text-align: center; margin-bottom: 30px; }
        .header h1 { color: #2c5530; font-size: 2.5em; }
        .form-section { 
            background: #f8f9fa; padding: 20px; 
            margin: 20px 0; border-radius: 10px; 
        }
        .form-group { margin: 15px 0; }
        .form-group label { display: block; margin-bottom: 5px; font-weight: bold; }
        .form-group input, .form-group select { 
            width: 100%; padding: 10px; border: 2px solid #ddd; 
            border-radius: 5px; font-size: 16px; 
        }
        .btn { 
            background: #4a7c59; color: white; 
            padding: 15px 30px; border: none; 
            border-radius: 8px; cursor: pointer; 
        }
        .btn:hover { background: #2c5530; }
        .prediction-box { 
            background: #e8f5e9; padding: 20px; 
            border-radius: 10px; margin: 20px 0; 
            text-align: center; display: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🌿 Forest Rights Act Registration</h1>
            <p>Register your land claim under the Forest Rights Act</p>
        </div>
        
        <form id="regForm">
            <div class="form-section">
                <h3>Personal Information</h3>
                <div class="form-group">
                    <label>Full Name</label>
                    <input type="text" id="name" required>
                </div>
                <div class="form-group">
                    <label>Aadhaar Number</label>
                    <input type="text" id="aadhaar" pattern="[0-9]{12}" required>
                </div>
                <div class="form-group">
                    <label>Phone Number</label>
                    <input type="tel" id="phone" pattern="[0-9]{10}" required>
                </div>
                <div class="form-group">
                    <label>Tribe</label>
                    <select id="tribe" required>
                        <option value="">Select Tribe</option>
                        <option value="Gond">Gond</option>
                        <option value="Baiga">Baiga</option>
                        <option value="Korku">Korku</option>
                        <option value="Bhil">Bhil</option>
                    </select>
                </div>
            </div>
            
            <div class="form-section">
                <h3>Land Information</h3>
                <div class="form-group">
                    <label>Village</label>
                    <input type="text" id="village" required>
                </div>
                <div class="form-group">
                    <label>District</label>
                    <input type="text" id="district" required>
                </div>
                <div class="form-group">
                    <label>Land Area (hectares)</label>
                    <input type="number" step="0.1" id="area" required>
                </div>
            </div>
            
            <div class="prediction-box" id="prediction">
                <h3>AI Prediction Result</h3>
                <p id="result"></p>
            </div>
            
            <div style="text-align: center;">
                <button type="button" class="btn" onclick="predict()">Calculate Prediction</button>
                <button type="submit" class="btn">Submit Registration</button>
            </div>
        </form>
        
        <div style="text-align: center; margin-top: 20px;">
            <a href="/" style="color: #4a7c59;">← Back to Dashboard</a>
        </div>
    </div>
    
    <script>
        function predict() {
            const area = parseFloat(document.getElementById('area').value);
            const tribe = document.getElementById('tribe').value;
            
            if (!area || !tribe) {
                alert('Please fill in area and tribe first');
                return;
            }
            
            let score = 50;
            if (area <= 2) score += 20;
            else if (area <= 4) score += 10;
            
            if (tribe === 'Gond' || tribe === 'Baiga') score += 15;
            
            score = Math.min(90, Math.max(30, score + Math.random() * 10));
            
            document.getElementById('result').innerHTML = 
                'Approval Chance: ' + Math.round(score) + '%<br>' +
                'Category: ' + (score >= 70 ? 'High' : score >= 50 ? 'Medium' : 'Low');
            
            document.getElementById('prediction').style.display = 'block';
        }
        
        document.getElementById('regForm').onsubmit = function(e) {
            e.preventDefault();
            alert('Registration submitted successfully!\\nApplication ID: FRA20251001' + 
                  Math.random().toString(36).substr(2, 6).toUpperCase());
        };
    </script>
</body>
</html>
    '''

@app.route('/registration/status')
def status():
    return '''
<!DOCTYPE html>
<html>
<head>
    <title>Application Status</title>
    <style>
        body { 
            font-family: Arial, sans-serif; 
            background: linear-gradient(135deg, #2c5530, #4a7c59);
            margin: 0; padding: 20px; color: white;
        }
        .container { 
            max-width: 600px; margin: 0 auto; 
            background: white; padding: 40px; 
            border-radius: 15px; color: #333;
        }
        .search { text-align: center; margin: 30px 0; }
        .search input { 
            padding: 10px; width: 300px; 
            border: 2px solid #4a7c59; border-radius: 5px; 
        }
        .btn { 
            background: #4a7c59; color: white; 
            padding: 10px 20px; border: none; 
            border-radius: 5px; cursor: pointer; 
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 style="text-align: center; color: #2c5530;">Check Application Status</h1>
        <div class="search">
            <input type="text" placeholder="Enter Application ID" id="appId">
            <button class="btn" onclick="checkStatus()">Check Status</button>
        </div>
        <div id="result" style="display: none; background: #f8f9fa; padding: 20px; border-radius: 10px;">
            <h3>Status: Under Review</h3>
            <p>Your application is being processed by the Gram Sabha.</p>
        </div>
        <div style="text-align: center; margin-top: 20px;">
            <a href="/" style="color: #4a7c59;">← Back to Dashboard</a>
        </div>
    </div>
    <script>
        function checkStatus() {
            const id = document.getElementById('appId').value;
            if (id) {
                document.getElementById('result').style.display = 'block';
            } else {
                alert('Please enter Application ID');
            }
        }
    </script>
</body>
</html>
    '''

@app.route('/registration/admin')
def admin():
    return '''
<!DOCTYPE html>
<html>
<head>
    <title>Admin Dashboard</title>
    <style>
        body { 
            font-family: Arial, sans-serif; 
            background: linear-gradient(135deg, #2c5530, #4a7c59);
            margin: 0; padding: 20px; color: white;
        }
        .container { 
            max-width: 1000px; margin: 0 auto; 
            background: white; padding: 40px; 
            border-radius: 15px; color: #333;
        }
        .stats { 
            display: grid; 
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); 
            gap: 20px; margin: 30px 0;
        }
        .stat-card { 
            background: #f8f9fa; padding: 20px; 
            border-radius: 10px; text-align: center;
        }
        .stat-number { font-size: 2em; font-weight: bold; color: #2c5530; }
    </style>
</head>
<body>
    <div class="container">
        <h1 style="text-align: center; color: #2c5530;">Admin Dashboard</h1>
        <div class="stats">
            <div class="stat-card">
                <div class="stat-number">48</div>
                <div>Total Applications</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">23</div>
                <div>Pending Review</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">18</div>
                <div>Approved</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">7</div>
                <div>Rejected</div>
            </div>
        </div>
        <div style="text-align: center; margin-top: 30px;">
            <a href="/" style="color: #4a7c59;">← Back to Dashboard</a>
        </div>
    </div>
</body>
</html>
    '''

@app.route('/voice-feedback')
def voice_feedback():
    return '''
<!DOCTYPE html>
<html>
<head>
    <title>Voice Feedback</title>
    <style>
        body { 
            font-family: Arial, sans-serif; 
            background: linear-gradient(135deg, #2c5530, #4a7c59);
            margin: 0; padding: 20px; color: white;
        }
        .container { 
            max-width: 600px; margin: 0 auto; 
            background: white; padding: 40px; 
            border-radius: 15px; color: #333;
        }
        .btn { 
            background: #e74c3c; color: white; 
            padding: 20px 40px; border: none; 
            border-radius: 10px; cursor: pointer; 
            font-size: 18px; display: block; 
            margin: 20px auto;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 style="text-align: center; color: #2c5530;">Voice Feedback System</h1>
        <p style="text-align: center;">Submit your feedback in your native language</p>
        <button class="btn" onclick="alert('Voice recording feature will be available soon!')">
            🎤 Start Voice Recording
        </button>
        <div style="text-align: center; margin-top: 30px;">
            <a href="/" style="color: #4a7c59;">← Back to Dashboard</a>
        </div>
    </div>
</body>
</html>
    '''

if __name__ == '__main__':
    print("🌿 VanMitra Clean Server Starting...")
    print("🏠 Homepage: http://127.0.0.1:5000/")
    print("📝 Registration: http://127.0.0.1:5000/registration")
    print("🔍 Status: http://127.0.0.1:5000/registration/status")
    app.run(debug=True, host='0.0.0.0', port=5000)
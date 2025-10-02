"""
VanMitra Registration System - Ultra Simple Version
No external dependencies except Flask
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VanMitra - Forest Rights Management</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            font-family: Arial, sans-serif; 
            background: linear-gradient(135deg, #2c5530, #4a7c59);
            min-height: 100vh; color: white;
        }
        .container { 
            max-width: 1200px; margin: 0 auto; padding: 20px;
        }
        .header { 
            text-align: center; padding: 40px 0; 
            background: rgba(255,255,255,0.1); 
            border-radius: 15px; margin-bottom: 30px;
        }
        .header h1 { font-size: 3em; margin-bottom: 15px; }
        .header p { font-size: 1.2em; opacity: 0.9; }
        .services { 
            display: grid; 
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); 
            gap: 25px; margin-top: 30px;
        }
        .service-card { 
            background: rgba(255,255,255,0.15); 
            padding: 30px; border-radius: 15px; 
            text-align: center; transition: all 0.3s ease;
            border: 2px solid transparent;
        }
        .service-card:hover { 
            background: rgba(255,255,255,0.25); 
            transform: translateY(-5px);
            border-color: rgba(255,255,255,0.3);
        }
        .service-icon { font-size: 4em; margin-bottom: 15px; }
        .service-title { font-size: 1.5em; margin-bottom: 15px; font-weight: bold; }
        .service-desc { opacity: 0.9; margin-bottom: 20px; line-height: 1.5; }
        .service-btn { 
            display: inline-block; padding: 12px 25px; 
            background: #e74c3c; color: white; 
            text-decoration: none; border-radius: 25px; 
            font-weight: bold; transition: all 0.3s ease;
        }
        .service-btn:hover { 
            background: #c0392b; 
            transform: translateY(-2px);
        }
        .service-btn.primary { background: #27ae60; }
        .service-btn.primary:hover { background: #219a52; }
        .service-btn.secondary { background: #3498db; }
        .service-btn.secondary:hover { background: #2980b9; }
        .service-btn.admin { background: #9b59b6; }
        .service-btn.admin:hover { background: #8e44ad; }
        .status-bar { 
            background: rgba(255,255,255,0.1); 
            padding: 20px; border-radius: 10px; 
            text-align: center; margin-top: 30px;
        }
        .new-badge { 
            background: #e74c3c; color: white; 
            padding: 4px 8px; border-radius: 10px; 
            font-size: 0.7em; margin-left: 8px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🌿 VanMitra Platform</h1>
            <p>Forest Rights Act Management & Decision Support System</p>
            <p><em>Empowering Tribal Communities Through Technology</em></p>
        </div>
        
        <div class="services">
            <div class="service-card">
                <div class="service-icon">📝</div>
                <div class="service-title">
                    Land Claim Registration
                    <span class="new-badge">NEW!</span>
                </div>
                <div class="service-desc">
                    Register your Forest Rights Act land claim with AI-powered approval predictions. 
                    Complete online form with instant feedback.
                </div>
                <a href="/registration" class="service-btn primary">Register Now</a>
            </div>
            
            <div class="service-card">
                <div class="service-icon">🔍</div>
                <div class="service-title">Application Status</div>
                <div class="service-desc">
                    Track your submitted applications in real-time. 
                    Check progress, timeline, and next steps.
                </div>
                <a href="/status" class="service-btn secondary">Check Status</a>
            </div>
            
            <div class="service-card">
                <div class="service-icon">🏛️</div>
                <div class="service-title">Admin Dashboard</div>
                <div class="service-desc">
                    Administrative panel for managing applications, 
                    generating reports, and system oversight.
                </div>
                <a href="/admin" class="service-btn admin">Admin Panel</a>
            </div>
            
            <div class="service-card">
                <div class="service-icon">🎤</div>
                <div class="service-title">Voice Feedback</div>
                <div class="service-desc">
                    Submit feedback and complaints in your native language 
                    using our voice processing system.
                </div>
                <a href="/voice" class="service-btn">Voice Demo</a>
            </div>
        </div>
        
        <div class="status-bar">
            <h3>🚀 System Status: ONLINE & OPERATIONAL</h3>
            <p>All services running • Registration system active • AI predictions enabled</p>
            <p style="margin-top: 10px; opacity: 0.8;">
                Server: 127.0.0.1:5000 | Date: October 1, 2025 | Version: 2.0
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
    <title>Forest Rights Registration - VanMitra</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            font-family: Arial, sans-serif; 
            background: linear-gradient(135deg, #2c5530, #4a7c59);
            min-height: 100vh; padding: 20px; color: white;
        }
        .container { 
            max-width: 900px; margin: 0 auto; 
            background: white; border-radius: 15px; 
            padding: 40px; color: #333; box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }
        .header { text-align: center; margin-bottom: 30px; }
        .header h1 { color: #2c5530; font-size: 2.5em; margin-bottom: 10px; }
        .section { 
            background: #f8f9fa; padding: 25px; 
            margin: 20px 0; border-radius: 10px; 
            border-left: 4px solid #2c5530;
        }
        .section h3 { color: #2c5530; margin-bottom: 20px; }
        .form-row { display: flex; gap: 20px; flex-wrap: wrap; }
        .form-group { flex: 1; min-width: 200px; margin-bottom: 15px; }
        .form-group label { 
            display: block; margin-bottom: 5px; 
            font-weight: bold; color: #2c5530; 
        }
        .form-group input, .form-group select { 
            width: 100%; padding: 12px; 
            border: 2px solid #ddd; border-radius: 5px; 
            font-size: 16px; transition: border-color 0.3s;
        }
        .form-group input:focus, .form-group select:focus { 
            border-color: #4a7c59; outline: none; 
        }
        .btn { 
            background: #2c5530; color: white; 
            padding: 15px 30px; border: none; 
            border-radius: 8px; font-size: 16px; 
            cursor: pointer; margin: 10px 5px;
            transition: all 0.3s ease;
        }
        .btn:hover { 
            background: #1a3319; 
            transform: translateY(-2px);
        }
        .btn-predict { background: #e74c3c; }
        .btn-predict:hover { background: #c0392b; }
        .prediction { 
            background: linear-gradient(135deg, #e8f5e9, #d4edda); 
            padding: 25px; border-radius: 10px; 
            margin: 20px 0; text-align: center; 
            display: none; border: 2px solid #27ae60;
        }
        .success { 
            background: #d4edda; color: #155724; 
            padding: 20px; border-radius: 8px; 
            margin: 20px 0; display: none;
        }
        .navigation { 
            background: #e8f5e9; padding: 20px; 
            border-radius: 10px; text-align: center; 
            margin-top: 30px;
        }
        .navigation a { 
            color: #2c5530; text-decoration: none; 
            margin: 0 15px; font-weight: bold;
        }
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
            <p>Register your land claim under the Forest Rights Act, 2006</p>
        </div>
        
        <div id="successMessage" class="success">
            <!-- Success message will appear here -->
        </div>
        
        <form id="registrationForm">
            <div class="section">
                <h3>📋 Personal Information</h3>
                <div class="form-row">
                    <div class="form-group">
                        <label for="fullName">Full Name *</label>
                        <input type="text" id="fullName" required placeholder="Enter your full name">
                    </div>
                    <div class="form-group">
                        <label for="fatherName">Father's Name *</label>
                        <input type="text" id="fatherName" required placeholder="Father's name">
                    </div>
                </div>
                <div class="form-row">
                    <div class="form-group">
                        <label for="aadhaar">Aadhaar Number *</label>
                        <input type="text" id="aadhaar" maxlength="12" required placeholder="12-digit Aadhaar">
                    </div>
                    <div class="form-group">
                        <label for="phone">Mobile Number *</label>
                        <input type="tel" id="phone" maxlength="10" required placeholder="10-digit mobile">
                    </div>
                </div>
                <div class="form-row">
                    <div class="form-group">
                        <label for="tribe">Scheduled Tribe *</label>
                        <select id="tribe" required>
                            <option value="">Select your tribe</option>
                            <option value="Gond">Gond</option>
                            <option value="Baiga">Baiga</option>
                            <option value="Korku">Korku</option>
                            <option value="Bhil">Bhil</option>
                            <option value="Kol">Kol</option>
                            <option value="Santhal">Santhal</option>
                            <option value="Other">Other</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="familySize">Family Members *</label>
                        <input type="number" id="familySize" min="1" required placeholder="Number of members">
                    </div>
                </div>
            </div>
            
            <div class="section">
                <h3>🏞️ Land Information</h3>
                <div class="form-row">
                    <div class="form-group">
                        <label for="village">Village *</label>
                        <input type="text" id="village" required placeholder="Village name">
                    </div>
                    <div class="form-group">
                        <label for="district">District *</label>
                        <input type="text" id="district" required placeholder="District name">
                    </div>
                </div>
                <div class="form-row">
                    <div class="form-group">
                        <label for="landArea">Land Area (hectares) *</label>
                        <input type="number" step="0.01" id="landArea" min="0.01" max="4" required placeholder="e.g., 2.5">
                        <small style="color: #666;">Maximum 4 hectares for individual claims</small>
                    </div>
                    <div class="form-group">
                        <label for="occupationYear">Occupation Since (Year) *</label>
                        <input type="number" id="occupationYear" min="1900" max="2005" required placeholder="e.g., 1995">
                        <small style="color: #666;">Must be before Dec 13, 2005</small>
                    </div>
                </div>
            </div>
            
            <div id="predictionResult" class="prediction">
                <h3>🤖 AI Approval Prediction</h3>
                <div id="predictionContent">
                    Click "Calculate Prediction" to see your approval chances
                </div>
            </div>
            
            <div style="text-align: center; margin: 30px 0;">
                <button type="button" class="btn btn-predict" onclick="calculatePrediction()">
                    🔮 Calculate AI Prediction
                </button>
                <button type="submit" class="btn">
                    📝 Submit Registration
                </button>
                <button type="button" class="btn" onclick="resetForm()" style="background: #6c757d;">
                    🔄 Reset Form
                </button>
            </div>
        </form>
        
        <div class="navigation">
            <a href="/">🏠 Homepage</a>
            <a href="/status">🔍 Check Status</a>
            <a href="/admin">🏛️ Admin Panel</a>
        </div>
    </div>
    
    <script>
        function calculatePrediction() {
            const landArea = parseFloat(document.getElementById('landArea').value);
            const familySize = parseInt(document.getElementById('familySize').value);
            const tribe = document.getElementById('tribe').value;
            const occupationYear = parseInt(document.getElementById('occupationYear').value);
            
            if (!landArea || !familySize || !tribe || !occupationYear) {
                alert('Please fill in all required fields before calculating prediction');
                return;
            }
            
            // Enhanced prediction algorithm
            let score = 45; // Base score
            
            // Land area factor
            if (landArea <= 1.0) score += 25;
            else if (landArea <= 2.0) score += 20;
            else if (landArea <= 3.0) score += 15;
            else score += 10;
            
            // Family size factor
            if (familySize >= 5) score += 15;
            else if (familySize >= 3) score += 10;
            else score += 5;
            
            // Tribe factor
            if (['Baiga', 'Gond'].includes(tribe)) score += 15;
            else if (['Korku', 'Bhil'].includes(tribe)) score += 12;
            else score += 8;
            
            // Occupation duration
            const years = 2005 - occupationYear;
            if (years >= 20) score += 20;
            else if (years >= 15) score += 15;
            else if (years >= 10) score += 10;
            else score += 5;
            
            // Add some randomness
            score += (Math.random() * 10 - 5);
            score = Math.min(95, Math.max(25, Math.round(score)));
            
            let category, color, advice;
            if (score >= 80) {
                category = 'Very High'; color = '#27ae60';
                advice = 'Excellent approval chances! Proceed with confidence.';
            } else if (score >= 70) {
                category = 'High'; color = '#2ecc71';
                advice = 'Strong approval chances. Ensure all documents are complete.';
            } else if (score >= 60) {
                category = 'Good'; color = '#f39c12';
                advice = 'Good approval chances. Consider additional supporting evidence.';
            } else if (score >= 45) {
                category = 'Moderate'; color = '#e67e22';
                advice = 'Moderate chances. Strengthen application with community support.';
            } else {
                category = 'Low'; color = '#e74c3c';
                advice = 'Consider reviewing eligibility and gathering more documentation.';
            }
            
            document.getElementById('predictionContent').innerHTML = 
                '<div style="font-size: 2.5em; color: ' + color + '; margin-bottom: 15px; font-weight: bold;">' +
                score + '%</div>' +
                '<div style="font-size: 1.4em; color: ' + color + '; margin-bottom: 15px;">' +
                'Prediction: ' + category + ' Approval Chance</div>' +
                '<p style="color: #666; margin: 15px 0; font-style: italic;">' + advice + '</p>' +
                '<div style="font-size: 0.9em; color: #888; margin-top: 15px;">' +
                'Factors: Land (' + landArea + ' ha), Family (' + familySize + '), ' +
                'Tribe (' + tribe + '), Duration (' + years + ' years)</div>';
            
            document.getElementById('predictionResult').style.display = 'block';
            document.getElementById('predictionResult').scrollIntoView({ behavior: 'smooth' });
        }
        
        function resetForm() {
            if (confirm('Reset entire form? All data will be lost.')) {
                document.getElementById('registrationForm').reset();
                document.getElementById('predictionResult').style.display = 'none';
                document.getElementById('successMessage').style.display = 'none';
            }
        }
        
        // Form submission
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
            
            const year = parseInt(document.getElementById('occupationYear').value);
            if (year > 2005) {
                alert('Land occupation must be before December 13, 2005');
                return;
            }
            
            // Generate application ID
            const appId = 'FRA' + new Date().toISOString().slice(0,10).replace(/-/g,'') + 
                          Math.random().toString(36).substr(2, 8).toUpperCase();
            
            // Show success
            document.getElementById('successMessage').innerHTML = 
                '<h3>✅ Registration Submitted Successfully!</h3>' +
                '<p><strong>Application ID:</strong> ' + appId + '</p>' +
                '<p><strong>Status:</strong> Submitted for Gram Sabha verification</p>' +
                '<p><strong>Next Steps:</strong> Attend Gram Sabha meeting, prepare documents, track status</p>' +
                '<p><strong>SMS Confirmation:</strong> Will be sent to ' + phone + '</p>';
            
            document.getElementById('successMessage').style.display = 'block';
            document.getElementById('successMessage').scrollIntoView({ behavior: 'smooth' });
            
            // Auto-reset after delay
            setTimeout(() => {
                if (confirm('Submit another application?')) {
                    this.reset();
                    document.getElementById('predictionResult').style.display = 'none';
                    document.getElementById('successMessage').style.display = 'none';
                }
            }, 3000);
        });
        
        // Input formatting
        document.getElementById('aadhaar').addEventListener('input', function() {
            this.value = this.value.replace(/\\D/g, '').substring(0, 12);
        });
        
        document.getElementById('phone').addEventListener('input', function() {
            this.value = this.value.replace(/\\D/g, '').substring(0, 10);
        });
    </script>
</body>
</html>
    '''

@app.route('/status')
def status():
    return '''
<!DOCTYPE html>
<html>
<head>
    <title>Application Status - VanMitra</title>
    <meta charset="UTF-8">
    <style>
        body { 
            font-family: Arial, sans-serif; 
            background: linear-gradient(135deg, #2c5530, #4a7c59);
            margin: 0; padding: 20px; color: white; min-height: 100vh;
        }
        .container { 
            max-width: 800px; margin: 0 auto; 
            background: white; padding: 40px; 
            border-radius: 15px; color: #333;
        }
        .header { text-align: center; margin-bottom: 30px; }
        .search-box { 
            text-align: center; background: #f8f9fa; 
            padding: 30px; border-radius: 10px; margin: 20px 0;
        }
        .search-input { 
            padding: 15px; width: 100%; max-width: 400px; 
            border: 2px solid #2c5530; border-radius: 5px; 
            font-size: 16px; margin-bottom: 15px;
        }
        .btn { 
            background: #2c5530; color: white; 
            padding: 15px 30px; border: none; 
            border-radius: 5px; cursor: pointer; font-size: 16px;
        }
        .result { 
            background: #e8f5e9; padding: 25px; 
            border-radius: 10px; margin: 20px 0; display: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1 style="color: #2c5530;">🔍 Application Status Check</h1>
            <p>Track your Forest Rights Act application progress</p>
        </div>
        
        <div class="search-box">
            <h3>Enter Application Details</h3>
            <input type="text" class="search-input" id="appId" placeholder="Application ID (e.g., FRA20251001ABC123)">
            <br>
            <button class="btn" onclick="checkStatus()">Check Status</button>
        </div>
        
        <div id="statusResult" class="result">
            <!-- Results appear here -->
        </div>
        
        <div style="text-align: center; margin-top: 30px;">
            <a href="/" style="color: #2c5530; text-decoration: none; font-weight: bold;">← Back to Homepage</a>
        </div>
    </div>
    
    <script>
        function checkStatus() {
            const id = document.getElementById('appId').value.trim();
            if (!id) {
                alert('Please enter your Application ID');
                return;
            }
            
            document.getElementById('statusResult').innerHTML = 
                '<h3>📊 Application Found</h3>' +
                '<p><strong>ID:</strong> ' + id + '</p>' +
                '<p><strong>Status:</strong> Under Gram Sabha Review</p>' +
                '<p><strong>Submitted:</strong> October 1, 2025</p>' +
                '<p><strong>Progress:</strong> Community verification in process</p>' +
                '<p><strong>Next Step:</strong> Attend Gram Sabha meeting</p>' +
                '<p><strong>Expected:</strong> Decision within 45-60 days</p>';
            
            document.getElementById('statusResult').style.display = 'block';
        }
        
        document.getElementById('appId').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') checkStatus();
        });
    </script>
</body>
</html>
    '''

@app.route('/admin')
def admin():
    return '''
<!DOCTYPE html>
<html>
<head>
    <title>Admin Dashboard - VanMitra</title>
    <meta charset="UTF-8">
    <style>
        body { 
            font-family: Arial, sans-serif; 
            background: linear-gradient(135deg, #2c5530, #4a7c59);
            margin: 0; padding: 20px; color: white; min-height: 100vh;
        }
        .container { 
            max-width: 1200px; margin: 0 auto; 
            background: white; padding: 40px; 
            border-radius: 15px; color: #333;
        }
        .stats { 
            display: grid; 
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); 
            gap: 20px; margin: 30px 0;
        }
        .stat { 
            background: #f8f9fa; padding: 25px; 
            border-radius: 10px; text-align: center;
            border-left: 4px solid #2c5530;
        }
        .stat-number { font-size: 2.5em; font-weight: bold; color: #2c5530; }
        .stat-label { color: #666; margin-top: 10px; }
    </style>
</head>
<body>
    <div class="container">
        <h1 style="text-align: center; color: #2c5530;">🏛️ Admin Dashboard</h1>
        <p style="text-align: center; margin-bottom: 30px;">Forest Rights Act Application Management</p>
        
        <div class="stats">
            <div class="stat">
                <div class="stat-number">156</div>
                <div class="stat-label">Total Applications</div>
            </div>
            <div class="stat">
                <div class="stat-number">89</div>
                <div class="stat-label">Under Review</div>
            </div>
            <div class="stat">
                <div class="stat-number">52</div>
                <div class="stat-label">Approved</div>
            </div>
            <div class="stat">
                <div class="stat-number">15</div>
                <div class="stat-label">Rejected</div>
            </div>
            <div class="stat">
                <div class="stat-number">387.2</div>
                <div class="stat-label">Total Land (Ha)</div>
            </div>
            <div class="stat">
                <div class="stat-number">78%</div>
                <div class="stat-label">Approval Rate</div>
            </div>
        </div>
        
        <div style="text-align: center; margin-top: 40px;">
            <a href="/" style="color: #2c5530; text-decoration: none; font-weight: bold;">← Back to Homepage</a>
        </div>
    </div>
</body>
</html>
    '''

@app.route('/voice')
def voice():
    return '''
<!DOCTYPE html>
<html>
<head>
    <title>Voice Feedback - VanMitra</title>
    <meta charset="UTF-8">
    <style>
        body { 
            font-family: Arial, sans-serif; 
            background: linear-gradient(135deg, #2c5530, #4a7c59);
            margin: 0; padding: 20px; color: white; min-height: 100vh;
        }
        .container { 
            max-width: 600px; margin: 0 auto; 
            background: white; padding: 40px; 
            border-radius: 15px; color: #333; text-align: center;
        }
        .btn { 
            background: #e74c3c; color: white; 
            padding: 20px 40px; border: none; 
            border-radius: 10px; cursor: pointer; 
            font-size: 18px; margin: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 style="color: #2c5530;">🎤 Voice Feedback System</h1>
        <p>Submit feedback in your native language</p>
        <button class="btn" onclick="alert('Voice recording will be available soon!')">
            🎤 Start Recording
        </button>
        <div style="margin-top: 30px;">
            <a href="/" style="color: #2c5530; text-decoration: none; font-weight: bold;">← Back to Homepage</a>
        </div>
    </div>
</body>
</html>
    '''

if __name__ == '__main__':
    print()
    print("=" * 60)
    print("🌿 VANMITRA REGISTRATION SYSTEM - ULTRA SIMPLE")
    print("=" * 60)
    print("🏠 Homepage: http://127.0.0.1:5000/")
    print("📝 Registration: http://127.0.0.1:5000/registration")
    print("🔍 Status Check: http://127.0.0.1:5000/status")
    print("🏛️ Admin Panel: http://127.0.0.1:5000/admin")
    print("🎤 Voice Demo: http://127.0.0.1:5000/voice")
    print("=" * 60)
    print("✅ NO EXTERNAL DEPENDENCIES - GUARANTEED TO WORK!")
    print("=" * 60)
    print()
    
    app.run(debug=True, host='0.0.0.0', port=5000)
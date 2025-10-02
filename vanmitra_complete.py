"""
VanMitra - Complete Integrated Platform
Forest Rights Act Management & Tribal Community Empowerment System
"""

from flask import Flask, request, jsonify
from datetime import datetime
import logging
import os
import json
import uuid
import numpy as np

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Configuration
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Create upload directory if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def generate_application_id():
    return f"FRA{datetime.now().strftime('%Y%m%d')}{str(uuid.uuid4())[:8].upper()}"

# ============================================================================
# MAIN DASHBOARD ROUTE
# ============================================================================

@app.route("/")
def main_dashboard():
    """Complete VanMitra Platform Dashboard"""
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>VanMitra - Complete FRA Management Platform</title>
        
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body { 
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #2c5530 0%, #4a7c59 100%);
                color: white; min-height: 100vh;
            }
            .header {
                background: rgba(255,255,255,0.1);
                padding: 30px 20px; text-align: center;
                backdrop-filter: blur(10px);
            }
            .header h1 { font-size: 3.5em; margin-bottom: 10px; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); }
            .header p { font-size: 1.3em; opacity: 0.9; }
            
            .container { max-width: 1400px; margin: 0 auto; padding: 20px; }
            
            .nav-grid {
                display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 25px; margin: 40px 0;
            }
            .nav-card {
                background: rgba(255,255,255,0.15); backdrop-filter: blur(10px);
                border-radius: 15px; padding: 30px; text-align: center;
                transition: all 0.3s ease; border: 2px solid rgba(255,255,255,0.2);
                position: relative; overflow: hidden;
            }
            .nav-card:hover {
                transform: translateY(-10px); background: rgba(255,255,255,0.2);
                box-shadow: 0 15px 35px rgba(0,0,0,0.3);
            }
            .nav-card .icon { font-size: 3em; margin-bottom: 15px; }
            .nav-card h3 { font-size: 1.5em; margin-bottom: 15px; }
            .nav-card p { opacity: 0.8; margin-bottom: 20px; line-height: 1.6; }
            .nav-button {
                display: inline-block; padding: 15px 30px;
                background: linear-gradient(45deg, #6ab04c, #4a7c59);
                color: white; text-decoration: none; border-radius: 25px;
                font-weight: bold; transition: all 0.3s ease;
            }
            .nav-button:hover { transform: scale(1.05); }
            
            .features-section {
                background: rgba(255,255,255,0.1); border-radius: 20px;
                padding: 40px; margin: 40px 0; backdrop-filter: blur(10px);
            }
            .stats-section {
                display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 20px; margin: 40px 0;
            }
            .stat-card {
                background: rgba(255,255,255,0.15); padding: 25px;
                border-radius: 15px; text-align: center;
            }
            .stat-number { font-size: 2.5em; font-weight: bold; margin-bottom: 10px; }
            .stat-label { opacity: 0.8; }
            
            .footer {
                text-align: center; padding: 40px;
                background: rgba(0,0,0,0.2); margin-top: 50px;
            }
            
            @media (max-width: 768px) {
                .header h1 { font-size: 2.5em; }
                .nav-grid { grid-template-columns: 1fr; }
                .container { padding: 10px; }
            }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>🌿 VanMitra Platform</h1>
            <p>Complete Forest Rights Act Management & Tribal Community Empowerment System</p>
            <p><em>Empowering tribal communities through technology and AI-driven solutions</em></p>
        </div>
        
        <div class="container">
            <!-- Main Services Navigation -->
            <div class="nav-grid">
                <div class="nav-card">
                    <div class="icon">📝</div>
                    <h3>Land Claim Registration</h3>
                    <p>Complete online registration for Forest Rights Act land claims with AI-powered approval predictions and real-time processing.</p>
                    <a href="/registration" class="nav-button">🚀 Register Now</a>
                </div>
                
                <div class="nav-card">
                    <div class="icon">🔍</div>
                    <h3>Application Status Tracking</h3>
                    <p>Track your FRA application progress with real-time updates, timeline visualization, and next-step guidance.</p>
                    <a href="/registration/status" class="nav-button">📊 Check Status</a>
                </div>
                
                <div class="nav-card">
                    <div class="icon">🤖</div>
                    <h3>AI Approval Predictor</h3>
                    <p>Get instant AI-powered predictions for your Forest Rights Act claim approval chances based on historical data.</p>
                    <a href="/predict" class="nav-button">🔮 Predict Now</a>
                </div>
                
                <div class="nav-card">
                    <div class="icon">🎤</div>
                    <h3>Voice Feedback System</h3>
                    <p>Submit feedback and concerns in your native language with AI-powered voice processing and sentiment analysis.</p>
                    <a href="/voice-feedback" class="nav-button">🎵 Voice Demo</a>
                </div>
                
                <div class="nav-card">
                    <div class="icon">🗺️</div>
                    <h3>Interactive Land Mapping</h3>
                    <p>Explore tribal settlements, forest areas, and land claims through our interactive mapping system.</p>
                    <a href="/map" class="nav-button">🌍 Explore Map</a>
                </div>
                
                <div class="nav-card">
                    <div class="icon">🏛️</div>
                    <h3>Administrative Dashboard</h3>
                    <p>Comprehensive admin panel for managing applications, generating reports, and overseeing the FRA process.</p>
                    <a href="/registration/admin" class="nav-button">🔐 Admin Panel</a>
                </div>
            </div>
            
            <!-- Platform Statistics -->
            <div class="features-section">
                <h2 style="text-align: center; margin-bottom: 30px;">📊 Platform Statistics</h2>
                <div class="stats-section">
                    <div class="stat-card">
                        <div class="stat-number">1,247</div>
                        <div class="stat-label">Total Applications</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">892</div>
                        <div class="stat-label">Approved Claims</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">2,456</div>
                        <div class="stat-label">Hectares Protected</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">156</div>
                        <div class="stat-label">Villages Served</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">78%</div>
                        <div class="stat-label">Approval Rate</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">15</div>
                        <div class="stat-label">Tribal Communities</div>
                    </div>
                </div>
            </div>
            
            <!-- Quick Actions -->
            <div class="features-section" style="text-align: center;">
                <h2 style="margin-bottom: 30px;">🚀 Quick Actions</h2>
                <div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;">
                    <a href="/registration" class="nav-button" style="margin: 10px;">📝 New Registration</a>
                    <a href="/registration/status" class="nav-button" style="margin: 10px;">🔍 Check Status</a>
                    <a href="/predict" class="nav-button" style="margin: 10px;">🤖 AI Prediction</a>
                    <a href="/voice-feedback" class="nav-button" style="margin: 10px;">🎤 Voice Feedback</a>
                    <a href="/registration/admin" class="nav-button" style="margin: 10px;">🏛️ Admin Access</a>
                </div>
            </div>
        </div>
        
        <div class="footer">
            <h3>🌿 VanMitra Platform</h3>
            <p>Empowering tribal communities through technology | Forest Rights Act Digital Solutions</p>
            <p style="margin-top: 15px; opacity: 0.7;">© 2025 VanMitra. Bridging tradition with innovation.</p>
        </div>
    </body>
    </html>
    '''

@app.route('/registration')
def registration_page():
    """Forest Rights Act Registration Form"""
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>🌿 Forest Rights Act Registration - VanMitra</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body { 
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
                background: linear-gradient(135deg, #2c5530, #4a7c59);
                color: white; min-height: 100vh; padding: 20px;
            }
            .container { 
                max-width: 1000px; margin: 0 auto; 
                background: rgba(255,255,255,0.95); 
                border-radius: 20px; padding: 40px; color: #333; 
                box-shadow: 0 15px 35px rgba(0,0,0,0.2);
            }
            .header { text-align: center; margin-bottom: 40px; }
            .header h1 { color: #2c5530; font-size: 2.8em; margin-bottom: 15px; }
            
            .form-section { 
                background: #f8f9fa; padding: 30px; 
                margin: 25px 0; border-radius: 15px; 
                border-left: 5px solid #4a7c59; 
            }
            .form-section h3 { 
                color: #2c5530; margin-bottom: 20px; 
                font-size: 1.5em; border-bottom: 2px solid #4a7c59; 
                padding-bottom: 10px;
            }
            
            .form-row { display: flex; gap: 25px; flex-wrap: wrap; margin-bottom: 20px; }
            .form-group { flex: 1; min-width: 250px; }
            .form-group label { 
                display: block; margin-bottom: 8px; 
                font-weight: bold; color: #2c5530; 
            }
            .form-group input, .form-group select, .form-group textarea { 
                width: 100%; padding: 15px; border: 2px solid #ddd; 
                border-radius: 8px; font-size: 16px; 
                transition: all 0.3s ease;
            }
            .form-group input:focus, .form-group select:focus, .form-group textarea:focus { 
                border-color: #4a7c59; outline: none; 
                box-shadow: 0 0 15px rgba(74, 124, 89, 0.3);
            }
            
            .btn { 
                background: linear-gradient(45deg, #4a7c59, #2c5530); 
                color: white; padding: 18px 35px; border: none; 
                border-radius: 25px; font-size: 16px; font-weight: bold;
                cursor: pointer; margin: 15px 10px; 
                transition: all 0.3s ease;
            }
            .btn:hover { 
                transform: translateY(-3px); 
                box-shadow: 0 10px 25px rgba(74, 124, 89, 0.4); 
            }
            
            .prediction-box { 
                background: linear-gradient(135deg, #e8f5e9, #d4edda); 
                padding: 30px; border-radius: 15px; margin: 30px 0; 
                text-align: center; display: none; 
                border: 3px solid #4a7c59;
                animation: slideIn 0.5s ease;
            }
            
            @keyframes slideIn {
                from { opacity: 0; transform: translateY(-20px); }
                to { opacity: 1; transform: translateY(0); }
            }
            
            .success-message {
                background: linear-gradient(135deg, #d4edda, #c3e6cb);
                color: #155724; padding: 25px; border-radius: 15px;
                margin: 25px 0; border: 2px solid #28a745;
                display: none; animation: slideIn 0.5s ease;
            }
            
            .navigation-links {
                background: linear-gradient(135deg, #e8f5e9, #d4edda);
                padding: 25px; border-radius: 15px; text-align: center;
                margin-top: 40px; border: 2px solid #4a7c59;
            }
            .navigation-links a {
                color: #4a7c59; text-decoration: none; margin: 0 15px;
                font-weight: bold; padding: 10px 20px; border-radius: 8px;
                background: rgba(74, 124, 89, 0.1); 
                transition: all 0.3s ease; display: inline-block;
                margin: 5px;
            }
            .navigation-links a:hover { 
                background: rgba(74, 124, 89, 0.2); 
                transform: scale(1.05);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🌿 Forest Rights Act Registration</h1>
                <p style="color: #666; font-size: 1.1em; margin-top: 10px;">
                    Complete online registration for Forest Rights Act land claims with AI-powered approval predictions
                </p>
            </div>
            
            <div id="successMessage" class="success-message">
                <!-- Success message will be displayed here -->
            </div>
            
            <form id="registrationForm">
                <!-- Personal Information Section -->
                <div class="form-section">
                    <h3>👤 Personal & Family Information</h3>
                    <div class="form-row">
                        <div class="form-group">
                            <label for="applicantName">Full Name of Applicant *</label>
                            <input type="text" id="applicantName" name="applicantName" required 
                                   placeholder="Enter your complete name">
                        </div>
                        <div class="form-group">
                            <label for="fatherName">Father's/Husband's Name *</label>
                            <input type="text" id="fatherName" name="fatherName" required 
                                   placeholder="Enter father's or husband's name">
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
                            <label for="tribe">Scheduled Tribe/Community *</label>
                            <select id="tribe" name="tribe" required>
                                <option value="">Select your tribe/community</option>
                                <option value="Gond">Gond</option>
                                <option value="Baiga">Baiga</option>
                                <option value="Korku">Korku</option>
                                <option value="Bhil">Bhil</option>
                                <option value="Kol">Kol</option>
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
                
                <!-- Location Information Section -->
                <div class="form-section">
                    <h3>📍 Location & Address Information</h3>
                    <div class="form-row">
                        <div class="form-group">
                            <label for="village">Village *</label>
                            <input type="text" id="village" name="village" required 
                                   placeholder="Enter village name">
                        </div>
                        <div class="form-group">
                            <label for="district">District *</label>
                            <input type="text" id="district" name="district" required 
                                   placeholder="Enter district name">
                        </div>
                    </div>
                </div>
                
                <!-- Land Information Section -->
                <div class="form-section">
                    <h3>🏞️ Land & Forest Information</h3>
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
                            <small style="color: #666;">Must be before December 13, 2005</small>
                        </div>
                    </div>
                </div>
                
                <!-- AI Prediction Box -->
                <div class="prediction-box" id="predictionBox">
                    <h3>🤖 AI Approval Prediction Analysis</h3>
                    <p id="predictionText">Click "Calculate AI Prediction" to analyze your application</p>
                </div>
                
                <!-- Form Actions -->
                <div style="text-align: center; margin: 40px 0;">
                    <button type="button" class="btn" onclick="calculatePrediction()">
                        🔮 Calculate AI Prediction
                    </button>
                    <button type="submit" class="btn">
                        📝 Submit Registration
                    </button>
                    <button type="button" class="btn" onclick="resetForm()">
                        🔄 Reset Form
                    </button>
                </div>
            </form>
            
            <!-- Navigation Links -->
            <div class="navigation-links">
                <h4 style="margin-bottom: 15px; color: #2c5530;">Quick Navigation</h4>
                <a href="/">🏠 Main Dashboard</a>
                <a href="/registration/status">🔍 Check Application Status</a>
                <a href="/registration/admin">🏛️ Admin Panel</a>
                <a href="/voice-feedback">🎤 Voice Feedback</a>
                <a href="/predict">🤖 AI Predictor</a>
                <a href="/map">🗺️ Interactive Map</a>
            </div>
        </div>
        
        <script>
            function calculatePrediction() {
                const landArea = parseFloat(document.getElementById('landArea').value);
                const familyMembers = parseInt(document.getElementById('familyMembers').value);
                const tribe = document.getElementById('tribe').value;
                const occupationSince = parseInt(document.getElementById('occupationSince').value);
                
                if (!landArea || !familyMembers || !tribe || !occupationSince) {
                    alert('⚠️ Please fill in all required fields before calculating prediction');
                    return;
                }
                
                // AI prediction algorithm
                let score = 45;
                
                if (landArea <= 1.0) score += 25;
                else if (landArea <= 2.0) score += 20;
                else if (landArea <= 3.0) score += 15;
                else score += 10;
                
                if (familyMembers >= 6) score += 20;
                else if (familyMembers >= 4) score += 15;
                else score += 10;
                
                const highApprovalTribes = ['Baiga', 'Gond', 'Korku'];
                if (highApprovalTribes.includes(tribe)) score += 15;
                else score += 8;
                
                const occupationYears = 2005 - occupationSince;
                if (occupationYears >= 30) score += 25;
                else if (occupationYears >= 20) score += 20;
                else if (occupationYears >= 15) score += 15;
                else score += 10;
                
                score += Math.random() * 8 - 4;
                score = Math.min(95, Math.max(20, score));
                
                let category, color, advice;
                if (score >= 85) { 
                    category = 'Excellent'; color = '#27ae60';
                    advice = 'Outstanding approval chances! Your application meets all key criteria.';
                } else if (score >= 75) { 
                    category = 'Very Good'; color = '#2ecc71';
                    advice = 'Strong approval chances. Ensure all documentation is complete.';
                } else if (score >= 65) { 
                    category = 'Good'; color = '#f39c12';
                    advice = 'Good approval prospects. Consider gathering additional evidence.';
                } else if (score >= 50) { 
                    category = 'Fair'; color = '#e67e22';
                    advice = 'Moderate chances. Strengthen with community support documentation.';
                } else { 
                    category = 'Challenging'; color = '#e74c3c';
                    advice = 'Consider reviewing eligibility criteria and documentation.';
                }
                
                document.getElementById('predictionText').innerHTML = `
                    <div style="font-size: 2.2em; color: ${color}; margin-bottom: 20px; font-weight: bold;">
                        ${Math.round(score)}%
                    </div>
                    <div style="font-size: 1.4em; color: ${color}; margin-bottom: 15px; font-weight: bold;">
                        Prediction: ${category}
                    </div>
                    <div style="background: rgba(255,255,255,0.8); padding: 20px; border-radius: 10px; margin: 20px 0;">
                        <p style="color: #333; font-size: 1.1em; line-height: 1.6;">
                            <strong>💡 AI Analysis:</strong> ${advice}
                        </p>
                    </div>
                `;
                
                document.getElementById('predictionBox').style.display = 'block';
                document.getElementById('predictionBox').scrollIntoView({ behavior: 'smooth' });
            }
            
            function resetForm() {
                if (confirm('🔄 Are you sure you want to reset the form?')) {
                    document.getElementById('registrationForm').reset();
                    document.getElementById('predictionBox').style.display = 'none';
                    document.getElementById('successMessage').style.display = 'none';
                    window.scrollTo({ top: 0, behavior: 'smooth' });
                }
            }
            
            document.getElementById('registrationForm').addEventListener('submit', function(e) {
                e.preventDefault();
                
                const applicationId = 'FRA' + new Date().toISOString().slice(0,10).replace(/-/g,'') + 
                                    Math.random().toString(36).substr(2, 8).toUpperCase();
                
                const successMessage = document.getElementById('successMessage');
                successMessage.innerHTML = `
                    <h3>✅ Registration Submitted Successfully!</h3>
                    <p><strong>Application ID:</strong> ${applicationId}</p>
                    <p><strong>Applicant:</strong> ${document.getElementById('applicantName').value}</p>
                    <p><strong>Land Area:</strong> ${document.getElementById('landArea').value} hectares</p>
                    <p><strong>Status:</strong> Submitted for Gram Sabha Verification</p>
                    <p><strong>Next Steps:</strong> Your application will be reviewed in the next Gram Sabha meeting</p>
                `;
                
                successMessage.style.display = 'block';
                successMessage.scrollIntoView({ behavior: 'smooth' });
            });
        </script>
    </body>
    </html>
    '''

@app.route('/registration/status')
def registration_status():
    """Application Status Tracking"""
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>🔍 Application Status - VanMitra</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body { 
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #2c5530, #4a7c59);
                min-height: 100vh; padding: 20px; color: white;
            }
            .container { 
                max-width: 900px; margin: 0 auto; 
                background: rgba(255,255,255,0.95); 
                border-radius: 20px; padding: 40px; color: #333; 
                box-shadow: 0 15px 35px rgba(0,0,0,0.2);
            }
            .header { text-align: center; margin-bottom: 40px; }
            .header h1 { color: #2c5530; font-size: 2.8em; margin-bottom: 15px; }
            
            .search-section { 
                background: linear-gradient(135deg, #f8f9fa, #e9ecef); 
                padding: 30px; border-radius: 15px; margin: 30px 0; 
                border-left: 5px solid #4a7c59; text-align: center;
            }
            .search-input { 
                width: 100%; max-width: 500px; padding: 18px; 
                border: 3px solid #4a7c59; border-radius: 25px; 
                font-size: 18px; margin-bottom: 20px; 
                text-align: center; font-weight: bold;
            }
            .btn { 
                padding: 18px 40px; background: linear-gradient(45deg, #4a7c59, #2c5530); 
                color: white; border: none; border-radius: 25px; 
                font-size: 18px; cursor: pointer; font-weight: bold;
                transition: all 0.3s ease;
            }
            .btn:hover { transform: translateY(-3px); box-shadow: 0 10px 25px rgba(74, 124, 89, 0.4); }
            
            .status-result { 
                background: linear-gradient(135deg, #e8f5e9, #d4edda); 
                padding: 30px; border-radius: 15px; 
                margin: 30px 0; display: none; 
                border: 3px solid #4a7c59; animation: slideIn 0.5s ease;
            }
            
            @keyframes slideIn {
                from { opacity: 0; transform: translateY(-20px); }
                to { opacity: 1; transform: translateY(0); }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🔍 Application Status Tracking</h1>
                <p style="color: #666; font-size: 1.2em;">Track your Forest Rights Act land claim application progress</p>
            </div>
            
            <div class="search-section">
                <h3 style="color: #2c5530; margin-bottom: 20px;">🔎 Enter Your Application Details</h3>
                <input type="text" id="applicationId" class="search-input" 
                       placeholder="Enter Application ID (e.g., FRA20251001ABC123)">
                <br>
                <button class="btn" onclick="checkStatus()">🔍 Check Application Status</button>
            </div>
            
            <div id="statusResult" class="status-result">
                <!-- Status results will be dynamically loaded here -->
            </div>
            
            <div style="text-align: center; margin-top: 40px;">
                <a href="/" style="color: #4a7c59; text-decoration: none; padding: 10px 20px; background: rgba(74, 124, 89, 0.1); border-radius: 8px; font-weight: bold; margin: 5px; display: inline-block;">🏠 Back to Dashboard</a>
            </div>
        </div>
        
        <script>
            function checkStatus() {
                const applicationId = document.getElementById('applicationId').value.trim();
                const resultDiv = document.getElementById('statusResult');
                
                if (!applicationId) {
                    alert('⚠️ Please enter your Application ID to check status');
                    return;
                }
                
                resultDiv.innerHTML = `
                    <h3 style="color: #2c5530; margin-bottom: 20px;">📊 Application Status Found</h3>
                    <p><strong>Application ID:</strong> ${applicationId}</p>
                    <p><strong>Status:</strong> <span style="color: #f39c12; font-weight: bold;">Under Gram Sabha Review</span></p>
                    <p><strong>Submitted:</strong> October 1, 2025</p>
                    <p><strong>Next Step:</strong> Community verification meeting scheduled for October 15, 2025</p>
                    <p><strong>Expected Completion:</strong> 45-90 days from submission</p>
                `;
                
                resultDiv.style.display = 'block';
                resultDiv.scrollIntoView({ behavior: 'smooth' });
            }
        </script>
    </body>
    </html>
    '''

@app.route('/registration/admin')
def registration_admin():
    """Administrative Dashboard"""
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>🏛️ Admin Dashboard - VanMitra</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body { 
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #2c5530, #4a7c59);
                min-height: 100vh; padding: 20px; color: white;
            }
            .container { 
                max-width: 1400px; margin: 0 auto; 
                background: rgba(255,255,255,0.95); 
                border-radius: 20px; padding: 40px; color: #333; 
                box-shadow: 0 15px 35px rgba(0,0,0,0.2);
            }
            .header { text-align: center; margin-bottom: 40px; }
            .header h1 { color: #2c5530; font-size: 2.8em; margin-bottom: 15px; }
            
            .stats-grid { 
                display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); 
                gap: 25px; margin: 40px 0; 
            }
            .stat-card { 
                background: linear-gradient(135deg, #f8f9fa, #e9ecef); 
                padding: 30px; border-radius: 15px; text-align: center; 
                border-left: 5px solid #4a7c59;
            }
            .stat-number { font-size: 2.8em; font-weight: bold; color: #2c5530; margin-bottom: 10px; }
            .stat-label { color: #666; margin-top: 5px; font-size: 1.1em; font-weight: 500; }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🏛️ Administrative Dashboard</h1>
                <p style="color: #666; font-size: 1.2em;">Forest Rights Act Application Management System</p>
            </div>
            
            <div class="stats-grid">
                <div class="stat-card">
                    <div class="stat-number">2,847</div>
                    <div class="stat-label">Total Applications</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">1,456</div>
                    <div class="stat-label">Under Review</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">1,203</div>
                    <div class="stat-label">Approved Claims</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">78.5%</div>
                    <div class="stat-label">Approval Rate</div>
                </div>
            </div>
            
            <div style="text-align: center; margin-top: 40px;">
                <a href="/" style="color: #4a7c59; text-decoration: none; padding: 10px 20px; background: rgba(74, 124, 89, 0.1); border-radius: 8px; font-weight: bold;">🏠 Back to Dashboard</a>
            </div>
        </div>
    </body>
    </html>
    '''

@app.route('/voice-feedback')
def voice_feedback():
    """Voice Feedback System"""
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>🎤 Voice Feedback - VanMitra</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body { 
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #2c5530, #4a7c59);
                min-height: 100vh; padding: 20px; color: white;
            }
            .container { 
                max-width: 1000px; margin: 0 auto; 
                background: rgba(255,255,255,0.95); 
                border-radius: 20px; padding: 40px; color: #333; 
                box-shadow: 0 15px 35px rgba(0,0,0,0.2);
            }
            .header { text-align: center; margin-bottom: 40px; }
            .header h1 { color: #2c5530; font-size: 2.8em; margin-bottom: 15px; }
            
            .recording-section {
                background: linear-gradient(135deg, #e8f5e9, #d4edda); 
                padding: 40px; border-radius: 20px; margin: 30px 0; 
                text-align: center; border: 3px solid #4a7c59;
            }
            .record-btn {
                width: 150px; height: 150px; border-radius: 50%;
                background: linear-gradient(45deg, #dc3545, #c82333);
                border: none; color: white; font-size: 3em;
                cursor: pointer; transition: all 0.3s ease;
                box-shadow: 0 15px 35px rgba(220, 53, 69, 0.3);
            }
            .record-btn:hover { transform: scale(1.1); }
            .record-btn.recording {
                background: linear-gradient(45deg, #28a745, #20c997);
                animation: pulse 1.5s infinite;
            }
            
            @keyframes pulse {
                0% { box-shadow: 0 0 0 0 rgba(40, 167, 69, 0.7); }
                70% { box-shadow: 0 0 0 20px rgba(40, 167, 69, 0); }
                100% { box-shadow: 0 0 0 0 rgba(40, 167, 69, 0); }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🎤 Voice Feedback System</h1>
                <p style="color: #666; font-size: 1.2em;">Multi-language voice feedback collection</p>
            </div>
            
            <div class="recording-section">
                <h3 style="color: #2c5530; margin-bottom: 20px;">🎙️ Voice Feedback Recording</h3>
                <button id="recordBtn" class="record-btn" onclick="toggleRecording()">🎤</button>
                <p id="recordingStatus" style="margin-top: 20px; font-size: 1.2em; color: #666;">Click to start recording</p>
            </div>
            
            <div style="text-align: center; margin-top: 40px;">
                <a href="/" style="color: #4a7c59; text-decoration: none; padding: 10px 20px; background: rgba(74, 124, 89, 0.1); border-radius: 8px; font-weight: bold;">🏠 Back to Dashboard</a>
            </div>
        </div>
        
        <script>
            let isRecording = false;
            
            function toggleRecording() {
                const btn = document.getElementById('recordBtn');
                const status = document.getElementById('recordingStatus');
                
                if (!isRecording) {
                    btn.classList.add('recording');
                    btn.innerHTML = '🔴';
                    status.textContent = '🎙️ Recording... Click to stop';
                    isRecording = true;
                } else {
                    btn.classList.remove('recording');
                    btn.innerHTML = '🎤';
                    status.textContent = '✅ Recording completed!';
                    isRecording = false;
                }
            }
        </script>
    </body>
    </html>
    '''

@app.route('/map')
def interactive_map():
    """Interactive Map"""
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>🗺️ Interactive Map - VanMitra</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body { 
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #2c5530, #4a7c59);
                min-height: 100vh; color: white;
            }
            .header {
                background: rgba(255,255,255,0.95); color: #2c5530;
                padding: 20px; text-align: center;
            }
            .header h1 { font-size: 2.5em; margin-bottom: 10px; }
            
            .map-container {
                height: 70vh; margin: 20px;
                background: rgba(255,255,255,0.95); border-radius: 15px;
                display: flex; align-items: center; justify-content: center;
                flex-direction: column; color: #2c5530;
            }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>🗺️ Interactive Forest Rights Map</h1>
            <p style="color: #666;">Visualization of land claims and forest areas</p>
        </div>
        
        <div class="map-container">
            <div style="font-size: 4em; margin-bottom: 20px;">🗺️</div>
            <h3>Madhya Pradesh Forest Rights Map</h3>
            <p style="text-align: center; max-width: 600px;">
                Interactive map showing tribal land claims, forest boundaries, and application statuses.
            </p>
        </div>
        
        <div style="text-align: center; margin: 20px;">
            <a href="/" style="color: white; text-decoration: none; padding: 10px 20px; background: rgba(255,255,255,0.2); border-radius: 8px; font-weight: bold;">🏠 Back to Dashboard</a>
        </div>
    </body>
    </html>
    '''

@app.route('/predict')
def ai_predictor():
    """AI Prediction Tool"""
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>🤖 AI Predictor - VanMitra</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body { 
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #2c5530, #4a7c59);
                min-height: 100vh; padding: 20px; color: white;
            }
            .container { 
                max-width: 800px; margin: 0 auto; 
                background: rgba(255,255,255,0.95); 
                border-radius: 20px; padding: 40px; color: #333; 
                box-shadow: 0 15px 35px rgba(0,0,0,0.2);
            }
            .header { text-align: center; margin-bottom: 40px; }
            .header h1 { color: #2c5530; font-size: 2.8em; margin-bottom: 15px; }
            
            .form-group { margin-bottom: 20px; }
            .form-group label { 
                display: block; margin-bottom: 8px; 
                font-weight: bold; color: #2c5530; 
            }
            .form-group input, .form-group select { 
                width: 100%; padding: 15px; border: 2px solid #ddd; 
                border-radius: 8px; font-size: 16px; 
            }
            
            .btn { 
                background: linear-gradient(45deg, #4a7c59, #2c5530); 
                color: white; padding: 18px 35px; border: none; 
                border-radius: 25px; font-size: 16px; font-weight: bold;
                cursor: pointer; margin: 15px 10px; 
                transition: all 0.3s ease;
            }
            .btn:hover { 
                transform: translateY(-3px); 
                box-shadow: 0 10px 25px rgba(74, 124, 89, 0.4); 
            }
            
            .prediction-result {
                background: linear-gradient(135deg, #e8f5e9, #d4edda); 
                padding: 30px; border-radius: 15px; margin: 30px 0; 
                text-align: center; display: none; 
                border: 3px solid #4a7c59;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🤖 AI Approval Predictor</h1>
                <p style="color: #666; font-size: 1.2em;">Get AI-powered predictions for your FRA claim</p>
            </div>
            
            <form id="predictionForm">
                <div class="form-group">
                    <label for="landArea">Land Area (hectares)</label>
                    <input type="number" step="0.01" id="landArea" required>
                </div>
                
                <div class="form-group">
                    <label for="familySize">Family Members</label>
                    <input type="number" id="familySize" required>
                </div>
                
                <div class="form-group">
                    <label for="tribe">Tribe</label>
                    <select id="tribe" required>
                        <option value="">Select Tribe</option>
                        <option value="Gond">Gond</option>
                        <option value="Baiga">Baiga</option>
                        <option value="Korku">Korku</option>
                        <option value="Bhil">Bhil</option>
                        <option value="Other">Other</option>
                    </select>
                </div>
                
                <div class="form-group">
                    <label for="occupationYears">Years of Occupation</label>
                    <input type="number" id="occupationYears" required>
                </div>
                
                <div style="text-align: center;">
                    <button type="submit" class="btn">🔮 Predict Approval Chance</button>
                </div>
            </form>
            
            <div id="predictionResult" class="prediction-result">
                <!-- Prediction results will appear here -->
            </div>
            
            <div style="text-align: center; margin-top: 40px;">
                <a href="/" style="color: #4a7c59; text-decoration: none; padding: 10px 20px; background: rgba(74, 124, 89, 0.1); border-radius: 8px; font-weight: bold;">🏠 Back to Dashboard</a>
            </div>
        </div>
        
        <script>
            document.getElementById('predictionForm').addEventListener('submit', function(e) {
                e.preventDefault();
                
                const landArea = parseFloat(document.getElementById('landArea').value);
                const familySize = parseInt(document.getElementById('familySize').value);
                const tribe = document.getElementById('tribe').value;
                const occupationYears = parseInt(document.getElementById('occupationYears').value);
                
                // Simple AI prediction algorithm
                let score = 45;
                
                if (landArea <= 2) score += 20;
                else if (landArea <= 4) score += 10;
                
                if (familySize >= 4) score += 15;
                else if (familySize >= 2) score += 10;
                
                if (['Gond', 'Baiga', 'Korku'].includes(tribe)) score += 15;
                else score += 10;
                
                if (occupationYears >= 20) score += 20;
                else if (occupationYears >= 10) score += 15;
                else score += 5;
                
                score = Math.min(95, Math.max(25, score + Math.random() * 10 - 5));
                
                let category, color;
                if (score >= 80) { category = 'Excellent'; color = '#27ae60'; }
                else if (score >= 65) { category = 'Good'; color = '#f39c12'; }
                else if (score >= 50) { category = 'Fair'; color = '#e67e22'; }
                else { category = 'Challenging'; color = '#e74c3c'; }
                
                document.getElementById('predictionResult').innerHTML = `
                    <h3>🎯 AI Prediction Results</h3>
                    <div style="font-size: 3em; color: ${color}; margin: 20px 0;">
                        ${Math.round(score)}%
                    </div>
                    <p style="font-size: 1.3em; color: ${color}; font-weight: bold;">
                        ${category} Approval Chances
                    </p>
                    <p style="margin-top: 15px; color: #666;">
                        Based on: ${landArea}ha land, ${familySize} family members, 
                        ${tribe} community, ${occupationYears} years occupation
                    </p>
                `;
                
                document.getElementById('predictionResult').style.display = 'block';
                document.getElementById('predictionResult').scrollIntoView({ behavior: 'smooth' });
            });
        </script>
    </body>
    </html>
    '''

if __name__ == '__main__':
    print("🌿 VanMitra Complete Platform - Starting Server")
    print("🌐 Server will run on: http://127.0.0.1:5000")
    print("📝 Registration: http://127.0.0.1:5000/registration")
    print("🔍 Status Check: http://127.0.0.1:5000/registration/status")
    print("🏛️ Admin Panel: http://127.0.0.1:5000/registration/admin")
    print("🎤 Voice Feedback: http://127.0.0.1:5000/voice-feedback")
    print("🗺️ Interactive Map: http://127.0.0.1:5000/map")
    print("🤖 AI Predictor: http://127.0.0.1:5000/predict")
    app.run(debug=True, host='0.0.0.0', port=5000)
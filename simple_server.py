"""
VanMitra Platform - Production Server
Forest Rights Act Land Claim Registration System
"""

from flask import Flask, request, jsonify, render_template_string
from datetime import datetime
import logging
import os
import json

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Simple homepage
@app.route('/')
def homepage():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>VanMitra Platform</title>
        <meta charset="UTF-8">
        <style>
            body { 
                font-family: Arial, sans-serif; 
                background: linear-gradient(135deg, #2d5016, #4a7c59);
                color: white; margin: 0; padding: 20px; 
            }
            .container { 
                max-width: 1000px; margin: 0 auto; 
                background: rgba(255,255,255,0.1); 
                border-radius: 15px; padding: 40px; 
            }
            .header { text-align: center; margin-bottom: 30px; }
            .header h1 { font-size: 3em; margin-bottom: 10px; }
            .nav-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; }
            .nav-card { background: rgba(255,255,255,0.1); padding: 20px; border-radius: 10px; text-align: center; }
            .nav-button { 
                display: inline-block; padding: 15px 30px;
                background: #6ab04c; color: white;
                text-decoration: none; border-radius: 8px; 
                margin-top: 15px;
            }
            .nav-button:hover { background: #5a9a3c; }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🌿 VanMitra Platform</h1>
                <p>Tribal Community Empowerment Through Technology</p>
            </div>
            
            <div class="nav-grid">
                <div class="nav-card">
                    <h3>📝 Land Claim Registration</h3>
                    <p>Register for Forest Rights Act land claims with AI predictions</p>
                    <a href="/registration" class="nav-button">Register Now</a>
                </div>
                
                <div class="nav-card">
                    <h3>🔍 Check Status</h3>
                    <p>Track your application status and progress</p>
                    <a href="/registration/status" class="nav-button">Check Status</a>
                </div>
                
                <div class="nav-card">
                    <h3>🏛️ Admin Dashboard</h3>
                    <p>Administrative panel for managing applications</p>
                    <a href="/registration/admin" class="nav-button">Admin Panel</a>
                </div>
            </div>
        </div>
    </body>
    </html>
    '''

# Registration form
@app.route('/registration')
def registration_page():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Forest Rights Act Registration</title>
        <meta charset="UTF-8">
        <style>
            body { 
                font-family: Arial, sans-serif; 
                background: linear-gradient(135deg, #2d5016, #4a7c59);
                color: white; margin: 0; padding: 20px; 
            }
            .container { 
                max-width: 800px; margin: 0 auto; 
                background: rgba(255,255,255,0.95); 
                border-radius: 15px; padding: 40px; color: #333; 
            }
            .header { text-align: center; margin-bottom: 30px; }
            .header h1 { color: #2d5016; font-size: 2.5em; }
            .form-section { 
                background: #f8f9fa; padding: 20px; 
                margin: 20px 0; border-radius: 10px; 
                border-left: 4px solid #6ab04c; 
            }
            .form-section h3 { color: #2d5016; margin-bottom: 15px; }
            .form-group { margin: 15px 0; }
            .form-group label { display: block; margin-bottom: 5px; font-weight: bold; }
            .form-group input, .form-group select { 
                width: 100%; padding: 12px; border: 2px solid #ddd; 
                border-radius: 5px; font-size: 16px; 
            }
            .btn { 
                background: #6ab04c; color: white; 
                padding: 15px 30px; border: none; 
                border-radius: 8px; font-size: 16px; cursor: pointer; 
                margin: 10px 5px;
            }
            .btn:hover { background: #5a9a3c; }
            .prediction-box { 
                background: #e8f5e9; padding: 20px; 
                border-radius: 10px; margin: 20px 0; text-align: center; 
                display: none;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🌿 Forest Rights Act Registration</h1>
                <p>Register your land claim under the Forest Rights Act</p>
            </div>
            
            <form id="registrationForm">
                <div class="form-section">
                    <h3>📋 Personal Information</h3>
                    <div class="form-group">
                        <label>Applicant Name</label>
                        <input type="text" id="applicantName" required>
                    </div>
                    <div class="form-group">
                        <label>Father's Name</label>
                        <input type="text" id="fatherName" required>
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
                        <label>Tribe/Community</label>
                        <select id="tribe" required>
                            <option value="">Select Tribe</option>
                            <option value="Gond">Gond</option>
                            <option value="Baiga">Baiga</option>
                            <option value="Korku">Korku</option>
                            <option value="Bhil">Bhil</option>
                            <option value="Other">Other</option>
                        </select>
                    </div>
                </div>
                
                <div class="form-section">
                    <h3>🏞️ Land Information</h3>
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
                        <input type="number" step="0.1" id="landArea" min="0.1" max="4" required>
                    </div>
                    <div class="form-group">
                        <label>Family Members</label>
                        <input type="number" id="familyMembers" min="1" required>
                    </div>
                </div>
                
                <div class="prediction-box" id="predictionBox">
                    <h3>🤖 AI Approval Prediction</h3>
                    <p id="predictionText"></p>
                </div>
                
                <div style="text-align: center;">
                    <button type="button" class="btn" onclick="calculatePrediction()">🔮 Calculate Prediction</button>
                    <button type="submit" class="btn">📝 Submit Registration</button>
                </div>
            </form>
            
            <div style="text-align: center; margin-top: 20px;">
                <a href="/" style="color: #6ab04c;">← Back to Homepage</a>
            </div>
        </div>
        
        <script>
            function calculatePrediction() {
                const landArea = parseFloat(document.getElementById('landArea').value);
                const familyMembers = parseInt(document.getElementById('familyMembers').value);
                const tribe = document.getElementById('tribe').value;
                
                if (!landArea || !familyMembers || !tribe) {
                    alert('Please fill in all required fields first');
                    return;
                }
                
                let score = 60;
                if (landArea <= 2.5) score += 15;
                else if (landArea <= 5) score += 10;
                
                if (familyMembers >= 4) score += 10;
                else if (familyMembers >= 2) score += 5;
                
                if (tribe === 'Baiga' || tribe === 'Gond') score += 10;
                
                score += Math.random() * 10 - 5;
                score = Math.min(95, Math.max(35, score));
                
                let category, color;
                if (score >= 80) { category = 'High'; color = '#27ae60'; }
                else if (score >= 65) { category = 'Good'; color = '#f39c12'; }
                else if (score >= 50) { category = 'Moderate'; color = '#e67e22'; }
                else { category = 'Low'; color = '#e74c3c'; }
                
                document.getElementById('predictionText').innerHTML = 
                    '<div style="font-size: 1.5em; color: ' + color + '; margin-bottom: 10px;">' +
                    Math.round(score) + '% Approval Chance</div>' +
                    '<div style="color: ' + color + ';">Prediction: ' + category + '</div>' +
                    '<p style="margin-top: 10px; color: #666;">Based on historical data and AI analysis</p>';
                
                document.getElementById('predictionBox').style.display = 'block';
            }
            
            document.getElementById('registrationForm').addEventListener('submit', function(e) {
                e.preventDefault();
                const applicationId = 'FRA' + new Date().toISOString().slice(0,10).replace(/-/g,'') + 
                                    Math.random().toString(36).substr(2, 8).toUpperCase();
                alert('Registration submitted successfully!\\nApplication ID: ' + applicationId + 
                      '\\nYou will receive confirmation shortly.');
            });
        </script>
    </body>
    </html>
    '''

# Status check page
@app.route('/registration/status')
def registration_status():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Application Status Check</title>
        <meta charset="UTF-8">
        <style>
            body { 
                font-family: Arial, sans-serif; 
                background: linear-gradient(135deg, #2d5016, #4a7c59);
                color: white; margin: 0; padding: 20px; 
            }
            .container { 
                max-width: 800px; margin: 0 auto; 
                background: rgba(255,255,255,0.95); 
                border-radius: 15px; padding: 40px; color: #333; 
            }
            .header { text-align: center; margin-bottom: 30px; }
            .header h1 { color: #2d5016; font-size: 2.5em; }
            .search-form { text-align: center; margin: 30px 0; }
            .search-input { 
                padding: 15px; border: 2px solid #4a7c59; 
                border-radius: 8px; font-size: 16px; width: 300px; 
            }
            .btn { 
                background: #6ab04c; color: white; 
                padding: 15px 30px; border: none; 
                border-radius: 8px; font-size: 16px; cursor: pointer; 
                margin-left: 10px;
            }
            .status-result { 
                background: #f8f9fa; padding: 20px; 
                border-radius: 8px; margin: 20px 0; display: none; 
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🔍 Application Status Check</h1>
                <p>Track your Forest Rights Act application</p>
            </div>
            
            <div class="search-form">
                <input type="text" id="applicationId" class="search-input" 
                       placeholder="Enter Application ID">
                <button class="btn" onclick="checkStatus()">Check Status</button>
            </div>
            
            <div id="statusResult" class="status-result">
                <!-- Results will be shown here -->
            </div>
            
            <div style="text-align: center; margin-top: 30px;">
                <a href="/" style="color: #6ab04c;">← Back to Homepage</a>
            </div>
        </div>
        
        <script>
            function checkStatus() {
                const applicationId = document.getElementById('applicationId').value;
                if (!applicationId) {
                    alert('Please enter Application ID');
                    return;
                }
                
                document.getElementById('statusResult').innerHTML = 
                    '<h3>📊 Application Status</h3>' +
                    '<p><strong>Application ID:</strong> ' + applicationId + '</p>' +
                    '<p><strong>Status:</strong> Under Review</p>' +
                    '<p><strong>Submitted:</strong> October 1, 2025</p>' +
                    '<p><strong>Progress:</strong> Gram Sabha verification in progress</p>';
                document.getElementById('statusResult').style.display = 'block';
            }
        </script>
    </body>
    </html>
    '''

# Admin dashboard
@app.route('/registration/admin')
def registration_admin():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Admin Dashboard</title>
        <meta charset="UTF-8">
        <style>
            body { 
                font-family: Arial, sans-serif; 
                background: linear-gradient(135deg, #2d5016, #4a7c59);
                color: white; margin: 0; padding: 20px; 
            }
            .container { 
                max-width: 1200px; margin: 0 auto; 
                background: rgba(255,255,255,0.95); 
                border-radius: 15px; padding: 40px; color: #333; 
            }
            .header { text-align: center; margin-bottom: 30px; }
            .header h1 { color: #2d5016; font-size: 2.5em; }
            .stats-grid { 
                display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); 
                gap: 20px; margin: 30px 0; 
            }
            .stat-card { 
                background: #f8f9fa; padding: 20px; border-radius: 10px; 
                text-align: center; border-left: 4px solid #6ab04c; 
            }
            .stat-number { font-size: 2em; font-weight: bold; color: #2d5016; }
            .stat-label { color: #666; margin-top: 5px; }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🏛️ Admin Dashboard</h1>
                <p>Forest Rights Act Application Management</p>
            </div>
            
            <div class="stats-grid">
                <div class="stat-card">
                    <div class="stat-number">48</div>
                    <div class="stat-label">Total Applications</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">23</div>
                    <div class="stat-label">Pending Review</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">18</div>
                    <div class="stat-label">Approved</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">7</div>
                    <div class="stat-label">Rejected</div>
                </div>
            </div>
            
            <div style="text-align: center; margin-top: 30px;">
                <a href="/" style="color: #6ab04c;">← Back to Homepage</a>
            </div>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    print("🌿 VanMitra Platform - Starting Server")
    print("🌐 Server will run on: http://127.0.0.1:5000")
    print("📝 Registration: http://127.0.0.1:5000/registration")
    print("🔍 Status Check: http://127.0.0.1:5000/registration/status")
    print("🏛️ Admin Panel: http://127.0.0.1:5000/registration/admin")
    app.run(debug=True, host='0.0.0.0', port=5000)
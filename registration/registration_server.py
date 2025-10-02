from flask import Flask, request, jsonify, render_template, redirect, url_for
import json
import os
from datetime import datetime
import uuid

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads/registrations'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}
REGISTRATIONS_FILE = 'data/registrations.json'

# Ensure directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs('data', exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def load_registrations():
    """Load existing registrations from JSON file"""
    try:
        with open(REGISTRATIONS_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_registration(registration_data):
    """Save new registration to JSON file"""
    registrations = load_registrations()
    registrations.append(registration_data)
    
    with open(REGISTRATIONS_FILE, 'w') as f:
        json.dump(registrations, f, indent=2)

@app.route('/registration')
def registration_page():
    """Serve the registration form"""
    return render_template('registration/land_claim_registration.html')

@app.route('/api/register-claim', methods=['POST'])
def register_claim():
    """Handle land claim registration submission"""
    try:
        # Generate unique application ID
        application_id = f"FRA{datetime.now().strftime('%Y%m%d')}{str(uuid.uuid4())[:8].upper()}"
        
        # Extract form data
        registration_data = {
            'application_id': application_id,
            'submission_date': datetime.now().isoformat(),
            'status': 'submitted',
            'personal_details': {
                'applicant_name': request.form.get('applicantName'),
                'father_name': request.form.get('fatherName'),
                'aadhaar': request.form.get('aadhaar'),
                'phone': request.form.get('phone'),
                'tribe': request.form.get('tribe'),
                'family_members': int(request.form.get('familyMembers', 0)),
                'address': {
                    'village': request.form.get('village'),
                    'tehsil': request.form.get('tehsil'),
                    'district': request.form.get('district'),
                    'state': request.form.get('state')
                }
            },
            'land_details': {
                'claim_type': request.form.get('claimType'),
                'land_area': float(request.form.get('landArea', 0)),
                'occupation_since': int(request.form.get('occupationSince', 0)),
                'forest_type': request.form.get('forestType'),
                'survey_number': request.form.get('surveyNumber'),
                'boundaries': request.form.get('boundaries'),
                'land_use': request.form.getlist('landUse')
            },
            'remarks': request.form.get('remarks'),
            'documents': {}
        }
        
        # Handle file uploads
        uploaded_files = {}
        for field_name in ['aadhaarDoc', 'tribalCert', 'occupationProof', 'photograph', 'additionalDocs']:
            if field_name in request.files:
                files = request.files.getlist(field_name)
                file_paths = []
                
                for file in files:
                    if file and file.filename and allowed_file(file.filename):
                        # Create unique filename
                        filename = f"{application_id}_{field_name}_{uuid.uuid4().hex[:8]}.{file.filename.rsplit('.', 1)[1].lower()}"
                        file_path = os.path.join(UPLOAD_FOLDER, filename)
                        file.save(file_path)
                        file_paths.append(filename)
                
                if file_paths:
                    uploaded_files[field_name] = file_paths if len(file_paths) > 1 else file_paths[0]
        
        registration_data['documents'] = uploaded_files
        
        # Save registration
        save_registration(registration_data)
        
        # Calculate approval probability using the existing prediction logic
        approval_data = calculate_approval_probability(registration_data)
        registration_data['prediction'] = approval_data
        
        return jsonify({
            'success': True,
            'application_id': application_id,
            'message': 'Registration submitted successfully!',
            'approval_probability': approval_data,
            'next_steps': [
                'Visit Gram Sabha for community verification',
                'Submit application to Sub-Divisional Level Committee (SDLC)',
                'Await field verification by forest officials',
                'Track application status online'
            ]
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'message': 'Registration failed. Please try again.'
        }), 500

def calculate_approval_probability(registration_data):
    """Calculate FRA approval probability based on registration data"""
    try:
        land_details = registration_data['land_details']
        personal_details = registration_data['personal_details']
        
        # Extract key factors
        land_area = land_details.get('land_area', 0)
        family_members = personal_details.get('family_members', 1)
        occupation_since = land_details.get('occupation_since', 2000)
        claim_type = land_details.get('claim_type', '')
        
        # Basic scoring algorithm
        score = 0.5  # Base score
        
        # Land area factor (smaller areas have higher approval rates)
        if land_area <= 2.0:
            score += 0.2
        elif land_area <= 4.0:
            score += 0.1
        else:
            score -= 0.1
        
        # Family size factor
        if family_members >= 3:
            score += 0.1
        
        # Occupation period factor (longer occupation = higher approval)
        occupation_years = 2005 - occupation_since
        if occupation_years >= 20:
            score += 0.2
        elif occupation_years >= 10:
            score += 0.1
        
        # Claim type factor
        if 'Individual' in claim_type:
            score += 0.1
        elif 'Community' in claim_type:
            score += 0.05
        
        # Ensure score is between 0 and 1
        score = max(0.1, min(0.95, score))
        
        # Determine assessment level
        if score >= 0.7:
            assessment = "High"
            recommendation = "Strong case with good approval chances. Ensure all documents are complete."
        elif score >= 0.5:
            assessment = "Medium"
            recommendation = "Moderate approval chances. Strengthen documentation and community support."
        else:
            assessment = "Low"
            recommendation = "Consider improving documentation and seeking legal assistance."
        
        return {
            'probability': round(score, 3),
            'percentage': f"{score * 100:.1f}%",
            'assessment': assessment,
            'recommendation': recommendation,
            'factors': {
                'land_area': land_area,
                'family_size': family_members,
                'occupation_years': occupation_years,
                'claim_type': claim_type
            }
        }
        
    except Exception as e:
        return {
            'probability': 0.5,
            'percentage': "50.0%",
            'assessment': "Unknown",
            'recommendation': "Unable to calculate. Please ensure all data is provided correctly.",
            'error': str(e)
        }

@app.route('/api/check-status/<application_id>')
def check_application_status(application_id):
    """Check the status of a land claim application"""
    registrations = load_registrations()
    
    for registration in registrations:
        if registration['application_id'] == application_id:
            return jsonify({
                'success': True,
                'application': registration
            })
    
    return jsonify({
        'success': False,
        'message': 'Application not found'
    }), 404

@app.route('/api/registrations')
def get_all_registrations():
    """Get all registrations (for admin dashboard)"""
    registrations = load_registrations()
    
    # Calculate statistics
    stats = {
        'total_applications': len(registrations),
        'submitted': len([r for r in registrations if r.get('status') == 'submitted']),
        'under_review': len([r for r in registrations if r.get('status') == 'under_review']),
        'approved': len([r for r in registrations if r.get('status') == 'approved']),
        'rejected': len([r for r in registrations if r.get('status') == 'rejected']),
        'total_land_area': sum([r['land_details']['land_area'] for r in registrations]),
        'total_families': sum([r['personal_details']['family_members'] for r in registrations])
    }
    
    return jsonify({
        'success': True,
        'registrations': registrations,
        'statistics': stats
    })

@app.route('/registration/status')
def status_page():
    """Serve the status checking page"""
    return render_template('registration/status_check.html')

@app.route('/registration/admin')
def admin_dashboard():
    """Serve the admin dashboard for registration management"""
    return render_template('registration/admin_dashboard.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
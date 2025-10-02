from flask import Flask

app = Flask(__name__)

@app.route('/registration')
def test_registration():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Land Claim Registration - VanMitra</title>
        <meta charset="UTF-8">
        <style>
            body { 
                font-family: Arial, sans-serif; 
                background: linear-gradient(135deg, #2d5016, #4a7c59);
                color: white; 
                margin: 0; 
                padding: 20px; 
            }
            .container { 
                max-width: 800px; 
                margin: 0 auto; 
                background: rgba(255,255,255,0.9); 
                border-radius: 15px; 
                padding: 30px; 
                color: #333; 
            }
            .header { text-align: center; margin-bottom: 30px; }
            .header h1 { color: #2d5016; font-size: 2.5em; }
            .form-group { margin: 20px 0; }
            .form-group label { display: block; margin-bottom: 5px; font-weight: bold; }
            .form-group input, .form-group select { 
                width: 100%; 
                padding: 10px; 
                border: 2px solid #ddd; 
                border-radius: 5px; 
                font-size: 16px; 
            }
            .btn { 
                background: #6ab04c; 
                color: white; 
                padding: 15px 30px; 
                border: none; 
                border-radius: 5px; 
                font-size: 16px; 
                cursor: pointer; 
                width: 100%; 
                margin-top: 20px; 
            }
            .btn:hover { background: #5a9a3c; }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🌿 Forest Rights Act Registration</h1>
                <p>Register your land claim under the Forest Rights Act</p>
            </div>
            
            <form action="/api/register-claim" method="POST">
                <div class="form-group">
                    <label for="name">Applicant Name</label>
                    <input type="text" id="name" name="applicantName" required>
                </div>
                
                <div class="form-group">
                    <label for="father">Father's Name</label>
                    <input type="text" id="father" name="fatherName" required>
                </div>
                
                <div class="form-group">
                    <label for="aadhaar">Aadhaar Number</label>
                    <input type="text" id="aadhaar" name="aadhaar" required>
                </div>
                
                <div class="form-group">
                    <label for="phone">Phone Number</label>
                    <input type="tel" id="phone" name="phone" required>
                </div>
                
                <div class="form-group">
                    <label for="tribe">Tribe/Community</label>
                    <select id="tribe" name="tribe" required>
                        <option value="">Select Tribe</option>
                        <option value="Gond">Gond</option>
                        <option value="Baiga">Baiga</option>
                        <option value="Korku">Korku</option>
                        <option value="Bhil">Bhil</option>
                        <option value="Other">Other</option>
                    </select>
                </div>
                
                <div class="form-group">
                    <label for="village">Village</label>
                    <input type="text" id="village" name="village" required>
                </div>
                
                <div class="form-group">
                    <label for="district">District</label>
                    <input type="text" id="district" name="district" required>
                </div>
                
                <div class="form-group">
                    <label for="landArea">Land Area (in hectares)</label>
                    <input type="number" step="0.1" id="landArea" name="landArea" required>
                </div>
                
                <button type="submit" class="btn">📝 Submit Registration</button>
            </form>
            
            <div style="text-align: center; margin-top: 20px;">
                <a href="/" style="color: #6ab04c;">← Back to Homepage</a>
            </div>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True, port=5001)
#!/usr/bin/env python3
"""
Simple server test to verify Flask app is accessible
"""

import requests
import time

def test_server():
    print("🔍 Testing VanMitra Server Connection...")
    print("=" * 50)
    
    base_url = "http://127.0.0.1:5000"
    
    # Test endpoints
    endpoints = [
        ("/", "Main Page"),
        ("/voice-feedback", "Voice Feedback Page"),
        ("/voice-analytics", "Analytics Dashboard"),
        ("/process-demo-voice", "Demo Voice Processing")
    ]
    
    for endpoint, description in endpoints:
        url = base_url + endpoint
        try:
            print(f"\n🌐 Testing: {description}")
            print(f"URL: {url}")
            
            response = requests.get(url, timeout=5)
            
            if response.status_code == 200:
                print(f"✅ SUCCESS: {response.status_code} - {description} is working")
                print(f"📄 Content length: {len(response.text)} characters")
            else:
                print(f"⚠️  WARNING: {response.status_code} - Unexpected status code")
                
        except requests.exceptions.ConnectionError:
            print(f"❌ ERROR: Cannot connect to {url}")
            print("   Server might not be running or port blocked")
        except requests.exceptions.Timeout:
            print(f"⏰ TIMEOUT: Server took too long to respond")
        except Exception as e:
            print(f"❌ ERROR: {str(e)}")
    
    print("\n" + "=" * 50)
    print("🎯 QUICK ACCESS LINKS:")
    print(f"🏠 Main Dashboard: {base_url}")
    print(f"🎤 Voice Feedback: {base_url}/voice-feedback")
    print(f"📊 Analytics: {base_url}/voice-analytics")
    
    print("\n💡 If you still can't access:")
    print("1. Try http://localhost:5000 instead of 127.0.0.1")
    print("2. Check Windows Firewall settings")
    print("3. Try a different browser or incognito mode")
    print("4. Make sure no antivirus is blocking the connection")

if __name__ == "__main__":
    test_server()
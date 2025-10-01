#!/usr/bin/env python3
"""
Simple connectivity test for VanMitra server
"""
import urllib.request
import urllib.error

def test_connection():
    urls = [
        "http://localhost:5000",
        "http://127.0.0.1:5000",
        "http://192.168.248.65:5000"
    ]
    
    print("🔍 Testing VanMitra Server Connectivity...")
    print("=" * 50)
    
    for url in urls:
        try:
            print(f"\n🌐 Testing: {url}")
            response = urllib.request.urlopen(url, timeout=5)
            if response.getcode() == 200:
                print(f"✅ SUCCESS: Server is accessible at {url}")
                content = response.read().decode('utf-8')
                if "VanMitra" in content:
                    print("📄 Confirmed: VanMitra application is running correctly")
                return url
            else:
                print(f"⚠️ WARNING: Server responded with status {response.getcode()}")
        except urllib.error.URLError as e:
            print(f"❌ ERROR: Cannot connect - {str(e)}")
        except Exception as e:
            print(f"❌ ERROR: {str(e)}")
    
    print("\n❌ Could not connect to any URL")
    return None

if __name__ == "__main__":
    working_url = test_connection()
    
    if working_url:
        print(f"\n🎯 SUCCESS! Your VanMitra app is accessible at:")
        print(f"🏠 Main Dashboard: {working_url}")
        print(f"🎤 Voice Feedback: {working_url}/voice-feedback")
        print(f"📊 Analytics: {working_url}/voice-analytics")
    else:
        print("\n🔧 Troubleshooting suggestions:")
        print("1. Check Windows Firewall settings")
        print("2. Try running as administrator")
        print("3. Check if antivirus is blocking connections")
        print("4. Try a different port (modify app.py)")
    
    print("\n✨ Happy testing!")
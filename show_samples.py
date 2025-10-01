#!/usr/bin/env python3
"""
Quick Sample Data Display for VanMitra
Shows sample data examples directly in terminal
"""

def show_samples():
    print("🌿 VanMitra - Sample Data Examples")
    print("=" * 60)
    
    print("\n🎤 VOICE FEEDBACK SAMPLES")
    print("-" * 30)
    
    voice_samples = [
        {
            "id": "VF20241001001",
            "language": "Hindi",
            "original": "हमारे जंगल में अवैध कटाई हो रही है। वन विभाग को तुरंत कार्रवाई करनी चाहिए।",
            "translation": "Illegal cutting is happening in our forest. Forest department should take immediate action.",
            "sentiment": "Negative (-0.75)",
            "keywords": ["forest", "illegal", "cutting", "department", "action"],
            "category": "Forest Rights",
            "priority": "High",
            "actions": ["Contact forest department", "Legal aid consultation"]
        },
        {
            "id": "VF20241001002", 
            "language": "Bengali",
            "original": "আমাদের গ্রামে স্বাস্থ্য কেন্দ্র খুবই প্রয়োজন। নিকটতম হাসপাতাল অনেক দূরে।",
            "translation": "Our village desperately needs a health center. The nearest hospital is very far.",
            "sentiment": "Negative (-0.45)",
            "keywords": ["village", "health", "center", "hospital", "far"],
            "category": "Healthcare", 
            "priority": "Medium",
            "actions": ["Health department contact", "Mobile health camp request"]
        },
        {
            "id": "VF20241001003",
            "language": "English",
            "original": "The new digital FRA process is much more transparent and faster than before. We appreciate this improvement.",
            "translation": "The new digital FRA process is much more transparent and faster than before. We appreciate this improvement.",
            "sentiment": "Positive (+0.62)",
            "keywords": ["digital", "process", "transparent", "faster", "improvement"],
            "category": "General Community Issue",
            "priority": "Low",
            "actions": ["Document positive feedback", "Share best practices"]
        }
    ]
    
    for sample in voice_samples:
        print(f"\n📝 {sample['id']} ({sample['language']})")
        print(f"Original: {sample['original']}")
        print(f"Translation: {sample['translation']}")
        print(f"Sentiment: {sample['sentiment']}")
        print(f"Keywords: {', '.join(sample['keywords'])}")
        print(f"Category: {sample['category']} | Priority: {sample['priority']}")
        print(f"Actions: {', '.join(sample['actions'])}")
    
    print("\n" + "=" * 60)
    print("\n📊 FRA CLAIMS SAMPLES")
    print("-" * 30)
    
    fra_samples = [
        {
            "claim_id": "FRA20240001",
            "community": "Gond",
            "state": "Chhattisgarh", 
            "area": "245.7 hectares",
            "families": 45,
            "status": "Approved",
            "probability": "87%",
            "date": "2024-03-15"
        },
        {
            "claim_id": "FRA20240002",
            "community": "Santhal",
            "state": "Jharkhand",
            "area": "156.3 hectares", 
            "families": 32,
            "status": "Pending",
            "probability": "62%",
            "date": "2024-08-22"
        },
        {
            "claim_id": "FRA20240003",
            "community": "Bhil",
            "state": "Rajasthan",
            "area": "89.2 hectares",
            "families": 18,
            "status": "Under Review", 
            "probability": "74%",
            "date": "2024-09-10"
        }
    ]
    
    for claim in fra_samples:
        print(f"\n🏘️ {claim['claim_id']} - {claim['community']} Community")
        print(f"Location: {claim['state']}")
        print(f"Area: {claim['area']} | Families: {claim['families']}")
        print(f"Status: {claim['status']} | Approval Probability: {claim['probability']}")
        print(f"Submitted: {claim['date']}")
    
    print("\n" + "=" * 60)
    print("\n📈 ANALYTICS DASHBOARD SAMPLES")
    print("-" * 30)
    
    analytics = {
        "total_claims": 247,
        "approved": 89,
        "pending": 112, 
        "rejected": 46,
        "voice_feedback": 156,
        "positive_sentiment": 67,
        "negative_sentiment": 58,
        "neutral_sentiment": 31
    }
    
    print(f"📊 Total FRA Claims: {analytics['total_claims']}")
    print(f"   ✅ Approved: {analytics['approved']} ({analytics['approved']/analytics['total_claims']*100:.1f}%)")
    print(f"   ⏳ Pending: {analytics['pending']} ({analytics['pending']/analytics['total_claims']*100:.1f}%)")
    print(f"   ❌ Rejected: {analytics['rejected']} ({analytics['rejected']/analytics['total_claims']*100:.1f}%)")
    
    print(f"\n🎤 Voice Feedback: {analytics['voice_feedback']} total")
    print(f"   😊 Positive: {analytics['positive_sentiment']} ({analytics['positive_sentiment']/analytics['voice_feedback']*100:.1f}%)")
    print(f"   😞 Negative: {analytics['negative_sentiment']} ({analytics['negative_sentiment']/analytics['voice_feedback']*100:.1f}%)")
    print(f"   😐 Neutral: {analytics['neutral_sentiment']} ({analytics['neutral_sentiment']/analytics['voice_feedback']*100:.1f}%)")
    
    print("\n" + "=" * 60)
    print("\n🚀 HOW TO USE THESE SAMPLES")
    print("-" * 30)
    print("1. 🎤 Voice Feedback: Go to http://127.0.0.1:5000/voice-feedback")
    print("   • Click 'Try Demo Voice' to see sample processing")
    print("   • Upload any audio file to test real processing")
    
    print("\n2. 📊 Analytics: Go to http://127.0.0.1:5000/voice-analytics") 
    print("   • View dashboard with sample charts and data")
    print("   • See trends and distribution visualizations")
    
    print("\n3. 🤖 FRA Predictor: Go to http://127.0.0.1:5000/")
    print("   • Test with sample values: 25 claims, 150 hectares")
    print("   • Try different combinations to see predictions")
    
    print("\n✨ All sample data is realistic and ready for demonstration!")

if __name__ == "__main__":
    show_samples()
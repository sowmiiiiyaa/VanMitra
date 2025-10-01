#!/usr/bin/env python3
"""
Sample Data Generator for VanMitra FRA System
Generates realistic sample data for testing and demonstration
"""

import json
import random
from datetime import datetime, timedelta
import os

class VanMitraSampleGenerator:
    def __init__(self):
        self.tribal_communities = [
            "Gond", "Santhal", "Bhil", "Munda", "Ho", "Kurukh", "Khasi", 
            "Meena", "Bodo", "Rabha", "Dimasa", "Karbi", "Mizo", "Naga"
        ]
        
        self.states = [
            "Jharkhand", "Chhattisgarh", "Odisha", "Madhya Pradesh", 
            "Maharashtra", "Rajasthan", "Gujarat", "Assam", "Meghalaya", 
            "Tripura", "Mizoram", "Nagaland", "Manipur", "Arunachal Pradesh"
        ]
        
        self.issue_types = [
            "Forest Rights", "Healthcare", "Education", "Water Supply", 
            "Employment", "Infrastructure", "Land Rights", "Cultural Preservation"
        ]
        
        self.voice_samples = [
            {
                "language": "Hindi",
                "text": "हमारे जंगल में अवैध कटाई हो रही है। वन विभाग को तुरंत कार्रवाई करनी चाहिए।",
                "translation": "Illegal cutting is happening in our forest. Forest department should take immediate action.",
                "sentiment": "Negative",
                "priority": "High"
            },
            {
                "language": "Bengali", 
                "text": "আমাদের গ্রামে স্বাস্থ্য কেন্দ্র খুবই প্রয়োজন। নিকটতম হাসপাতাল অনেক দূরে।",
                "translation": "Our village desperately needs a health center. The nearest hospital is very far.",
                "sentiment": "Negative",
                "priority": "Medium"
            },
            {
                "language": "Kannada",
                "text": "ನಮ್ಮ ಮಕ್ಕಳಿಗೆ ಉತ್ತಮ ಶಿಕ್ಷಣ ಸೌಲಭ್ಯ ಬೇಕು। ಸರ್ಕಾರ ಸಹಾಯ ಮಾಡಬೇಕು।",
                "translation": "Our children need better educational facilities. Government should help us.",
                "sentiment": "Neutral",
                "priority": "Medium"
            },
            {
                "language": "English",
                "text": "The new digital FRA process is much more transparent and faster than before. We appreciate this improvement.",
                "translation": "The new digital FRA process is much more transparent and faster than before. We appreciate this improvement.",
                "sentiment": "Positive", 
                "priority": "Low"
            },
            {
                "language": "Tamil",
                "text": "எங்கள் கிராமத்தில் தண்ணீர் பஞ்சம் உள்ளது। உடனடி நடவடிக்கை தேவை।",
                "translation": "There is water scarcity in our village. Immediate action is needed.",
                "sentiment": "Negative",
                "priority": "High"
            }
        ]

    def generate_fra_claims_data(self, count=50):
        """Generate sample FRA claims data"""
        claims = []
        
        for i in range(count):
            claim = {
                "claim_id": f"FRA{2024}{str(i+1).zfill(4)}",
                "community": random.choice(self.tribal_communities),
                "state": random.choice(self.states),
                "district": f"District_{random.randint(1, 30)}",
                "village": f"Village_{random.randint(1, 500)}",
                "forest_area_hectares": round(random.uniform(10, 1000), 2),
                "number_of_families": random.randint(5, 200),
                "claim_type": random.choice(["Individual", "Community", "Mixed"]),
                "status": random.choice(["Pending", "Approved", "Rejected", "Under Review"]),
                "submission_date": (datetime.now() - timedelta(days=random.randint(1, 365))).strftime("%Y-%m-%d"),
                "approval_probability": round(random.uniform(0.1, 0.95), 2),
                "priority": random.choice(["High", "Medium", "Low"])
            }
            claims.append(claim)
        
        return claims

    def generate_voice_feedback_data(self, count=20):
        """Generate sample voice feedback analysis results"""
        feedback_data = []
        
        for i in range(count):
            sample = random.choice(self.voice_samples)
            
            feedback = {
                "feedback_id": f"VF{datetime.now().strftime('%Y%m%d')}{str(i+1).zfill(3)}",
                "timestamp": (datetime.now() - timedelta(hours=random.randint(1, 168))).isoformat(),
                "community": random.choice(self.tribal_communities),
                "state": random.choice(self.states),
                "original_language": sample["language"],
                "original_text": sample["text"],
                "english_translation": sample["translation"],
                "sentiment": sample["sentiment"],
                "sentiment_scores": {
                    "positive": round(random.uniform(0, 1), 3),
                    "negative": round(random.uniform(0, 1), 3),
                    "neutral": round(random.uniform(0, 1), 3),
                    "compound": round(random.uniform(-1, 1), 3)
                },
                "keywords": self.extract_keywords(sample["translation"]),
                "issue_category": random.choice(self.issue_types),
                "priority_level": sample["priority"],
                "urgency_indicators": self.get_urgency_indicators(sample["sentiment"]),
                "recommended_actions": self.get_recommendations(random.choice(self.issue_types))
            }
            feedback_data.append(feedback)
        
        return feedback_data

    def extract_keywords(self, text):
        """Extract sample keywords from text"""
        words = text.lower().split()
        keywords = []
        important_words = ["forest", "health", "education", "water", "government", 
                          "village", "children", "hospital", "school", "rights"]
        
        for word in words:
            clean_word = word.strip(".,!?")
            if clean_word in important_words or len(clean_word) > 6:
                keywords.append(clean_word)
        
        return list(set(keywords))[:5]

    def get_urgency_indicators(self, sentiment):
        """Get urgency indicators based on sentiment"""
        if sentiment == "Negative":
            return random.choice([
                ["High negative sentiment detected", "Urgent language used"],
                ["Community distress indicators"], 
                ["Immediate attention required"]
            ])
        elif sentiment == "Positive":
            return []
        else:
            return random.choice([[], ["Follow-up recommended"]])

    def get_recommendations(self, issue_type):
        """Get recommendations based on issue type"""
        recommendations = {
            "Forest Rights": ["Contact forest department", "Legal aid consultation", "Community meeting"],
            "Healthcare": ["Reach out to health department", "Mobile health camp request", "NGO assistance"],
            "Education": ["Contact education department", "Teacher recruitment request", "Infrastructure development"],
            "Water Supply": ["Water department notification", "Bore well request", "Pipeline extension"],
            "Employment": ["Skill development programs", "MGNREGA enrollment", "Self-help group formation"],
            "Infrastructure": ["Local development authority", "Road construction request", "Electricity board contact"]
        }
        return recommendations.get(issue_type, ["General administrative support"])

    def generate_analytics_data(self):
        """Generate sample analytics and dashboard data"""
        analytics = {
            "overview_stats": {
                "total_claims": random.randint(200, 500),
                "approved_claims": random.randint(50, 150),
                "pending_claims": random.randint(80, 200),
                "rejected_claims": random.randint(20, 80),
                "total_voice_feedback": random.randint(100, 300),
                "positive_feedback": random.randint(30, 100),
                "negative_feedback": random.randint(40, 120),
                "neutral_feedback": random.randint(20, 80)
            },
            "monthly_trends": {
                "claims_submitted": [random.randint(10, 50) for _ in range(12)],
                "approval_rate": [round(random.uniform(0.3, 0.8), 2) for _ in range(12)],
                "voice_feedback_count": [random.randint(5, 25) for _ in range(12)]
            },
            "state_wise_distribution": {
                state: random.randint(10, 100) for state in self.states[:10]
            },
            "community_wise_stats": {
                community: random.randint(5, 50) for community in self.tribal_communities[:8]
            }
        }
        return analytics

    def save_sample_data(self):
        """Save all sample data to files"""
        os.makedirs("sample_data", exist_ok=True)
        
        # Generate and save FRA claims data
        claims_data = self.generate_fra_claims_data(50)
        with open("sample_data/fra_claims_sample.json", "w", encoding="utf-8") as f:
            json.dump(claims_data, f, indent=2, ensure_ascii=False)
        
        # Generate and save voice feedback data
        voice_data = self.generate_voice_feedback_data(20)
        with open("sample_data/voice_feedback_sample.json", "w", encoding="utf-8") as f:
            json.dump(voice_data, f, indent=2, ensure_ascii=False)
        
        # Generate and save analytics data
        analytics_data = self.generate_analytics_data()
        with open("sample_data/analytics_sample.json", "w", encoding="utf-8") as f:
            json.dump(analytics_data, f, indent=2, ensure_ascii=False)
        
        # Generate sample CSV for Excel import
        self.generate_csv_samples()
        
        return {
            "fra_claims": len(claims_data),
            "voice_feedback": len(voice_data),
            "analytics": "Generated",
            "files_created": [
                "sample_data/fra_claims_sample.json",
                "sample_data/voice_feedback_sample.json", 
                "sample_data/analytics_sample.json",
                "sample_data/fra_claims_sample.csv",
                "sample_data/voice_feedback_sample.csv"
            ]
        }

    def generate_csv_samples(self):
        """Generate CSV files for easy import"""
        import csv
        
        # FRA Claims CSV
        claims_data = self.generate_fra_claims_data(30)
        with open("sample_data/fra_claims_sample.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=claims_data[0].keys())
            writer.writeheader()
            writer.writerows(claims_data)
        
        # Voice Feedback CSV
        voice_data = self.generate_voice_feedback_data(15)
        # Flatten the nested dictionaries for CSV
        flattened_voice = []
        for item in voice_data:
            flat_item = item.copy()
            flat_item.update({
                "sentiment_positive": item["sentiment_scores"]["positive"],
                "sentiment_negative": item["sentiment_scores"]["negative"],
                "sentiment_neutral": item["sentiment_scores"]["neutral"],
                "sentiment_compound": item["sentiment_scores"]["compound"],
                "keywords_list": ", ".join(item["keywords"]),
                "urgency_indicators_list": ", ".join(item["urgency_indicators"]),
                "recommended_actions_list": ", ".join(item["recommended_actions"])
            })
            # Remove nested dictionaries
            del flat_item["sentiment_scores"]
            del flat_item["keywords"] 
            del flat_item["urgency_indicators"]
            del flat_item["recommended_actions"]
            flattened_voice.append(flat_item)
        
        with open("sample_data/voice_feedback_sample.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=flattened_voice[0].keys())
            writer.writeheader()
            writer.writerows(flattened_voice)

    def print_sample_overview(self):
        """Print a sample overview"""
        print("🌿 VanMitra Sample Data Overview")
        print("=" * 50)
        
        print("\n📊 FRA Claims Sample:")
        claims = self.generate_fra_claims_data(3)
        for claim in claims:
            print(f"  • {claim['claim_id']}: {claim['community']} community in {claim['state']}")
            print(f"    Area: {claim['forest_area_hectares']} hectares | Status: {claim['status']}")
        
        print("\n🎤 Voice Feedback Sample:")
        voice = self.generate_voice_feedback_data(3)
        for feedback in voice:
            print(f"  • {feedback['feedback_id']}: {feedback['original_language']} feedback")
            print(f"    Sentiment: {feedback['sentiment']} | Priority: {feedback['priority_level']}")
            print(f"    Issue: {feedback['issue_category']}")
        
        print("\n📈 Analytics Sample:")
        analytics = self.generate_analytics_data()
        stats = analytics["overview_stats"]
        print(f"  • Total Claims: {stats['total_claims']}")
        print(f"  • Approved: {stats['approved_claims']} | Pending: {stats['pending_claims']}")
        print(f"  • Voice Feedback: {stats['total_voice_feedback']}")
        print(f"  • Sentiment: {stats['positive_feedback']} positive, {stats['negative_feedback']} negative")

def main():
    print("🎯 VanMitra Sample Data Generator")
    print("=" * 40)
    
    generator = VanMitraSampleGenerator()
    
    # Print sample overview
    generator.print_sample_overview()
    
    print("\n" + "=" * 40)
    print("💾 Generating complete sample dataset...")
    
    # Save all sample data
    result = generator.save_sample_data()
    
    print(f"\n✅ Sample data generated successfully!")
    print(f"📁 Files created: {len(result['files_created'])}")
    print(f"📊 FRA Claims: {result['fra_claims']} samples")
    print(f"🎤 Voice Feedback: {result['voice_feedback']} samples")
    
    print("\n📂 Files saved in 'sample_data' directory:")
    for file in result['files_created']:
        print(f"  • {file}")
    
    print("\n🚀 Ready to use with VanMitra system!")

if __name__ == "__main__":
    main()
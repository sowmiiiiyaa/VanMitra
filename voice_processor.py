"""
Voice Notes Processing Pipeline for Tribal Community Feedback
Processes voice notes through speech-to-text, translation, sentiment analysis, and insights generation
"""

import os
import json
import re
from datetime import datetime
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer
from collections import Counter
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class VoiceNotesProcessor:
    def __init__(self):
        """Initialize the voice notes processor with required NLTK data"""
        self.setup_nltk()
        self.sia = SentimentIntensityAnalyzer()
        
    def setup_nltk(self):
        """Download required NLTK data"""
        try:
            nltk.data.find('tokenizers/punkt')
            nltk.data.find('corpora/stopwords')
            nltk.data.find('vader_lexicon')
        except LookupError:
            logger.info("Downloading required NLTK data...")
            nltk.download('punkt', quiet=True)
            nltk.download('stopwords', quiet=True)
            nltk.download('vader_lexicon', quiet=True)
    
    def speech_to_text(self, audio_path):
        """
        Convert speech to text using OpenAI Whisper (or dummy data for testing)
        Args: audio_path (str): Path to audio file
        Returns: str: Transcribed text
        """
        try:
            # For production, uncomment and use actual Whisper:
            # import whisper
            # model = whisper.load_model("base")
            # result = model.transcribe(audio_path)
            # return result['text']
            
            # Dummy data for testing (simulating various regional languages)
            dummy_texts = [
                "यह एक परीक्षण वॉयस नोट है। हमारे समुदाय को वन अधिकार की समस्या है।",
                "আমাদের গ্রামে জল সরবরাহের সমস্যা আছে। সরকারের সাহায্য চাই।",
                "ನಮ್ಮ ಸಮುದಾಯಕ್ಕೆ ಶಿಕ್ಷಣ ಸೌಲಭ್ಯಗಳು ಬೇಕು। ಮಕ್ಕಳಿಗೆ ಶಾಲೆ ದೂರದಲ್ಲಿದೆ।",
                "हमारे जंगल में अवैध कटाई हो रही है। वन विभाग को इसकी जानकारी देनी चाहिए।",
                "Our community needs better healthcare facilities. The nearest hospital is very far."
            ]
            
            # Simulate processing by returning one of the dummy texts
            import random
            transcribed_text = random.choice(dummy_texts)
            logger.info(f"Transcribed audio from {audio_path}")
            return transcribed_text
            
        except Exception as e:
            logger.error(f"Error in speech-to-text: {e}")
            return "Error in transcription"
    
    def translate_to_english(self, text):
        """
        Translate text to English using AI4Bharat or similar models
        Args: text (str): Input text in any language
        Returns: str: English translated text
        """
        try:
            # For production, use AI4Bharat or Google Translate API:
            # from transformers import pipeline
            # translator = pipeline("translation", model="ai4bharat/indictrans2-indic-en-1B")
            # result = translator(text)
            # return result[0]['translation_text']
            
            # Dummy translation mapping for testing
            translation_map = {
                "यह एक परीक्षण वॉयस नोट है। हमारे समुदाय को वन अधिकार की समस्या है।": 
                "This is a test voice note. Our community has forest rights issues.",
                
                "আমাদের গ্রামে জল সরবরাহের সমস্যা আছে। সরকারের সাহায্য চাই।": 
                "Our village has water supply problems. We need government assistance.",
                
                "ನಮ್ಮ ಸಮುದಾಯಕ್ಕೆ ಶಿಕ್ಷಣ ಸೌಲಭ್ಯಗಳು ಬೇಕು। ಮಕ್ಕಳಿಗೆ ಶಾಲೆ ದೂರದಲ್ಲಿದೆ।": 
                "Our community needs educational facilities. The school is far for children.",
                
                "हमारे जंगल में अवैध कटाई हो रही है। वन विभाग को इसकी जानकारी देनी चाहिए।": 
                "Illegal cutting is happening in our forest. Forest department should be informed about this.",
                
                "Our community needs better healthcare facilities. The nearest hospital is very far.": 
                "Our community needs better healthcare facilities. The nearest hospital is very far."
            }
            
            english_text = translation_map.get(text, text)
            logger.info("Text translated to English")
            return english_text
            
        except Exception as e:
            logger.error(f"Error in translation: {e}")
            return text  # Return original text if translation fails
    
    def analyze_sentiment(self, text):
        """
        Analyze sentiment using NLTK's VADER sentiment analyzer
        Args: text (str): English text
        Returns: dict: Sentiment analysis results
        """
        try:
            scores = self.sia.polarity_scores(text)
            
            # Determine overall sentiment
            if scores['compound'] >= 0.05:
                overall_sentiment = 'Positive'
            elif scores['compound'] <= -0.05:
                overall_sentiment = 'Negative'
            else:
                overall_sentiment = 'Neutral'
            
            return {
                'overall_sentiment': overall_sentiment,
                'positive_score': round(scores['pos'], 3),
                'negative_score': round(scores['neg'], 3),
                'neutral_score': round(scores['neu'], 3),
                'compound_score': round(scores['compound'], 3)
            }
            
        except Exception as e:
            logger.error(f"Error in sentiment analysis: {e}")
            return {'overall_sentiment': 'Neutral', 'error': str(e)}
    
    def extract_keywords(self, text, num_keywords=10):
        """
        Extract keywords and main topics from text
        Args: text (str): Input text
        Returns: list: List of important keywords
        """
        try:
            # Clean and tokenize text
            text = re.sub(r'[^\w\s]', '', text.lower())
            words = word_tokenize(text)
            
            # Remove stopwords
            stop_words = set(stopwords.words('english'))
            keywords = [word for word in words if word.isalpha() and len(word) > 2 and word not in stop_words]
            
            # Count frequency and return top keywords
            word_freq = Counter(keywords)
            top_keywords = [word for word, count in word_freq.most_common(num_keywords)]
            
            return top_keywords
            
        except Exception as e:
            logger.error(f"Error in keyword extraction: {e}")
            return []
    
    def categorize_issues(self, text):
        """
        Categorize the type of community issues mentioned
        Args: text (str): English text
        Returns: list: List of identified issue categories
        """
        categories = {
            'forest_rights': ['forest', 'rights', 'land', 'cutting', 'trees', 'deforestation'],
            'healthcare': ['health', 'hospital', 'medical', 'doctor', 'medicine', 'clinic'],
            'education': ['school', 'education', 'children', 'learning', 'teacher', 'books'],
            'water': ['water', 'supply', 'well', 'drinking', 'clean', 'pipeline'],
            'employment': ['job', 'work', 'employment', 'income', 'livelihood', 'wages'],
            'infrastructure': ['road', 'electricity', 'transport', 'bridge', 'building']
        }
        
        identified_categories = []
        text_lower = text.lower()
        
        for category, keywords in categories.items():
            if any(keyword in text_lower for keyword in keywords):
                identified_categories.append(category.replace('_', ' ').title())
        
        return identified_categories if identified_categories else ['General Community Issue']
    
    def generate_summary(self, text, max_sentences=2):
        """
        Generate a simple extractive summary
        Args: text (str): Input text
        Returns: str: Summary
        """
        try:
            sentences = sent_tokenize(text)
            if len(sentences) <= max_sentences:
                return text
            
            # Simple extractive summary - take first and last sentences
            summary = '. '.join(sentences[:max_sentences])
            return summary
            
        except Exception as e:
            logger.error(f"Error in summarization: {e}")
            return text[:100] + "..." if len(text) > 100 else text
    
    def generate_insights(self, sentiment_result, keywords, categories, summary):
        """
        Generate comprehensive insights from analysis results
        Args: Various analysis results
        Returns: dict: Comprehensive insights
        """
        insights = {
            'priority_level': 'Medium',
            'recommended_actions': [],
            'urgency_indicators': []
        }
        
        # Determine priority based on sentiment and categories
        if sentiment_result['overall_sentiment'] == 'Negative':
            if sentiment_result['compound_score'] < -0.5:
                insights['priority_level'] = 'High'
            else:
                insights['priority_level'] = 'Medium'
        elif sentiment_result['overall_sentiment'] == 'Positive':
            insights['priority_level'] = 'Low'
        
        # Generate recommendations based on categories
        action_map = {
            'Forest Rights': 'Contact forest department and legal aid services',
            'Healthcare': 'Reach out to health department and NGOs',
            'Education': 'Contact education department and local authorities',
            'Water': 'Alert water supply department and local representatives',
            'Employment': 'Connect with skill development and employment schemes',
            'Infrastructure': 'File request with local development authorities'
        }
        
        for category in categories:
            if category in action_map:
                insights['recommended_actions'].append(action_map[category])
        
        # Identify urgency indicators
        urgent_words = ['urgent', 'emergency', 'crisis', 'immediate', 'help', 'danger']
        if any(word in ' '.join(keywords) for word in urgent_words):
            insights['urgency_indicators'].append('Contains urgent language')
        
        if sentiment_result['negative_score'] > 0.7:
            insights['urgency_indicators'].append('High negative sentiment detected')
        
        return insights
    
    def process_voice_note(self, audio_path, save_results=True):
        """
        Complete pipeline to process a voice note
        Args: audio_path (str): Path to audio file
        Returns: dict: Complete analysis results
        """
        logger.info(f"Starting processing of voice note: {audio_path}")
        
        results = {
            'timestamp': datetime.now().isoformat(),
            'audio_file': audio_path,
            'processing_steps': {}
        }
        
        try:
            # Step 1: Speech to Text
            transcribed_text = self.speech_to_text(audio_path)
            results['processing_steps']['transcription'] = transcribed_text
            
            # Step 2: Translation
            english_text = self.translate_to_english(transcribed_text)
            results['processing_steps']['translation'] = english_text
            
            # Step 3: Sentiment Analysis
            sentiment_result = self.analyze_sentiment(english_text)
            results['processing_steps']['sentiment'] = sentiment_result
            
            # Step 4: Extract Keywords
            keywords = self.extract_keywords(english_text)
            results['processing_steps']['keywords'] = keywords
            
            # Step 5: Categorize Issues
            categories = self.categorize_issues(english_text)
            results['processing_steps']['categories'] = categories
            
            # Step 6: Generate Summary
            summary = self.generate_summary(english_text)
            results['processing_steps']['summary'] = summary
            
            # Step 7: Generate Insights
            insights = self.generate_insights(sentiment_result, keywords, categories, summary)
            results['processing_steps']['insights'] = insights
            
            # Final results
            results['final_analysis'] = {
                'original_text': transcribed_text,
                'english_text': english_text,
                'sentiment': sentiment_result['overall_sentiment'],
                'sentiment_scores': sentiment_result,
                'keywords': keywords[:5],  # Top 5 keywords
                'issue_categories': categories,
                'summary': summary,
                'priority_level': insights['priority_level'],
                'recommended_actions': insights['recommended_actions'],
                'urgency_indicators': insights['urgency_indicators']
            }
            
            # Save results if requested
            if save_results:
                self.save_results(results)
            
            logger.info("Voice note processing completed successfully")
            return results
            
        except Exception as e:
            logger.error(f"Error in processing voice note: {e}")
            results['error'] = str(e)
            return results
    
    def save_results(self, results):
        """Save processing results to JSON file"""
        try:
            # Create results directory if it doesn't exist
            os.makedirs('voice_analysis_results', exist_ok=True)
            
            # Generate filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"voice_analysis_results/analysis_{timestamp}.json"
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(results, f, indent=2, ensure_ascii=False)
            
            logger.info(f"Results saved to {filename}")
            
        except Exception as e:
            logger.error(f"Error saving results: {e}")
    
    def print_results(self, results):
        """Print formatted results to console"""
        if 'error' in results:
            print(f"❌ Error: {results['error']}")
            return
        
        analysis = results['final_analysis']
        
        print("\n" + "="*60)
        print("🎤 VOICE NOTE ANALYSIS RESULTS")
        print("="*60)
        
        print(f"\n📝 Original Text: {analysis['original_text']}")
        print(f"\n🔤 English Translation: {analysis['english_text']}")
        
        print(f"\n😊 Sentiment: {analysis['sentiment']}")
        print(f"   Positive: {analysis['sentiment_scores']['positive_score']}")
        print(f"   Negative: {analysis['sentiment_scores']['negative_score']}")
        print(f"   Neutral: {analysis['sentiment_scores']['neutral_score']}")
        print(f"   Compound: {analysis['sentiment_scores']['compound_score']}")
        
        print(f"\n🔑 Keywords: {', '.join(analysis['keywords'])}")
        print(f"\n📂 Issue Categories: {', '.join(analysis['issue_categories'])}")
        print(f"\n📋 Summary: {analysis['summary']}")
        
        print(f"\n⚡ Priority Level: {analysis['priority_level']}")
        
        if analysis['recommended_actions']:
            print(f"\n💡 Recommended Actions:")
            for action in analysis['recommended_actions']:
                print(f"   • {action}")
        
        if analysis['urgency_indicators']:
            print(f"\n🚨 Urgency Indicators:")
            for indicator in analysis['urgency_indicators']:
                print(f"   • {indicator}")
        
        print("\n" + "="*60)


# Example usage and testing
if __name__ == "__main__":
    # Initialize processor
    processor = VoiceNotesProcessor()
    
    # Test with dummy audio files
    test_files = [
        "sample_voice_note_1.wav",
        "sample_voice_note_2.mp3", 
        "sample_voice_note_3.wav"
    ]
    
    print("🎤 Testing Voice Notes Processing Pipeline")
    print("="*50)
    
    for audio_file in test_files:
        print(f"\n🎵 Processing: {audio_file}")
        results = processor.process_voice_note(audio_file)
        processor.print_results(results)
        print("\n" + "-"*50)
    
    print("\n✅ All tests completed!")
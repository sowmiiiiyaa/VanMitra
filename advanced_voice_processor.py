#!/usr/bin/env python3
"""
Advanced Voice Notes Processing Pipeline for Tribal Community Feedback
Supports OpenAI Whisper, AI4Bharat NLP, and comprehensive analysis
"""

import os
import json
import logging
import warnings
from datetime import datetime
from pathlib import Path
import numpy as np

# Suppress warnings for cleaner output
warnings.filterwarnings("ignore")

# Core libraries
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer
from collections import Counter

# Audio processing
try:
    import librosa
    AUDIO_SUPPORT = True
except ImportError:
    AUDIO_SUPPORT = False
    print("⚠️ librosa not installed. Audio file analysis will be limited.")

# AI/ML libraries
try:
    import whisper
    WHISPER_AVAILABLE = True
except ImportError:
    WHISPER_AVAILABLE = False
    print("⚠️ OpenAI Whisper not installed. Using dummy transcription.")

try:
    from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
    TRANSFORMERS_AVAILABLE = True
except ImportError:
    TRANSFORMERS_AVAILABLE = False
    print("⚠️ Transformers not installed. Using basic NLP methods.")

# Visualization
try:
    import matplotlib.pyplot as plt
    import seaborn as sns
    VISUALIZATION_AVAILABLE = True
except ImportError:
    VISUALIZATION_AVAILABLE = False
    print("⚠️ Matplotlib/Seaborn not installed. Text-only output.")

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class TribalVoiceProcessor:
    """
    Advanced Voice Processing Pipeline for Tribal Community Feedback
    Supports multiple languages and provides comprehensive analysis
    """
    
    def __init__(self, use_whisper=True, use_ai4bharat=True):
        """
        Initialize the voice processor with optional advanced features
        
        Args:
            use_whisper (bool): Whether to use OpenAI Whisper for speech-to-text
            use_ai4bharat (bool): Whether to use AI4Bharat models for translation
        """
        self.use_whisper = use_whisper and WHISPER_AVAILABLE
        self.use_ai4bharat = use_ai4bharat and TRANSFORMERS_AVAILABLE
        
        # Initialize NLTK data
        self._setup_nltk()
        
        # Load models
        self._load_models()
        
        # Sample data for demonstration
        self._setup_sample_data()
        
        logger.info("TribalVoiceProcessor initialized successfully")
    
    def _setup_nltk(self):
        """Download and setup required NLTK data"""
        required_nltk_data = [
            'punkt', 'stopwords', 'vader_lexicon', 'averaged_perceptron_tagger'
        ]
        
        for data_name in required_nltk_data:
            try:
                nltk.data.find(f'tokenizers/{data_name}')
            except LookupError:
                try:
                    nltk.data.find(f'corpora/{data_name}')
                except LookupError:
                    try:
                        nltk.data.find(f'sentiment/{data_name}')
                    except LookupError:
                        logger.info(f"Downloading NLTK data: {data_name}")
                        nltk.download(data_name, quiet=True)
        
        # Initialize sentiment analyzer
        self.sentiment_analyzer = SentimentIntensityAnalyzer()
    
    def _load_models(self):
        """Load AI models"""
        self.whisper_model = None
        self.translator = None
        self.summarizer = None
        self.classifier = None
        
        # Load Whisper model
        if self.use_whisper:
            try:
                logger.info("Loading Whisper model...")
                self.whisper_model = whisper.load_model("base")
                logger.info("Whisper model loaded successfully")
            except Exception as e:
                logger.error(f"Failed to load Whisper: {e}")
                self.use_whisper = False
        
        # Load AI4Bharat translator
        if self.use_ai4bharat:
            try:
                logger.info("Loading AI4Bharat translation model...")
                # Using IndicBART for Indian language translation
                self.translator = pipeline(
                    "translation", 
                    model="ai4bharat/IndicBARTSS",
                    tokenizer="ai4bharat/IndicBARTSS"
                )
                logger.info("AI4Bharat model loaded successfully")
            except Exception as e:
                logger.error(f"Failed to load AI4Bharat: {e}")
                self.use_ai4bharat = False
        
        # Load summarization model
        if TRANSFORMERS_AVAILABLE:
            try:
                logger.info("Loading summarization model...")
                self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
                logger.info("Summarization model loaded successfully")
            except Exception as e:
                logger.warning(f"Failed to load summarizer: {e}")
        
        # Load advanced sentiment classifier
        if TRANSFORMERS_AVAILABLE:
            try:
                logger.info("Loading advanced sentiment classifier...")
                self.classifier = pipeline("sentiment-analysis", 
                                         model="cardiffnlp/twitter-roberta-base-sentiment-latest")
                logger.info("Advanced sentiment classifier loaded successfully")
            except Exception as e:
                logger.warning(f"Failed to load advanced classifier: {e}")
    
    def _setup_sample_data(self):
        """Setup sample voice data for testing"""
        self.sample_voices = {
            "hindi_forest_rights": {
                "language": "Hindi",
                "text": "हमारे जंगल में अवैध कटाई हो रही है। वन विभाग को इसकी जानकारी देनी चाहिए। हमारे समुदाय के अधिकार संरक्षित होने चाहिए।",
                "translation": "Illegal cutting is happening in our forest. Forest department should be informed about this. Our community rights should be protected.",
                "audio_file": "sample_hindi_forest.wav"
            },
            "bengali_healthcare": {
                "language": "Bengali", 
                "text": "আমাদের গ্রামে স্বাস্থ্য কেন্দ্র নেই। নিকটতম হাসপাতাল ৫০ কিলোমিটার দূরে। গর্ভবতী মহিলা এবং শিশুদের জন্য এটি খুবই সমস্যা।",
                "translation": "There is no health center in our village. The nearest hospital is 50 kilometers away. This is a big problem for pregnant women and children.",
                "audio_file": "sample_bengali_health.wav"
            },
            "kannada_education": {
                "language": "Kannada",
                "text": "ನಮ್ಮ ಮಕ್ಕಳಿಗೆ ಉತ್ತಮ ಶಿಕ್ಷಣ ಸೌಲಭ್ಯ ಬೇಕು। ಶಾಲೆಯಲ್ಲಿ ಪುಸ್ತಕಗಳು ಮತ್ತು ಶಿಕ್ಷಕರ ಕೊರತೆ ಇದೆ। ಸರ್ಕಾರ ಈ ಸಮಸ್ಯೆಗೆ ಗಮನ ಕೊಡಬೇಕು।",
                "translation": "Our children need better educational facilities. There is a shortage of books and teachers in school. Government should pay attention to this problem.",
                "audio_file": "sample_kannada_education.wav"
            },
            "tamil_water": {
                "language": "Tamil",
                "text": "எங்கள் கிராமத்தில் தண்ணீர் பஞ்சம் உள்ளது। கிணறுகள் வறண்டு போயுள்ளன। குடிநீருக்காக மக்கள் மிகவும் சிரமப்படுகிறார்கள்।",
                "translation": "There is water scarcity in our village. Wells have dried up. People are struggling a lot for drinking water.",
                "audio_file": "sample_tamil_water.wav"
            },
            "english_positive": {
                "language": "English",
                "text": "The new government schemes are helping our community a lot. The forest rights process has become more transparent. We are happy with the digital initiatives.",
                "translation": "The new government schemes are helping our community a lot. The forest rights process has become more transparent. We are happy with the digital initiatives.",
                "audio_file": "sample_english_positive.wav"
            }
        }
    
    def speech_to_text(self, audio_file_path):
        """
        Convert speech to text using Whisper or dummy data
        
        Args:
            audio_file_path (str): Path to audio file
            
        Returns:
            dict: Transcription result with text and language
        """
        logger.info(f"Processing audio file: {audio_file_path}")
        
        if self.use_whisper and os.path.exists(audio_file_path):
            try:
                # Use real Whisper for actual audio files
                result = self.whisper_model.transcribe(audio_file_path)
                return {
                    "text": result["text"],
                    "language": result.get("language", "unknown"),
                    "confidence": 0.95  # Whisper doesn't provide confidence, using high value
                }
            except Exception as e:
                logger.error(f"Whisper transcription failed: {e}")
        
        # Use sample data for demonstration
        sample_key = Path(audio_file_path).stem
        for key, sample in self.sample_voices.items():
            if sample_key in sample["audio_file"] or sample["audio_file"] in audio_file_path:
                return {
                    "text": sample["text"],
                    "language": sample["language"].lower(),
                    "confidence": 0.90
                }
        
        # Default fallback
        import random
        sample = random.choice(list(self.sample_voices.values()))
        logger.info(f"Using sample data for demonstration: {sample['language']}")
        return {
            "text": sample["text"],
            "language": sample["language"].lower(),
            "confidence": 0.85
        }
    
    def translate_to_english(self, text, source_language):
        """
        Translate text to English using AI4Bharat or fallback methods
        
        Args:
            text (str): Text to translate
            source_language (str): Source language
            
        Returns:
            dict: Translation result
        """
        if source_language.lower() == "english":
            return {"translated_text": text, "confidence": 1.0}
        
        logger.info(f"Translating {source_language} text to English")
        
        if self.use_ai4bharat and self.translator:
            try:
                # AI4Bharat translation
                result = self.translator(text, 
                                       src_lang=source_language[:2], 
                                       tgt_lang="en")
                return {
                    "translated_text": result[0]["translation_text"],
                    "confidence": result[0].get("score", 0.80)
                }
            except Exception as e:
                logger.error(f"AI4Bharat translation failed: {e}")
        
        # Use sample translations for demonstration
        for sample in self.sample_voices.values():
            if sample["text"] == text:
                return {
                    "translated_text": sample["translation"],
                    "confidence": 0.85
                }
        
        # Fallback: return original text
        logger.warning("Translation failed, using original text")
        return {"translated_text": text, "confidence": 0.50}
    
    def analyze_sentiment(self, text):
        """
        Analyze sentiment using multiple methods
        
        Args:
            text (str): Text to analyze
            
        Returns:
            dict: Comprehensive sentiment analysis
        """
        logger.info("Analyzing sentiment")
        
        # NLTK VADER sentiment analysis
        vader_scores = self.sentiment_analyzer.polarity_scores(text)
        
        # Advanced transformer-based sentiment (if available)
        transformer_result = None
        if self.classifier:
            try:
                result = self.classifier(text)
                transformer_result = {
                    "label": result[0]["label"],
                    "score": result[0]["score"]
                }
            except Exception as e:
                logger.warning(f"Advanced sentiment analysis failed: {e}")
        
        # Determine overall sentiment
        compound = vader_scores["compound"]
        if compound >= 0.05:
            overall_sentiment = "Positive"
        elif compound <= -0.05:
            overall_sentiment = "Negative"
        else:
            overall_sentiment = "Neutral"
        
        return {
            "overall_sentiment": overall_sentiment,
            "vader_scores": vader_scores,
            "transformer_result": transformer_result,
            "confidence": abs(compound) if compound != 0 else 0.5
        }
    
    def extract_keywords(self, text, num_keywords=10):
        """
        Extract keywords and key phrases from text
        
        Args:
            text (str): Input text
            num_keywords (int): Number of keywords to extract
            
        Returns:
            dict: Keywords and phrases
        """
        logger.info("Extracting keywords")
        
        # Clean and tokenize
        words = word_tokenize(text.lower())
        
        # Remove stopwords and non-alphabetic tokens
        stop_words = set(stopwords.words('english'))
        keywords = [word for word in words 
                   if word.isalpha() and len(word) > 2 and word not in stop_words]
        
        # Get word frequencies
        word_freq = Counter(keywords)
        top_keywords = [word for word, _ in word_freq.most_common(num_keywords)]
        
        # Extract key phrases (simple bigrams)
        from nltk import bigrams
        word_pairs = list(bigrams(keywords))
        phrase_freq = Counter([' '.join(pair) for pair in word_pairs])
        top_phrases = [phrase for phrase, _ in phrase_freq.most_common(5)]
        
        return {
            "keywords": top_keywords,
            "key_phrases": top_phrases,
            "word_frequencies": dict(word_freq.most_common(num_keywords))
        }
    
    def categorize_issue(self, text):
        """
        Categorize the type of community issue
        
        Args:
            text (str): Input text
            
        Returns:
            dict: Issue categorization result
        """
        logger.info("Categorizing community issue")
        
        categories = {
            "Forest Rights": {
                "keywords": ["forest", "tree", "land", "cutting", "deforestation", "rights", "illegal", "timber"],
                "weight": 0
            },
            "Healthcare": {
                "keywords": ["health", "hospital", "doctor", "medicine", "clinic", "medical", "treatment", "disease"],
                "weight": 0
            },
            "Education": {
                "keywords": ["school", "education", "teacher", "student", "book", "learning", "children", "study"],
                "weight": 0
            },
            "Water Supply": {
                "keywords": ["water", "well", "drinking", "clean", "supply", "pipeline", "shortage", "scarcity"],
                "weight": 0
            },
            "Employment": {
                "keywords": ["job", "work", "employment", "income", "livelihood", "wages", "unemployment"],
                "weight": 0
            },
            "Infrastructure": {
                "keywords": ["road", "electricity", "transport", "bridge", "building", "connectivity"],
                "weight": 0
            },
            "Cultural Preservation": {
                "keywords": ["culture", "tradition", "heritage", "festival", "language", "customs"],
                "weight": 0
            }
        }
        
        text_lower = text.lower()
        
        # Calculate weights for each category
        for category, data in categories.items():
            for keyword in data["keywords"]:
                if keyword in text_lower:
                    data["weight"] += 1
        
        # Find the category with highest weight
        best_category = max(categories.items(), key=lambda x: x[1]["weight"])
        
        if best_category[1]["weight"] == 0:
            primary_category = "General Community Issue"
            confidence = 0.5
        else:
            primary_category = best_category[0]
            confidence = min(best_category[1]["weight"] / 3, 1.0)  # Normalize confidence
        
        # Get all categories with non-zero weights
        relevant_categories = [cat for cat, data in categories.items() if data["weight"] > 0]
        
        return {
            "primary_category": primary_category,
            "relevant_categories": relevant_categories,
            "confidence": confidence,
            "category_weights": {cat: data["weight"] for cat, data in categories.items()}
        }
    
    def generate_summary(self, text):
        """
        Generate text summary
        
        Args:
            text (str): Input text
            
        Returns:
            dict: Summary result
        """
        logger.info("Generating text summary")
        
        if self.summarizer and len(text) > 100:
            try:
                # Use transformer-based summarization
                summary_result = self.summarizer(text, 
                                               max_length=100, 
                                               min_length=20, 
                                               do_sample=False)
                return {
                    "summary": summary_result[0]["summary_text"],
                    "method": "transformer",
                    "confidence": 0.85
                }
            except Exception as e:
                logger.warning(f"Advanced summarization failed: {e}")
        
        # Fallback: extractive summary using sentence ranking
        sentences = sent_tokenize(text)
        if len(sentences) <= 2:
            return {
                "summary": text,
                "method": "original",
                "confidence": 1.0
            }
        
        # Simple extractive summary: take first and most important sentences
        summary = ". ".join(sentences[:2])
        return {
            "summary": summary,
            "method": "extractive",
            "confidence": 0.70
        }
    
    def assess_priority(self, sentiment_result, category_result, keywords):
        """
        Assess priority level of the issue
        
        Args:
            sentiment_result (dict): Sentiment analysis result
            category_result (dict): Issue categorization result
            keywords (list): Extracted keywords
            
        Returns:
            dict: Priority assessment
        """
        logger.info("Assessing issue priority")
        
        priority_score = 0
        factors = []
        
        # Sentiment factor
        sentiment = sentiment_result["overall_sentiment"]
        compound = sentiment_result["vader_scores"]["compound"]
        
        if sentiment == "Negative":
            if compound < -0.6:
                priority_score += 3
                factors.append("High negative sentiment")
            elif compound < -0.3:
                priority_score += 2
                factors.append("Moderate negative sentiment")
            else:
                priority_score += 1
                factors.append("Mild negative sentiment")
        
        # Category factor
        high_priority_categories = ["Forest Rights", "Healthcare", "Water Supply"]
        if category_result["primary_category"] in high_priority_categories:
            priority_score += 2
            factors.append(f"High-priority category: {category_result['primary_category']}")
        
        # Urgency keywords
        urgent_keywords = ["urgent", "emergency", "immediate", "crisis", "danger", "critical"]
        keyword_text = " ".join(keywords).lower()
        urgent_count = sum(1 for word in urgent_keywords if word in keyword_text)
        if urgent_count > 0:
            priority_score += urgent_count
            factors.append(f"Urgency indicators found: {urgent_count}")
        
        # Determine priority level
        if priority_score >= 4:
            priority_level = "High"
        elif priority_score >= 2:
            priority_level = "Medium"
        else:
            priority_level = "Low"
        
        return {
            "priority_level": priority_level,
            "priority_score": priority_score,
            "contributing_factors": factors,
            "recommended_timeline": self._get_timeline_recommendation(priority_level)
        }
    
    def _get_timeline_recommendation(self, priority_level):
        """Get recommended action timeline based on priority"""
        timelines = {
            "High": "Immediate action required (within 24-48 hours)",
            "Medium": "Action needed within 1-2 weeks",
            "Low": "Address within 1 month"
        }
        return timelines.get(priority_level, "Standard timeline")
    
    def generate_actionable_insights(self, analysis_results):
        """
        Generate actionable insights and recommendations
        
        Args:
            analysis_results (dict): Complete analysis results
            
        Returns:
            dict: Actionable insights and recommendations
        """
        logger.info("Generating actionable insights")
        
        category = analysis_results["category"]["primary_category"]
        sentiment = analysis_results["sentiment"]["overall_sentiment"]
        priority = analysis_results["priority"]["priority_level"]
        
        # Department mappings
        department_map = {
            "Forest Rights": "Forest Department & Tribal Affairs",
            "Healthcare": "Health Department & Public Health",
            "Education": "Education Department & Child Welfare",
            "Water Supply": "Water Resources & Rural Development",
            "Employment": "Labor Department & Skill Development",
            "Infrastructure": "Public Works & Rural Development",
            "Cultural Preservation": "Cultural Affairs & Tribal Welfare"
        }
        
        # Action recommendations
        action_recommendations = {
            "Forest Rights": [
                "File complaint with Forest Department",
                "Contact legal aid services",
                "Document evidence with photos/videos",
                "Organize community meeting",
                "Reach out to environmental NGOs"
            ],
            "Healthcare": [
                "Contact District Medical Officer",
                "Request mobile health camp",
                "Apply for community health center",
                "Connect with health NGOs",
                "Document health emergencies"
            ],
            "Education": [
                "Contact Block Education Officer",
                "Request teacher recruitment",
                "Apply for infrastructure development",
                "Organize parent-teacher meeting",
                "Connect with education NGOs"
            ],
            "Water Supply": [
                "Contact Water Department",
                "Apply for bore well/hand pump",
                "Request water tanker service",
                "Form water user committee",
                "Document water quality issues"
            ],
            "Employment": [
                "Contact employment office",
                "Apply for skill development programs",
                "Register for MGNREGA",
                "Form self-help groups",
                "Connect with microfinance institutions"
            ],
            "Infrastructure": [
                "Contact PWD/Rural Development",
                "Submit development proposal",
                "Form village development committee",
                "Apply for infrastructure funds",
                "Document connectivity issues"
            ]
        }
        
        # Get specific recommendations
        responsible_department = department_map.get(category, "District Administration")
        specific_actions = action_recommendations.get(category, [
            "Contact district administration",
            "File formal complaint",
            "Organize community meeting",
            "Document the issue",
            "Seek NGO assistance"
        ])
        
        # Additional recommendations based on sentiment
        if sentiment == "Negative" and priority == "High":
            specific_actions.insert(0, "URGENT: Escalate to senior officials immediately")
        
        return {
            "responsible_department": responsible_department,
            "immediate_actions": specific_actions[:3],
            "follow_up_actions": specific_actions[3:],
            "escalation_path": self._get_escalation_path(priority),
            "success_metrics": self._get_success_metrics(category),
            "timeline": analysis_results["priority"]["recommended_timeline"]
        }
    
    def _get_escalation_path(self, priority):
        """Get escalation path based on priority"""
        paths = {
            "High": ["Local Official → Block Officer → District Collector → State Government"],
            "Medium": ["Local Official → Block Officer → District Officer"],
            "Low": ["Local Official → Block Officer"]
        }
        return paths.get(priority, ["Local Official"])
    
    def _get_success_metrics(self, category):
        """Get success metrics for tracking progress"""
        metrics = {
            "Forest Rights": ["Forest cover maintained", "Illegal activities stopped", "Rights documentation completed"],
            "Healthcare": ["Health facility established", "Medical staff available", "Health indicators improved"],
            "Education": ["School infrastructure completed", "Teachers recruited", "Enrollment increased"],
            "Water Supply": ["Clean water access", "Water quality improved", "Consistent supply established"],
            "Employment": ["Jobs created", "Skills developed", "Income increased"],
            "Infrastructure": ["Infrastructure completed", "Connectivity improved", "Service access enhanced"]
        }
        return metrics.get(category, ["Issue resolved", "Community satisfied", "Service improved"])
    
    def process_voice_feedback(self, audio_file_path, save_results=True):
        """
        Complete voice feedback processing pipeline
        
        Args:
            audio_file_path (str): Path to audio file
            save_results (bool): Whether to save results to file
            
        Returns:
            dict: Complete analysis results
        """
        logger.info(f"Starting complete voice feedback processing: {audio_file_path}")
        
        results = {
            "timestamp": datetime.now().isoformat(),
            "audio_file": audio_file_path,
            "processing_status": "in_progress"
        }
        
        try:
            # Step 1: Speech to Text
            logger.info("Step 1: Speech to Text conversion")
            speech_result = self.speech_to_text(audio_file_path)
            results["transcription"] = speech_result
            
            # Step 2: Translation
            logger.info("Step 2: Translation to English")
            translation_result = self.translate_to_english(
                speech_result["text"], 
                speech_result["language"]
            )
            results["translation"] = translation_result
            
            english_text = translation_result["translated_text"]
            
            # Step 3: Sentiment Analysis
            logger.info("Step 3: Sentiment Analysis")
            sentiment_result = self.analyze_sentiment(english_text)
            results["sentiment"] = sentiment_result
            
            # Step 4: Keyword Extraction
            logger.info("Step 4: Keyword Extraction")
            keyword_result = self.extract_keywords(english_text)
            results["keywords"] = keyword_result
            
            # Step 5: Issue Categorization
            logger.info("Step 5: Issue Categorization")
            category_result = self.categorize_issue(english_text)
            results["category"] = category_result
            
            # Step 6: Text Summary
            logger.info("Step 6: Text Summarization")
            summary_result = self.generate_summary(english_text)
            results["summary"] = summary_result
            
            # Step 7: Priority Assessment
            logger.info("Step 7: Priority Assessment")
            priority_result = self.assess_priority(
                sentiment_result, 
                category_result, 
                keyword_result["keywords"]
            )
            results["priority"] = priority_result
            
            # Step 8: Actionable Insights
            logger.info("Step 8: Generating Actionable Insights")
            insights = self.generate_actionable_insights(results)
            results["insights"] = insights
            
            # Compile final analysis
            results["final_analysis"] = {
                "original_text": speech_result["text"],
                "original_language": speech_result["language"],
                "english_text": english_text,
                "sentiment": sentiment_result["overall_sentiment"],
                "sentiment_confidence": sentiment_result["confidence"],
                "keywords": keyword_result["keywords"][:5],
                "key_phrases": keyword_result["key_phrases"][:3],
                "issue_category": category_result["primary_category"],
                "priority_level": priority_result["priority_level"],
                "summary": summary_result["summary"],
                "responsible_department": insights["responsible_department"],
                "immediate_actions": insights["immediate_actions"],
                "timeline": insights["timeline"]
            }
            
            results["processing_status"] = "completed"
            logger.info("Voice feedback processing completed successfully")
            
            # Save results if requested
            if save_results:
                self._save_results(results)
            
            return results
            
        except Exception as e:
            logger.error(f"Error in voice feedback processing: {e}")
            results["processing_status"] = "failed"
            results["error"] = str(e)
            return results
    
    def _save_results(self, results):
        """Save processing results to JSON file"""
        try:
            # Create results directory
            results_dir = Path("voice_analysis_results")
            results_dir.mkdir(exist_ok=True)
            
            # Generate filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = results_dir / f"voice_analysis_{timestamp}.json"
            
            # Save results
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(results, f, indent=2, ensure_ascii=False)
            
            logger.info(f"Results saved to {filename}")
            
        except Exception as e:
            logger.error(f"Failed to save results: {e}")
    
    def create_visualization_dashboard(self, results):
        """
        Create visualization dashboard for results
        
        Args:
            results (dict): Analysis results
        """
        if not VISUALIZATION_AVAILABLE:
            logger.warning("Visualization libraries not available")
            return
        
        try:
            fig, axes = plt.subplots(2, 2, figsize=(15, 10))
            fig.suptitle('Voice Feedback Analysis Dashboard', fontsize=16)
            
            # Sentiment visualization
            sentiment_data = results["sentiment"]["vader_scores"]
            sentiment_labels = ['Positive', 'Negative', 'Neutral']
            sentiment_values = [sentiment_data['pos'], sentiment_data['neg'], sentiment_data['neu']]
            
            axes[0, 0].pie(sentiment_values, labels=sentiment_labels, autopct='%1.1f%%')
            axes[0, 0].set_title('Sentiment Distribution')
            
            # Keywords visualization
            keywords = results["keywords"]["keywords"][:8]
            keyword_freqs = [results["keywords"]["word_frequencies"].get(word, 1) for word in keywords]
            
            axes[0, 1].bar(keywords, keyword_freqs)
            axes[0, 1].set_title('Top Keywords')
            axes[0, 1].tick_params(axis='x', rotation=45)
            
            # Category confidence
            category_weights = results["category"]["category_weights"]
            categories = list(category_weights.keys())
            weights = list(category_weights.values())
            
            axes[1, 0].barh(categories, weights)
            axes[1, 0].set_title('Issue Category Relevance')
            
            # Priority factors
            priority_factors = results["priority"]["contributing_factors"]
            if priority_factors:
                factor_counts = {factor: 1 for factor in priority_factors}
                axes[1, 1].bar(range(len(priority_factors)), [1]*len(priority_factors))
                axes[1, 1].set_xticks(range(len(priority_factors)))
                axes[1, 1].set_xticklabels([f"Factor {i+1}" for i in range(len(priority_factors))], 
                                         rotation=45)
                axes[1, 1].set_title('Priority Factors')
            
            plt.tight_layout()
            
            # Save visualization
            viz_dir = Path("visualizations")
            viz_dir.mkdir(exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            viz_path = viz_dir / f"dashboard_{timestamp}.png"
            plt.savefig(viz_path, dpi=300, bbox_inches='tight')
            
            logger.info(f"Visualization saved to {viz_path}")
            plt.show()
            
        except Exception as e:
            logger.error(f"Failed to create visualization: {e}")
    
    def print_detailed_results(self, results):
        """
        Print detailed analysis results in a formatted way
        
        Args:
            results (dict): Analysis results
        """
        if results.get("processing_status") == "failed":
            print(f"❌ Processing failed: {results.get('error', 'Unknown error')}")
            return
        
        print("\n" + "="*80)
        print("🎤 TRIBAL VOICE FEEDBACK ANALYSIS RESULTS")
        print("="*80)
        
        final = results.get("final_analysis", {})
        
        # Basic Information
        print(f"\n📝 TRANSCRIPTION & TRANSLATION")
        print("-" * 40)
        print(f"Original Language: {final.get('original_language', 'Unknown')}")
        print(f"Original Text: {final.get('original_text', 'N/A')}")
        print(f"English Translation: {final.get('english_text', 'N/A')}")
        
        # Sentiment Analysis
        print(f"\n😊 SENTIMENT ANALYSIS")
        print("-" * 40)
        sentiment = final.get('sentiment', 'Unknown')
        confidence = final.get('sentiment_confidence', 0)
        print(f"Overall Sentiment: {sentiment} (Confidence: {confidence:.2f})")
        
        if 'sentiment' in results:
            vader = results['sentiment']['vader_scores']
            print(f"Positive Score: {vader['pos']:.3f}")
            print(f"Negative Score: {vader['neg']:.3f}")
            print(f"Neutral Score: {vader['neu']:.3f}")
            print(f"Compound Score: {vader['compound']:.3f}")
        
        # Keywords and Phrases
        print(f"\n🔑 KEYWORDS & KEY PHRASES")
        print("-" * 40)
        keywords = final.get('keywords', [])
        key_phrases = final.get('key_phrases', [])
        print(f"Keywords: {', '.join(keywords)}")
        print(f"Key Phrases: {', '.join(key_phrases)}")
        
        # Issue Categorization
        print(f"\n📂 ISSUE CATEGORIZATION")
        print("-" * 40)
        print(f"Primary Category: {final.get('issue_category', 'Unknown')}")
        if 'category' in results:
            relevant_cats = results['category'].get('relevant_categories', [])
            if relevant_cats:
                print(f"Relevant Categories: {', '.join(relevant_cats)}")
        
        # Priority Assessment
        print(f"\n⚡ PRIORITY ASSESSMENT")
        print("-" * 40)
        priority = final.get('priority_level', 'Unknown')
        timeline = final.get('timeline', 'Standard timeline')
        print(f"Priority Level: {priority}")
        print(f"Recommended Timeline: {timeline}")
        
        if 'priority' in results:
            factors = results['priority'].get('contributing_factors', [])
            if factors:
                print("Contributing Factors:")
                for factor in factors:
                    print(f"  • {factor}")
        
        # Summary
        print(f"\n📋 SUMMARY")
        print("-" * 40)
        print(f"Summary: {final.get('summary', 'N/A')}")
        
        # Actionable Insights
        print(f"\n💡 ACTIONABLE INSIGHTS")
        print("-" * 40)
        dept = final.get('responsible_department', 'District Administration')
        print(f"Responsible Department: {dept}")
        
        actions = final.get('immediate_actions', [])
        if actions:
            print("Immediate Actions Required:")
            for i, action in enumerate(actions, 1):
                print(f"  {i}. {action}")
        
        # Additional insights
        if 'insights' in results:
            insights = results['insights']
            follow_up = insights.get('follow_up_actions', [])
            if follow_up:
                print("\nFollow-up Actions:")
                for i, action in enumerate(follow_up, 1):
                    print(f"  {i}. {action}")
            
            escalation = insights.get('escalation_path', [])
            if escalation:
                print(f"\nEscalation Path: {' → '.join(escalation)}")
            
            metrics = insights.get('success_metrics', [])
            if metrics:
                print("\nSuccess Metrics:")
                for metric in metrics:
                    print(f"  • {metric}")
        
        print("\n" + "="*80)


def main():
    """
    Main function to demonstrate the voice processing pipeline
    """
    print("🌿 Tribal Community Voice Feedback Processing Pipeline")
    print("=" * 70)
    print("🎯 Advanced AI-powered analysis for community empowerment")
    print("🚀 Features: Whisper STT, AI4Bharat Translation, Advanced NLP")
    print("=" * 70)
    
    # Initialize processor
    processor = TribalVoiceProcessor(use_whisper=True, use_ai4bharat=True)
    
    # Sample audio files for testing
    sample_files = [
        "sample_hindi_forest_rights.wav",
        "sample_bengali_healthcare.wav", 
        "sample_kannada_education.wav",
        "sample_tamil_water_crisis.wav",
        "sample_english_positive_feedback.wav"
    ]
    
    print(f"\n🧪 Processing {len(sample_files)} sample voice feedbacks...")
    
    all_results = []
    
    for i, audio_file in enumerate(sample_files, 1):
        print(f"\n{'='*50}")
        print(f"📱 Processing Sample {i}: {audio_file}")
        print(f"{'='*50}")
        
        # Process voice feedback
        results = processor.process_voice_feedback(audio_file, save_results=True)
        all_results.append(results)
        
        # Print detailed results
        processor.print_detailed_results(results)
        
        # Create visualization (optional)
        if VISUALIZATION_AVAILABLE:
            try:
                processor.create_visualization_dashboard(results)
            except Exception as e:
                logger.warning(f"Visualization failed: {e}")
        
        print(f"\n{'='*50}")
    
    # Summary statistics
    print(f"\n📊 PROCESSING SUMMARY")
    print("=" * 30)
    successful = sum(1 for r in all_results if r.get("processing_status") == "completed")
    print(f"✅ Successfully processed: {successful}/{len(sample_files)}")
    
    # Sentiment distribution
    sentiments = [r.get("final_analysis", {}).get("sentiment") for r in all_results 
                 if r.get("processing_status") == "completed"]
    sentiment_counts = Counter(sentiments)
    print(f"📈 Sentiment Distribution: {dict(sentiment_counts)}")
    
    # Category distribution
    categories = [r.get("final_analysis", {}).get("issue_category") for r in all_results 
                 if r.get("processing_status") == "completed"]
    category_counts = Counter(categories)
    print(f"📂 Issue Categories: {dict(category_counts)}")
    
    print(f"\n🎉 Voice feedback processing pipeline completed successfully!")
    print(f"📁 Results saved in 'voice_analysis_results' directory")
    if VISUALIZATION_AVAILABLE:
        print(f"📊 Visualizations saved in 'visualizations' directory")


if __name__ == "__main__":
    main()
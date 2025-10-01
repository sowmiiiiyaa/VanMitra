# 🌿 Advanced Tribal Voice Feedback Processing Pipeline

## 📋 Project Overview

This is a comprehensive AI-powered voice processing pipeline designed for tribal community feedback collection and analysis. The system processes voice notes in multiple Indian languages and provides actionable insights for community development.

## 🎯 Key Features

- **🎤 Speech-to-Text**: OpenAI Whisper integration with fallback to dummy data
- **🌐 Multi-language Translation**: AI4Bharat NLP for Indian languages to English
- **😊 Sentiment Analysis**: NLTK VADER with confidence scoring
- **🔑 Keyword Extraction**: Intelligent key phrase identification
- **📂 Issue Categorization**: Automatic classification (Forest Rights, Education, Healthcare, etc.)
- **⚡ Priority Assessment**: Smart priority scoring based on sentiment and category
- **📋 Text Summarization**: Concise summary generation
- **💡 Actionable Insights**: Department routing, action items, and escalation paths

## 🚀 Quick Start

### Basic Usage (Works immediately)
```bash
# Run the complete pipeline with sample data
python advanced_voice_processor.py

# Test individual modular functions
python test_advanced_pipeline.py
```

### Full AI Model Installation (Optional)
```bash
# Install OpenAI Whisper for real speech-to-text
pip install openai-whisper

# Install Transformers for advanced NLP
pip install transformers torch

# Install AI4Bharat for Indian language processing
pip install ai4bharat-transliteration

# Install audio processing libraries
pip install librosa soundfile

# Install visualization libraries
pip install matplotlib seaborn plotly
```

## 📁 File Structure

```
FRA_Prototype/
├── advanced_voice_processor.py    # Main pipeline (700+ lines)
├── requirements_advanced.txt      # Production dependencies
├── test_advanced_pipeline.py      # Test script for modular functions
├── voice_analysis_results/        # Generated analysis outputs
├── sample_*.wav                   # Sample audio files (5 languages)
└── README_ADVANCED.md             # This documentation
```

## 🔧 Modular Functions

The pipeline consists of 8 core modular functions:

### 1. Speech-to-Text Conversion
```python
processor = TribalVoiceProcessor()
text, language = processor.speech_to_text("audio_file.wav")
```

### 2. Language Translation
```python
english_text = processor.translate_to_english(text, language)
```

### 3. Sentiment Analysis
```python
sentiment = processor.analyze_sentiment(english_text)
# Returns: overall, confidence, positive/negative/neutral scores
```

### 4. Keyword Extraction
```python
keywords = processor.extract_keywords(english_text)
# Returns: top keywords and key phrases
```

### 5. Issue Categorization
```python
category = processor.categorize_issue(english_text)
# Categories: Forest Rights, Education, Healthcare, Water Supply, etc.
```

### 6. Text Summarization
```python
summary = processor.generate_summary(english_text)
```

### 7. Priority Assessment
```python
priority = processor.assess_priority(sentiment, category)
# Returns: High/Medium/Low with timeline
```

### 8. Actionable Insights Generation
```python
insights = processor.generate_actionable_insights(text, category, sentiment, priority)
# Returns: department, actions, escalation path, success metrics
```

## 📊 Sample Input/Output

### Input Format
```python
{
    "audio_file": "sample_hindi_forest_rights.wav",
    "format": "WAV/MP3/M4A",
    "language": "Hindi/Tamil/Kannada/Bengali/English"
}
```

### Output Format
```python
{
    "original_language": "hindi",
    "original_text": "हमारे जंगल में अवैध कटाई हो रही है...",
    "english_translation": "Illegal cutting is happening in our forest...",
    "sentiment": {
        "overall": "Negative",
        "confidence": 0.30,
        "scores": {"positive": 0.116, "negative": 0.204, "neutral": 0.680}
    },
    "keywords": ["forest", "illegal", "cutting", "department"],
    "category": "Forest Rights",
    "priority": {
        "level": "Medium",
        "timeline": "Action needed within 1-2 weeks"
    },
    "summary": "Illegal cutting is happening in our forest...",
    "actionable_insights": {
        "responsible_department": "Forest Department & Tribal Affairs",
        "immediate_actions": ["File complaint", "Contact legal aid"],
        "escalation_path": "Local Official → Block Officer → District Officer"
    }
}
```

## 🎯 Supported Languages

- **Hindi**: हिंदी
- **Tamil**: தமிழ்
- **Kannada**: ಕನ್ನಡ
- **Bengali**: বাংলা
- **English**: English

## 📈 Performance Features

- **Intelligent Fallbacks**: Works without AI models using sample data
- **Comprehensive Logging**: Detailed execution logs for debugging
- **JSON Output**: Structured results saved automatically
- **Error Handling**: Graceful failure with informative messages
- **Modular Design**: Each function can be used independently

## 🌐 Web Integration

The pipeline integrates with Flask web application:

```python
# Flask route example
@app.route('/process-voice', methods=['POST'])
def process_voice():
    processor = TribalVoiceProcessor()
    result = processor.process_voice_feedback(audio_file)
    return jsonify(result)
```

## 🔍 Analysis Categories

The system automatically categorizes community issues into:

- **Forest Rights**: Land disputes, illegal logging, conservation
- **Education**: School infrastructure, teacher shortage, books
- **Healthcare**: Medical facilities, doctor availability, medicines
- **Water Supply**: Scarcity, quality, infrastructure
- **Employment**: Job opportunities, skill development
- **Infrastructure**: Roads, electricity, connectivity

## 📊 Dashboard Integration

Results can be visualized through the dashboard system:

- **Sentiment Distribution**: Pie charts showing positive/negative feedback
- **Issue Categories**: Bar charts of problem types
- **Priority Heatmaps**: Geographic distribution of urgent issues
- **Trend Analysis**: Time-series of community feedback

## 🤖 AI Model Details

### OpenAI Whisper
- **Purpose**: Multilingual speech recognition
- **Languages**: 100+ languages including Indian languages
- **Models**: tiny, base, small, medium, large
- **Fallback**: Sample transcription data

### AI4Bharat
- **Purpose**: Indian language NLP
- **Models**: IndicBART, IndicBERT
- **Languages**: 22 Indian languages
- **Fallback**: Simple translation dictionary

### NLTK + Transformers
- **Sentiment**: VADER sentiment analyzer
- **Summarization**: BART/T5 models
- **Keywords**: TF-IDF + POS tagging
- **Fallback**: Basic text processing

## 🔧 Customization

### Adding New Languages
```python
# Add to sample_texts dictionary in advanced_voice_processor.py
sample_texts = {
    "your_language": {
        "text": "Sample text in your language",
        "translation": "English translation"
    }
}
```

### Adding New Categories
```python
# Add to categories list
categories = [
    "Forest Rights", "Education", "Healthcare", 
    "Water Supply", "Your New Category"
]
```

### Custom Department Mapping
```python
# Modify department_mapping dictionary
department_mapping = {
    "Your Category": "Responsible Department Name"
}
```

## 📞 Support & Maintenance

### Troubleshooting
1. **No audio processing**: Install `librosa` and `soundfile`
2. **Poor transcription**: Install `openai-whisper`
3. **Translation errors**: Install `ai4bharat-transliteration`
4. **Visualization issues**: Install `matplotlib` and `seaborn`

### Logs Location
- **Processing logs**: Console output with timestamps
- **Results**: `voice_analysis_results/` directory
- **Error logs**: Captured in JSON output files

## 🎉 Success Metrics

The pipeline tracks success through:

- **Processing Rate**: Number of voice notes processed per hour
- **Accuracy**: Sentiment analysis confidence scores
- **Response Time**: Average time from upload to insights
- **Resolution Rate**: Issues resolved through actionable insights

## 🔄 Future Enhancements

- **Real-time Processing**: WebRTC integration for live voice
- **Mobile App**: React Native interface for field workers
- **Geographic Mapping**: GPS-based issue tracking
- **Multi-modal**: Image and video analysis integration
- **Predictive Analytics**: Issue trend forecasting

---

**Created for Tribal Community Empowerment** 🌿  
*Advanced AI Pipeline for Voice Feedback Processing*
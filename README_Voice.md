# 🎤 VanMitra Voice Feedback Analysis

## Overview
VanMitra is an AI-powered system for processing voice feedback from tribal communities. It converts voice notes into actionable insights through speech-to-text, translation, sentiment analysis, and intelligent categorization.

## Features

### 🎵 Voice Processing Pipeline
- **Speech-to-Text**: Convert audio files to text (supports WAV, MP3, OGG, M4A, FLAC)
- **Multi-language Support**: Processes Hindi, Bengali, Kannada, Tamil, and other regional languages
- **Auto-Translation**: Translates to English using AI4Bharat or similar models
- **Sentiment Analysis**: Identifies positive, negative, or neutral sentiment
- **Keyword Extraction**: Finds important topics and themes
- **Issue Categorization**: Classifies into categories (Forest Rights, Healthcare, Education, etc.)
- **Priority Assessment**: Determines urgency and recommended actions

### 📊 Analytics Dashboard
- Real-time sentiment distribution
- Issue category breakdown
- Weekly trends analysis
- Priority level tracking
- Recent feedback overview

## Quick Start

### 1. Install Dependencies
```bash
# Install basic dependencies
pip install -r requirements.txt

# Download NLTK data (automatic on first run)
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('vader_lexicon')"
```

### 2. Test the Voice Processor
```bash
# Run the test suite to verify everything works
python test_voice_processor.py
```

### 3. Start the Flask Application
```bash
python app.py
```

### 4. Access the Application
- **Main Dashboard**: http://localhost:5000
- **Voice Feedback Upload**: http://localhost:5000/voice-feedback
- **Analytics Dashboard**: http://localhost:5000/voice-analytics

## Usage

### Upload Voice Notes
1. Go to the Voice Feedback page
2. Upload an audio file or try the demo
3. View the AI-generated analysis results

### View Analytics
1. Access the Analytics Dashboard
2. See sentiment distribution, trends, and insights
3. Review recent voice note analysis

## File Structure
```
FRA_Prototype/
├── app.py                          # Main Flask application
├── voice_processor.py              # Voice processing pipeline
├── test_voice_processor.py         # Test suite
├── requirements.txt                # Python dependencies
├── templates/
│   ├── index.html                  # Main dashboard
│   ├── voice_feedback.html         # Voice upload interface
│   └── voice_analytics.html        # Analytics dashboard
├── static/
│   └── css/
│       └── style.css              # Styling
├── uploads/                        # Temporary audio file storage
└── voice_analysis_results/         # Analysis results (JSON)
```

## API Endpoints

### Voice Processing
- `POST /upload-voice` - Upload and process voice file
- `GET /process-demo-voice` - Process demo voice note
- `GET /voice-feedback` - Voice upload interface
- `GET /voice-analytics` - Analytics dashboard

### Traditional Analysis
- `POST /predict` - FRA approval prediction
- `POST /analyze` - Text sentiment analysis

## Development Mode

The system currently runs in demo mode with simulated data:

### Current Implementation (Demo)
- ✅ Complete UI/UX interface
- ✅ File upload handling
- ✅ Dummy speech-to-text conversion
- ✅ Dummy translation (multiple languages)
- ✅ Real sentiment analysis (NLTK VADER)
- ✅ Real keyword extraction
- ✅ Issue categorization logic
- ✅ Priority assessment
- ✅ Analytics dashboard

### Production Setup
To enable real speech processing:

1. **Install Speech Libraries**:
```bash
pip install openai-whisper torch torchaudio
```

2. **Install Translation Libraries**:
```bash
pip install transformers sentencepiece
```

3. **Update voice_processor.py**:
   - Uncomment Whisper integration in `speech_to_text()`
   - Uncomment translation model in `translate_to_english()`
   - Configure AI4Bharat models

## Example Voice Note Analysis

### Input (Hindi)
> "हमारे जंगल में अवैध कटाई हो रही है। वन विभाग को इसकी जानकारी देनी चाहिए।"

### Output
- **Translation**: "Illegal cutting is happening in our forest. Forest department should be informed about this."
- **Sentiment**: Negative (compound: -0.6)
- **Keywords**: forest, illegal, cutting, department
- **Category**: Forest Rights
- **Priority**: High
- **Action**: Contact forest department and legal aid services

## Configuration

### Supported Audio Formats
- WAV (recommended)
- MP3
- OGG
- M4A
- FLAC

### File Size Limits
- Maximum: 16MB per file
- Recommended: Under 10MB for faster processing

### Language Support
- **Input**: Hindi, Bengali, Kannada, Tamil, Telugu, Malayalam, Marathi, Gujarati, Punjabi, English
- **Output**: English (for consistency in analysis)

## Troubleshooting

### Common Issues

1. **NLTK Data Error**:
```bash
python -c "import nltk; nltk.download('all')"
```

2. **Audio File Upload Issues**:
   - Check file format (must be audio)
   - Verify file size (under 16MB)
   - Ensure uploads/ directory exists

3. **Memory Issues**:
   - Reduce audio file size
   - Close other applications
   - Use smaller Whisper model (base instead of large)

### Error Messages
- "No voice file provided" → Select an audio file
- "Invalid file type" → Use supported audio formats
- "Processing timeout" → File too large or complex

## Performance Optimization

### For Production
- Use GPU for Whisper (faster transcription)
- Implement audio preprocessing (noise reduction)
- Add file compression for uploads
- Use Redis for caching results
- Implement batch processing for multiple files

### Current Performance (Demo Mode)
- Processing time: ~1-2 seconds per file
- Memory usage: ~50-100MB
- Concurrent users: ~10-20 (development server)

## Security Considerations

- Audio files are temporarily stored and deleted after processing
- No permanent storage of voice data
- Results can be saved as JSON (optional)
- HTTPS recommended for production
- File type validation prevents malicious uploads

## Future Enhancements

### Planned Features
- [ ] Real-time voice recording in browser
- [ ] Multi-speaker detection and separation
- [ ] Emotion detection (beyond sentiment)
- [ ] Voice quality assessment
- [ ] Automatic report generation
- [ ] Integration with government databases
- [ ] Mobile app companion
- [ ] Voice authentication for security

### AI Improvements
- [ ] Custom fine-tuned models for tribal dialects
- [ ] Context-aware translation
- [ ] Intent classification
- [ ] Automated follow-up suggestions
- [ ] Predictive priority scoring

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is part of the VanMitra initiative for tribal community empowerment.

## Support

For issues or questions:
1. Check the troubleshooting section
2. Review the error logs
3. Test with demo data first
4. Verify all dependencies are installed

---

**Ready to empower tribal communities with AI! 🌿🎤**
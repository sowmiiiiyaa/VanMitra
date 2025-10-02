# VanMitra Project Files Guide

## 🎯 Main Application Files (KEEP THESE)

### Primary Server (Currently Running)
- **`vanmitra_complete.py`** - ⭐ MAIN PRODUCTION FILE
  - Complete integrated platform with all features
  - Dashboard, Registration, Status Tracking, Admin Panel, Voice Feedback, Map, AI Predictor
  - Currently running successfully on localhost:5000
  - **USE THIS FOR DEVELOPMENT AND PRODUCTION**

### Backup/Alternative Servers
- **`simple_server.py`** - ✅ RELIABLE BACKUP
  - Clean, working basic version
  - Good for testing and fallback
  - Has core features: registration, status check, admin panel

- **`integrated_vanmitra.py`** - ⚠️ COMPREHENSIVE BUT NEEDS DEBUGGING
  - Most feature-rich version
  - Has some route issues but contains advanced features
  - Keep for reference and future enhancement

## 🔧 Configuration Files (ESSENTIAL)

### Dependencies & Deployment
- **`requirements.txt`** - Python package dependencies
- **`requirements_advanced.txt`** - Advanced feature dependencies
- **`requirements_production.txt`** - Production environment dependencies
- **`Dockerfile`** - Container deployment configuration
- **`deploy.bat`** / **`deploy.sh`** - Deployment automation scripts
- **`Procfile`** - Cloud platform deployment configuration

### Documentation
- **`README.md`** - Main project documentation
- **`DEPLOYMENT_GUIDE.md`** - Step-by-step deployment instructions
- **`IMPLEMENTATION_SUMMARY.md`** - Feature implementation summary
- **`README_ADVANCED.md`** - Advanced features documentation
- **`README_Voice.md`** - Voice processing documentation

## 🎤 Voice Processing Components

- **`voice_processor.py`** - Core voice processing functionality
- **`advanced_voice_processor.py`** - Enhanced voice features with AI
- **`voice_analysis_results/`** - Voice processing output directory

## 📊 Data & Assets

### Static Assets
- **`static/`** - CSS, JavaScript, images, fonts
- **`templates/`** - HTML template files
- **`dashboard/`** - Dashboard-specific files
- **`map/`** - Interactive map components

### Data Storage
- **`data/`** - Application data and databases
- **`sample_data.json`** - Test data for development
- **`uploads/`** - User uploaded files
- **`voice_analysis_results/`** - Voice processing outputs

## 🧪 Testing & Development Files

### Test Files
- **`test_server.py`** - Server functionality tests
- **`test_registration.py`** - Registration system tests
- **`test_voice_processor.py`** - Voice processing tests
- **`test_advanced_pipeline.py`** - Advanced feature tests

### Development Utilities
- **`generate_samples.py`** - Generate test data
- **`show_samples.py`** - Display sample data
- **`simple_test.py`** - Basic functionality tests

## 🚀 Current Status

### ✅ Working (October 2, 2025)
- **`vanmitra_complete.py`** - Running on http://localhost:5000
- All main features operational:
  - 🏠 Dashboard
  - 📝 Registration with AI predictions
  - 🔍 Status tracking
  - 🏛️ Admin panel
  - 🎤 Voice feedback
  - 🗺️ Interactive map
  - 🤖 AI predictor

### 📝 Usage Instructions

1. **For Daily Use:** Run `python vanmitra_complete.py`
2. **For Testing:** Run `python simple_server.py`
3. **For Development:** Edit `vanmitra_complete.py`
4. **For Deployment:** Follow `DEPLOYMENT_GUIDE.md`

### 🎯 Next Steps

1. **Keep all files** - They provide different functionality levels
2. **Use `vanmitra_complete.py`** as your main application
3. **Backup regularly** - Your project is valuable
4. **Document changes** - Update this guide when adding features

## 📞 Support

If you need to modify features or add new functionality:
1. Start with `vanmitra_complete.py`
2. Test changes with `simple_server.py` first
3. Use the test files to validate functionality
4. Update documentation when adding features

---

**Project Status:** ✅ FULLY FUNCTIONAL  
**Main Server:** `vanmitra_complete.py`  
**Access URL:** http://localhost:5000  
**Last Updated:** October 2, 2025
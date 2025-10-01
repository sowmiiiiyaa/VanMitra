@echo off
REM Quick Deploy Script for VanMitra Platform (Windows)

echo 🌿 VanMitra Platform - Quick Deploy Script (Windows)
echo ====================================================

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python not found. Please install Python 3.8+
    pause
    exit /b 1
)

echo ✅ Python found
python --version

REM Install production requirements
echo 📦 Installing requirements...
pip install -r requirements_production.txt
if %errorlevel% neq 0 (
    echo ❌ Failed to install requirements
    pause
    exit /b 1
)

REM Download NLTK data
echo 📚 Setting up NLTK data...
python -c "import nltk; nltk.download('vader_lexicon'); nltk.download('averaged_perceptron_tagger')"

REM Create necessary directories
echo 📁 Creating directories...
if not exist "uploads" mkdir uploads
if not exist "voice_analysis_results" mkdir voice_analysis_results
if not exist "logs" mkdir logs

REM Set environment variables
set FLASK_APP=production_server.py
if not defined PORT set PORT=5000
if not defined HOST set HOST=0.0.0.0
set DEBUG=False

echo 🚀 Starting VanMitra Platform...
echo 🌐 Access at: http://localhost:%PORT%
echo 📱 Network access: Check your IP address and use http://YOUR_IP:%PORT%
echo.
echo Press Ctrl+C to stop the server
echo ====================================================

REM Start the server
python production_server.py

pause
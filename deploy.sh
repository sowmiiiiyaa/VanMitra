#!/bin/bash
# Quick Deploy Script for VanMitra Platform

echo "🌿 VanMitra Platform - Quick Deploy Script"
echo "=========================================="

# Check if Python is installed
if ! command -v python &> /dev/null; then
    echo "❌ Python not found. Please install Python 3.8+"
    exit 1
fi

echo "✅ Python found: $(python --version)"

# Install production requirements
echo "📦 Installing requirements..."
pip install -r requirements_production.txt

# Download NLTK data
echo "📚 Setting up NLTK data..."
python -c "import nltk; nltk.download('vader_lexicon'); nltk.download('averaged_perceptron_tagger')"

# Create necessary directories
echo "📁 Creating directories..."
mkdir -p uploads
mkdir -p voice_analysis_results
mkdir -p logs

# Set environment variables
export FLASK_APP=production_server.py
export PORT=${PORT:-5000}
export HOST=${HOST:-0.0.0.0}
export DEBUG=False

echo "🚀 Starting VanMitra Platform..."
echo "🌐 Access at: http://localhost:$PORT"
echo "📱 Network access: http://$(hostname -I | awk '{print $1}'):$PORT"
echo ""
echo "Press Ctrl+C to stop the server"
echo "=========================================="

# Start the server
python production_server.py
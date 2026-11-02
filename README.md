# Kannada_shakthi_Hackathon - Kannada Saathi

Situation-based Kannada phrasebook with voice playback and quizzes designed to help non-Kannada speakers learn and converse in everyday situations across Karnataka.

**Tech Stack**: Python (Flask), HTML5, CSS3, JavaScript, Web Speech API (TTS & Speech Synthesis).

## Features
- **Scenario-based learning**: Practical phrases for daily life (Auto/Cab, Market, Hotel/Restaurant, Emergency, Workplace, Social greetings).
- **Audio pronunciation**: Listen to native Kannada pronunciations.
- **Interactive Quiz**: Test knowledge with real-time feedback.
- **Search**: Fast lookup across English, Kannada script, and Romanized transliteration.

## Local Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   python app.py
   ```
   Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## Deployment on Render

This project is ready to be hosted as a Web Service on [Render](https://render.com):

- **Runtime**: `Python`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app`

## Project Structure
- `app.py`: Flask routes and JSON API (`/api/scenarios`, `/api/phrases/<id>`, `/api/search`, `/api/quiz/<id>`)
- `data.py`: Curated phrases categorized by situation
- `templates/`: Jinja2 HTML templates (`index.html`)
- `static/`: CSS stylesheet and frontend JavaScript
- `render.yaml`: Render deployment configuration
- `requirements.txt`: Python package dependencies

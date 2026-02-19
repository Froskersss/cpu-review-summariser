# CPU Review Summarizer

This is my project submission for Summer Internship Evaluation for Amity University Haryana for the academic year 2025/26.

## Project Overview

A web-based CPU review summarizer that aggregates reviews from multiple sources and presents them in an easy-to-read format.

### Idea
As an avid follower of the personal computer industry, reading reviews across multiple websites is often tedious. This project consolidates review articles from multiple reliable sources, summarizes them using advanced NLP models, and presents the information through an intuitive web interface.

### Websites Selected
- **TechPowerUp**: High-quality technical CPU reviews
- **TechSpot**: Comprehensive consumer-focused reviews

### CPUs Covered
- AMD Ryzen 9 9950X3D
- Intel Core i9 285K
- Intel Core i7 14700K
- AMD Ryzen 7 7700X
- Intel Core i5 13600K
- AMD Ryzen 5 5600X

### Methodology
1. **Data Collection**: Review articles scraped from TechPowerUp and TechSpot using ethical web scraping
2. **Summarization**: Articles summarized using the Google T5-base LLM model (high performance for text-to-text tasks)
3. **Web Interface**: Flask-based web application for user-friendly content delivery

## Project Structure

```
cpu-review-summariser-implementFlask/
├── app.py                      # Main Flask application with routes
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── data/                       # Data storage
│   ├── final_data_with_images.csv  # CPU data with summaries and image paths
│   ├── review_links.json       # External review URLs (TechPowerUp & TechSpot)
│   └── [other CSV files]       # Raw review data
├── templates/                  # HTML templates
│   ├── base.html              # Base template with navigation
│   ├── index.html             # Homepage with search and CPU image gallery
│   ├── cpu_summary.html       # Individual CPU summary page
│   ├── cpu.html               # CPU review links page
│   └── cpu_list.html          # All CPUs grid view
├── static/                    # Static assets
│   ├── style.css              # Responsive stylesheet
│   └── [CPU images]           # CPU product images
└── VENV_/                     # Python virtual environment
```

## Features

- **Homepage**: Search bar and dropdown navigation with CPU image gallery
- **CPU Summary Pages**: Individual pages with summarized reviews and manufacturer info
- **Full Reviews**: Quick-link buttons to view full reviews on TechPowerUp and TechSpot
- **CPU List**: Browse all CPUs in a responsive grid layout
- **Responsive Design**: Mobile-friendly interface with CSS grid and flexbox
- **Search Functionality**: Find CPUs by name across both Intel and AMD

## Installation & Setup

### Prerequisites
- Python 3.13+
- Virtual environment (already set up in `VENV_/`)

### Setup Steps

1. **Activate Virtual Environment**
   ```powershell
   .\VENV_\Scripts\Activate.ps1
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Application**
   ```bash
   python app.py
   ```

4. **Access Web App**
   - Open your browser and navigate to `http://localhost:5000`

## Dependencies

- Flask 3.1.2 - Web framework
- Pandas 3.0.1 - Data processing
- NumPy 2.4.2 - Numerical computing
- BeautifulSoup4 - Web scraping (if data collection needed)
- Requests - HTTP library
- Werkzeug 3.1.5 - WSGI utilities
- Jinja2 3.1.6 - Template engine

See `requirements.txt` for complete dependency list.

## API Routes

- `GET /` - Homepage with search and image gallery
- `POST /search` - Search CPUs by name
- `GET /cpu/<name>` - CPU review links page
- `GET /cpu/<name>/summary` - CPU summary page
- `GET /cpu-list` - All CPUs in grid layout

## Data Files

- **final_data_with_images.csv**: Contains CPU name, full review, summarized review, image reference, and manufacturer
- **review_links.json**: Maps CPU names to TechPowerUp and TechSpot review URLs

## Future Enhancements

- Database integration for dynamic content
- User authentication and ratings system
- CPU comparison tool
- Performance benchmark visualization
- Advanced filtering and sorting

## License

Submitted for academic evaluation purposes.

# AI Interview Analyzer

Automated analysis of interview transcripts with bias detection and structured summarization.

## Overview

This tool analyzes interview transcripts to generate structured summaries and identify potential hiring biases across 10 protected characteristics (gender, age, race, education, etc.). It provides actionable recommendations for improving interview practices and promoting fair hiring.

## Installation

```bash
git clone https://github.com/tejus05/ai-interview-analyzer.git
cd ai-interview-analyzer
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Configuration

1. Get a Gemini API key from [Google AI Studio](https://ai.google.dev)
2. Create a `.env` file:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Usage

```bash
streamlit run app.py
```

**Options:**
- **Sample Data**: Pre-loaded interview scenarios (fair, biased, multi-issue)
- **Custom Analysis**: Paste your own interview transcripts

## Output

- **Structured Summary**: Executive summary, strengths, areas for improvement, recommendations
- **Bias Detection**: Interactive dashboard with severity levels and category breakdowns
- **Visualizations**: Charts and word clouds for bias pattern analysis

## Technical Stack

- **Web Interface**: Streamlit for interactive dashboard
- **AI Engine**: Google Gemini 1.5 Flash for NLP analysis
- **Data Visualization**: Plotly for interactive charts, Matplotlib for word clouds
- **Data Processing**: Python with Pandas for transcript analysis

## License

This project is licensed under the MIT License - see the [LICENSE](https://choosealicense.com/licenses/mit) file for details.
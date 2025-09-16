# 🎯 AI-Powered Interview Analyzer

An intelligent tool that analyzes interview transcripts to generate structured summaries and detect potential biases, promoting fair hiring practices.

## Features

- **Structured Summarization**: Generates executive summaries, candidate strengths, areas for improvement, and hiring recommendations
- **Bias Detection**: Identifies potential biases related to gender, age, race, education, and other protected characteristics  
- **Visual Dashboard**: Interactive charts and word clouds to visualize bias patterns
- **Actionable Recommendations**: Provides specific suggestions for improving interview practices
- **Sample Data**: Pre-loaded interview transcripts for testing and demonstration

## Quick Start

### Prerequisites
- Python 3.8 or higher
- Google Gemini API key (get one at [ai.google.dev](https://ai.google.dev))

### Installation

1. **Navigate to the project directory**
   ```bash
   cd ai-interview-analyzer
   ```

2. **Create and activate a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   # or
   venv\Scripts\activate     # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   Or install individually if you encounter issues:
   ```bash
   pip install streamlit google-generativeai plotly matplotlib
   ```

4. **Get your Gemini API key**
   - Visit [Google AI Studio](https://ai.google.dev)
   - Create an API key
   - Keep it handy for the next step

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser**
   - The app will automatically open at `http://localhost:8501`
   - Enter your Gemini API key in the sidebar
   - Start analyzing interviews!

## How to Use

### Option 1: Use Sample Data
1. Check the "Load Sample Data" checkbox
2. Select from various interview scenarios (fair interviews, biased interviews, etc.)
3. Click "Analyze Interview" to see results

### Option 2: Analyze Your Own Interview
1. Paste your interview transcript in the text area
2. Make sure your Gemini API key is entered
3. Click "Analyze Interview"

### Understanding the Results

**Structured Summary**
- Executive summary of the interview
- Candidate's key strengths
- Areas for improvement
- Overall hiring recommendation

**Bias Detection Dashboard**  
- Table of detected biases with severity levels
- Bar chart showing bias categories
- Word cloud of suspicious phrases

**Recommendations**
- Specific suggestions for improving interview practices
- Guidelines for fair and inclusive hiring

## File Structure

```
ai-interview-analyzer/
├── app.py              # Main Streamlit application
├── analyzer.py         # Core analysis logic with Gemini API
├── sample_data.py      # Sample interview transcripts
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Sample Interview Types

The application includes several sample interviews for testing:

- **Fair Technical Interview**: Professional, skills-focused interview
- **Biased Interview - Gender**: Contains gender-based bias and stereotypes
- **Biased Interview - Age**: Age discrimination examples
- **Biased Interview - Education**: Educational elitism and class bias  
- **Biased Interview - Multiple Issues**: Intersecting biases (race, gender, age)
- **Professional Unbiased Interview**: Best practices example

## Technical Details

### AI Integration
- Uses Google's Gemini Pro model for analysis
- Optimized prompts for structured output
- JSON-based response parsing for reliability

### Bias Detection Categories
- Gender/Sex
- Age  
- Race/Ethnicity
- Religion
- Sexual Orientation
- Disability
- Education Background
- Socioeconomic Status
- Appearance
- Personal Life

### Visualizations
- Plotly charts for interactive bias category analysis
- Word clouds for suspicious phrase visualization
- Responsive design for different screen sizes

## Limitations

- Requires internet connection for Gemini API calls
- Analysis quality depends on transcript clarity and completeness
- Bias detection is AI-powered and may not catch all subtle biases
- Free Gemini API has rate limits

## Privacy & Ethics

- No interview data is stored permanently
- API calls are made directly to Google's servers
- Tool is designed to promote fair hiring, not replace human judgment
- Should be used as a supplementary aid, not the sole decision-making tool

## Troubleshooting

**"API key not configured" error**
- Make sure you've entered your Gemini API key in the sidebar
- Verify the key is valid and has proper permissions

**"Analysis failed" error**  
- Check your internet connection
- Verify your API key hasn't exceeded rate limits
- Try with a shorter transcript

**Charts not displaying**
- Ensure all dependencies are installed correctly
- Try refreshing the page

**Package installation issues**
- Use a virtual environment: `python -m venv venv && source venv/bin/activate`
- Install packages individually if batch installation fails
- Update pip: `pip install --upgrade pip`

## Contributing

This is a proof-of-concept project. Feel free to:
- Report issues or bugs
- Suggest improvements
- Add new bias detection categories
- Improve the sample data

## License

This project is for educational and research purposes. Please use responsibly and in compliance with your organization's policies.

---

**Disclaimer**: This tool is designed to assist in identifying potential biases but should not be the sole basis for hiring decisions. Human judgment and comprehensive evaluation processes remain essential for fair hiring practices.
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import pandas as pd
import os
from collections import Counter
from dotenv import load_dotenv
from analyzer import InterviewAnalyzer
from sample_data import SAMPLE_INTERVIEWS

load_dotenv()

# Configure page
st.set_page_config(
    page_title="AI Interview Analyzer",
    layout="wide"
)

def main():
    with st.container():
        st.title("AI-Powered Interview Analyzer")
        st.markdown("*Structured summaries with bias detection for fair hiring practices*")
        st.divider()
    
    # Initialize analyzer with API key from .env
    analyzer = InterviewAnalyzer()
    api_key = os.getenv('GEMINI_API_KEY')
    
    if not api_key:
        st.error("GEMINI_API_KEY not found in .env file. Please add your API key to the .env file.")
        return
    
    try:
        analyzer.set_api_key(api_key)
    except Exception as e:
        st.error(f"Failed to configure API key: {str(e)}")
        return
    
    with st.container():
        st.header("Interview Transcript Input")
        
        col1, col2 = st.columns([3, 1])
        
        with col2:
            use_sample = st.checkbox("Load Sample Data", help="Use pre-loaded interview transcripts for testing")
            if use_sample:
                sample_choice = st.selectbox(
                    "Choose a sample interview:",
                    options=list(SAMPLE_INTERVIEWS.keys()),
                    help="Select from various interview scenarios"
                )
        
        with col1:
            if use_sample:
                transcript = SAMPLE_INTERVIEWS[sample_choice]
                st.text_area("Interview Transcript", value=transcript, height=200, disabled=True)
            else:
                transcript = st.text_area(
                    "Paste the interview transcript here:",
                    height=200,
                    placeholder="Enter the complete interview conversation between interviewer and candidate..."
                )
        
        st.markdown("---")
        
        col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
        with col_btn2:
            analyze_button = st.button(
                "Analyze Interview", 
                type="primary", 
                disabled=not transcript,
                width='stretch'
            )
    
    if analyze_button:
        if not transcript.strip():
            st.error("Please provide an interview transcript to analyze")
            return
            
        with st.spinner("Analyzing interview transcript..."):
            try:
                summary_data = analyzer.generate_summary(transcript)
                bias_data = analyzer.detect_bias(transcript)
                recommendations = analyzer.generate_recommendations(bias_data)
                
                st.divider()
                st.header("Analysis Results")
                
                tab1, tab2, tab3 = st.tabs(["Summary", "Bias Detection", "Recommendations"])
                
                with tab1:
                    with st.container():
                        display_summary(summary_data)
                
                with tab2:
                    with st.container():
                        display_bias_dashboard(bias_data)
                
                with tab3:
                    with st.container():
                        display_recommendations(recommendations)
                
            except Exception as e:
                st.error(f"Analysis failed: {str(e)}")
                st.info("Please check your API key and internet connection")
                return

def display_summary(summary_data):
    """Display the structured interview summary"""
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Executive Summary")
        with st.container(border=True):
            st.write(summary_data.get('executive_summary', 'No executive summary available'))
        
        st.subheader("Candidate Strengths")
        with st.container(border=True):
            strengths = summary_data.get('strengths', [])
            if strengths:
                for strength in strengths:
                    st.write(f"• {strength}")
            else:
                st.write("No specific strengths identified")
    
    with col2:
        st.subheader("Areas for Improvement")
        with st.container(border=True):
            improvements = summary_data.get('improvements', [])
            if improvements:
                for improvement in improvements:
                    st.write(f"• {improvement}")
            else:
                st.write("No specific areas for improvement identified")
        
        st.subheader("Overall Recommendation")
        recommendation = summary_data.get('recommendation', 'No recommendation available')
        
        if 'hire' in recommendation.lower() or 'recommend' in recommendation.lower():
            st.success(recommendation)
        elif 'not' in recommendation.lower() or 'reject' in recommendation.lower():
            st.error(recommendation)
        else:
            st.info(recommendation)

def display_bias_dashboard(bias_data):
    """Display bias detection dashboard with visualizations"""
    bias_items = bias_data.get('bias_items', [])
    
    if bias_items:
        st.subheader("Detected Biases")
        with st.container(border=True):
            df = pd.DataFrame(bias_items)
            st.dataframe(df, width='stretch')
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.subheader("Bias Categories Overview")
            bias_counts = df['Bias_Type'].value_counts()
            
            if len(bias_counts) > 0:
                fig = px.bar(
                    x=bias_counts.index, 
                    y=bias_counts.values,
                    labels={'x': 'Bias Type', 'y': 'Count'},
                    title="Bias Detection by Category"
                )
                fig.update_layout(showlegend=False, height=400, margin=dict(l=0, r=0, t=40, b=0))
                st.plotly_chart(fig, width='stretch')
        
        with col2:
            st.subheader("Suspicious Phrases Analysis")
            suspicious_phrases = [item.get('Example_Phrase', '') for item in bias_items if item.get('Example_Phrase', '').strip()]
            
            if suspicious_phrases:
                all_words = []
                for phrase in suspicious_phrases:
                    words = phrase.lower().split()
                    filtered_words = [word.strip('.,!?;:"()[]') for word in words 
                                    if len(word) > 3 and word not in ['this', 'that', 'with', 'have', 'will', 'they', 'what', 'your', 'from', 'they', 'were', 'been', 'said']]
                    all_words.extend(filtered_words)
                
                if all_words:
                    word_counts = Counter(all_words)
                    top_words = dict(word_counts.most_common(10))
                    
                    if top_words:
                        fig = px.bar(
                            x=list(top_words.values()),
                            y=list(top_words.keys()),
                            orientation='h',
                            labels={'x': 'Frequency', 'y': 'Suspicious Words'},
                            title="Most Frequent Suspicious Words",
                            color=list(top_words.values()),
                            color_continuous_scale='Reds'
                        )
                        fig.update_layout(height=400, showlegend=False, margin=dict(l=0, r=0, t=40, b=0))
                        st.plotly_chart(fig, width='stretch')
                    else:
                        st.info("No significant word patterns detected")
                else:
                    st.info("No significant word patterns detected")
            else:
                st.info("No suspicious phrases detected")
        
        with st.expander("View All Suspicious Phrases"):
            for i, phrase in enumerate(suspicious_phrases, 1):
                st.write(f"{i}. \"{phrase}\"")
    else:
        with st.container(border=True):
            st.success("No significant biases detected in this interview")

def display_recommendations(recommendations):
    """Display actionable recommendations"""
    if recommendations and len(recommendations) > 0:
        st.subheader("Actionable Recommendations")
        
        cols = st.columns(2)
        for i, rec in enumerate(recommendations):
            col_idx = i % 2
            with cols[col_idx]:
                with st.container(border=True):
                    st.write(f"**{i + 1}.** {rec}")
    else:
        with st.container(border=True):
            st.info("No specific recommendations at this time. The interview appears to follow fair hiring practices.")

if __name__ == "__main__":
    main()
import google.generativeai as genai
import json
import re
from typing import Dict, List, Any

class InterviewAnalyzer:
    """
    Core analyzer for interview transcripts using Gemini API
    Handles summarization, bias detection, and recommendations
    """
    
    def __init__(self):
        self.api_key = None
        self.model = None
        
    def set_api_key(self, api_key: str):
        """Configure Gemini API with the provided key"""
        self.api_key = api_key
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')
    
    def generate_summary(self, transcript: str) -> Dict[str, Any]:
        """
        Generate structured summary of interview transcript
        Returns: Dictionary with executive_summary, strengths, improvements, recommendation
        """
        if not self.model:
            raise Exception("API key not configured")
            
        prompt = f"""
        Analyze this interview transcript and provide a structured summary in JSON format.
        
        Interview Transcript:
        {transcript}
        
        Please return a JSON object with these exact keys:
        {{
            "executive_summary": "2-3 sentence overview of the interview",
            "strengths": ["list", "of", "candidate", "strengths"],
            "improvements": ["areas", "for", "improvement"],
            "recommendation": "overall hiring recommendation with brief reasoning"
        }}
        
        Focus on:
        - Technical skills demonstrated
        - Communication abilities
        - Problem-solving approach
        - Cultural fit indicators
        - Professional experience relevance
        
        Keep it concise and professional. Return only valid JSON.
        """
        
        try:
            response = self.model.generate_content(prompt)
            # Extract JSON from response
            json_match = re.search(r'\{.*\}', response.text, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
            else:
                # Fallback if JSON parsing fails
                return self._parse_summary_fallback(response.text)
        except Exception as e:
            return {
                "executive_summary": "Analysis failed. Please check your API key and try again.",
                "strengths": [],
                "improvements": [],
                "recommendation": f"Error: {str(e)}"
            }
    
    def detect_bias(self, transcript: str) -> Dict[str, Any]:
        """
        Detect potential biases in interview questions and discussion
        Returns: Dictionary with bias_items list
        """
        if not self.model:
            raise Exception("API key not configured")
            
        prompt = f"""
        Analyze this interview transcript for potential biases and discriminatory language.
        
        Interview Transcript:
        {transcript}
        
        Look for biases related to:
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
        
        Return a JSON object with this structure:
        {{
            "bias_items": [
                {{
                    "Bias_Type": "specific bias category",
                    "Example_Phrase": "exact phrase from transcript",
                    "Severity": "Low/Medium/High"
                }}
            ]
        }}
        
        Only include clear examples of bias. If no significant biases are found, return empty bias_items array.
        Be specific about phrases and accurate about severity levels.
        Return only valid JSON.
        """
        
        try:
            response = self.model.generate_content(prompt)
            # Extract JSON from response
            json_match = re.search(r'\{.*\}', response.text, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
            else:
                return {"bias_items": []}
        except Exception as e:
            return {
                "bias_items": [{
                    "Bias_Type": "Analysis Error",
                    "Example_Phrase": f"Failed to analyze: {str(e)}",
                    "Severity": "Unknown"
                }]
            }
    
    def generate_recommendations(self, bias_data: Dict[str, Any]) -> List[str]:
        """
        Generate actionable recommendations based on bias detection results
        Returns: List of recommendation strings
        """
        if not self.model:
            return ["API key not configured"]
            
        bias_items = bias_data.get('bias_items', [])
        
        if not bias_items:
            return [
                "Great job! No significant biases were detected in this interview.",
                "Continue following structured interview practices and focusing on job-relevant skills.",
                "Consider using standardized questions to maintain consistency across all candidates."
            ]
        
        prompt = f"""
        Based on these detected biases in an interview, provide 3-5 specific, actionable recommendations for improvement:
        
        Detected Biases:
        {json.dumps(bias_items, indent=2)}
        
        Provide recommendations that are:
        - Specific and actionable
        - Professional and constructive
        - Focused on improving interview practices
        - Aimed at promoting fair and inclusive hiring
        
        Return as a simple JSON array of strings:
        ["recommendation 1", "recommendation 2", "recommendation 3"]
        
        Each recommendation should be 1-2 sentences maximum.
        """
        
        try:
            response = self.model.generate_content(prompt)
            # Extract JSON array from response
            json_match = re.search(r'\[.*\]', response.text, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
            else:
                # Fallback recommendations
                return self._generate_fallback_recommendations(bias_items)
        except Exception as e:
            return [f"Error generating recommendations: {str(e)}"]
    
    def _parse_summary_fallback(self, text: str) -> Dict[str, Any]:
        """Fallback parser if JSON extraction fails"""
        return {
            "executive_summary": "Summary parsing failed - please check the transcript format",
            "strengths": ["Analysis incomplete"],
            "improvements": ["Technical issue occurred"],
            "recommendation": "Please try again with a valid API key"
        }
    
    def _generate_fallback_recommendations(self, bias_items: List[Dict]) -> List[str]:
        """Generate basic recommendations when AI generation fails"""
        recommendations = []
        
        bias_types = [item.get('Bias_Type', '').lower() for item in bias_items]
        
        if any('gender' in bt for bt in bias_types):
            recommendations.append("Avoid questions about family planning, marital status, or use gender-specific language.")
        
        if any('age' in bt for bt in bias_types):
            recommendations.append("Focus on skills and experience rather than age-related questions or assumptions.")
        
        if any('education' in bt for bt in bias_types):
            recommendations.append("Evaluate candidates based on demonstrated skills rather than educational pedigree.")
        
        recommendations.append("Use structured interviews with standardized questions for all candidates.")
        recommendations.append("Consider having multiple interviewers to reduce individual bias.")
        
        return recommendations[:5]  # Return max 5 recommendations
from cachetools import LRUCache
import google.generativeai as genai
import json
import re
from dotenv import load_dotenv
import os



response_cache = LRUCache(maxsize=100)

load_dotenv()


api_key = os.getenv("GENAI_API_KEY")
if not api_key:
    raise ValueError("API key is not set. Please check your .env file.")


genai.configure(api_key=api_key)


SCORING_PROMPT = """
You are an AI expert grading student responses about AI concepts.

Question: {question}
Student Response: {response}

Score the response on a scale of 1-10 and provide specific feedback in brief.
"""
        

def score_response(question, response):

    prompt = SCORING_PROMPT.format(question=question, response=response)

    model = genai.GenerativeModel("gemini-1.5-flash")
    result = model.generate_content(prompt)

    print(f"Response Text: {result.text}")

    score , feedback =extract_score_and_feedback(result.text)

    
    return score, feedback

def extract_score_and_feedback(response_text):

    score_match = re.search(r"Score: (\d+)", response_text)
    feedback_match = re.search(r"Feedback:\s*(.*)", response_text)

    if score_match:
        score = int(score_match.group(1)) 
    else:
        score = None  

    if feedback_match:
        feedback = feedback_match.group(1).strip() 
    else:
        feedback = None 

    return score, feedback



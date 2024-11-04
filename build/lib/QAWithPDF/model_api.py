import os
from dotenv import load_dotenv
import sys

from llama_index.llms.gemini import Gemini
from IPython.display import Markdown, display
import google.generativeai as genai
from logger import logging
from exception import CustomException

load_dotenv()

google_api_key=os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=google_api_key)

def load_model():
    
    """
    Loads a Gemini-Pro model for natural language processing.

    Returns:
    - Gemini: An instance of the Gemini class initialized with the 'gemini-pro' model.
    """
    try:
        model=Gemini(models='gemini-pro',api_key=google_api_key)
        return model
    except Exception as e:
        raise CustomException(e,sys)
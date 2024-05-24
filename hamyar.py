import google.generativeai as genai
from rich.console import Console
from rich.markdown import Markdown
import sys

API_KEY = "AIzaSyCtOeQwtlABMLwqJgDXD7UhZgQ8u_x5heA"

def main():
        print("------Gemini------")
        chat()
        
    
def chat():
    genai.configure(api_key=API_KEY)

    # Set up the model
    generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
    }

    safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    ]

    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                generation_config=generation_config,
                                safety_settings=safety_settings)


    while True:
        convo = model.start_chat(history=[])
        try: 
            message = input("Input: ")
        except EOFError:
            sys.exit()
        try:
            convo.send_message(message)
            console = Console()
            md = Markdown(convo.last.text)
            print("Output:")
            console.print(md)
        except:
            sys.exit("an error occurred")
        print("------------------")
    
main()

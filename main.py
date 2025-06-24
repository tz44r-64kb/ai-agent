import os
import sys
from dotenv import load_dotenv
args = sys.argv[1:]

if not args:
    print("AI Code Assistant")
    print('\nUsage: python main.py "your prompt here"')
    print('Example: "python3 main.py "How do I build a calculator app?"')
    sys.exit(1)

prompt = " ".join(args)
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents=prompt
        )

prompt_token_count = response.usage_metadata.prompt_token_count
candidates_token_count = response.usage_metadata.candidates_token_count

print(response.text)
print(f"Prompt tokens: {prompt_token_count}")
print(f"Response tokens: {candidates_token_count}")

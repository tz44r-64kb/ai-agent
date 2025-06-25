import os
import sys
from dotenv import load_dotenv
from google.genai import types
from google import genai

def main():
    load_dotenv()
    args = sys.argv[1:]

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here"')
        print('Example: "python3 main.py "How do I build a calculator app?"')
        sys.exit(1)
    
    is_verbose = "--verbose" in args
    prompt = " ".join(args)
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)


    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),        
    ]

    if is_verbose:
        print(f"User prompt: {prompt}")

    generate_content(client, messages, is_verbose)

def generate_content(client, messages, is_verbose):
    response = client.models.generate_content(
            model="gemini-2.0-flash-001", 
            contents=messages
            )

    prompt_token_count = response.usage_metadata.prompt_token_count
    candidates_token_count = response.usage_metadata.candidates_token_count

    print(response.text)
    if is_verbose:
        print(f"Prompt tokens: {prompt_token_count}")
        print(f"Response tokens: {candidates_token_count}")


if __name__ == "__main__":
    main()

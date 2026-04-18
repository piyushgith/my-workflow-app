import os
import sys
from anthropic import Anthropic

def run_morning_call():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY not found.")
        sys.exit(1)

    client = Anthropic(api_key=api_key)

    try:
        message = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=512,
            messages=[
                {"role": "user", "content": "Generate a concise 3-point summary of tech news for today."}
            ]
        )
        print(f"Claude Response:\n{message.content[0].text}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_morning_call()

import os
import sys
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

if len(sys.argv) < 2:
    print("No prompt sent")
    sys.exit(1)

reply = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=str(sys.argv[1])
)


print(reply.text)
print(f"Prompt tokens: {reply.usage_metadata.prompt_token_count}")
print(f"Response tokens: {reply.usage_metadata.candidates_token_count}")

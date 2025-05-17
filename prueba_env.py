from dotenv import load_dotenv
import os

load_dotenv()

print("Variable API_KEY:", os.getenv("API_KEY"))

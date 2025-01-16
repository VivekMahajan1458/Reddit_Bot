import os

# Reddit API Credentials
CLIENT_ID = os.environ.get('JSNvUdzR9-VVjr8qoG_eTQ')
CLIENT_SECRET = os.environ.get('exh9ocGq_zS-6ioLnF-KpR3n2IM2_w')
USER_AGENT = "Redit_Bot by u/Hour-Tip-4483"  # Replace with your bot's name

# Groq API Credentials
GROQ_API_KEY = os.environ.get('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')
GROQ_API_ENDPOINT = "https://api.groq.io/v1/search?api_key=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&query=test" 

# Scheduling 
POSTING_TIMES = ["19:04", "19:05"]  # Example: Post at 9 AM and 3 PM
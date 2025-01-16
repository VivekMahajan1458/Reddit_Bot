import praw
import schedule
import time
from generate_groq_content import generate_groq_content

# Reddit API Initialization
reddit = praw.Reddit(
    client_id='JSNvUdzR9-VVjr8qoG_eTQ',
    client_secret='exh9ocGq_zS-6ioLnF-KpR3n2IM2_w',
    user_agent="Redit_Bot by u/Hour-Tip-4483"
)

# Define a function to post to Reddit
def post_to_reddit():
    try:
        # Generate title and content using the Groq API
        title = generate_groq_content("Generate an interesting title for a Reddit post.")
        text = generate_groq_content("Write a captivating Reddit post.")

        # Post to the test subreddit
        subreddit = reddit.subreddit("test")
        submission = subreddit.submit(title, selftext=text)

        print(f"Successfully posted: {submission.url}")
    except praw.exceptions.PRAWException as e:
        print(f"Reddit API Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

# Schedule a single post immediately for testing
schedule.every(1).seconds.do(post_to_reddit)  # Post once right now for testing

# Run the scheduler
if __name__ == "__main__":
    print("Reddit bot is running and will post shortly...")
    while True:
        schedule.run_pending()
        time.sleep(1)

# Reddit Bot Project

This project is a Reddit bot that automatically generates content using the Groq API and posts it to a specified subreddit at scheduled times.

## Features
- Automatically generates content using the Groq API.
- Posts content to Reddit using the Reddit API.
- Scheduled daily posts at predefined times.

## Prerequisites
- Python 3.6 or later.
- `pip` (Python package manager) for installing dependencies.

## Installation
1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/Reddit_Bot.git
   cd Reddit_Bot

2. Create a virtual environment:

     python3 -m venv venv
   
3. Activate the virtual environment

     venv\Scripts\activate

4. Install the required dependencies:

     pip install -r requirements.txt


This section guides users through the setup process, so they can run your project on their own machine.


### **5. Usage Instructions**

Explain how to run your project after setting it up. In this case, you'll show how to configure the API keys, edit the relevant files, and run the bot.

```markdown
## Usage
1. Edit `config.py` with your Reddit and Groq API credentials.
2. Run the `reddit_bot.py` script to start posting content:

   ```bash
   python reddit_bot.py
3. The bot will post at the scheduled times defined in POSTING_TIMES.

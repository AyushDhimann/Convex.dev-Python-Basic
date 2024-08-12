from flask import Flask, render_template, request, redirect, url_for
from convex import ConvexClient
import random
import os
from dotenv import load_dotenv
from datetime import datetime

app = Flask(__name__)

# Load environment variables from .env.local
load_dotenv(dotenv_path='.env.local')

# Initialize Convex Client
convex_url = os.getenv("CONVEX_URL")
if convex_url is None:
    raise ValueError("CONVEX_URL environment variable is not set.")

client = ConvexClient(convex_url)

def generate_user_name():
    """Generate a random user name."""
    return f"User {random.randint(1000, 9999)}"

@app.route('/')
def index():
    try:
        # Fetch messages using the 'messages:list' query
        messages = client.query("messages:list")
        # Format creation time in the desired format
        for message in messages:
            message['_creationTime'] = datetime.fromisoformat(message['_creationTime']).strftime("%H:%M:%S")
    except Exception as e:
        print(f"Error fetching messages: {e}")
        messages = []
    return render_template('templates/index.html', messages=messages)

@app.route('/send', methods=['POST'])
def send_message():
    body = request.form.get('body')
    if body:
        user_name = generate_user_name()  # Generate a new user name for each message
        try:
            # Send a new message using the 'messages:send' mutation
            client.mutation("messages:send", {"body": body, "author": user_name})
        except Exception as e:
            print(f"Error sending message: {e}")
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
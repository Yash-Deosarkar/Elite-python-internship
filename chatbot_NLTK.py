import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from datetime import datetime
import random

# nltk.download('punkt')
# nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def preprocess(text):
    tokens = word_tokenize(text.lower())
    filtered = [word for word in tokens if word.isalpha() and word not in stop_words]
    return filtered

def respond(user_input):
    tokens = preprocess(user_input)

    if any(word in tokens for word in ['hello', 'hi', 'hey']):
        return random.choice(["Hey there!", "Hello! How can I assist you?", "Hi! Need any help?"])

    elif any(word in tokens for word in ['bye', 'exit', 'quit']):
        return "Goodbye! Have a great day. 👋"

    elif 'time' in tokens:
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}"

    elif any(word in tokens for word in ['weather', 'sunny', 'rain']):
        return "I can't fetch live weather now, but I hope it's pleasant where you are ☀️"

    elif any(word in tokens for word in ['your', 'name']):
        return "I'm EL-Bot, your internship assistant 🤖"

    elif any(word in tokens for word in ['help', 'support']):
        return "I'm here to help! You can ask me about weather, time, or just say hi 😄"

    elif any(word in tokens for word in ['joke', 'funny', 'laugh']):
        return random.choice([
            "Why did the Python developer go broke? Because he used up all his cache 😂",
            "Why don’t programmers like nature? It has too many bugs!",
            "Why do Java developers wear glasses? Because they don’t see sharp!"
        ])

    elif any(word in tokens for word in ['python', 'language', 'code']):
        return "Python is awesome! You can build websites, automate tasks, and even make AI with it 🐍"

    elif any(word in tokens for word in ['thanks', 'thank', 'thx']):
        return "You're most welcome! 😊"

    else:
        return "Hmm, I didn't quite get that. Can you rephrase?"

# Start chatbot
print("🤖 EL-Bot: Yash's Chatbot here (type 'exit' to quit)")
while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit', 'bye']:
        print("EL-Bot:", respond(user_input))
        break
    print("EL-Bot:", respond(user_input))

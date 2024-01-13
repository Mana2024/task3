import nltk
from nltk.chat.util import Chat, reflections

# Define pairs for the chatbot to understand and respond to
pairs = [
    ["hi|hello|hey", ["Hi there!", "Hello!", "Hey!"]],
    ["how are you", ["I'm good, thank you!", "I'm doing well, how about you?"]],
    ["what is your name", ["I'm a chatbot. You can call me ChatGPT.", "I don't have a name. You can just call me Chatbot."]],
    ["your name", ["I'm just a chatbot.", "No name here, just call me Chatbot."]],
    ["bye|goodbye", ["Goodbye!", "Bye! Take care."]],
    ["", ["I'm not sure how to respond to that.", "Can you please rephrase that?", "I'm still learning!"]],
]

# Create a chatbot using NLTK's Chat class
chatbot = Chat(pairs, reflections)

# Function to start the conversation with the user
def start_chat():
    print("Hello! I'm a text-based chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break
        else:
            response = chatbot.respond(user_input)
            print("Chatbot:", response)

# Download NLTK data (if not already downloaded)
nltk.download('punkt')

# Start the chat
start_chat()

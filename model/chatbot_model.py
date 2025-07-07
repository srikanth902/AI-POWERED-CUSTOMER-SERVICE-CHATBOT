from transformers import pipeline

chatbot = pipeline("text-generation", model="gpt2")

# Rule-based fallback dictionary
custom_responses = {
    "hi": "Hi! How are you doing today?",
    "hello": "Hello there! How can I help you?",
    "how are you": "I'm doing well, thank you! How can I assist you today?",
    "what is your name": "I'm an AI-powered assistant created to help you!",
    "bye": "Goodbye! Have a great day!",
    "thank you": "You're welcome! Let me know if there's anything else I can do."
}

def generate_response(user_input):
    user_input_lower = user_input.lower().strip()

    for key in custom_responses:
        if key in user_input_lower:
            return custom_responses[key]

    # Fallback to GPT-2 for more complex or unknown inputs
    response = chatbot(user_input, max_length=60, num_return_sequences=1)
    return response[0]['generated_text'].strip()

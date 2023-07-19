# Project 3 - DSA
# Building a custom chatbot using GPT-4 and Python

# Import
import openai

# Key (Add the user key in this field)
openai.api_key = "add_key_user_here"

# Func to text generation from Language Model

def gera_texto(texto):

    # Gets the answer from the Language Model
    response = openai.Completion.create(        
        # Model used
        # Another models available at https://platforrm.openai.com/account/rate-limits
        engine = "text-davinci-003",

        # Starting text for the chatbot
        prompt = texto,

        # Answer length 
        max_tokens = 150,

        # Number of conclusions generated for each prompt
        n = 5,

        # No stop-sequences for the output
        stop = None,

        # Selecting the randomizer index (0-1)
        # Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
        temperature = 0.8,
    )

    return response.choices[0].text.strip()

# Main function

def main():
    print("\n Welcome to Arborians chatbot!")
    print("www.arborians.com")
    print("(Type 'bye' to end the chat.)")

    # Loop
    while True:

        # input
        user_message = input("\nYour question: ")

        # Setting 'bye'
        if user_message.lower() == "bye":
            break

        # Variable declaration (collecting the input)
        gpt4_prompt = f"\nUsuário: {user_message}\nChatbot:"

        # Gets the output running the function
        chatbot_response = gera_texto(gpt4_prompt)

        # Printing the output
        print(f"\nChatbot: {chatbot_response}")

# Main
if __name__ == "__main__":
    main()
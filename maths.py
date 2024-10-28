import openai
import re

# Set up OpenAI API Key
openai.api_key = 'your_openai_api_key_here'

# Function to check if input is a simple math problem
def is_math_problem(user_input):
    math_pattern = r"^\s*[\d+\-*/.()]+\s*$"
    return bool(re.match(math_pattern, user_input))

# Function to solve basic math questions
def solve_math_expression(expression):
    try:
        result = eval(expression)
        return f"The answer is: {result}"
    except Exception as e:
        return "Sorry, I couldn't understand the math expression."

# Main chatbot response function using the new API
def chatbot_response(user_input):
    if is_math_problem(user_input):
        return solve_math_expression(user_input)
    else:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        return response.choices[0].message["content"]

# Chat loop
print("Welcome to the Math Solver Bot! (type 'quit' to exit)")
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Bot:", response)
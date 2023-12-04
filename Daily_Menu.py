import random
import json
from food_data import food_preferences
from dishes_data import dishes

def get_user_preference(category, choices):
    """
    Prompts the user to choose a preference from a list of options within a specified category.

    Parameters:
    category (str): The category for which the preference is sought.
    choices (list): A list of available choices.

    Returns:
    str: The user's chosen preference as a string.
    """
    choice_input = input(f"What kind of {category} do you prefer? (Options: {', '.join(choices)})\n")
    while choice_input not in choices:
        choice_input = input(f"Please choose a valid option for {category}: (Options: {', '.join(choices)})\n")
    return choice_input

def suggest_menu():
    """
    Suggests a menu based on the user's preferences for various food categories.

    It prompts the user for their preferences in categories such as meat type, cooking style, flavor, 
    and calorie level, and then suggests a dish based on these preferences.

    Returns:
    str: A string describing the suggested meal.
    """
    preferred_meat = get_user_preference('meat', food_preferences['meat'])
    cooking_style = get_user_preference('cooking_style', food_preferences['cooking_style'])
    flavor = get_user_preference('flavor', food_preferences['flavor'])
    calories = get_user_preference('calories', food_preferences['calories'])

    chosen_dish = dishes.get((preferred_meat, cooking_style, flavor, calories), 'Custom Dish')

    meal_suggestion = f"We suggest {chosen_dish} with a {flavor} flavor and around {calories} calories."
    return meal_suggestion

def get_response(question):
    """
    Provides a response to a given user question or input.

    Parameters:
    question (str): The user's question or input.

    Returns:
    str: A response string. If the input is 'menu', it triggers the suggest_menu function.
         For other predefined inputs like 'help' or 'exit', it provides standard responses. 
         Otherwise, it returns a default message.
    """
    if question.lower() == 'menu':
        return suggest_menu()

    responses = {
        "help": "Sure, I can help you. What do you need assistance with?",
        "exit": "Thank you for using our service. Have a great day!"
    }

    clean_question = question.lower().strip()

    return responses.get(clean_question, "I'm not sure how to answer that. Can you ask something else?")


def main():
    """
    The main function of the script.

    """
    print("Welcome to the Conversation and Menu Suggestion System!")
    while True:
        user_input = input("Ask me a question,like help,and exit or type 'menu' for a meal suggestion: ")
        if user_input.lower() == 'exit':
            print(get_response(user_input))
            break
        else:
            print(get_response(user_input))

if __name__ == "__main__":
    main()

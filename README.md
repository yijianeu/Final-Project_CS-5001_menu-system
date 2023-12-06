# Final Project Report

* Student Name: Yijia Cao
* Github Username: yijianeu
* Semester: Fall 2023
* Course: CS-5001



## Description 
Creating a menu system to help decide daily meals is a practical and valuable tool. It would consider personal preferences, dietary restrictions, and nutritional goals to suggest meal options. This system could alleviate the daily stress of meal decision-making by offering tailored suggestions based on a set of criteria, including:

* Preferred types of meat or protein sources.
* Desired cooking styles (grilled, baked, steamed, etc.).
* Flavor preferences (spicy, savory, sweet, etc.).
* Caloric intake based on individual dietary needs.



## Key Features
* The system asks the user a series of questions concerning their preferences for different food categories, such as type of meat, cooking method, flavor profile, and number of calories. This enables the provision of a highly personalized meal plan that accommodates the dietary needs and preferences of every individual.
* The 'get_user_preference' function allows the system to have a conversational interaction with the user by requesting their preferences and verifying the accuracy of their selections. User engagement is increased by this interaction, which resembles a casual conversation.
* The system is easy to use even for non-techies, as it provides clear prompts and straightforward instructions.
* The script is very flexible to accommodate a variety of cuisines and changing dietary trends because it uses predefined data sets (food_preferences and dishes_data), which make it easy to add new food categories or dishes to the system.

## Guide
Here's a step-by-step breakdown of how the user would interact with the system:

* Welcome Menu: When the system starts, it greets the user with a welcome message, inviting them to interact with the menu system.
* Guided Choices: The user is guided through a series of choices. Each step narrows down the options, making it easy for the user to make decisions without feeling overwhelmed.

Sequential Selection:

* Menu: The user starts by indicating they want a meal suggestion by typing 'menu'.
* Meat: The system then prompts the user to select their preferred type of meat from the available options.
* Cooking: Next, the user chooses their desired cooking style, further customizing the meal to their liking.
* Flavor: The user selects their preferred flavor profile, adding another layer of personalization.
* Calories: Finally, the user chooses a calorie range, allowing them to align the meal with their dietary goals.

* Resulting Meal Suggestion: After the user has made all their selections, the system generates a meal suggestion that matches their preferences in meat, cooking style, flavor, and calories.


## Installation Instructions
* Prepare the Python Files: Ensure you have the main Python file (Daily_menu.py) and the two data files (food_data.py and dishes_data.py) saved in the same directory.
* API Keys: There is no API key required
* Run the Program: Navigate to the directory containing your Python files in the command line, and then run the main Python script. 

## Code Review
* The 'get_user_preference' function is a crucial component of interacting with the user to obtain their preferences. It has a validation loop to ensure that the input from the user matches one of the options.

  <img width="805" alt="Screenshot 2023-12-06 at 1 21 14 PM" src="https://github.com/yijianeu/Final-Project_CS-5001_menu-system/assets/152763320/115953a4-ec4e-4d92-955a-4920992c830f">

* The "suggest_menu" function dynamically creates a meal suggestion based on user input, demonstrating the use of data structures (like dictionaries) and control flow to match user preferences with available dishes.

  <img width="749" alt="Screenshot 2023-12-06 at 1 22 27 PM" src="https://github.com/yijianeu/Final-Project_CS-5001_menu-system/assets/152763320/3dc6a42e-112f-4b83-8837-599b47405e3c">



  


## Example Runs
Here is the example runs:


<img width="569" alt="Screenshot 2023-12-06 at 1 15 04 PM" src="https://github.com/yijianeu/Final-Project_CS-5001_menu-system/assets/152763320/fb98fd60-074f-41bb-a595-6b5379bee314">




## Testing
How did you test your code? What did you do to make sure your code was correct? If you wrote unit tests, you can link to them here. If you did run tests, make sure you document them as text files, and include them in your submission. 

> _Make it easy for us to know you *ran the project* and *tested the project* before you submitted this report!_


## Missing Features / What's Next
The system could be designed to learn from past choices to better tailor future meal suggestions, making it an adaptive tool for meal planning. It would also be beneficial if the system could incorporate a grocery list feature to ensure all ingredients for the selected meals are noted, making shopping more efficient. Such a system's implementation could range from a simple app to a more complex AI-driven platform that could integrate with smart kitchen appliances for a seamless culinary experience. It would be a modern solution to the timeless question of "What should I eat today?

## Final Reflection
Write at least a paragraph about your experience in this course. What did you learn? What do you need to do to learn more? Key takeaways? etc.

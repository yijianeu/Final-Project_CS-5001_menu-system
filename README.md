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

* The 'get_response' function answers questions from users and, based on the input, starts the appropriate function or response. Moreover, it has a simple response system for common inputs like "help" and "exit."

  <img width="759" alt="Screenshot 2023-12-06 at 1 23 48 PM" src="https://github.com/yijianeu/Final-Project_CS-5001_menu-system/assets/152763320/4e8c57ca-f4ad-48af-9cf8-9f42baf0278a">

* The main function keeps prompting the user until they decide to quit by using a while True loop.

  <img width="761" alt="Screenshot 2023-12-06 at 1 24 32 PM" src="https://github.com/yijianeu/Final-Project_CS-5001_menu-system/assets/152763320/56af3719-38c5-493a-a0d0-cbd4056aeccc">


## Example Runs
Here is the example runs:


<img width="569" alt="Screenshot 2023-12-06 at 1 15 04 PM" src="https://github.com/yijianeu/Final-Project_CS-5001_menu-system/assets/152763320/fb98fd60-074f-41bb-a595-6b5379bee314">




## Testing
* I wrote a series of unit tests to validate the functionality of each component of my system. The tests were specifically designed to cover key functions like 'get_user_preference', 'suggest_menu', and 'get_response'.
* I ran each unit test to confirm that each part of my system was working as it should. This was essential to make sure every function performed as planned in a range of scenarios.
* I asked different people to run the project on their systems. This was done to identify any potential weaknesses, usability issues, or bugs that might not have been evident during unit and integration testing.

* The Daily_Menu_test.py is the file about my test file to test this project

## Missing Features / What's Next
The meal planning tool could be made adaptive by incorporating the system's ability to learn from previous selections and better customize meal recommendations in the future. To make shopping more effective, it would also be advantageous if the system could include a grocery list feature that would guarantee that all the ingredients for the meals that have been chosen are noted. The implementation of such a system could take the form of a straightforward app or a more intricate AI-driven platform that works in tandem with smart kitchen appliances to provide a seamless culinary experience. It would be a cutting-edge response to the age-old query, "What should I eat today?"

## Final Reflection
My journey through CS 5001 has been an incredibly enriching experience, marking my first significant step into the field of computer science. This course has not only introduced me to the fundamentals of programming but also deepened my understanding in several key areas:

1. Python Code Structure:
   * The course gave me a thorough understanding of the syntax and organization of Python. I place great value on learning how to write code that is neat and well-organized.
2. Logical Thinking:
   * Understanding the logic behind different Python functions and how they interact has helped me become a better problem solver.
4. Building Information Systems:
   * One of my greatest achievements to date has been learning how to create simple information systems. This application of knowledge in the real world demonstrates how effectively the course imparts practical skills.

CS 5001 has been more than just an introductory course; it has been a gateway to the vast and dynamic field of computer science. My acquired knowledge and skills form the basis for my future academic endeavors and professional growth in this field. I have no doubt that the foundations laid in this course will act as a roadmap for me as I pursue my computer science career.

from Daily_Menu import (get_response, suggest_menu)

food_preferences = {
    'meat': ['chicken', 'beef', 'pork', 'tofu(vegan)'],
    'cooking_style': ['grilled', 'stir-fried', 'baked', 'steamed'],
    'flavor': ['salty', 'sweet', 'spicy', 'sour'],
    'calories': ['500', '700', '900', '1200']
}

dishes = {
    ('tofu(vegan)', 'grilled', 'salty', '500'): 'Grilled Tofu with Savory Glaze',
    ('chicken', 'baked', 'spicy', '700'): 'Spicy Baked Chicken with Hot Sauce',
    ('beef', 'steamed', 'sweet', '900'): 'Sweet Steamed Beef with Maple Glaze',
}

def check_result(test_name, result, expected):
    if result != expected:
        print(f"Failed: {test_name}\nExpected: {expected}\nGot: {result}")
        return 1
    return 0

def test_get_response():
    count = 0

    result = get_response('help')
    expected = "Sure, I can help you. What do you need assistance with?"
    count += check_result("get_response('help')", result, expected)

    result = get_response('exit')
    expected = "Thank you for using our service. Have a great day!"
    count += check_result("get_response('exit')", result, expected)

    result = get_response('unknown')
    expected = "I'm not sure how to answer that. Can you ask something else?"
    count += check_result("get_response('unknown')", result, expected)

    return count

def test_suggest_menu():
    count = 0

    preferences = [('tofu(vegan)', 'grilled', 'salty', '500'),
                   ('chicken', 'baked', 'spicy', '700'),
                   ('beef', 'steamed', 'sweet', '900')]

    expected_dishes = ['Grilled Tofu with Savory Glaze',
                       'Spicy Baked Chicken with Hot Sauce',
                       'Sweet Steamed Beef with Maple Glaze']

    for i, pref in enumerate(preferences):
        test_name = f"suggest_menu with preferences {pref}"
        result = suggest_menu(pref[0], pref[1], pref[2], pref[3])
        expected = expected_dishes[i]
        count += check_result(test_name, result, expected)

    return count

if __name__ == "__main__":
    total_count = 0
    total_count += test_get_response()
    total_count += test_suggest_menu()
    print("\nTotal Incorrect Results:", total_count)




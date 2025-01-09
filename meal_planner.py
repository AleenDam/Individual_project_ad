from datetime import datetime

def greet_user():
    """
    Greets user with their name and today's date.
    Asks user to enter their name to print out the greeting message.
    """
    user = input('Enter your name: ')
    today = datetime.today()
    form_date = today.strftime('%A, %d. %B %Y')
    print(f'Hello {user}. Are you hungry?')
    print(f'Let us plan your meal for today, {form_date}.')

 
def choose_meal():
    '''
    Asks user to choose a meal from the given options.
    Returns: Name of the chosen meal as a string.
    '''
    meals = [
        'Chicken & Chips',
        'Chilli Con Carne',
        'Broccoli Soup',
        'Vegan Apple Crumble',
        'Garlic Mushroom Pie',
        'Spaghetti Bolognese',
        'Grilled Salmon'
    ]

    print('\nWhat do you fancy as a mouth-watering meal? \nPlease note, that all recipes are for 4 people.')
    print('\nChoose your desired meal option and enter the number: ')
    for i, meal in enumerate(meals, start=1):
        print(f'{i}. {meal}')
    try:
        choice = int(input('\nEnter the number of your choice: '))
        if 1 <= choice <= len(meals):
            return meals[choice -1]   
        else:
            print('Invalid choice. Please enter a number between 1 and 7.') 
            return choose_meal()    
    except ValueError:
        print('Invalid input. Please enter a valid number.') 


def main():
    '''
    Main function to plan a meal by choosing a recipe as an interaction with the user.
    Functions: greet_user, choose_meal and print_shopping_list.
    Return: printing a shopping list with prices per item and the final sum for the chosen recipe.
    '''
    greet_user()  
    meal_choice = choose_meal()
    recipes = {
        'Chicken & Chips': chicken_chips,
        'Chilli Con Carne': chilli_con_carne,
        'Broccoli Soup': broccoli_soup,
        'Vegan Apple Crumble': vegan_apple_crumble,
        'Garlic Mushroom Pie': garlic_mushroom_pie,
        'Spaghetti Bolognese': spaghetti_bolognese,
        'Grilled Salmon': grilled_salmon
    }
    selected_recipe = recipes.get(meal_choice)
    if selected_recipe:
        print_shopping_list(selected_recipe, meal_choice)
    else:
        print('Recipe not found') 


ingredient_prices = {
    'Broccoli': 0.5,
    'Onions': 0.4,
    'Lemons': 0.9,
    'Spring onions': 0.3,
    'Bread': 3,
    'Cheddar cheese': 3,
    'Veg stock cube': 0.5,
    'Parsley': 2.9,
    'Mix seeds': 3.5,
    'Apples': 0.2,
    'Sugar': 1.5,
    'Lemon': 0.7,
    'Vegan butter': 3.9,
    'Plain flour': 1.5,
    'Almonds': 3,
    'Cinnamon': 1.4,
    'Mushrooms': 0.1,
    'Baby spinach': 2.5,
    'Garlic': 0.5,
    'Potatoes': 0.2,
    'Eggs': 0.3,
    'Cornichons': 0.2,
    'Goat cheese': 4,
    'Salmon fillet': 8,
    'Lemongrass': 0.5,
    'Ginger': 0.8,
    'Soy sauce': 3,
    'Chilli': 0.4,
    'Lime': 0.6,
    'Spaghetti': 1.8,
    'Red onions': 0.5,
    'Carrots': 0.1,
    'Celery' : 1,
    'Rosemary': 0.2,
    'Bacon': 2.9,
    'Chicken legs': 1.8,
    'Sweet potato': 3,
    'Paprika': 2,
    'Black beans': 1.8,
    'Coriander': 2,
    'Beef minced': 3.9,
    'Cherry tomatoes': 0.3,
    'Honey': 2.5,
    'Oregano': 1.8
}


def print_shopping_list(recipe, meal_name):
    '''
    Prints the shopping list of needed ingredients for the chosen meal.
    Args: recipe(dict): Dictionary containing ingredients and amounts.
        meal_name(str): Name of the meal.
    '''
    print(f'\nShopping list for your {meal_name}: ')
    total_cost = 0
    for i in range(len(recipe['ingredients'])):
        ingredient = recipe['ingredients'][i]
        amount = recipe['amount'][i]
        price_per_unit = ingredient_prices.get(ingredient, 0)
        
        if price_per_unit == 0:
            print('Warning: Price for {ingredient} not found.')
        cost = amount * price_per_unit
        total_cost += cost
        print(f'{ingredient}: {amount} piece(s) for €{price_per_unit} per piece.')

    print(f'\nFor your meal * {meal_name} * you will spend {total_cost:.2f} Euro in your market.') 

def create_recipe(ingredients, amounts):
    '''
    Function that combines ingredients and amounts to create a recipe.
    * note: All recipes are taken from the official website of Jamie Oliver https://www.jamieoliver.com/
    Returns: parameter ingredients and amounts, that are keys in dictionary
        and are being used by the other function - print_shopping_list.
        Price - extracted from the variable ingredient_prices original list.
    '''
    return {
        'ingredients': ingredients,
        'amount' : amounts,
        'price' : [ingredient_prices[ingredient] for ingredient in ingredients]
    }    

  

chicken_chips = {'ingredients' : ['Potatoes', 'Onions', 'Oregano', 'Lemons', 'Chicken legs'],
                        'amount' : [10, 3, 1, 3, 4]}


chilli_con_carne = {'ingredients' : ['Sweet potato', 'Paprika', 'Black beans', 'Chilli', 'Coriander', 'Beef minced','Lime','Cherry tomatoes'],
                        'amount' : [1, 1, 1, 1, 1, 1, 0.5, 8]}


broccoli_soup = {'ingredients' : ['Broccoli', 'Spring onions', 'Bread', 'Cheddar cheese', 'Veg stock cube', 'Parsley', 'Mix seeds'],
                        'amount' : [1, 4, 1, 1, 1, 1, 1]}


vegan_apple_crumble = {'ingredients' : ['Apples', 'Sugar', 'Lemon', 'Vegan butter', 'Plain flour', 'Almonds', 'Cinnamon'],
                        'amount' : [7, 1, 1, 1, 1, 1, 1]}


garlic_mushroom_pie = {'ingredients' : ['Mushrooms', 'Baby spinach', 'Garlic', 'Potatoes', 'Eggs', 'Cornichons', 'Goat cheese'],
                        'amount' : [12, 1, 1, 10, 4, 8, 1 ]}

spaghetti_bolognese = {'ingredients' : ['Spaghetti', 'Red onions', 'Garlic', 'Carrots', 'Celery', 'Rosemary', 'Bacon'],
                        'amount' : [1, 3, 3, 3, 3, 2, 1 ]}

grilled_salmon = {'ingredients' : ['Salmon fillet', 'Lemongrass', 'Ginger', 'Garlic', 'Soy sauce', 'Honey', 'Chilli', 'Spring onions', 'Lime'],
                        'amount' : [1, 1, 1, 1, 1, 1, 1, 2, 2]}

main()


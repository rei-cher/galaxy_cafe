"""
Helpers modulo

Helper functions
"""
import game_state

def calculate_rep_species(dish, ingredients, game):
    """
    Calcualtes reputation based on the species criteria
    """
    customer = game.get_current_customer()
    
    for ingredient in ingredients.keys():
        if ingredient in customer.get_species().get_preferences():
            game.add_reputation(1)
        elif ingredient in customer.get_species().get_restrictions():
            game.add_reputation(-2)
        elif ingredient in customer.get_species().get_dislikes():
            game.add_reputation(-1)

def calculate_rep_personality(dish, ingredients, game):
    customer = game.get_current_customer()
    personality = customer.get_personality()

    match personality:
        case "Picky":
            if all(ingredient in ingredients.keys() for item in dish.get_menu_ingredients()):
                game.add_reputation(2)
            
            for item in dish.get_menu_ingredients():
                if ingredients[item] == "Rare" or ingredients[item] == "Legendary":
                    game.add_reputation(-1)

        case "Adventurous":
            for item in dish.get_menu_ingredients():
                if ingredients[item] == "Rare" or ingredients[item] == "Legendary":
                    game.add_reputation(1)

            if all(ingredients.get(item) == "Common" or ingredients.get(item) == "Uncommon" for item in dish.get_menu_ingredients()):
                game.add_reputation(-2)

def calculate_rep_budget(dish, game):
    customer = game.get_current_customer()

    ratio = dish.get_menu_price() / customer.get_credit()

    if ratio <= 0.5:
        game.add_reputation(2)
    elif ratio < 1:
        game.add_reputation(1)
    elif ratio == 1:
        game.add_reputation(0)
    elif ratio < 1.5:
        game.add_reputation(-1)
    else:
        game.add_reputation(-2)

def calculate_profit(dish, ingredients, game):
    calculate_rep_species(dish, ingredients, game)

    game.set_reputation(0)
    calculate_rep_personality(dish, ingredients, game)
    calculate_rep_budget(dish, game)

    rep = game.get_reputation()

    if rep > 0:
        game.add_profit(dish.get_menu_price())
    elif rep == 0:
        game.add_profit(dish.get_menu_price() * 0.5)
    else:
        game.add_profit(0)
    
    game.set_state("CAFE")


def serve_dish(dish, ingredients, game):
    customer = game.get_current_customer()

    customer.set_credit(customer.get_credit() - dish.get_menu_price())
    
    calculate_profit(dish, ingredients, game)

def alien_dossier(customer) -> str:
    species = customer.get_species()

    print(f"Dietary restriction: {", ".join(species.get_restrictions()) or "None"}")
    print(f"Preferred ingredients: {", ".join(species.get_preferences()) or "None"}")
    print(f"Dietary restriction: {", ".join(species.get_dislikes()) or "None"}")

    print("\n(6) Back")
    print("(9) Exit")

    nav = "DETAILS"

    choice = input("> ")

    match choice:
        case "6":
            nav = "CAFE"
        case "9":
            nav = "EXIT"

    return nav

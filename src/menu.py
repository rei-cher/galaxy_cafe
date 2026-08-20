"""
Menu modulo

Declares the menu item class
Loads and format data from given json file
"""
import json

from decor import path_exists
from helpers import serve_dish
from terminal import clear_screen, display_customer

class Menu_Item:
    """
    Menu Item class 

    Requires:
        name: str
        ingredients: list[str]
        price: int
    """
    def __init__(self, name: str, ingredients: list[str], price: int):
        """
        Object initializator

        Populates properties from provided arguments
        """
        self._menu_name = name
        self._ingredients = ingredients
        self._price = price

    def get_menu_name(self) -> str:
        """
        Returns menu item name
        """
        return self._menu_name

    def get_menu_ingredients(self) -> list[str]:
        """
        Returns list of the ingredients for the specific dish
        """
        return self._ingredients

    def get_menu_price(self) -> int:
        """
        Returns the price of the dish
        """
        return self._price

@path_exists
def load_ingredients(filename: str) -> dict:
    """
    Reads provided json file and returns dictionary for ingredients only
    """
    with open(filename, "r") as file:
        data = json.load(file)

    return data["ingredients"]

def show_ingredients(ingredients: dict) -> str:
    """
    Prints out menu for ingredients
    First will be ingredients printed out with the following format:
        Ingredient name -> ingredient rarity

    Then, the additional menu items are printed: 'Back' and 'Exit' options

    Return: string for the corresponding action for the main menu loop state
    """
    for ingredient, rarity in ingredients.items():
        print(f"{ingredient} -> {rarity}")

    print("\n(6) Back")
    print("(9) Exit")

    nav = "INGREDIENTS"

    choice = input("> ")

    match choice:
        case "6":
            nav = "CAFE"
        case "9":
            nav = "EXIT"

    return nav

@path_exists
def load_menu(filename: str) -> dict[str, Menu_Item]:
    """
    Reads provided json file and returs dictionary of dish name
    and menu item object for that dish
    """
    with open(filename, "r") as file:
        data = json.load(file)

    menu_items = {}

    for record in data["menu"]:
        new_menu_item = Menu_Item(
                record["name"],
                record["ingredients"],
                record["price"]
                )

        menu_items[record["name"]] = new_menu_item

    return menu_items

def menu_list(menu_items) -> str:
    """
    Prints out menu for dishes
    First will be dishes printed out with the following format:
        Dish name
            Ingredients
            Price

    Then, the additional menu items are printed: 'Back' and 'Exit' options

    Return: string for the corresponding action for the main menu loop state
    """
    for menu_item in menu_items.values():
        print(f"{menu_item.get_menu_name()}\n"
              f"\tIngredients: {', '.join(menu_item.get_menu_ingredients())}\n"
              f"\tPrice: {menu_item.get_menu_price():.2f}\n")

    print("(6) Back")
    print("(9) Exit")

    nav = "MENU"
    
    choice = input("> ")
    match choice:
        case "6":
            nav = "CAFE"
        case "9":
            nav = "EXIT"

    return nav

def show_dish(menu_items, ingredients, game) -> str:
    """
    Prints out menu with dishes that can be surved to the customer

    Based on the user's input, the dish can be:
        served
        go to the next dish

    Additionally, user can either for back or exit by corresponding
    menu options

    If menu has to be server, the serve_dish function is called

    Return: string for the corresponding action for the main menu loop state
    """
    menu_items = list(menu_items.values())
    item = 0

    nav = "SERVE"

    while True:
        clear_screen()
        
        customer = game.get_current_customer()

        display_customer(customer, game)

        print("++++++++++")
        print("|  DISH  |")
        print("++++++++++")
        print(f"{menu_items[item].get_menu_name()}\n"
               f"\tIngredients: {', '.join(menu_items[item].get_menu_ingredients())}\n"
              f"\tPrice: {menu_items[item].get_menu_price():.2f}\n")
        print("\n\n(1) Serve")
        print("(2) Next Dish")
        print("(6) Back")
        print("(9) Exit")

        choice  = input("> ")
        
        match choice:
            case "1":
                serve_dish(menu_items[item], ingredients, game)
                game.add_overall_rep(game.get_reputation())
                game.next_customer()
                nav = "CAFE"
                break
            case "2":
                item = (item + 1) % len(menu_items)
            case "6":
                nav = "CAFE"
                break
            case "9":
                nav = "EXIT"
                break

    return nav

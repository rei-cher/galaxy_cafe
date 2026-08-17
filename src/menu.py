import json

from helpers import serve_dish
from terminal import clear_screen, display_customer

class Menu_Item:
    def __init__(self, name: str, ingredients: list[str], price: int):
        self._menu_name = name
        self._ingredients = ingredients
        self._price = price

    def get_menu_name(self) -> str:
        return self._menu_name

    def get_menu_ingredients(self) -> list[str]:
        return self._ingredients

    def get_menu_price(self) -> int:
        return self._price

def load_ingredients(filename: str) -> dict:
    with open(filename, "r") as file:
        data = json.load(file)

    return data["ingredients"]

def show_ingredients(ingredients: dict):
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

def load_menu(filename: str) -> dict[str, Menu_Item]:
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
    for menu_item in menu_items.values():
        print(f"{menu_item.get_menu_name()}\n"
              f"\tIngredients: {', '.join(menu_item.get_menu_ingredients())}\n"
              f"\tPrice: {menu_item.get_menu_price()}\n")

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

def show_dish(menu_items, customer) -> str:
    menu_items = list(menu_items.values())
    item = 0
    nav = "SERVE"

    while True:
        clear_screen()
        display_customer(customer)

        print("++++++++++")
        print("|  DISH  |")
        print("++++++++++")
        print(f"{menu_items[item].get_menu_name()}\n"
               f"\tIngredients: {', '.join(menu_items[item].get_menu_ingredients())}\n"
               f"\tPrice: {menu_items[item].get_menu_price()}\n")
        print("\n\n(1) Serve")
        print("(2) Next Dish")
        print("(6) Back")
        print("(9) Exit")

        choice  = input("> ")
        
        match choice:
            case "1":
                serve_dish(menu_items[item], customer)
                nav = "SERVED"
                break
            case "2":
                if item == len(menu_items)-1:
                    item = 0
                else :
                    item+=1
            case "6":
                nav = "CAFE"
                break
            case "9":
                nav = "EXIT"
                break

    return nav

        

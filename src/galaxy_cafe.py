import sys

from game_state import GameState
from screen import show_menu
from species import load_species
from customer import load_customers
from menu import load_ingredients, load_menu

def main():
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <species.json> <customers.json> <menu.json>"
              )
        sys.exit(1)

    species = load_species(sys.argv[1])
    customers = load_customers(sys.argv[2], species)
    ingredients = load_ingredients(sys.argv[3])
    menu_items = load_menu(sys.argv[3])

    game_state = GameState(customers)

    show_menu(game_state, ingredients, menu_items)

if __name__ == "__main__":
    main()

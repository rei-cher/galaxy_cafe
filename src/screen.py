import os
import sys

from menu import menu_list, show_dish, show_ingredients
from terminal import clear_screen, display_customer
from helpers import alien_dossier

def display_start_menu():
    clear_screen()
    print("(1) Open Cafe")
    print("(9) Exit")

    nav = "MAIN_MENU"
    choice = input("> ")

    if choice == "1":
        nav = "CAFE"

    if choice == "9":
        nav = "EXIT"

    return nav

def display_commands():
    print("(1) Menu")
    print("(2) Ingredients")
    print("(3) Species Details")
    print("(4) Serve")
    print("(5) Next Customer")
    print("(6) Progress")
    print("(9) Exit")

    nav = "CAFE"
    choice = input("> ")

    match choice:
        case "1":
            nav = "MENU"
        case "2":
            nav = "INGREDIENTS"
        case "3":
            nav = "DETAILS"
        case "4":
            nav = "SERVE"
        case "5":
            nav = "NEXT"
        case "6":
            nav = "PROGRESS"
        case "9":
            nav = "EXIT"

    return nav

def show_menu(game, ingredients, menu_items):
    while game.get_state() != "EXIT":
        customer = game.get_current_customer()
        match game.get_state():
            case "MAIN_MENU":
                game.set_state(display_start_menu())

            case "CAFE":
                clear_screen()
                display_customer(customer, game)
                game.set_state(display_commands())

            case "MENU":
                clear_screen()
                display_customer(customer, game)
                game.set_state(menu_list(menu_items))

            case "INGREDIENTS":
                clear_screen()
                display_customer(customer, game)
                game.set_state(show_ingredients(ingredients))

            case "DETAILS":
                clear_screen()
                display_customer(customer, game)
                game.set_state(alien_dossier(customer))

            case "SERVE":
                game.set_state(show_dish(menu_items, ingredients, game))

            case "NEXT":
                game.next_customer()
                game.set_state("CAFE")



    os.system("cls" if os.name == "nt" else "clear")
    sys.exit(1)

import os
import sys

from menu import menu_list

def display_banner():
    print("++++++++++++++++++")
    print("   Galaxt Cafe")
    print("++++++++++++++++++")

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    display_banner()

def display_start_menu():
    clear_screen()
    print("(1) Open Cafe")
    print("(9) Close")

    nav = "MAIN_MENU"
    choice = input("> ")

    if choice == "1":
        nav = "CAFE"

    if choice == "9":
        nav = "EXIT"

    return nav

def display_customer(customer):
    print()
    print(f"Customer: {customer.get_customer_name()} "
          f"({customer.get_species().get_species_name()}) "
          f"{customer.get_personality()} "
          f"Credits: {customer.get_credit()}"
          )
    print()

def display_commands():
    print("(1) Menu")
    print("(2) Ingredients")
    print("(3) Alien Dossier")
    print("(4) Serve")
    print("(5) Progress")
    print("(9) Exit")

    nav = "CAFE"
    choice = input("> ")

    match choice:
        case "1":
            nav = "MENU"
        case "2":
            nav = "INGREDIENTS"
        case "3":
            nav = "DOSSIER"
        case "4":
            nav = "SERVE"
        case "5":
            nav = "PROGRESS"
        case "9":
            nav = "EXIT"

    return nav

def show_menu(customers, ingredients, menu_items):
    state = "MAIN_MENU"
    customer = 0

    while state != "EXIT":
        

        if state == "MAIN_MENU":
            state = display_start_menu()

        if state == "CAFE":
            clear_screen()
            display_customer(customers[customer])
            state = display_commands()

        if state == "MENU":
            clear_screen()
            display_customer(customers[customer])
            state = menu_list(menu_items)


        if state == "SERVE":
            customer+=1
            state = "CAFE"

    os.system("cls" if os.name == "nt" else "clear")
    sys.exit(1)

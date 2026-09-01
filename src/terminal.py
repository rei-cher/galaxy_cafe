"""
Terminal modulo

Menu screen behaviors
"""
import os

def display_banner():
    """
    Prints Galaxy cafe banner
    """
    print("++++++++++++++++++")
    print("   Galaxy Cafe")
    print("++++++++++++++++++")

def clear_screen():
    """
    Clears the screen
    """
    os.system("cls" if os.name == "nt" else "clear")
    display_banner()

def display_customer(customer, game):
    """
    Prints out current customer information like name, species, etc
    """
    print()
    print(f"Customer: {customer.get_customer_name()} "
          f"({customer.get_species().get_species_name()}) "
          f"{customer.get_personality()} "
          f"Credits: {customer.get_credit():.2f}\n"
          f"Reputation for previous choice: {game.get_reputation()}\n"
          f"\t\tOverall Reputation: {game.get_overall_rep()}\n"
          f"\t\tTotal Profit: {game.get_profit_credits():.2f}"
          f"\nCustomer # {game.get_tracker()}"
          )
    print()

def game_over(game):
    """
    Prints game over screen with stats
    """
    nav = "EXIT"
    clear_screen()
    ent = None
    print(f"GAME OVER\n"
          f"Overall reputation: {game.get_overall_rep()}\n"
          f"Total profit: {game.get_profit_credits()}\n"
          )

    ent = input("Press enter to exit")
    if ent:
        nav = "EXIT"
    return nav
    

def display_progress(game):
    clear_screen()
    
    nav = "PROGRESS"

    print(f"Current profit: {game.get_profit_credits()}\n"
          f"Overall cafe reputation: {game.get_overall_rep()}\n"
          f"Reputation earned for the last serving: {game.get_reputation()}\n"
          f"Total number of customers in line: {game.get_customers_len()}\n"
          f"Customers serverd: {game.get_tracker()}\n"
          )

    print("\n\n(6) Back\n(9) Exit")

    choice = input("> ")

    match choice:
        case "6":
            nav = "CAFE"
        case "9":
            nav = "EXIT"

    return nav

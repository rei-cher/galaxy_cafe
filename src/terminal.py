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
          )
    print()

def game_over(game):
    """
    Prints game over screen with stats
    """
    clear_screen()
    print(f"GAME OVER\n"
          f"Overall reputation: {game.get_overall_rep()}\n"
          f"Total profit: {game.get_profit_credits()}"
          f"\nState: {game.get_state()}"
          )

    if input("Press enter to exit"):
        return "EXIT"


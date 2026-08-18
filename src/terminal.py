import os

def display_banner():
    print("++++++++++++++++++")
    print("   Galaxt Cafe")
    print("++++++++++++++++++")

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    display_banner()

def display_customer(customer, game):
    print()
    print(f"Customer: {customer.get_customer_name()} "
          f"({customer.get_species().get_species_name()}) "
          f"{customer.get_personality()} "
          f"Credits: {customer.get_credit()}\n"
          f"\t\tReputation: {game.get_reputation()}\n"
          f"\t\tTotal Profit: {game.get_profit_credits()}"
          )
    print()


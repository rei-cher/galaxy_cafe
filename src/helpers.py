def serve_dish(dish, customer):
    customer.set_credit(customer.get_credit() - dish.get_menu_price())

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

import json

from decor import path_exists
from species import Species

class Customer(Species):
    def __init__(self, name: str, species: str, personality: str, credit: int):
        super().__init__(
                species.get_species_name(),
                species.get_restrictions(),
                species.get_preferences(),
                species.get_dislikes()
                )
        self._customer_name = name
        self._species = species
        self._personality = personality
        self._credit = credit


    def get_customer_name(self) -> str:
        return self._customer_name

    def get_species(self) -> Species:
        return self._species

    def get_personality(self) -> str:
        return self._personality

    def get_credit(self) -> str:
        return self._credit

    def set_credit(self, credit: int):
        self._credit = credit

@path_exists
def load_customers(filename: str, species: dict[str, Species]) -> list[Customer]:
    with open(filename, "r") as file:
        data = json.load(file)

    customers = []

    for record in data["customers"]:
        species_name = record["species"]

        customer = Customer(
                record["name"],
                species[species_name],
                record["personality"],
                record["credits"]
                )
        
        customers.append(customer)

    return customers

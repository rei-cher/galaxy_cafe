import sys

from species import load_species
from customer import load_customers

def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <species.json> <customers.json>"
              )
        sys.exit(1)

    species = load_species(sys.argv[1])
    customers = load_customers(sys.argv[2], species)

    for customer in customers:
        print(f"Customer: {customer.get_customer_name()}")
        print(f"Species: {customer.get_species().get_species_name()}")
        print(f"Restrictions: {customer.get_species().get_restrictions()}")
        print(f"Personality: {customer.get_personality()}")
        print(f"Credits: {customer.get_credit()}")
        print()

if __name__ == "__main__":
    main()

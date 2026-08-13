import json

class Species:
    def __init__(self, name: str, restrictions: list[str], preferences: list[str], dislikes: list[str]):
        self._species_name = name
        self._restrictions = restrictions
        self._preferences = preferences
        self._dislikes = dislikes

    def get_species_name(self) -> str:
        return self._species_name

    def get_restrictions(self) -> list[str]:
        return self._restrictions

    def get_preferences(self) -> list[str]:
        return self._preferences

    def get_dislikes(self) -> list[str]:
        return self._dislikes

def load_species(filename: str) -> dict[str, Species]:
    with open(filename, "r") as file:
        data = json.load(file)

    species = {}

    for record in data["species"]:
        new_species = Species(
                record["name"],
                record["dietary_restrictions"],
                record["preferred_ingredients"],
                record["least_preferred_ingredients"]
                )

        species[record["name"]] = new_species

    return species

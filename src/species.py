"""
Species modulo

Declares the species class
Loads and format data from given json file
"""
import json

from decor import path_exists

class Species:
    """
    Species class

    Requires:
        name: str
        restrictions: list[str]
        preferences: list[str]
        dislikes: list[str]
    """
    def __init__(self, name: str, restrictions: list[str], preferences: list[str], dislikes: list[str]):
        """
        Object initializator

        Populates properties from provided arguments
        """
        self._species_name = name
        self._restrictions = restrictions
        self._preferences = preferences
        self._dislikes = dislikes

    def get_species_name(self) -> str:
        """
        Returns name of the species
        """
        return self._species_name

    def get_restrictions(self) -> list[str]:
        """
        Returns dietary restrictions of the species
        """
        return self._restrictions

    def get_preferences(self) -> list[str]:
        """
        Returns preferred ingredients of the species
        """
        return self._preferences

    def get_dislikes(self) -> list[str]:
        """
        Returns least preferred ingredients of the species
        """
        return self._dislikes

@path_exists
def load_species(filename: str) -> dict[str, Species]:
    """
    Reads provided json files and returns dictionary with information
    for each species
    """
    with open(filename, "r") as file:
        data = json.load(file)

    species = {}

    for record in data["species"]:
        new_species = Species(
                record["name"],
                [] if record["dietary_restrictions"] == "None" else record["dietary_restrictions"],
                [] if record["preferred_ingredients"] == "None" else record["preferred_ingredients"],
                [] if record["least_preferred_ingredients"] == "None" else record["least_preferred_ingredients"]
                )

        species[record["name"]] = new_species

    return species

# The Galactic Cafe

## Introduction

In the bustling heart of the Andromeda Sector lies Nexus Station, a colossal spaceport teeming with life from countless galaxies. Here, amidst the clang of landing gears and the cacophony of alien languages, sits your haven – the "Galactic Cafe." It's not your average space diner. Sure, you serve up steaming mugs of nebula brew and energizing space-slug burgers, but the "Galactic Cafe" is more than just fuel for weary travelers. It's a crossroads, a melting pot where space explorers, eccentric scientists, and even the occasional intergalactic bounty hunter find a moment of respite and a taste of home (or at least something close enough).

You, a seasoned chef with a knack for understanding the most peculiar palates, have inherited this interstellar eatery from your adventurous Aunt Pypi. Now, it's your turn to navigate the vibrant chaos of the station, decipher the cryptic cravings of your alien clientele, and keep the "Galactic Cafe" a beacon of deliciousness in the vast expanse of space. But beware, not every customer is easy to please. There are rumors of a particularly picky space pirate with a fiery temper and a penchant for ultra-rare meteor steaks. Can you whip up a dish that satisfies even the most outlandish tastes and maintain the legendary reputation of the "Galactic Cafe"?

**Note:** This practical project is intended for OOP practice in Python. 

**Relevant JQR Items:**

- 7.1: (U) Describe purpose and use of foundational Python mechanics
- 7.2: (U) Demonstrate the proper declaration and use of Python data types and object-oriented constructs
- 7.3: (U) Demonstrate the ability to perform basic arithmetic operations using Python operators while ensuring proper order of operations (PEMDAS)
- 7.4: (U) Demonstrate the ability to perform file management operations in Python
- 7.5: (U) Demonstrate the ability to create and implement functions to meet a requirement
- 7.6: (U) Demonstrate the ability to perform data validation
- 7.7: (U) Demonstrate skill in creating and implementing conditional statements, expressions, and constructs
- 7.8: (U) Describe the terms and fundamentals associated with object oriented programming using Python
- 7.9: (U) Demonstrate the ability to parse command line arguments using built-in functionality.

## Requirements

This project aims to build a text-based simulation of an intergalactic cafe where patrons from various alien species are served menu items picked by the user. Score will be kept to keep track of how well the user can choose items for each customer.

### Main Application:
Implement a text-based UI for user interaction. The UI may, at your discretion, use a command approach, or a nested menu structure. Nested menu implementations should be easy to navigate, and have the ability to return to higher levels of the nested structure.

Using the list of menu items, ingredients, and their properties provided in the ```menu.json``` file, create a ```cosmic_cup.py``` file that functions as follows:

- On startup, the program should create a queue of customers from one of the customer list JSON files [customers_small.json](assets/customers/customers_small.json), [customers_medium.json](assets/customers/customers_medium.json), [customers_large.json](assets/customers/customers_large.json). Each customer is of a certain species and should inherit their respective species attributes along with their own individual attributes. 


- **Species:**
    - A set of alien species with unique characteristics including:
        - Species name
        - Dietary Restrictions
        - Preferred ingredients
        - Least preferred ingredients

- **Customers:**
    - Use one of the customer JSON files provided. Each customer will be of a certain species and inherit that species respective traits in addition to having their own particular attributes. 
        - Customer name
        - Species
        - Personality (ie. picky, neutral, or adventurous)
        - Credits
    
- **Food:**
    - A menu of intergalactic eats with various properties such as:
        - Name 
        - Ingredients
        - Price
        - Rarity (ie. common, uncommon, rare, legendary)


    For example, one customer looks something like this:
    ```
    Name: Glitch Fixer
    Species: Debugian
    Personality: Picky
    Credits: 120
    ```
    
- The food menu data should be parsed and stored as you see fit to interact with all relevant data throughout the runtime of the program
- The user should be presented with customer details of the next customer in line and should then be prompted to choose an item from the menu to serve that customer.
- Feedback will be provided on the user's choice and they will be scored on the [scale](#rating-criteria) defined below.
- After all customers have been served, the user will be presented with their overall rating and profit earned for that day. 


The food menu, species, and customer list JSON files for the ```cosmic_cup.py``` must be passed as a positional arguments with running ```cosmic_cup.py```  
- IE:  ```./cosmic_cup.py menu.json species.json customers_small.py```

The customer, menu, and cafe storefront functionality, should be implemented using an object-oriented approach.

Whenever displayed to the terminal, all component values should display their respective measurement units.  IE:  ```Price 200``` should be ```200.00 credits``` as a 2 decimal float value


### Scoring Criteria
To assess the user's choice of menu item for the customer in a quantitative way, the following scoring criteria should be implemented:

**Assign points based on how well the chosen menu item aligns with the customer's species, restrictions, and preferences from the Species class.**

| Points | Condition |
| --------| -------|
| +1 | for each preferred ingredient present in the dish |
| -2 | for each dietary restriction violated by the dish. |
| -1 | for each least preferred ingredient in the dish |


**Assign points based on the personality of the individual customer. Depending on which personality type the customer is assigned, use these point modifiers based on what dish the user chooses to serve**

| Customer Personality Type | Points | Condition |
| --------| -------| ----- |
| Picky | +2 | if a served dish contains every one of their preferred ingredients |
| Picky | -1 | for each rare or legendary ingredient in the dish served |
| Adventurous | +1 | for each rare or legendary ingredient in the dish served |
| Adventurous | -2 | for a serving a dish that contains only common or uncommon ingredients |
| Neutral | 0 | no point modifiers for customers with this personality type |

**Assign points based on the price of the dish served vs. the customer's budget.**

| Points | Condition |
| --------| -------|
| +2 | if the price of the dish served is less than or equal to 0.5x of the customer's available credits (ie. customer credits = 10, price = 4) |
| +1 | if the price of the dish served is greater than 0.5x and less than 1x of the customer's available credits (ie. customer credits = 10, price = 7) |
| 0 | if the price of the dish served is equal to the customer's available credits (ie. customer credits = 10, price = 10) |
| -1 | if the price of the dish served is greater than 1x and less than 1.5x of the customer's available credits (ie. customer credits = 10, price = 12) |
| -2 | if the price of the dish served is greater than or equal to 1.5x the customer's available credits (ie. customer credits = 10, price = 15) |

**Assess profit earned based on the price of the item and a customer's review**

| Profit | Condition |
|-----|-----|
| +price of dish | Customer's review is > 0 |
| +0.5x price of dish | Customer's review = 0 |
| +0 credits | Customer's review is < 0 |

### Example:

**Customer: Zorp the Magnificent (Zolarian, Picky, 100 Credits)**

Dish: Nebula Burger [Space-Slug (rare), Spiced Greens (common), Nebula Sauce (common)]

**Scoring:**

- Dietary (+3): Zolarians can eat everything.
- Preferred (+0): Zolarians have no preference listed.
- Least Preferred (-0): Not implemented in this example.
- Picky (-1): Nebula Burger has Space-Slug which is a rare ingredient.
- Budget (+2): Nebula Burger costs 20 Credits, well within Zorp's budget (price <= 0.5x Zorp's 100 credits).

**Final Score: +4 reputation, +20 credits** (This indicates a decent choice for Zorp, mostly catering to his pickiness and budgetary constraints.)

---

**Customer: Trace the Space-Bug Hunter (Debugian, Adventurous, 20 credits)**

Dish: Nebula Noodle Soup [Space-Weed (uncommon), Bland Broth (common), Nebula Noodles (common)]

**Scoring:**

- Dietary (-2): Space-Weed is a restricted ingredient for Debugians, violating their dietary restrictions.
- Preferred (+0): This dish does not contain any ingredients preferred by Debugians.
- Least Preferred (-1): Bland Broth is notoriously disliked by Debugians.
- Adventurous (-2): Nebula Noodle Soup contains no rare or legendary ingredients, making it unappealing to an adventurous palette.
- Budget (-1): Nebula Noodle Soup costs 25 Credits, slightly outside of Trace's budget (price <= 1.5x Trace's 20 credits).

**Final Score: -6 reputation, +0 credits** (This indicates a very poor choice for Trace by not considering the dietary restrictions, and preferences of his species, along with Trace's individual personality and budget.)

---

**Customer: Logicus the Binary Wanderer  (Booleanite, Picky, 10 credits)**

Dish: Cosmic Comet Casserole [Stardust Spice (rare), Comet Chunks (uncommon), Galactic Greens (common)]

**Scoring:**

- Dietary (+3): Booleanites have no dietary restrictions against any of the ingredients in this dish
- Preferred (+0): This dish does not contain any ingredients preferred by Booleanites.
- Least Preferred (-0): This dish does not contain any ingredients least preffered by Booleanites.
- Picky (-1): Stardust Spice is a rare ingredient, making it far too adventourous for a picky palette.
- Budget (-2): Cosmic Comet Casserole costs 30 Credits, well above Logicus's budget (price >= 1.5x Logicus's 10 credits).

**Final Score: +0 reputation, +15 credits** (This indicates a neutral for Logicus by heavily considering the dietary restrictions of his species, but failing to account for Logicus's individual personality and budget along with the preferences of his species.)

---

**At the end of all customer interactions, the program should display a final reputation rating, total customer's served, and profit earned for that iteration before exiting the program.** 

## Deliverables

The specific deliverables and point breakdown are available in the project rubric.  For your reference, here is an example checklist of features to design unit tests for, assuming a command based approach

| Area                 | Requirement                                                                                       |
|----------------------|--------------------------------------------------------------------------------------------------|
| Application                 | ```galactic_cafe.py``` successfully parses JSON data appropriately on startup                            |
| Menu Display    | Implementation of `list` command to view available menu items                                          |
| Ingredient Details         | Implementation of `ingredients` command to view all available ingredients and their rarity                                 |
| Species Details | Implementation of `alien_dossier` command to view details about a specific species                              |
| Serving Customers     | Implementation of `serve` command to complete the purchase and serve the current customer the dish of your choosing                        |
| Measurement Units | All component values should display their respective measurement units as defined in the project requirements |
| Show Progress | Implementation of `progress` command to show current ratings and profit earned | 
| Object-Oriented      | Use of object-oriented programming to implement the cafe and its various components (ie. species, menu items, etc.)  |
| Modular | Code is appropriately broken down into separate files/modules based on function |
| Graceful Shutdown | The program must be able to gracefully handle and exit on receiving SIGINT |

### Example List of Commands

**Note:  While this is only an example of what commands could be implemented from the menu, the specification and rubric require that the functionality of all these commands be incorporated into the project somehow.**


| Command       | Arguments               | Output                                             |
|---------------|-------------------------|----------------------------------------------------|
| `help` | none | Lists all available commands and their function |
| `list`          | none     | List all available menu items   |
| `ingredients`      | none                 | List all available ingredients present on the menu |
| `alien_dossier` | species (optional) | Display detail about a particular species. If none is specified, display all species and their details       |
| `serve`         | menu_item | Serve the specified menu item to the current customer     |
| `progress`       | none | Show current reputation rating and profit earned |

## Sources

- A list of menu items and ingredients with the corresponding properties can be found in [menu.json](assets/menu.json)

- A list of alien species and their properties can be found in [species.json](assets/species.json)

- Customer lists of various sizes can also be found at [customers_small.json](assets/customers/customers_small.json), [customers_medium.json](assets/customers/customers_medium.json), [customers_large.json](assets/customers/customers_large.json)

- The scoring rubric used to assess performance on this project can be found in [rubric.md](assets/rubric.md)


## Hints

- Instructors may use different menu, customer, and ingredient files for testing. Do **NOT** hardcode in values for any of the data in the JSON files, as they may change. 
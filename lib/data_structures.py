# lib/data_structures.py

spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(foods):
    """Return a list of names from the list of spicy foods."""
    return [food["name"] for food in foods]


def get_spiciest_foods(foods):
    """Return foods with heat_level greater than 5."""
    return [food for food in foods if food["heat_level"] > 5]


def print_spicy_foods(foods):
    """Print each food in format: Name (Cuisine) | Heat Level: 🌶 * heat_level"""
    for food in foods:
        peppers = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {peppers}")


def get_spicy_food_by_cuisine(foods, cuisine):
    """Return the first food that matches given cuisine."""
    for food in foods:
        if food["cuisine"] == cuisine:
            return food


def print_spiciest_foods(foods):
    """Print only the foods with heat_level greater than 5."""
    spiciest = get_spiciest_foods(foods)
    print_spicy_foods(spiciest)


def get_average_heat_level(foods):
    """Return the average heat level of all foods as an integer."""
    total = sum(food["heat_level"] for food in foods)
    return total // len(foods)  # integer division


def create_spicy_food(foods, new_food):
    """Return foods list with new food added."""
    foods.append(new_food)
    return foods

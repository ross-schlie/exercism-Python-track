"""exercism cater waiter (sets) module."""

from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)
#OMNIVORE

def clean_ingredients(dish_name, dish_ingredients):
    """
    Get a 'clean' set of ingredients per dish.

    :param dish_name: str
    :param dish_ingredients: list
    :return: tuple of (dish_name, ingredient set)

    This function should return a `tuple` with the name of the dish as the first item,
    followed by the de-duped `set` of ingredients as the second item.
    """

    return tuple([dish_name, set(dish_ingredients)])


def check_drinks(drink_name, drink_ingredients):
    """
    Check if drinks ingredients contain alcohol or not.

    :param drink_name: str
    :param drink_ingredients: list
    :return: str drink name + ("Mocktail" or "Cocktail")

    The function should return the name of the drink followed by "Mocktail" if the drink has
    no alcoholic ingredients, and drink name followed by "Cocktail" if the drink includes alcohol.
    """

    drink_type = ' Mocktail'
    for ingredient in drink_ingredients:
        if ingredient in ALCOHOLS:
            drink_type = ' Cocktail'
            break

    return drink_name + drink_type


def categorize_dish(dish_name, dish_ingredients):
    """
    Categorize dish based on ingredients.

    :param dish_name: str
    :param dish_ingredients: list
    :return: str "dish name: CATEGORY"

    This function should return a string with the `dish name: <CATEGORY>` (which meal category the dish belongs to).
    All dishes will "fit" into one of the categories imported from `categories.py`
    (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).
    """

    category = 'OMNIVORE'
    if dish_ingredients.issubset(VEGAN):
        category = 'VEGAN'
    elif dish_ingredients.issubset(VEGETARIAN):
        category = 'VEGETARIAN'
    elif dish_ingredients.issubset(PALEO):
        category = 'PALEO'
    elif dish_ingredients.issubset(KETO):
        category = 'KETO'

    return dish_name + ': ' + category


def tag_special_ingredients(dish):
    """
    Label Allergens and Restricted Foods.

    :param dish: tuple of (str of dish name, list of dish ingredients)
    :return: tuple of (str of dish name, set of dish special ingredients)

    Return the dish name followed by the `set` of ingredients that require a special note on the dish description.
    For the purposes of this exercise, all allergens or special ingredients that need to be tracked are in the
    SPECIAL_INGREDIENTS constant imported from `categories.py`.
    """

    ingredients = set(dish[1])
    special = ingredients.intersection(SPECIAL_INGREDIENTS)
    return tuple([dish[0], special])


def compile_ingredients(dishes):
    """
    Compile a "Master List" of Ingredients.

    :param dishes: list of dish ingredient sets
    :return: set

    This function should return a `set` of all ingredients from all listed dishes.
    """

    ingredients = set()
    for dish in dishes:
        ingredients = ingredients.union(dish)

    return ingredients


def separate_appetizers(dishes, appetizers):
    """
    Get list of dishes that are not appetizers.

    :param dishes: list of dish names
    :param appetizers: list of appetizer names
    :return: list of dish names

    The function should return the list of dish names with appetizer names removed.
    Either list could contain duplicates and may require de-duping.
    """

    dishes_set = set(dishes)
    appetizer_set = set(appetizers)
    return list(dishes_set.difference(appetizer_set))


def singleton_ingredients(dishes, intersection):
    """
    Find ingredients used in only one recipe.

    :param dishes:  list of ingredient sets
    :param intersection: constant - one of (VEGAN_INTERSECTION,VEGETARIAN_INTERSECTION,PALEO_INTERSECTION,
                                            KETO_INTERSECTION,OMNIVORE_INTERSECTION)
    :return: set of singleton ingredients

    Each dish is represented by a `set` of its ingredients.
    Each `<CATEGORY>_INTERSECTION` is an `intersection` of all dishes in the category.
    The function should return a `set` of ingredients that only appear in a single dish.
    """

    differences = []
    for dish in dishes:
        differences = dish.symmetric_difference(differences)

    return differences - intersection

from . import light_spellbook


def validate_ingredients(ingredients: str) -> str:
    ing_list: list = light_spellbook.light_spell_allowed_ingredients()
    ingredients_lower = ingredients.lower()
    for ing in ing_list:
        if ing in ingredients_lower:
            return f"{ingredients} - VALID"

    return f"{ingredients} - INVALID"

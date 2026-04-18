import alchemy
import elements


def healing_potion():
    return f"Healing potion brewed with ’{alchemy.create_earth()}’ and ’{alchemy.create_air()}’"


def strength_potion():
    return f"Strength potion brewed with ’{elements.create_fire()}’ and ’{elements.create_water()}’"

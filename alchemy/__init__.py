# . means current directory
# When import a package, python automatically executes `__init__.py`
from .elements import create_air

from .transmutation.recipes import lead_to_gold
from .elements import create_earth
from .potions import healing_potion
from .potions import strength_potion

# __all__ = list defines what is allowed to be imported
# if u don't specify __all__ 👉 It will import all names that don’t start with _


__all__ = [
    "create_air",
    "create_earth",
    "lead_to_gold",
    "healing_potion",
    "strength_potion",
]

# . means current directory
# When import a package, python automatically executes `__init__.py`
from .elements import create_air

from .transmutation.recipes import lead_to_gold

# This is an alias
from .potions import healing_potion as heal
from .potions import strength_potion

# __all__ = list defines what is allowed to be imported
# if u don't specify __all__ 👉 It will import all names that don’t start with _


__all__ = [
    "create_air",
    "lead_to_gold",
    "strength_potion",
    "heal",
]

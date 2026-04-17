# . means current directory
# When import a package, python automatically executes `__init__.py`
from .elements import create_air

# __all__ = list defines what is allowed to be imported
# if u don't specify __all__ 👉 It will import all names that don’t start with _

__all__ = ["create_air"]

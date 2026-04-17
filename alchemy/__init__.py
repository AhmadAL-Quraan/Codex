# . means current directory
# When import a package, python automatically executes `__init__.py`
from .elements import create_air

# __all__ = list defines what is allowed to be imported

__all__ = ["create_air"]

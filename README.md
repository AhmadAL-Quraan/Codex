# Codex project 


*  This project aims to understand how modules and pakages managed and handled in python.

## Concepts

* When you write `import package`, python will search for this package in project root directory.

* Type of import in python:
  
    1) `import package`: This will go directly to `__init__` in this package.
    2) `from package import package/function/class,..`: 

       If name is a module (file) → it imports that module.

       If name is a function/class/variable → it imports that directly.

       If name is a subpackage (folder with __init__.py) → it imports that subpackage
    3) `import package.submodel`: In this case if the submodel exist, it will won't go to `__init__` to search for it.
  

* `__init__.py`: Is the first file python will search for when you import **all** modules from a package.
  
    ```python 
    from package import *
    ```
    There is a variable named `__all__`, which is a list that determines which packages should be imported. If not specified, any package that doesn't start with `_`, will be imported . 

>`__init__.py` is not searched when accessing subbmodels like `from alchemy import elements`, it only will be searched when `import alchemy` issued, and `__all__` will only be used when `from alchemy import *`

* The package could by a **file** like `elements.py` or a **directory** like `alchemy`.

* You can access submodel directly when calling a package.
```python
import alchemy
alchemy.elements.create_earth() # Even thow create_earth is not in __init__
```


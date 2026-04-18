# Codex project 


*  This project aims to understand how modules and pakages managed and handled in python.

## Concepts

* In python `import package` -> This called **absolute path** starts from **root** of the project, while `from . import package` or `from .package import something` -> both of these called **relative imports**.

* Type of import in python:
  
    1) `import package`: if package was a directory, this will go directly to `__init__` in this package.
    2) `from package import package/function/class,..`: 

       If name is a module (file) → it imports that module.

       If name is a function/class/variable → it imports that directly.

       If name is a subpackage (folder with __init__.py) → it imports that subpackage
    3) `import package.submodel`: In this case if the submodel exist, it will won't go to `__init__` to search for it.
  

* `__init__.py`: Is the first file python will search for when you import **all** modules from a package or the package itself.
  
    ```python 
    from package import * #or 
    import package
    ```
    There is a variable named `__all__`, which is a list that determines which packages should be imported when you import all of packages from a package using *, `from package import *`. If not specified, any package that exist inside that package and doesn't start with `_`, will be imported. 

>`__init__.py` is not searched when accessing subbmodels like `from alchemy import elements`, it only will be searched when `import alchemy` issued, and `__all__` will only be used when `from alchemy import *`

* The package could by a **file** like `elements.py` or a **directory** like `alchemy`.

* You can access submodel directly when calling a package.
```python
import alchemy
alchemy.elements.create_earth() # Even thow create_earth is not in __init__
```


* In directory named `alchemy`, if you imported in `__init__` an internal package(in current directory not in root for example) like `from .package import class/function/...` then this will be called an **alias** if u used it in another file from `alchemy` package.

   So in another file if u did:
```python 
import alchemy
alchemy.class # This is called alias to this class imported from previous package
```

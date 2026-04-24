# Codex project 


*  This project aims to understand how modules and pakages managed and handled in python.

## Concepts

* We have two phrases here:
  
  **Module**: A single .py file .
  
  **Package**: A directory which has `__init__` file.

* `import package` -> This called **absolute path** starts from **root** of the project.

* `from . import package` or `from .package import something` -> both of these called **relative imports**.

* Type of import in python:
  
    1) `import package`: if package was a directory, this will go directly to `__init__` in this package.
    2) `from package import subpackage/module/function/class,..`: 

       If name is a module (file) → it imports that module.

       if name is a function/class/variable → it imports that directly.

       if name is a subpackage (folder with __init__.py) → it imports that subpackage
    3) `import package.submodel`: in this case if the submodel exist, it will won't go to `__init__` to search for it.
  
> Absolute imports are used for clarity and when accessing modules from outside the package, while relative imports are useful inside a package to keep code concise and avoid hardcoding the package name. Relative imports can also help manage internal dependencies and reduce coupling.


* `__init__.py`: is the first file python will search for when you import **all** modules from a package or the package itself.
  
    ```python 
    from package import * #or 
    import package
    ```
    there is a variable named `__all__`, which is a list that determines which packages should be imported when you import all of packages from a package using *, `from package import *`. if not specified, any package that exist inside that package and doesn't start with `_`, will be imported. 

>`__init__.py` is not searched when accessing subbmodels like `from alchemy import elements`, it only will be searched when `import alchemy` issued, and `__all__` will only be used when `from alchemy import *`

* the package could by a **file** like `elements.py` or a **directory** like `alchemy`.

* you can access submodel directly when calling a package.
```python
import alchemy
alchemy.elements.create_earth() # even thow create_earth is not in __init__
```


* in directory named `alchemy`, if you imported in `__init__` an internal package(in current directory not in root for example) like `from .package import class/function/...` then this will be called an **alias** if u used it in another file from `alchemy` package.

   so in another file if u did:
```python 
import alchemy
alchemy.class # this is called alias to this class imported from previous package
```






## Mistakes to avoid in import 

### Circular imoprt 

```python 
# A.py 
import B 

# B.py 
import A
```
💥 Result: ImportError (partially initialized module)

### Missing `__init__.py`

  If you forget:
    `alchemy/__init__.py`

    👉 Python might not treat it as a package

### Importing the wrong thing
```python
import elements
elements()
```

❌ WRONG — elements is a module, not a function


### Name shadowing (VERY common)

You create a file 
```python
random.py
```

Then: 
```python
import random
```
👉 Python imports your file, not the standard library 😬

💥 Weird bugs happen


### Re-import confusion

```python 
from module import *
```

❌ Bad practice:

* pollutes namespace

* hides where things come from

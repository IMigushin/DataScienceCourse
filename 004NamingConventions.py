# VARIABLE NAMING CONVENTIONS
# Described in PEP 8 mostly.
# Link:
# https://www.python.org/dev/peps/pep-0008/

# Rule 1
# Variables must be read easy

# Rule 2
# Kebab case is NOT allowed in Python: type-of-variable.
# Snake case is allowed in Python: type_of_variable.
# Camel case is allowed in Python: typeOfVariable.

# Rule 3
# Banned characters for naming as single character variable names:
# - 'l' (lowercase letter el),
# - 'O' (uppercase letter oh),
# - 'I' (uppercase letter eye).
# In some fonts, these characters are indistinguishable from the numerals 1 and 0.
# When tempted to use 'l', use 'L' instead.

# Rule 4
# Type Variable Names
# Names of type variables introduced in PEP 484 should normally use CapWords preferring short names:
#   T, AnyStr, Num.
# It's recommended to add suffixes _co or _contra to the vars used to declare (co-/contra)variant behavior correspondingly:
#   from typing import TypeVar
#   VT_co = TypeVar('VT_co', covariant=True)
#   KT_contra = TypeVar('KT_contra', contravariant=True)
# Link:
# https://www.python.org/dev/peps/pep-0484/

# Rule 5
# Don't start name with number

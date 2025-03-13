# Type Casting 
 - Type casting is technique to  convert one data type to another
 int to str, str to int and int to bool
# Mutable and Immutable

## Immutable 
 -Once created, their values can not be modified , If you try to change them, a new object is created
  - memory address change after changing the value of variable
 - Example:
   - Nuumbers: int,float,complex
   - Strings:str
   - Tuples:tuple
   - Frozen Sets: frozenset
   - Boolean: bool

                x = 10
                print(id(x))  # Memory address of x
                x = x + 5
                print(id(x))  # New memory address (a new object is created)

## Mutable
- Their values can be modied after creation
 - Memory address same after updating variable
 - Example:
  - Lists: list
  - Dictionaries: dict
  - Sets: set
  - Byte Arrays: bytearray

        my_list = [1, 2, 3]
        print(id(my_list))  # Memory address before modification
        my_list.append(4)  
        print(id(my_list))  # Memory address remains the same (modified in place)

# Data Types 
 - Numbers : 1234 , 3.14, 0b11, Decimal(),Fraction()
 - String: "spam", "Bob's"
 - List : [1,2,3,4]  , list(range(10))
 - Tuple : (1,"spam",4, "U-")
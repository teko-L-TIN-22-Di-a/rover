# How we used Python

Here are some [best-practices] for python.

## Constructs we use

### \_\_init\_\_

Is the constructor for a class.

### \_\_main\_\_ — Top-level code environment

`__main__` is the name of the environment where top-level code is run. It's the first Python module which starts running.
It's the `entry point` of the application.

See [source] for more information.

### Property Decorator

For creating properties, we used the [Property Decorator].

## Modules

A module can be a collection of classes.

## Classes

Rover is a class (can be more than one)
map is also a class
window is also a class (need inheritance from tk)

### Inheritance in Python

See [Inheritance] for more information.

To call the parent method use the `super()` keyword.

To call the current method of the class, use the `self` keyword.

## Naming styles

### Overview

| Type                       | Public                           | Internal                                                                    |
| -------------------------- | -------------------------------- | --------------------------------------------------------------------------- |
| Packages                   | lowernounder                     |                                                                             |
| Modules                    | lower_with_under                 | _lower_with_under                                                           |
| Classes                    | CapWords                         | _CapWords                                                                   |
| Exceptions                 | CapWords *or* CapWordsError      |                                                                             |
| Functions                  | lower_with_under()               | _lower_with_under()                                                         |
| Class Constants            | CAPS_WITH_UNDER _CAPS_WITH_UNDER |                                                                             |
| Class Variables            | lower_with_under                 | _lower_with_under                                                           |
| Instance Variables         | lower_with_under                 | _lower_with_under (protected) *or* __lower_with_under (private)             |
| Method Names               | lower_with_under(self)           | _lower_with_under(self) (protected) *or* __lower_with_under(self) (private) |
| Function/Method Parameters | lower_with_under                 |                                                                             |
| Local Variables            | lower_with_under                 |                                                                             |

[Real Pyhton naming styles]

[Private variables] doesn't exists in python, you just give them a different name.

### Single and double underscore

Single Trailing Underscore( var_ ): Used by convention to avoid naming conflicts with Python keywords. Double Leading Underscore( __var ): Triggers name mangling when used in a class context. Enforced by the Python interpreter.

[Inheritance ]: https://www.python-lernen.de/vererbung-python.htm
[source]: https://docs.python.org/3/library/__main__.html
[best-practices]: https://data-flair.training/blogs/python-best-practices
[Real Pyhton naming styles]: https://realpython.com/python-pep8/#:~:text=Naming%20Styles,-The%20table%20below&text=Use%20a%20lowercase%20single%20letter,with%20underscores%20to%20improve%20readability.&text=Start%20each%20word%20with%20a,not%20separate%20words%20with%20underscores
[Private variables]: https://www.scaler.com/topics/python-private-variables/
[Property decorator]: [https://www.programiz.com/python-programming/property]

# How we used Python

## Constructs we use

### __init__

Is like the constructor for Java / C#.

### __main__

### __main__ — Top-level code environment

#### What is the “top-level code environment”?

`__main__` is the name of the environment where top-level code is run. It's the first Python module which starts running.
It's the `entry point` of the application.

[source]

## Modules

main is a module
[modules]

## Classes

rover is a class (can be more than one)
map is also a class
window is also a class (need inheritance from tk)

## Difference Module & Classes

## Vererbung in Python

[Vererbung]

## priavte variables

<https://www.scaler.com/topics/python-private-variables/>

### self vs super()

super refers to sibling or parent method statically. self refers to class of the instance dynamically.

## Naming

<https://realpython.com/python-pep8/#:~:text=Naming%20Styles,-The%20table%20below&text=Use%20a%20lowercase%20single%20letter,with%20underscores%20to%20improve%20readability.&text=Start%20each%20word%20with%20a,not%20separate%20words%20with%20underscores>.

## classes

CapCase

## functions

snake_case

## private vairables

Prefix with _ underscore

## single and double underscore

Single Trailing Underscore( var_ ): Used by convention to avoid naming conflicts with Python keywords. Double Leading Underscore( __var ): Triggers name mangling when used in a class context. Enforced by the Python interpreter.

## Fragen

* Für was ist das (self) in der Parameterliste?

[Vererbung]: https://www.python-lernen.de/vererbung-python.htm
[modules]: https://docs.python.org/3/tutorial/modules.html#tut-modules
[source]: https://docs.python.org/3/library/__main__.html

# About

## Decisions we made

* The Map doesnt care about the rover. There shouldn't be a dependency.
* All imported Modules which are not created by us, will be wrapped. This makes it easy to replace them with other ones and the dependency are clear.
* Every Object should handle it's own stuff. The map shouldn't do stuff for the rover etc.
* Using the [Property decorator]
* Sorting of properties, methods (private members etc.)
* Vererbung anschauen
* Methodennamen dienen als zusätzlche Beschreibung für Setzen von Variabeln und Funktionen. Deshalb gibt es teilweise Methoden mit nur einer Zeile. Dadurch
ist der Code aber einfacher zu verstehen und es ergibt sich in der jeweiligen Klasse einen sauberen Überblick, was die Klasse macht.

[Property decorator]: [https://www.programiz.com/python-programming/property]

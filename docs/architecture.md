# Architecture

## Workflows

* rover can move forward / backwards / left / right. (if one movement should be deactivated, they have to be splitted worklows)
* rover doesn't hit the obstacles.

## Forbidden Dependencies

* The map -> rover

## Dependencies

All imported Modules which are not created by us, will be wrapped. This makes it easy to replace them with other ones and the dependency are clear.

## Method naming

Method names should be an extended description on what the method actually does. Long method names are allowed.

## Class Diagram

![Class Diagram](images/classes.svg)

## Packages

![Packages](images/packages.svg)

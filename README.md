# Design Patterns

Code snippets to describe different design patterns in Python

## Interface

- *Java*, *C#*, *VB* &rarr; built-in support
- *C++* &rarr; using **Abstract Base Class**
- *Python*
    1. **Mixin** &rarr; implementation (breaks the *Dependency Inversion* rule of **SOLID**)
    2. **ABC** (*PEP 3119*)

## Strategy (Policy)

- **Behavioral** pattern (control operations of object)
- Family of algorithms (independent with different implementations but same input/output) &rarr; encapsulate &oplus; interchangable
- *Sign*: sequence of `if`-`elif`-`else`
- **Implementation**
  1. *Object* (using **ABC**)
  2. *Function* (ordinary or `lambda`)

![Strategy Pattern Structure](/assets/strategy.png)

## Observer

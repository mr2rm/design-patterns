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

![Strategy Pattern Structure](/assets/strategy_uml.png)

## Observer (Dependents, Publish-Subscribe)

- **Behavioral** pattern
- Used for *Event Monitoring*
- Defines one-to-many relationship: state changes &rarr; notify dependents
- **Subject** (publisher)
  - Attach/Detach observers
  - Notify observers &rarr; call `update` method of observer
- **Observer** (interested in subject changes)
  - Update &rarr; get state of subject
- **Instruction**
  1. *Observer:* Attach to or detach from subject
  2. *Subject:* send notification
  3. *Observer:* recieve notification
  4. *Observer:* get/set state of subject
- **SOLID** Check
  - S &rarr; subject, object (observer) and main
  - OID &rarr; *ABC*
  - Encapsulation (*OOP*) &rarr; self-contained observers
- Use cases
  - Events in **GUI** apps (e.g. mouse and keyboard)
  - **MVC** &rarr; **M**: Subject & **V**: Observer
  - Push notification
- Prevent *Dangling Reference* by using **Context Manager** in Python

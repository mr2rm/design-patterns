# Design Patterns

Code snippets to describe different design patterns in Python

## Interface

- *Java*, *C#*, *VB* &rarr; built-in support
- *C++* &rarr; using **Abstract Base Class**
- *Python*
    1. **Mixin** &rarr; implementation (breaks the *Dependency Inversion* rule of **SOLID**)
    2. **ABC** (*PEP 3119*)

## Strategy (Policy) [Behavioral]

- Family of algorithms (independent with different implementations but same input/output) &rarr; encapsulate &oplus; interchangable
- *Sign*: sequence of `if`-`elif`-`else`
- **Implementation**
  1. *Object* (using **ABC**)
  2. *Function* (ordinary or `lambda`)

![Strategy Pattern](/assets/strategy.png)

## Observer (Dependents, Publish-Subscribe) [Behavioral]

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

![Observer Pattern](/assets/observer.png)

### Command (Action, Transaction) [Behavioral]

- Used for *toolkits*, *CLIs*, *GUI menus* (each item as a command)
- Request objects &rarr; common structure
- **Features**
  - Encapsulate request to object
  - Parameterize objects (in different requests)
  - Queues and logs operation (e.g. update db, audit trail of requests)
  - Validation, Undoable operations and *Macros* (sequence of commands)
- **Non-Command**
  - Sequence of `if`-`elif`-`else` &rarr; fragile (*Strategy* not worked on methods with different signs)
  - Everything (parse, validate and execute): one class &rarr; ~~S~~
  - Add, change, delete command &rarr; ~~O~~
  - Implementation dependant &rarr; ~~D~~
- **Components**
  - *Client* &rarr; request to do something (e.g. by keyboard or own app)
  - *Invoker* &rarr; ask command to perform request (main module)
  - *Command* &rarr; how to perform action (can use *Reciever*)
  - *Reciever* &rarr; helps command (optional)
    - Concrete object or method of *Command* (depends on complexity)
- Encapsulate commands (separate & hide executation info) &rArr; O
- Utilise *Null Pattern* (undefined commands)
- Import commands in invoker: ~~O~~ &rarr; package includes all commands (load on runtime)

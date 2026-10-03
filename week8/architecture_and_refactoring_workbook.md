1. Current Architecture Problems

| Problem                            | Evidence                                                       | Impact                                                            | Refactoring                                             |
|------------------------------------|----------------------------------------------------------------|-------------------------------------------------------------------|---------------------------------------------------------|
| Mixed Presentation & Workflow      | Scripts mix terminal print() and input() with business loops.  | Cannot unit test business logic without interactive prompts.      | Extract a dedicated CLI menu into presentation/.        |
| Lack of Persistence Abstraction    | Code stores records in global lists or calls storage directly. | Cannot swap in-memory storage for SQLite without rewriting logic. | Create an AppointmentRepository protocol/interface.     |
| God Service Coordinates Everything | A single controller handles all actions across all entities.   | High coupling; hard to maintain and refactor.                     | Split into focused services (e.g., AppointmentService). |

2. Layer Responsibilities

| Layer        | Responsibilities                                                         | Must not contain                                                  |
|--------------|--------------------------------------------------------------------------|-------------------------------------------------------------------|
| Presentation | Render CLI text, capture user keystrokes/prompts, parse command choices. | Domain validation logic, business rules, or database connections. |
| Service      | Orchestrate use cases, coordinate clash checks, invoke repository saves. | Direct console input()/print() calls or raw database drivers.     |
| Domain       | Model entities (Patient, Practitioner, Appointment), enforce invariants. | UI references, persistence code, external API clients.            |
| Repository   | Define abstract data-access contracts (Protocol / ABC).                  | Concrete SQL statements or presentation logic.                    |
| Persistence  | Implement repository contracts (e.g., in-memory dicts, SQLite tables).   | Business workflow rules or presentation formatting.               |


3. SOLID Review

- SRP (Single Responsibility Principle): Relevant. Ensure AppointmentService coordinates only booking workflows, while domain entities retain their internal state transitions
- OCP (Open/Closed Principle): Relevant. New storage mechanisms (e.g., CSV or SQLite) can be added by implementing the repository interface without altering existing service logic
- LSP (Liskov Substitution Principle): Relevant. Any repository implementation (in-memory or SQLite) can be substituted into the service layer without breaking behavior
- ISP (Interface Segregation Principle): Relevant. Keep the repository interface restricted to the specific methods needed for the current prototype (e.g., save, find_by_id, find_all)
- DIP (Dependency Inversion Principle): Relevant. AppointmentService depends on the abstract repository interface, injected via its constructor.
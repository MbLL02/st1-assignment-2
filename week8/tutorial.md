1. Where does this belong?

| Responsibility                      | Layer                       | Reason                                                                            |
|-------------------------------------|-----------------------------|-----------------------------------------------------------------------------------|
| Read menu input                     | Presentation                | Handles human-computer interaction and terminal input reading.                    |
| Check appointment status transition | Domain                      | Encapsulates the core business invariants and lifecycle state of the entity.      |
| Coordinate booking use case         | Service/ Application        | Orchestrates workflow execution, fetching records and invoking domain operations. |
| Execute SQLite INSERT               | Presistence/ Infrastructure | Communicates directly with the storage medium or database engine.                 |
| Format confirmation message         | Presentation                | Formats output data into user-facing console strings.                             |
| Find appointment by ID              | Repository                  | Abstracts data collection retrieval mechanisms away from workflow logic.          |

2. Architecture Smell Hunt

- Presentation / UI coupling: Using input() and direct print() calls inside business logic prevents automated testing and prevents reusing logic in a future web or mobile GUI
  - Layer: Presentation
- Persistence leak: Embedding SQL queries directly alongside business rules ties domain entities to a specific database schema
  - Layer: Persistence (implementing a Repository interface)
- Misplaced domain rules: Checking appointment clash logic inside UI/menu loops leads to duplicate logic and incomplete validation
  - Layer: Domain / Service
- Scattered input validation: Validating basic string inputs everywhere instead of at the domain boundary leads to boilerplate and inconsistent checks
  - Layer: Domain (Patient, Practitioner, Appointment constructors)
- God Object / Low cohesion: A single module handling multiple orthogonal concerns violates the Single Responsibility Principle, making debugging and maintenance difficult
  - Propose layered separation: Separate into distinct presentation/, services/, domain/, and persistence/ packages.

3. SOLID without Overengineering

- ClinicManager handles every use case. Which principle is threatened?
  - Single Responsibility Principle (SRP): It acts as a God Object with multiple reasons to change (booking, reporting, patient registration, GP scheduling)
- AppointmentService imports sqlite3 directly. What dependency concern exists?
  - Dependency Inversion Principle (DIP) violation: The high-level application service depends directly on a low-level database implementation rather than an abstraction (interface/protocol), preventing in-memory test mocking
- A repository interface has 20 methods but a client needs two. What concern exists?
  - Interface Segregation Principle (ISP) violation: Clients are forced to depend on broad, bloated interfaces containing methods they never use
- Should every class have an interface? Explain
  - No, Introducing interfaces for stable domain classes or simple data holders adds unnecessary indirection and premature complexity. Use interfaces/abstractions only at architectural boundaries (such as repositories or external third-party services) where interchangeable implementations or testing fakes are required.

4. AI Architecture Critique

- Microservices & Event Bus: Reject. A small community clinic prototype runs locally on a single machine; distributed microservices and asynchronous buses introduce network latency, distributed failures, and deployment overhead that directly violate the client brief
- Dependency-Injection (DI) Framework: Reject / Defer. Frameworks like dependency-injector are excessive; plain constructor injection is sufficient for passing repositories into services in standard Python
- Six Interfaces: Modify. Keep only one focused repository interface (e.g., AppointmentRepository) that supports current use-case requirements (ISP).
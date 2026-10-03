1. UML to Code Trace

| UML Element        | Python Element          | Implemented | Notes                                                      |
|--------------------|-------------------------|-------------|------------------------------------------------------------|
| Patient Class      | class Patient           | Yes         | Encapsulates ID, name, and phone with validation.          |
| Practitioner Class | class Practitioner      | Yes         | Encapsulates ID, name, and specialty.                      |
| Appointment Class  | class Appointment       | Yes         | Encapsulates ID, patient, GP, datetime, and status.        |
| status Attribute   | AppointmentStatus(Enum) | Yes         | Replaced plain string with Enum to prevent invalid states. |
| cancel() Method    | def cancel(self)        | Yes         | Guard clause blocks repeated or invalid cancellations.     |

2. Domain Invariants

| Class        | Invarients/ Rule                                       | How Protected                                                      |
|--------------|--------------------------------------------------------|--------------------------------------------------------------------|
| Patient      | Mandatory attributes cannot be empty or whitespace.    | Checked in __init__; stripped and stored as private properties.    |
| Practitioner | Cannot create a practitioner with missing credentials. | Validated on constructor initialization.                           |
| Appointment  | Only SCHEDULED appointments can be cancelled.          | cancel() checks status and raises ValueError if already cancelled. |
| Appointment  | Must link to real instantiated domain entities.        | isinstance() checks ensure types are Patient and Practitioner.     |

3. AI Pair-Programming Record

| Ai Contribution                     | Conforms | Decision | Reason                                                             | Verification                              |
|-------------------------------------|----------|----------|--------------------------------------------------------------------|-------------------------------------------|
| AppointmentStatus Enum              | Yes      | Accepted | Restricts status to explicit domain states.                        | Tested enum equality in unit calls.       |
| SQL database connection in cancel() | No       | Rejected | Violates separation of concerns; out of scope for domain entities. | Verified pure in-memory state transition. |
| NotificationService parameter       | No       | Rejected | Invented dependency not supported by client brief.                 | Excluded from appointment constructor.    |

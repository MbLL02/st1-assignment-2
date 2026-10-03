1. Encapsulation Review

| Class        | Protected                                                                                                                                           | Public Opertaions                                    |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| Patient      | patient_id, name, and phone must be non-empty strings and trimmed of whitespace.                                                                    | get_details(), property getters for attributes.      |
| Practitioner | practitioner_id, name, and specialty must be non-empty valid strings.                                                                               | get_details(), property getters.                     |
| Appointment  | status cannot be changed arbitrarily from outside; patient and practitioner references must be valid non-None instances; date_time must be present. | cancel(), get_summary(), property getters for state. |

2. Composition or Inheritance

- Appointment and Patient: 
  - Composition/association: An appointment "has-a" patient participant, not "is-a" patient.
- Appointment and Practitioner: 
  - Composition/association: An appointment associates a practitioner for a timeslot; inheriting would break behavioural subtyping.
- Doctor and Practitioner: 
  - Inheritance: A Doctor "is-a" specialized kind of healthcare practitioner sharing common practitioner traits.
- Child Appointment
  - Composition/association: A clinic aggregates or manages a collection of appointments; it is not an appointment itself.

3. Responsibility Allocation
- Who decides whether SCHEDULED can become CANCELLED?
  - The Appointment class itself encapsulates this state transition rule inside its cancel() method to maintain its own lifecycle invariant
- Who validates a patient name?
  - The Patient class constructor (or validator property setter) validates its own attributes at object instantiation
- Should Appointment execute SQL? Why?
  - No, Domain entities must remain focused solely on business logic (Single Responsibility Principle); coupling database queries to business models violates separation of concerns and hinders automated testing
- Should the UI decide whether a status transition is legal?
  - No, UI layers can display options, but domain validity must be enforced by the domain entity to prevent inconsistent states across different interfaces

4. AI Code Critique 

- Problem: Public status mutation (e.g., appt.status = "Cancelled" directly)
  - Correction: Make status private (self._status) and mutate strictly through the public cancel() method
- Problem: Embedded SQL inside cancel()
  - Correction: Remove all persistence logic; domain entities should only update in-memory state
- Problem: Coupling to NotificationManager
  - Correction: Remove external notification dependencies; messaging is out of scope and creates unnecessary architectural coupling
- Problem: Inheriting from PatientRecord
  - Correction: Use composition/association: Appointment holds a reference to a Patient object
- Problem: Lack of transition guards (allowing double cancellation)
  - Correction: Raise an exception or return False if an already cancelled appointment attempts to cancel again. 
  
5. Exit Question

Classes may be written in Python by a programmer, but if classes do nothing more than hold dumb data as public properties (anemic domain model), intermingle the domain logic with I/O or database operations, or make use of an inheritance hierarchy that is not appropriate, then there is no encapsulation, cohesion, or abstraction.
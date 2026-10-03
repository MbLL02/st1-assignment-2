1. Candidate Concepts

| Candidate    | Class?         | Reason                                                                                                                        |
|--------------|----------------|-------------------------------------------------------------------------------------------------------------------------------|
| Patient      | Yes            | Core domain entity with distinct identity, state (name, contact, patient ID), and booking history.                            |
| Practitioner | Yes            | Core domain entity representing healthcare providers with schedules and consultation records.                                 |
| Appointment  | Yes            | Crucial associational entity that links a patient to a practitioner at a specific time and tracks lifecycle status.           |
| Name         | No             | An attribute (string primitive), not an independent domain entity with separate operational responsibilities.                 |
| Clinic       | Optional / Yes | Can serve as an overarching coordinator/aggregate root managing collections, but can also be modelled as a simple controller. |
| Database     | No             | An infrastructure and implementation detail, not a business domain concept in the problem space.                              |
| Cancellation | No             | An event or state change represented by an attribute value (status = "Cancelled") on Appointment, not an entity.              |
| Status       | No             | An attribute representing an enumerated state ("Scheduled", "Cancelled", "Completed"), not a standalone class.                |

2. Crc Cards

Patient

| Responsibility                                                                             | Collaborators |
|--------------------------------------------------------------------------------------------|---------------|
| Maintain patient demographic data (ID, name, phone); hold reference to appointment history | Appointment   |

Practitioner

| Responsibility                                                                                       | Collaborators |
|------------------------------------------------------------------------------------------------------|---------------|
| Maintain GP details (ID, name, specialty); check schedule availability and identify booking clashes. | Appointment   |

Appointment

| Responsibility                                                                                                       | Collaborators         |
|----------------------------------------------------------------------------------------------------------------------|-----------------------|
| Maintain appointment state (ID, date/time, status); link a specific patient and GP; handle cancellation transitions. | Patient, Practitioner |

3. Relationship Reasoning

- Patient to Appointment: which relationship and why?
  - Association (1 to 0..*): A Patient can exist independently without appointments, but can be associated with zero or many Appointment records over time. 
- Practitioner to Appointment: what multiplicity?   1 to 0..* (One GP to zero or many appointments): A Practitioner can be scheduled for zero, one, or multiple distinct appointments, but each individual appointment must have exactly one assigned GP.
- Should Appointment inherit from Patient?
  - No, An appointment is an administrative event, not a kind of patient (it fails the "is-a" test). Making it inherit would violate basic object-oriented principles.
- Does Clinic need to own every object?
  - No, Direct ownership via tight composition creates unnecessary coupling. A lightweight clinic or scheduling coordinator need only hold collections of references, allowing entities to remain modular and independently testable.

4. AI Model Critique
- Over-Engineering & Anti-Patterns: The AI has decomposed simple domain logic into excessive anemic manager classes (*Manager / *Engine).
- Scope Creep: NotificationManager is out of scope because messaging and notifications are not confirmed requirements in the client brief.
- Recommendation: Consolidate data and behavior back into the core domain entities (Patient, Practitioner, Appointment). A single simple coordinator or facade (like SmartCareSystem or Clinic) is sufficient for high-level operations. 




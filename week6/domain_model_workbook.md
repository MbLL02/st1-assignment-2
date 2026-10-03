1. Requirement-to-Concept Trace

| Requirement  | Concept       | State/behaviour                                                         | Decision                         |
|--------------|---------------|-------------------------------------------------------------------------|----------------------------------|
| FR-01, FR-02 | Patient       | State: patient_id, name, phone / Behaviour: get_details()               | Included as Domain Entity        |
| FR-03, FR-04 | Practitioner  | State: practitioner_id, name, specialty / Behaviour: is_available(time) | Included as Domain Entity        |
| FR-05, FR-06 | Appointment   | State: appointment_id, time, status / Behaviour: check_clash()          | Included as Associational Entity |
| FR-07, FR-08 | Appointment   | State: status / Behaviour: cancel()                                     | Included as State Transition     |
| FR-10        | Clinic/System | State: collections of records / Behaviour: generate_summary_report()    | Included as Coordinator          |



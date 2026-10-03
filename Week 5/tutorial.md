1. Stakeholder map

|Stakeholder   |  Need | Potential Conflict  |
|---|---|---|
| Clinic Receptionist  | Fast, intuitive booking interface to schedule patients rapidly during peak phone hours.  |  May prioritize speed over entering thorough patient data, conflicting with data integrity rules. |
| Practicioner (GP)  | Uninterrupted consultation schedules and adequate buffer times between patients.  | Strict scheduling limits receptionist flexibility when accommodating urgent walk-in appointments.  |
|  Patient |  Accurate, prompt consultations without long waiting times or booking mix-ups. |   Flexible cancellation preferences may disrupt clinic schedule density and GP utilization|
| Clinic Management  |  Accurate operational reports and maximum appointment capacity | High-volume booking targets may cause practitioner fatigue or rushed patient care.  |
|  Unit Assesor |  A simple, maintainable Python prototype that adheres strictly to course scope. |  Desires for advanced third-party enterprise tools conflict with keeping the prototype small and testable. |

2. Functional or Non-Functional?
- [x] Functional | The system shall allow staff to cancel an appointment.
- [x] Non-functional | The system should remain responsive for the course-scale dataset.
- [x] Functional | The system shall retain cancelled appointments.
- [x] Non-functional | Core business logic should be independently testable.
- [x] Functional | The system shall search for a patient by ID.

3. Repair Ambiguous Requirements
- "The system should be easy to use."
  - Problem: Subjective and unmeasurable; cannot be verified by a test case.
  - Clarification question: Can a trained receptionist create a new appointment in fewer than three terminal prompts or within 30 seconds without error?
- "Patient search should be fast."
  - Problem: "Fast" is vague and depends on hardware and dataset size.
  - Clarification question: Must search queries return matching patient records in under 1 second for a dataset of up to 1,000 records?
- "The system should securely manage data."
  - Problem: Lacks specific security criteria, access roles, or regulatory standards.
  - Clarification question: Does this require local file access restrictions and masking patient identifiers, or full encrypted role-based access?
- "Appointments should normally be easy to cancel."
  - Problem: "Normally" and "easy" are conditional and undefined.
  - Clarification question: What specific cancellation steps are required, and are there time constraints (e.g., minimum notice period) before a status updates to "Cancelled"?

4. AI requirement Audit

|  AI Suggestion | Classification  |  Evidence / reason |
|---|---|---|
|  Patients receive SMS reminders | Assumption requiring validation | Useful feature, but not explicitly requested by management in the Stage 1/2 brief.  |
| Facial Recognition login  |  Out of Scope |  Unnecessary biometric overhead; directly violates the client's request for a simple system |
|  Receptionists create appointments |  Confirmed | Directly requested in client brief to replace paper/spreadsheet bookings.  |
|Online payment| Out of Scope  | Financial transactions and gateways are not part of this clinic's core booking prototype.  |
| Practitioners view schedules  |  Confirmed |  Explicitly requested to solve "limited visibility of practitioner availability". |
| AI recommends treatments  |  Out of Scope | Clinical diagnostic decision tools violate the administrative nature of the brief.  |
|  Cancelled appointments remain in history|  Confirmed |  Directly addresses the problem of "lack of reliable appointment history". |

5. Exit Question: Why is 'AI suggested it' not sufficient evidence for a requirement?

AI models generate plausible text based on general training patterns rather than the verified operational needs of the actual client. Without explicit client confirmation, AI-generated items risk scope creep, introduce unnecessary technical overhead, and distort the project's core objectives.



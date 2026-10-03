AI design Review 

| AI Suggestion                             | Evidence                                           | Decision | Reason                                                           | Model Change                                          |
|-------------------------------------------|----------------------------------------------------|----------|------------------------------------------------------------------|-------------------------------------------------------|
| Add AppointmentManager and PatientManager | None in brief; clinic wants a simple system.       | Rejected | Over-engineering that splits state from behavior unnecessarily.  | Kept behavior inside entity classes.                  |
| Add status attribute to Appointment       | FR-07 and FR-08 require tracking cancelled states. | Accepted | Essential for keeping cancellation history intact.               | Added status: str to Appointment.                     |
| Add User superclass with role inheritance | Unconfirmed assumption about user login levels.    | Modified | Deferred; keep Patient and Practitioner independent for Stage 3. | Retained flat entities without inheritance hierarchy. |

Reflection

The most challenging decision to make during Stage 3 modelling was deciding on how to model the transition between statuses and the cancellation process without having to introduce an additional Cancellation class, which was unnecessary and would have complicated the system unnecessarily. I decided to consider the cancellation a transition of state for the Appointment class. When using AI to give me ideas for designing my domain, the AI made over-design of the domain and introduced an enterprise service architecture with PatientManager, AppointmentManager and NotificationManager classes. However, this went against the client's request in the brief for a simple system that can be used in a small clinic. The final design used was fully backed up by the functional requirements (FR-01 to FR-08) set out in Stage 2.



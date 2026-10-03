1. Problem and Scope: 

Problem: SmartCare Community Clinic relies on fragmented spreadsheets and paper records, resulting in duplicate bookings, lost patient files, untracked cancellations, and zero visibility into practitioner schedules.

In Scope: Patient record creation and search, practitioner schedule tracking, appointment creation with clash detection, appointment cancellation, appointment history retention, and console-based operational summaries.

Out of Scope: Online billing/payment gateways, patient self-service portals, biometric/facial login, automated clinical diagnostics/treatment suggestions, and third-party hospital integrations.

Provisional: Automated SMS/email reminders and CSV data persistence.

2. Stakeholders

| Stakeholder  |  Need | Evidence  |
|---|---|---|
| Receptionist  |  Rapid appointment scheduling and reliable patient search. |  Stated need to replace spreadsheet booking bottlenecks. |
|  Practicioner | Clear schedule view and reliable patient consultation history.  | Resolves "limited visibility of practitioner availability".  |
|  Patient |Accurate booking times without double bookings or lost records.   | Resolves "duplicate appointment bookings".  |
|  Clinic Management |  Basic operational reports on bookings and cancellations. | Explicitly requested in client brief.  |

3. Functional Requirements
- FR-01: The system shall record a new patient with a unique ID, full name, and contact phone number.   
- FR-02: The system shall search for existing patient records by patient ID or full name.   
- FR-03: The system shall record practitioner profiles including practitioner ID, full name, and consultation specialty.   
- FR-04: The system shall display the scheduled appointments for a selected practitioner.   
- FR-05: The system shall create an appointment linking a valid patient ID, practitioner ID, date, and start time.   
- FR-06: The system shall reject any booking that creates a time clash for the same practitioner.   
- FR-07: The system shall update an appointment's status to "Cancelled" upon receptionist request.   
- FR-08: The system shall retain cancelled appointments within the historical record rather than deleting them.   
- FR-09: The system shall display an appointment history for a specific patient.   
- FR-10: The system shall generate a summary report displaying total bookings, completed visits, and cancellations.

4. Non-Functional Requirements
- NFR-01 (Reliability / Data Integrity): The system shall prevent duplicate appointment records from being written to the data store under any circumstance.
- NFR-02 (Performance): The system shall return patient search results in less than 1 second for datasets of up to 1,000 records.
- NFR-03 (Usability): The console interface shall display descriptive validation error messages whenever invalid input is supplied.
- NFR-04 (Maintainability): The codebase shall separate core booking business logic from terminal input/output routines to facilitate future UI migration.
- NFR-05 (Testability): All validation and clash-detection rules shall be executable independently via unit test scripts.

5. User Stories
- US-01: As a receptionist, I want to search for a patient by their full name, so that I can quickly view their booking history while on the phone.
- US-02: As a receptionist, I want the system to block overlapping bookings for the same GP, so that the clinic avoids double bookings. 
- US-03: As a receptionist, I want to mark an appointment as cancelled, so that the practitioner's timeslot is freed up for other patients. 
- US-04: As a practitioner, I want to view my daily schedule, so that I know which patients I am consulting and when.
- US-05: As clinic management, I want a report of daily booking totals and cancellations, so that I can track operational clinic trends.

6. Acceptance Criteria
- Scenario 1: Successful Appointment Booking (US-02)   
  - GIVEN Dr. Doe has no appointment scheduled at 10:00 AM on 2026-10-15,   
    WHEN the receptionist schedules an appointment for patient Alice Smith at that time,   
  - THEN the system confirms the booking and marks the appointment status as "Scheduled".   
- Scenario 2: Negative/Failure Clash Detection (US-02)   
  - GIVEN Dr. Doe already has an appointment booked at 10:00 AM on 2026-10-15,   
  - WHEN the receptionist attempts to book patient Bob Johnson with Dr. Doe at that same date and time,   
  - THEN the system rejects the booking with an error message and leaves the existing schedule unchanged.   
- Scenario 3: Cancelling an Appointment (US-03)   
  - GIVEN an existing active appointment exists for patient Alice Smith,
  - WHEN the receptionist cancels the appointment,
  - THEN the status updates to "Cancelled", the record remains visible in audit history, and the timeslot becomes available for new bookings. 
7. Assumptions and Open questions
- Assumptions:
  - Standard consultation duration is fixed at 15 minutes unless specified otherwise.
  - Each patient has a unique identifier to avoid confusion between identical names.
  - The initial system will run locally in a single terminal session without multi-user network concurrency.   
- Open Questions:
  - What exact contact information is mandatory during patient intake (phone, email, Medicare)?
  - Does the clinic require emergency walk-in slots reserved in the GP schedule?


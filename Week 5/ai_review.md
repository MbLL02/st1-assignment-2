AI review and Reflection

|Ai suggestion   | Evidence  |  Decision | Reason  |  Verification |
|---|---|---|---|---|
|  Add a unique appointment_id attribute |  Case study notes difficulty locating records and tracking history. | Accepted  | Unique keys are necessary to cancel or update records unambiguously.  | Verified against FR-07 and cancellation logic.  |
| Implement SMS appointment reminders  | No direct mention in the client brief.     | Modified  |  Marked as a provisional future requirement; not needed in v0.2 core. | Confirmed against prototype scope  |
| Add patient credit card pre-authorisation  |  None; clinic brief requests booking management only |  Rejected |  Out of scope; creates compliance overhead for a community clinic | Confirmed with client brief guardrails.  |

Reflection:

In Stage 2, the use of Microsoft Copilot in the requirements analysis provided me with additional ideas about edge cases that I didn’t think about before – like what should happen to the appointment state after cancellations and the necessity of unique appointment IDs instead of using only patients' names. Yet, the AI was trying to overextend its functions by proposing too complicated enterprise-level functionalities, such as automated SMS notifications, payment gateways, and role-based access control, none of which was mentioned in the client brief at all. After AI critique, I redefined my cancellation requirement from just removing an appointment record to marking it with "Cancelled" status attribute, so that the clinic would always have a record of its history, which was required by the management. That review once again proved that each requirement has to be backed up with client evidence and not algorithmic ideas, as otherwise, development teams will be wasting their time implementing unneeded and complex functions which do not solve users’ issues.

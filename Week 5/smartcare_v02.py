# smartcare_v02.py
# Stage 2: Requirements-Driven SmartCare Prototype

appointments = []
_next_id = 1


def book_appointment(patient_name, practitioner_name, appointment_time):
  """Books a new appointment if valid and no practitioner clash exists (FR-05, FR-06)."""
  global _next_id

  # Input validation
  if not patient_name or not patient_name.strip():
    raise ValueError("Patient name cannot be empty or blank.")
  if not practitioner_name or not practitioner_name.strip():
    raise ValueError("Practitioner name cannot be empty or blank.")
  if not appointment_time or not appointment_time.strip():
    raise ValueError("Appointment time cannot be empty or blank.")

  # Double-booking check: practitioner cannot have two active appointments at the same time
  for appt in appointments:
    if (
        appt["practitioner"] == practitioner_name
        and appt["time"] == appointment_time
        and appt["status"] == "Scheduled"
    ):
      raise ValueError(
          f"Booking conflict: {practitioner_name} is already booked at"
          f" {appointment_time}."
      )

  appointment = {
      "appointment_id": _next_id,
      "patient": patient_name.strip(),
      "practitioner": practitioner_name.strip(),
      "time": appointment_time.strip(),
      "status": "Scheduled",  # Scheduled, Cancelled, Completed
  }
  appointments.append(appointment)
  _next_id += 1
  return appointment


def cancel_appointment(appointment_id):
  """Updates appointment status to 'Cancelled' without deleting historical record (FR-07, FR-08)."""
  for appt in appointments:
    if appt["appointment_id"] == appointment_id:
      if appt["status"] == "Cancelled":
        print(f"Appointment {appointment_id} is already cancelled.")
        return False
      appt["status"] = "Cancelled"
      print(f"Appointment {appointment_id} has been successfully cancelled.")
      return True
  raise ValueError(f"Appointment ID {appointment_id} not found.")


def display_appointments(show_cancelled=True):
  """Displays all appointments in the clinic log (FR-04, FR-09)."""
  if not appointments:
    print("No appointments recorded.")
    return

  print("\n--- Current SmartCare Appointments ---")
  for appt in appointments:
    if not show_cancelled and appt["status"] == "Cancelled":
      continue
    print(
        f"ID: {appt['appointment_id']} | Patient: {appt['patient']} |"
        f" Practitioner: {appt['practitioner']} | Time: {appt['time']} |"
        f" Status: {appt['status']}"
    )
  print("--------------------------------------\n")


if __name__ == "__main__":
  print("=== SmartCare Clinic System v0.2 ===")

  # 1. Normal bookings (Acceptance Scenario 1)
  appt1 = book_appointment(
      "Alice Smith", "Dr. John Doe", "2026-10-15 10:00 AM"
  )
  appt2 = book_appointment("Bob Johnson", "Dr. Jane Roe", "2026-10-15 11:30 AM")
  display_appointments()

  # 2. Testing clash detection / negative case (Acceptance Scenario 2)
  print("Testing double-booking prevention...")
  try:
    book_appointment("Charlie Brown", "Dr. John Doe", "2026-10-15 10:00 AM")
  except ValueError as error:
    print(f"Expected Error Caught: {error}\n")

  # 3. Testing cancellation keeping history (Acceptance Scenario 3)
  print("Testing appointment cancellation...")
  cancel_appointment(appt1["appointment_id"])
  display_appointments()
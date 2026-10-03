# smartcare_v04.py
# Stage 4: SmartCare Domain Model Implementation
from enum import Enum


class AppointmentStatus(Enum):
  """Enumeration for valid appointment states."""

  SCHEDULED = "Scheduled"
  CANCELLED = "Cancelled"
  COMPLETED = "Completed"


class Patient:
  """Represents a clinic patient (FR-01, FR-02)."""

  def __init__(self, patient_id: str, name: str, phone: str):
    if not patient_id or not str(patient_id).strip():
      raise ValueError("Patient ID cannot be blank.")
    if not name or not name.strip():
      raise ValueError("Patient name cannot be blank.")
    if not phone or not phone.strip():
      raise ValueError("Patient phone cannot be blank.")

    self._patient_id = str(patient_id).strip()
    self._name = name.strip()
    self._phone = phone.strip()

  @property
  def patient_id(self) -> str:
    return self._patient_id

  @property
  def name(self) -> str:
    return self._name

  @property
  def phone(self) -> str:
    return self._phone

  def get_details(self) -> str:
    return (
        f"Patient ID: {self._patient_id} | Name: {self._name} | Phone:"
        f" {self._phone}"
    )


class Practitioner:
  """Represents a healthcare general practitioner (FR-03, FR-04)."""

  def __init__(self, practitioner_id: str, name: str, specialty: str):
    if not practitioner_id or not str(practitioner_id).strip():
      raise ValueError("Practitioner ID cannot be blank.")
    if not name or not name.strip():
      raise ValueError("Practitioner name cannot be blank.")
    if not specialty or not specialty.strip():
      raise ValueError("Specialty cannot be blank.")

    self._practitioner_id = str(practitioner_id).strip()
    self._name = name.strip()
    self._specialty = specialty.strip()

  @property
  def practitioner_id(self) -> str:
    return self._practitioner_id

  @property
  def name(self) -> str:
    return self._name

  @property
  def specialty(self) -> str:
    return self._specialty

  def get_details(self) -> str:
    return (
        f"GP ID: {self._practitioner_id} | Name: {self._name} | Specialty:"
        f" {self._specialty}"
    )


class Appointment:
  """Associates a Patient and Practitioner for a scheduled consultation (FR-05 to FR-08)."""

  def __init__(
      self,
      appointment_id: int,
      patient: Patient,
      practitioner: Practitioner,
      date_time: str,
  ):
    if not isinstance(appointment_id, int) or appointment_id <= 0:
      raise ValueError("Appointment ID must be a positive integer.")
    if not isinstance(patient, Patient):
      raise TypeError("patient must be a valid Patient instance.")
    if not isinstance(practitioner, Practitioner):
      raise TypeError("practitioner must be a valid Practitioner instance.")
    if not date_time or not date_time.strip():
      raise ValueError("date_time cannot be blank.")

    self._appointment_id = appointment_id
    self._patient = patient
    self._practitioner = practitioner
    self._date_time = date_time.strip()
    self._status = AppointmentStatus.SCHEDULED

  @property
  def appointment_id(self) -> int:
    return self._appointment_id

  @property
  def patient(self) -> Patient:
    return self._patient

  @property
  def practitioner(self) -> Practitioner:
    return self._practitioner

  @property
  def date_time(self) -> str:
    return self._date_time

  @property
  def status(self) -> AppointmentStatus:
    return self._status

  def cancel(self) -> bool:
    """Enforces the invariant that only SCHEDULED appointments can be cancelled."""
    if self._status != AppointmentStatus.SCHEDULED:
      raise ValueError(
          f"Cannot cancel appointment with status {self._status.value}."
      )
    self._status = AppointmentStatus.CANCELLED
    return True

  def get_summary(self) -> str:
    return (
        f"Appt #{self._appointment_id}: {self._date_time} | Patient:"
        f" {self._patient.name} | GP: {self._practitioner.name} | Status:"
        f" {self._status.value}"
    )


if __name__ == "__main__":
  print("=== Stage 4 Behaviour Verification ===")

  # 1. Valid instantiation
  p = Patient("P001", "Alice Smith", "0412345678")
  doc = Practitioner("DR01", "Dr. John Doe", "General Practice")
  appt = Appointment(1, p, doc, "2026-10-20 10:00 AM")
  print(appt.get_summary())

  # 2. Status Transition: Cancel appointment
  appt.cancel()
  print("After cancellation:", appt.get_summary())

  # 3. Invariant check: Attempting repeated illegal cancellation
  try:
    appt.cancel()
  except ValueError as e:
    print("Caught expected repeated cancellation error:", e)

  # 4. Input validation check
  try:
    bad_patient = Patient("", "Bob", "123")
  except ValueError as e:
    print("Caught expected input validation error:", e)
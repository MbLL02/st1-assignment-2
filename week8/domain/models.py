from enum import Enum


class AppointmentStatus(Enum):
  SCHEDULED = "Scheduled"
  CANCELLED = "Cancelled"
  COMPLETED = "Completed"


class Patient:

  def __init__(self, patient_id: str, name: str, phone: str):
    if not patient_id or not patient_id.strip():
      raise ValueError("Patient ID cannot be blank.")
    if not name or not name.strip():
      raise ValueError("Name cannot be blank.")
    self.patient_id = patient_id.strip()
    self.name = name.strip()
    self.phone = phone.strip()


class Practitioner:

  def __init__(self, practitioner_id: str, name: str, specialty: str):
    if not practitioner_id or not practitioner_id.strip():
      raise ValueError("Practitioner ID cannot be blank.")
    if not name or not name.strip():
      raise ValueError("Name cannot be blank.")
    self.practitioner_id = practitioner_id.strip()
    self.name = name.strip()
    self.specialty = specialty.strip()


class Appointment:

  def __init__(
      self,
      appointment_id: int,
      patient: Patient,
      practitioner: Practitioner,
      date_time: str,
  ):
    if not isinstance(appointment_id, int) or appointment_id <= 0:
      raise ValueError("Appointment ID must be a positive integer.")
    self.appointment_id = appointment_id
    self.patient = patient
    self.practitioner = practitioner
    self.date_time = date_time.strip()
    self._status = AppointmentStatus.SCHEDULED

  @property
  def status(self) -> AppointmentStatus:
    return self._status

  def cancel(self):
    if self._status != AppointmentStatus.SCHEDULED:
      raise ValueError(
          f"Cannot cancel appointment with status {self._status.value}."
      )
    self._status = AppointmentStatus.CANCELLED
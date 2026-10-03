# domain_models.py
# Stage 3: SmartCare Domain Model Class Skeletons


class Patient:
  """Represents a clinic patient entity (FR-01, FR-02)."""

  def __init__(self, patient_id: str, name: str, phone: str):
    self.patient_id = patient_id
    self.name = name
    self.phone = phone

  def get_details(self) -> str:
    """Returns a formatted summary of patient details."""
    return f"Patient: {self.name} (ID: {self.patient_id}, Phone: {self.phone})"


class Practitioner:
  """Represents a clinic GP entity (FR-03, FR-04)."""

  def __init__(self, practitioner_id: str, name: str, specialty: str):
    self.practitioner_id = practitioner_id
    self.name = name
    self.specialty = specialty

  def get_schedule(self) -> list:
    """Returns the practitioner's scheduled appointments."""
    pass


class Appointment:
  """Associates a Patient and Practitioner for a consultation (FR-05 to FR-08)."""

  def __init__(
      self,
      appointment_id: int,
      patient: Patient,
      practitioner: Practitioner,
      date_time: str,
      status: str = "Scheduled",
  ):
    self.appointment_id = appointment_id
    self.patient = patient
    self.practitioner = practitioner
    self.date_time = date_time
    self.status = status

  def cancel(self) -> bool:
    """Transitions appointment status to 'Cancelled'."""
    pass

  def get_summary(self) -> str:
    """Returns a one-line summary of the appointment."""
    pass
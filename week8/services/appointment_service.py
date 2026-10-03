from typing import List, Optional
from domain.models import Appointment, AppointmentStatus, Patient, Practitioner
from repositories.appointment_repository import AppointmentRepository


class AppointmentService:
  """Orchestrates appointment booking workflows without mixing UI or DB details."""

  def __init__(self, repository: AppointmentRepository):
    self._repo = repository
    self._id_counter = 1

  def book_appointment(
      self, patient: Patient, practitioner: Practitioner, date_time: str
  ) -> Appointment:
    # Check for practitioner clash
    for appt in self._repo.find_all():
      if (
          appt.practitioner.practitioner_id == practitioner.practitioner_id
          and appt.date_time == date_time
          and appt.status == AppointmentStatus.SCHEDULED
      ):
        raise ValueError(
            f"Clash: {practitioner.name} is already booked at {date_time}."
        )

    appt = Appointment(self._id_counter, patient, practitioner, date_time)
    self._repo.save(appt)
    self._id_counter += 1
    return appt

  def cancel_appointment(self, appointment_id: int) -> None:
    appt = self._repo.find_by_id(appointment_id)
    if not appt:
      raise ValueError(f"Appointment #{appointment_id} does not exist.")
    appt.cancel()
    self._repo.save(appt)

  def list_appointments(self) -> List[Appointment]:
    return self._repo.find_all()
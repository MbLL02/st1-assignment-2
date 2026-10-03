from typing import Dict, List, Optional
from domain.models import Appointment
from repositories.appointment_repository import AppointmentRepository


class InMemoryAppointmentRepository(AppointmentRepository):
  """Concrete in-memory implementation for testing and simple prototype use."""

  def __init__(self):
    self._storage: Dict[int, Appointment] = {}

  def save(self, appointment: Appointment) -> None:
    self._storage[appointment.appointment_id] = appointment

  def find_by_id(self, appointment_id: int) -> Optional[Appointment]:
    return self._storage.get(appointment_id)

  def find_all(self) -> List[Appointment]:
    return list(self._storage.values())
from typing import List, Optional, Protocol
from domain.models import Appointment


class AppointmentRepository(Protocol):
  """Abstract interface for appointment persistence (DIP, ISP)."""

  def save(self, appointment: Appointment) -> None:
    ...

  def find_by_id(self, appointment_id: int) -> Optional[Appointment]:
    ...

  def find_all(self) -> List[Appointment]:
    ...
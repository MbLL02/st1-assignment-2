from domain.models import Patient, Practitioner
from persistence.in_memory_repository import InMemoryAppointmentRepository
from services.appointment_service import AppointmentService


def main():
  print("=== SmartCare Clinic v0.5 Layered Architecture ===")

  # Dependency Inversion: Inject repository into service
  repo = InMemoryAppointmentRepository()
  service = AppointmentService(repository=repo)

  p1 = Patient("P01", "Alice Smith", "0412345678")
  doc = Practitioner("DR01", "Dr. John Doe", "General Practice")

  # Use Case: Booking
  appt1 = service.book_appointment(p1, doc, "2026-10-30 09:00 AM")
  print(
      f"Booked: Appt #{appt1.appointment_id} for {appt1.patient.name} with"
      f" {appt1.practitioner.name}"
  )

  # Use Case: Cancel
  service.cancel_appointment(appt1.appointment_id)
  print(f"Status after cancel: {appt1.status.value}")


if __name__ == "__main__":
  main()
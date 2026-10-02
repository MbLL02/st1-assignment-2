#task 1
# Create and run a simple Python file with basic input,output statements
print("Welcome to SmartCare: Community Clinic Appointment Booking System!")
# First Appointment
patient1_name = 'Alice Smith'
practitioner1_name = 'Dr. John Doe'
appointment1_time = '2024-07-20 10:00 AM'
print(f"Patient: {patient1_name} | Practitioner: {practitioner1_name} | Time:
{appointment1_time}")
# Second Appointment
patient2_name = 'Bob Johnson'
practitioner2_name = 'Dr. Jane Roe'
appointment2_time = '2024-07-20 11:30 AM'
print(f"Patient: {patient2_name} | Practitioner: {practitioner2_name} | Time:
{appointment2_time}")

Part 1

SmartCare needs a small prototype that allows a receptionist to record patient appointments. Each appointment records patient name, practitioner name and appointment time. 

What data must be stored?  

Patient Name, Practitioner name, Appointment date and time, Appointment status 

What functions might be useful? 

display_appointments(): Iterate through records and print them cleanly.  
cancel_appointment(appointment_id): Remove or update status of an existing booking. check_availability(practitioner_name, appointment_time): Check if a practitioner is already booked at that time 

What could go wrong? 

Two booking could be made under the same GP  
There is no memory of any record right now as they are made under volatile memory  

What requirements are unclear? 

The exact timeslot of a booking or how long the booking lasts. 
What happens when two people have the same name, how would that be stored? 
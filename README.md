  # main_portfolio_project
This section focuses on showcasing proficiency in data analytics, Performed data cleaning, structured datasets, and wrote optimized SQL queries to extract insights. Created interactive Power BI dashboards showcasing trends and answering business questions, to highlight proficiency in data analytics, visualization, and driving data-informed decisions.

## Project 1: HOSPITAL OPERATIONAL MANAGEMENT ANALYSIS​

### About 

The 'Hospital Operational Management Analysis' project integrates SQL and Power BI to analyze hospital data, improve decision-making, and optimize resource utilization. SQL was used to create the database, define attributes, and populate data. Key business insights, related to room utilization, revenue generation, and medicine patterns, were derived through queries. Power BI dashboards were developed to visualize trends, including patient room turnover, department revenues, and prescription distributions, offering actionable strategies to optimize operations, enhance billing processes, and improve patient satisfaction (business questions) to improve the hospital operational performance. This project showcases expertise in data modeling, SQL analysis, and impactful visualizations.

### Steps 

- **Creating tables (DDL statements):**
  
1. Patient Table
   
o Attributes: PatientID, FirstName, LastName, DateOfBirth, Gender, Address, PhoneNumber, Email, EmergencyContactName, EmergencyContactPhone

o Purpose: Stores demographic details of patients.

2. Doctor Table
   
o Attributes: DoctorID, FirstName, LastName, Specialization, PhoneNumber, Email, DepartmentID, Availability

o Purpose: Stores the details of doctors, including their specialization and contact details.

3. Department Table
   
o Attributes: DepartmentID, DepartmentName, Location, PhoneExtension

o Purpose: Defines different hospital departments such as Cardiology, Neurology, etc.

4. Appointment Table

o Attributes: AppointmentID, PatientID, DoctorID, DepartmentID, AppointmentDate, AppointmentTime, Status (Scheduled, Completed, Cancelled)

o Purpose: Manages patient appointments with doctors.

5. Medical Records Table

o Attributes: RecordID, PatientID, DoctorID, VisitDate, Diagnosis, TreatmentPlan, Prescription

o Purpose: Records all patient medical history, including diagnosis and treatment.

6. Prescription Table
o Attributes: PrescriptionID, RecordID, MedicineID, Dosage, Frequency, Duration
o Purpose: Keeps track of prescribed medicines for each patient's medical record.

7. Medicine Table

o Attributes: MedicineID, MedicineName, Manufacturer, StockQuantity, Price

o Purpose: Stores information about available medicines.

8. Billing Table

o Attributes: BillingID, PatientID, TotalAmount, PaymentStatus (Paid/Unpaid), PaymentDate, PaymentMethod

o Purpose: Handles billing and payments for hospital services.

9. Staff Table

o Attributes: StaffID, FirstName, LastName, Role, DepartmentID, PhoneNumber, Email, ShiftHours

o Purpose: Stores information about non-medical staff (nurses, administrative staff, technicians, etc.).

10.Room Table

o Attributes: RoomID, RoomNumber, DepartmentID, RoomType (General, Private, ICU, etc.), AvailabilityStatus

o Purpose: Maintains information about hospital rooms and their status.

11.RoomAssignment Table

o Attributes: AssignmentID, RoomID, PatientID, AdmissionDate, DischargeDate

o Purpose: Records patient room assignments.


SQL Constraints to Enforce

 Primary Key Constraints: PatientID, DoctorID, DepartmentID, AppointmentID, etc.

 Foreign Key Constraints: Link PatientID in Appointment Table to PatientID in Patient Table.

 Not Null Constraints: For attributes that are essential, like FirstName, LastName, etc.

 Unique Constraints: For attributes like Email, PhoneNumber, RoomNumber, etc.

- Loading data:

Used sql queries to populate data

- **Created DML queries**
Formulated business questions and gathered insights for the business questions through queries.

Business Question 1:

![Business Question 1](https://github.com/arjunvk007/main_portfolio_project/blob/main/Portfolio%20Sql%20%20photos/BQ%201.png)

Business Question 2:

![Business Question 2](https://github.com/arjunvk007/main_portfolio_project/blob/main/Portfolio%20Sql%20%20photos/BQ2.png)


Business Question 3:

![Business Question 3](https://github.com/arjunvk007/main_portfolio_project/blob/main/Portfolio%20Sql%20%20photos/BQ%203.png)

Business Question 4:

![Business Question 4](https://github.com/arjunvk007/main_portfolio_project/blob/main/Portfolio%20Sql%20%20photos/BQ%204.png)

Business Question 5:

![Business Question 5](https://github.com/arjunvk007/main_portfolio_project/blob/main/Portfolio%20Sql%20%20photos/BQ%205.png)

Business Question 6:

![Business Question 6](https://github.com/arjunvk007/main_portfolio_project/blob/main/Portfolio%20Sql%20%20photos/BQ%206.png)

Business Question 7:

![Business Question 7](https://github.com/arjunvk007/main_portfolio_project/blob/main/Portfolio%20Sql%20%20photos/BQ%207.png)

Business Question 8:

![Business Question 8](https://github.com/arjunvk007/main_portfolio_project/blob/main/Portfolio%20Sql%20%20photos/BQ%208.png)

Business Question 9:

![Business Question 9](https://github.com/arjunvk007/main_portfolio_project/blob/main/Portfolio%20Sql%20%20photos/BQ%209.png)


Business Question 10:

![Business Question 10](https://github.com/arjunvk007/main_portfolio_project/blob/main/Portfolio%20Sql%20%20photos/BQ%2010.png)

Business Question 11:

![Business Question 11](https://github.com/arjunvk007/main_portfolio_project/blob/main/Portfolio%20Sql%20%20photos/BQ%2011.png)

Business Question 12:

![Business Question 12](https://github.com/arjunvk007/main_portfolio_project/blob/main/Portfolio%20Sql%20%20photos/BQ%2012.png)

Business Question 13:

![Business Question 13](https://github.com/arjunvk007/main_portfolio_project/blob/main/Portfolio%20Sql%20%20photos/BQ%2013.png)

Business Question 14:

![Business Question 14](https://github.com/arjunvk007/main_portfolio_project/blob/main/Portfolio%20Sql%20%20photos/BQ%2014.png)

Business Question 15:

![Business Question 15](https://github.com/arjunvk007/main_portfolio_project/blob/main/Portfolio%20Sql%20%20photos/BQ%2015.png)

- Connected the data in SQL to powerBI, to create dashboard

- Charts used:
  1. Bar Chart:

No. of Patients by Room Type (ICU, General, Private)
Total Revenue by Department (General Surgery, Orthopedics, Neurology, etc.)

2. Column Chart:
Turnover Rate (Admissions/Discharges) by Room Type

3. Pie Chart:

Medicine Prescription Count (Simvastatin, Metformin, Paracetamol, etc.)

4. Stacked Bar Chart:

Average Patient Count by Room

5. Radar Chart:

Number of Appointments by Department (Maternity, General Surgery, Neurology, etc.)

6. Table:

Room Type and Average Stay
ICU Prescribed Medicines and Count

7. KPI Cards:

Total Appointments (244K)
Number of Unpaid Patients (199)
Doctor with Most Patients (Alice Brown)

Dashboard:

![Visualization](https://github.com/arjunvk007/main_portfolio_project/blob/main/Portfolio%20Sql%20%20photos/Visualization.png)

Insights:


The analysis highlights key hospital operational insights and strategies. ICU rooms show the highest utilization (48.87%) and turnover, while private rooms are underutilized (17.88%), suggesting opportunities for marketing or pricing adjustments. General Surgery and Orthopedics contribute the most revenue (~$1.1M), while Dermatology and Emergency departments underperform. Medicine prescriptions are balanced, with frequent ICU drugs like Amoxicillin and Aspirin requiring stock monitoring and supplier negotiations. 

Strategies:

Strategies include optimizing room allocation, enhancing billing processes to reduce unpaid bills, focusing resources on high-revenue departments, improving patient experiences through feedback and loyalty programs, and expanding ICU/general room capacities to meet demand.

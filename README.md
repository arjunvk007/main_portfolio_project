  # main_portfolio_project
This section focuses on showcasing proficiency in data analytics, Performed data cleaning, structured datasets, and wrote optimized SQL queries to extract insights. Created interactive Power BI dashboards showcasing trends and answering business questions, to highlight proficiency in data analytics, visualization, and driving data-informed decisions.

# Project 1: HOSPITAL OPERATIONAL MANAGEMENT ANALYSIS​

### About 

The 'Hospital Operational Management Analysis' project integrates SQL and Power BI to analyze hospital data, improve decision-making, and optimize resource utilization. SQL was used to create the database, define attributes, and populate data. Key business insights, related to room utilization, revenue generation, and medicine patterns, were derived through queries. Power BI dashboards were developed to visualize trends, including patient room turnover, department revenues, and prescription distributions, offering actionable strategies to optimize operations, enhance billing processes, and improve patient satisfaction (business questions) to improve the hospital operational performance. This project showcases expertise in data modeling, SQL analysis, and impactful visualizations.

### Steps 

- **Creating tables (DDL statements):**
  
1. Patient Table: PatientID, FirstName, LastName, DateOfBirth, Gender, Address, PhoneNumber, Email, EmergencyContactName, EmergencyContactPhone

2. Doctor Table: DoctorID, FirstName, LastName, Specialization, PhoneNumber, Email, DepartmentID, Availability

3. Department Table: DepartmentID, DepartmentName, Location, PhoneExtension

4. Appointment Table: AppointmentID, PatientID, DoctorID, DepartmentID, AppointmentDate, AppointmentTime, Status (Scheduled, Completed, Cancelled)

5. Medical Records Table: RecordID, PatientID, DoctorID, VisitDate, Diagnosis, TreatmentPlan, Prescription

6. Prescription Table: PrescriptionID, RecordID, MedicineID, Dosage, Frequency, Duration

7. Medicine Table: MedicineID, MedicineName, Manufacturer, StockQuantity, Price

8. Billing Table: BillingID, PatientID, TotalAmount, PaymentStatus (Paid/Unpaid), PaymentDate, PaymentMethod

9. Staff Table: StaffID, FirstName, LastName, Role, DepartmentID, PhoneNumber, Email, ShiftHours

10.Room Table: RoomID, RoomNumber, DepartmentID, RoomType (General, Private, ICU, etc.), AvailabilityStatus

11.RoomAssignment Table: AssignmentID, RoomID, PatientID, AdmissionDate, DischargeDate

- **Loading data:**

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

- **Connected the data in SQL to powerBI, to create dashboard**

-  **Charts used:**
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

**Dashboard:**

![Visualization](https://github.com/arjunvk007/main_portfolio_project/blob/main/Portfolio%20Sql%20%20photos/Visualization.png)

**Insights:**


The analysis highlights key hospital operational insights and strategies. ICU rooms show the highest utilization (48.87%) and turnover, while private rooms are underutilized (17.88%), suggesting opportunities for marketing or pricing adjustments. General Surgery and Orthopedics contribute the most revenue (~$1.1M), while Dermatology and Emergency departments underperform. Medicine prescriptions are balanced, with frequent ICU drugs like Amoxicillin and Aspirin requiring stock monitoring and supplier negotiations. 

**Strategies:**

Key strategies include optimizing room utilization by promoting private rooms and reallocating ICU resources to manage high demand. Enhance billing processes with automated reminders and flexible payment plans to reduce unpaid bills. Focus on high-revenue departments like General Surgery and Orthopedics by allocating more resources. Improve medicine management through bulk supplier negotiations for high-demand drugs. Expand ICU/general room capacities and implement patient feedback systems and loyalty programs to enhance experiences and retention.

**Conclusion**

In 'Hospital Operational Management Analysis' project effectively utilized SQL for database creation, data entry, and generating key business insights through optimized queries. Power BI was used to develop dynamic visualizations, including bar charts, pie charts, and KPIs, to showcase trends in room utilization, revenue generation, and prescription patterns. The project provided actionable strategies to optimize resource allocation, improve billing processes, and enhance patient satisfaction.  This project demonstrated the effective use of technologies to derive actionable business strategies, showcasing strong skills in data analysis, visualization, and informed decision-making.

# Project 2: From Boom to Mainstream: Analyzing the Growth Trajectory of Cryptocurrency

## About

The project focuses on analyzing the historical trends, growth factors, and predictive trajectories of the cryptocurrency market. With growing interest and volatility in cryptocurrencies, the study aims to identify the key drivers of adoption, price changes, and forecast future market trends.

The analysis explores primary factors influencing cryptocurrency growth, price trends, market cap movements, and supply patterns for the top 10 cryptocurrencies (BTC, ETH, XRP, USDC, etc.). The dataset spans 2009–2024, with detailed insights from 2019–2023, incorporating attributes such as Price, Market Cap, Supply, and Volume.

For data preparation, initial inspections and cleaning were performed in Excel to ensure formatting consistency and handle missing values. Multiple Excel files were combined into a structured format, ensuring time-series data readiness. Using Power BI, the finalized dataset was visualized to uncover trends, anomalies, and patterns, providing actionable insights into cryptocurrency market behavior and predictions for the next five years.

**Steps**

1. Data Gathering:

  Collected historical cryptocurrency dataset from Kaggle, which was then consolidated to include only the top 10 cryptocurrencies by market value. This dataset provides insights into the trends, performance, and behavior of the leading cryptocurrencies, aiding in analysis and forecasting within the crypto market.

2. Data Cleaning:

- Filled missing values:

  Missing values were addressed by generating random values using find and replace option. This approach ensured dataset completeness for further analysis while maintaining variability without introducing systematic bias into the data.

- Cell Formatting and Value Separation:
  
  Uniform number formatting (e.g., two decimal places for currency) and Conditional Formatting were applied to highlight anomalies in Excel. Power Query Editor were used to separate values based on delimiters to seperate date and time to seperate values to differentiate London and New York time zones.
  
- Trimming Data:

  The TRIM function was used to remove leading, trailing, and extra spaces from text fields. This step ensured cleaner, more consistent data, eliminating unnecessary spaces that could interfere with data processing and formatting, thereby improving the overall quality and accuracy of the dataset.

- Standardization and Adjustments:
  
  Rounding the decimal values to 2 to standardize numeric precision for currency field. The dataset was organized by sorting columns (e.g., by date or price) and filtering data to focus on relevant subsets. These steps ensured uniformity and streamlined the dataset for more reliable analysis and decision-making.

3. Data Visualization:




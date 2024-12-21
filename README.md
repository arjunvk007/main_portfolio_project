  # main_portfolio_project
This section focuses on showcasing proficiency in data analytics, Performed data cleaning, structured datasets, and wrote optimized SQL queries to extract insights. Created interactive Power BI dashboards showcasing trends and answering business questions, to highlight proficiency in data analytics, visualization, and driving data-informed decisions.

# Project 1: HOSPITAL OPERATIONAL MANAGEMENT ANALYSIS​

## About 

The 'Hospital Operational Management Analysis' project integrates SQL and Power BI to analyze hospital data, improve decision-making, and optimize resource utilization. SQL was used to create the database, define attributes, and populate data. Key business insights, related to room utilization, revenue generation, and medicine patterns, were derived through queries. Power BI dashboards were developed to visualize trends, including patient room turnover, department revenues, and prescription distributions, offering actionable strategies to optimize operations, enhance billing processes, and improve patient satisfaction (business questions) to improve the hospital operational performance. This project showcases expertise in data modeling, SQL analysis, and impactful visualizations.

## Steps 

- #### **Creating tables (DDL statements):**
  
1. **Patient Table**: PatientID, FirstName, LastName, DateOfBirth, Gender, Address, PhoneNumber, Email, EmergencyContactName, EmergencyContactPhone

2. **Doctor Table**: DoctorID, FirstName, LastName, Specialization, PhoneNumber, Email, DepartmentID, Availability

3. **Department Table**: DepartmentID, DepartmentName, Location, PhoneExtension

4. **Appointment Table**: AppointmentID, PatientID, DoctorID, DepartmentID, AppointmentDate, AppointmentTime, Status (Scheduled, Completed, Cancelled)

5. **Medical Records Table**: RecordID, PatientID, DoctorID, VisitDate, Diagnosis, TreatmentPlan, Prescription

6. **Prescription Table**: PrescriptionID, RecordID, MedicineID, Dosage, Frequency, Duration

7. **Medicine Table**: MedicineID, MedicineName, Manufacturer, StockQuantity, Price

8. **Billing Table**: BillingID, PatientID, TotalAmount, PaymentStatus (Paid/Unpaid), PaymentDate, PaymentMethod

9. **Staff Table**: StaffID, FirstName, LastName, Role, DepartmentID, PhoneNumber, Email, ShiftHours

10.**Room Table**: RoomID, RoomNumber, DepartmentID, RoomType (General, Private, ICU, etc.), AvailabilityStatus

11.**RoomAssignment Table**: AssignmentID, RoomID, PatientID, AdmissionDate, DischargeDate

- #### **Loading data:**

Used sql queries to populate data

- #### **Created DML queries**
Formulated business questions and gathered insights for the business questions through queries.

**Business Question 1:**

![Business Question 1](https://github.com/arjunvk007/main_portfolio_project/blob/main/Portfolio%20Sql%20%20photos/BQ%201.png)

**Business Question 2:**

![Business Question 2](https://github.com/arjunvk007/main_portfolio_project/blob/main/Portfolio%20Sql%20%20photos/BQ2.png)

**Business Question 3:**

![Business Question 3](https://github.com/arjunvk007/main_portfolio_project/blob/main/Portfolio%20Sql%20%20photos/BQ%203.png)

**Business Question 4:**

![Business Question 4](https://github.com/arjunvk007/main_portfolio_project/blob/main/Portfolio%20Sql%20%20photos/BQ%204.png)

**Business Question 5:**

![Business Question 5](https://github.com/arjunvk007/main_portfolio_project/blob/main/Portfolio%20Sql%20%20photos/BQ%205.png)

**Business Question 6:**

![Business Question 6](https://github.com/arjunvk007/main_portfolio_project/blob/main/Portfolio%20Sql%20%20photos/BQ%206.png)

**Business Question 7:**

![Business Question 7](https://github.com/arjunvk007/main_portfolio_project/blob/main/Portfolio%20Sql%20%20photos/BQ%207.png)

**Business Question 8:**

![Business Question 8](https://github.com/arjunvk007/main_portfolio_project/blob/main/Portfolio%20Sql%20%20photos/BQ%208.png)

**Business Question 9:**

![Business Question 9](https://github.com/arjunvk007/main_portfolio_project/blob/main/Portfolio%20Sql%20%20photos/BQ%209.png)


**Business Question 10:**

![Business Question 10](https://github.com/arjunvk007/main_portfolio_project/blob/main/Portfolio%20Sql%20%20photos/BQ%2010.png)

**Business Question 11:**

![Business Question 11](https://github.com/arjunvk007/main_portfolio_project/blob/main/Portfolio%20Sql%20%20photos/BQ%2011.png)

**Business Question 12:**

![Business Question 12](https://github.com/arjunvk007/main_portfolio_project/blob/main/Portfolio%20Sql%20%20photos/BQ%2012.png)

**Business Question 13:**

![Business Question 13](https://github.com/arjunvk007/main_portfolio_project/blob/main/Portfolio%20Sql%20%20photos/BQ%2013.png)

**Business Question 14:**

![Business Question 14](https://github.com/arjunvk007/main_portfolio_project/blob/main/Portfolio%20Sql%20%20photos/BQ%2014.png)

**Business Question 15:**

![Business Question 15](https://github.com/arjunvk007/main_portfolio_project/blob/main/Portfolio%20Sql%20%20photos/BQ%2015.png)

- #### **Connected the data in SQL to powerBI, to create dashboard**

-  #### **Charts used:**
  
1. **Bar Chart:**

No. of Patients by Room Type (ICU, General, Private)
Total Revenue by Department (General Surgery, Orthopedics, Neurology, etc.)

2. **Column Chart:**
Turnover Rate (Admissions/Discharges) by Room Type

3. **Pie Chart:**

Medicine Prescription Count (Simvastatin, Metformin, Paracetamol, etc.)

4. **Stacked Bar Chart:**

Average Patient Count by Room

5. **Radar Chart:**

Number of Appointments by Department (Maternity, General Surgery, Neurology, etc.)

6. **Table:**

Room Type and Average Stay
ICU Prescribed Medicines and Count

7. **KPI Cards:**

Total Appointments (244K)
Number of Unpaid Patients (199)
Doctor with Most Patients (Alice Brown)

**Dashboard:**

![Visualization](https://github.com/arjunvk007/main_portfolio_project/blob/main/Portfolio%20Sql%20%20photos/Visualization.png)

### **Insights:**


The analysis highlights key hospital operational insights and strategies. ICU rooms show the highest utilization (48.87%) and turnover, while private rooms are underutilized (17.88%), suggesting opportunities for marketing or pricing adjustments. General Surgery and Orthopedics contribute the most revenue (~$1.1M), while Dermatology and Emergency departments underperform. Medicine prescriptions are balanced, with frequent ICU drugs like Amoxicillin and Aspirin requiring stock monitoring and supplier negotiations. 

### **Strategies:**

Key strategies include optimizing room utilization by promoting private rooms and reallocating ICU resources to manage high demand. Enhance billing processes with automated reminders and flexible payment plans to reduce unpaid bills. Focus on high-revenue departments like General Surgery and Orthopedics by allocating more resources. Improve medicine management through bulk supplier negotiations for high-demand drugs. Expand ICU/general room capacities and implement patient feedback systems and loyalty programs to enhance experiences and retention.

### **Conclusion**

In 'Hospital Operational Management Analysis' project effectively utilized SQL for database creation, data entry, and generating key business insights through optimized queries. Power BI was used to develop dynamic visualizations, including bar charts, pie charts, and KPIs, to showcase trends in room utilization, revenue generation, and prescription patterns. The project provided actionable strategies to optimize resource allocation, improve billing processes, and enhance patient satisfaction.  This project demonstrated the effective use of technologies to derive actionable business strategies, showcasing strong skills in data analysis, visualization, and informed decision-making.

# Project 2: From Boom to Mainstream: Analyzing the Growth Trajectory of Cryptocurrency

## **About**

The project focuses on analyzing the historical trends, growth factors, and predictive trajectories of the cryptocurrency market. With growing interest and volatility in cryptocurrencies, the study aims to identify the key drivers of adoption, price changes, and forecast future market trends.

The analysis explores primary factors influencing cryptocurrency growth, price trends, market cap movements, and supply patterns for the top 10 cryptocurrencies (BTC, ETH, XRP, USDC, etc.). The dataset spans 2009–2024, with detailed insights from 2019–2023, incorporating attributes such as Price, Market Cap, Supply, and Volume.

For data preparation, initial inspections and cleaning were performed in Excel to ensure formatting consistency and handle missing values. Multiple Excel files were combined into a structured format, ensuring time-series data readiness. Using Power BI, the finalized dataset was visualized to uncover trends, anomalies, and patterns, providing actionable insights into cryptocurrency market behavior and predictions for the next five years.

## **Steps**

1. ### **Data Collection and Challenges**

The dataset focuses on the top 10 cryptocurrencies by market cap, based on CoinMarketCap rankings as of November 1, 2024. Missing data for certain cryptocurrencies was replaced with the next available asset to maintain consistency. The primary attributes include Price, Market Cap, Current Supply, and Volume, with data provided in both CSV and Excel formats. The dataset spans 2009–2024, with a focused analysis on the years 2019–2023 for detailed trend insights.

Data collection posed challenges as no single source provided complete data for all attributes, requiring integration from multiple sources and extensive cross-referencing to ensure accuracy. Time-based price data presented specific issues, with the Principal Market Price missing for some assets. To address this, alternative benchmarks were used: 4:00 pm New York Price (aligned with U.S. market close) and 11:00 am London Price (covering Asian and European trading). However, these alternatives may miss daily highs/lows, limiting volatility insights..

2. ### **Data Cleaning:**

-  Date and Time Formatting: Utilized Power Query to split combined date-time columns into standardized date-only formats for consistency.
  
-  Table Formatting and Data Type Standardization: Enhanced readability by adding table borders and ensuring uniform data types across all columns.
  
-  Precision Standardization: Applied rounding to ensure numeric columns maintained a precision of two decimal places.
  
-  Duplicate Check: Verified datasets to confirm the absence of duplicate records, ensuring data accuracy.
  
-  Null Value Handling: Filled missing values in critical columns to maintain dataset continuity and reliability for analysis. To address missing data, interpolation estimated values for SOL based on trends, while median imputation filled minor gaps in XRP and ADA. BNB was removed due to insufficient data, and critical time rows were dropped to maintain time series integrity. These techniques ensured data quality and consistency.
  
3. ### **Data Visualization:**

- ### **Overview**

![Overview](https://github.com/arjunvk007/main_portfolio_project/blob/main/Portfolio%20Sql%20%20photos/Overview.png)

Designed an interactive dashboard to explore cryptocurrency market dynamics, focusing on growth potential, market capitalization, and price-supply relationships for key tokens (e.g., BTC, ETH, ADA).

Key Functionalities Implemented:

--  **Multi-Visual Representation:**

**Radar Chart:** Highlights top cryptocurrencies by market cap, providing a comparative view of their market dominance.

**Line Charts:** Show price trends versus supply for London and New York markets.

**Stacked Area Chart:** Visualizes the market cap distribution of all tracked cryptocurrencies over time.

--  **Interactive Features:**

**Token Selection:** Users can toggle between top-performing and high-growth tokens.

**Time Slider:** Allows filtering data between 2019 and 2024 for dynamic trend analysis.

--  **Advanced Data Analysis:**

Combined price, supply, and market cap data to create insights on regional and global cryptocurrency dynamics.

Highlighted discrepancies between London and New York markets, offering localized insights.

Used Text box to show the predicted top 3 cryptocurrencies in the present and future from the analysis.

--  **Design Enhancements:**

A clean, dark theme ensures a modern and professional look.

Intuitive layout simplifies navigation for quick decision-making.

- ### Price Trends: London vs. New York

![Price Trends](https://github.com/arjunvk007/main_portfolio_project/blob/main/Portfolio%20Sql%20%20photos/Price%20trends.png)

Developed a comprehensive visualization of cryptocurrency price trends, comparing 11:00 AM London and 4:00 PM New York market data across multiple tokens (e.g., BTC, ETH, ADA).

Key Functionalities Implemented:

--  **Data Aggregation:** Aggregated the price data of each of the top 10 cryptocurrencies to use as values and plot in the chart for comparison.

--  **Time-Series Visualization:** Created dual-line charts to compare price trends for each token, enabling clear and actionable insights.

--  **Trend Line:** Used trend lines to display trends for multiple tokens simultaneously, to predict future price trends to currencies.

--  **Interactive Features:** Incorporated filtering, zooming, and panning for enhanced usability and deeper analysis.

--  **Anomaly Detection:** Identified anomalies, such as price drops in stablecoins, using statistical methods and trendline analysis.

--  **User-Friendly Design:** Applied a clean, dark theme to enhance readability and ensure a professional look.

- ### **Market Cap Contributions Over Time**

![Market Caps](https://github.com/arjunvk007/main_portfolio_project/blob/main/Portfolio%20Sql%20%20photos/Market%20Cap.png)

Developed the visualization to track the market capitalization contributions of key cryptocurrencies (e.g., BTC, ETH, ADA) over time, showcasing trends and insights from 2019 to 2024.

Key Functionalities Implemented:

--  **Data Aggregation:** Collected and aggregated market cap data for multiple cryptocurrencies, ensuring accuracy and consistency over time.

--  **Time-Series Visualization:** Designed line charts for each token to display their market cap growth and fluctuations across years.

--  **Multi-Panel Layout:** Organized the dashboard into separate subplots, allowing comparative analysis of each cryptocurrency's market cap trends.

--  **Interactive Features:** Added a time slider to filter data for custom date ranges.

--  **Anomaly Detection:** Highlighted significant spikes and dips, such as DOGE’s 2021 surge and USDC’s post-2022 stability.

--  **User-Friendly Design:** Applied a clean, dark theme to enhance readability and ensure a professional look.

## **Conclusion**

The analysis of the top cryptocurrencies through price trends, market capitalization, and growth trajectories has provided valuable insights into the evolving dynamics of the cryptocurrency market. By leveraging data visualization, the study identified dominant players, stablecoins, and promising altcoins, shedding light on their potential for future growth. The integration of time-based benchmarks and robust data cleaning methods ensured accuracy and consistency in the dataset, enabling informed predictions.

# Project 3: Cyclistic Bike Share Analysis

## About

This case study examines the differing usage patterns between casual riders and annual members of Cyclistic’s bike-share services, with the goal of converting casual riders into annual members. Microsoft Excel was used for data cleaning, including standardizing formats, adding columns like duration and day_of_week, addressing missing data, and identifying duplicate entries. Key functions such as mean, median, and mode calculations, along with the CountIF function, were employed to determine the total number of casual and member riders. Pivot tables were leveraged to analyze average ride durations for each group, while bar charts were created to visualize usage trends by user type and day of the week.

## Steps

1. ### **Data Collection and Challenges**

The data provided with the case study was distributed across multiple monthly files for 2023 and 2024, presenting a significant challenge. The data cleaning process was time-consuming, as it required careful review and processing of each individual file. Aggregating the data for analysis involved performing calculations separately for each file. To streamline usage and improve accessibility, all the data needed to be consolidated into a single comprehensive file, ensuring efficient analysis and easier access.

2. ### **Data Cleaning**

- Changed Datatype: Converted date and time formats to a standard date format.

- Removed Duplicates: Used the "Remove Duplicates" option to eliminate redundant entries.

- Text Standardization: Applied the PROPER function for consistent letter casing and TRIM to remove unnecessary spaces.

- Day Identification: Used the WEEKDAY function to determine the day of the week for each ride.

- Filling Missing Data: Handled empty cells using “Find and Select” → “Go to Special” → “Blanks” and filled them with NA values.

- Sorting and Filtering: Identified blank cells and data irregularities using sort and filter options.

- Value Conversion: Converted text to numerical values using the VALUE function to resolve datatype errors.

- Error Handling: Used IFERROR to replace errors (e.g., #VALUE) with NA.

- Formatting: Improved readability by adjusting headings and adding gridlines.

- Proper Naming: Followed consistent naming conventions for cleaned datasets.

3. ### **Analyze**

- Mean, median, and mode functions were applied to analyze ride durations and the days of the week.

- The CountIF function was employed to determine the total number of casual riders and subscribed members.

- Pivot tables were utilized to calculate the average ride duration for each membership group, analyze weekday distributions by membership type, and count the total rides for each day of the week. Bar graphs and pie charts were generated from the pivot table data to visually represent these metrics. These processes facilitated the identification of patterns, anomalies, and outliers, ensuring the dataset’s reliability for analytical purposes. Clean and well-structured data enabled accurate insights into trends, customer behaviors, and operational dynamics, enhancing data visualization and supporting predictive modeling. This systematic approach improved data quality, empowering strategic planning and enabling informed decision-making for optimized outcomes.

Examples:

![202308](https://github.com/arjunvk007/main_portfolio_project/blob/main/Portfolio%20Sql%20%20photos/Analyze%20202308.png)

![202309](https://github.com/arjunvk007/main_portfolio_project/blob/main/Portfolio%20Sql%20%20photos/Analysis%20202309.png)

![202310](https://github.com/arjunvk007/main_portfolio_project/blob/main/Portfolio%20Sql%20%20photos/202310.png)

4. ### **Data Visualization**

**Cyclistic Bike Share Analysis 2023**

![Cyclistic Bike Share Analysis 2023](https://github.com/arjunvk007/main_portfolio_project/blob/main/Portfolio%20Sql%20%20photos/Bike%20share%20Analysis%202023.png)

**1. Graphs:**
   
**Line Charts:**

Used to display the number of ride members (Casual and Members) by bike type (Classic and Electric) over months (September to December).

Show trends in bike usage between Casual and Membership users.

**KPI Cards:**

Highlights key metrics like:

Average duration of rides for each month.

Total number of members for September, October, November, and December.

Easy to track the overall trend of participation and average time spent.

**2. Filters:**
   
Dropdown filters for months and user types (Casual or Member) enable dynamic interactivity.

Allows users to focus on specific groups or periods for better insight.

**3. Insight Generation:**

Feedback/Observation Section: Summarizes key trends (e.g., shift from classic bikes to electric bikes, seasonal effects on bike usage).

**Cyclistic Bike Share Analysis 2024 Q1**

![Cyclistic Bike Share Analysis 2024 Q1](https://github.com/arjunvk007/main_portfolio_project/blob/main/Portfolio%20Sql%20%20photos/Bike%20share%20Analysis%202024%20Q1.png)

**1. Graphs:**
   
Line Charts:

Similar functionality as the first image, comparing Casual and Membership usage by bike type.

Covers January to April of 2024.

KPI Cards:

Displays metrics such as:

Total number of members for January, February, March, and April.

Average daily usage for each month.

**3. Filters:**
   
Monthly and user-type filters are included to analyze different periods and user categories.

**4. Insight Generation:**
   
Feedback Section:

Highlights patterns, such as the decline in bike usage due to weather and the gradual recovery in Q1.

Notes increased electric bike demand in April.

**Cyclistic Bike Share Analysis 2024 Q2**

![Cyclistic Bike Share Analysis 2024 Q2](https://github.com/arjunvk007/main_portfolio_project/blob/main/Portfolio%20Sql%20%20photos/Bike%20share%20Analysis%202024%20Q2.png)

**1. Graphs:**
   
Line Charts:

Displays bike usage trends for June and July.

The data granularity appears finer, possibly on an hourly or daily basis.

KPI Cards:

Highlights the number of members for June and July.

**2. Filters:**
   
Filters for specific months and user types allow targeted analysis.

Focus remains on Casual and Membership categories.

**3. Insight Generation:**
   
Feedback Section:

Reiterates 2023 end-of-year patterns.

Observes seasonal trends in membership and bike usage.

## Conclusion

The analysis of Cyclistic’s bike-share data highlights distinct usage patterns between casual riders and annual members, influenced by seasonal and bike-type trends. Casual riders prefer leisure activities, with higher weekend usage and a growing shift toward electric bikes. In contrast, annual members demonstrate consistent weekday usage, indicating a focus on commuting. Casual riders tend to have longer ride durations, particularly during leisure periods, while annual members exhibit shorter, more frequent rides. Seasonal trends show reduced ridership in winter and recovery in spring and summer, emphasizing the need for adaptive strategies.

Key recommendations include:

- **Weekend Promotions for Casual Riders:** Offer discounts or special packages during weekends to align with casual riders' behavior and encourage higher usage.

- **Highlight Membership Benefits:** Promote membership plans tailored to frequent riders, emphasizing cost savings and convenience, especially for commuters.

- **Seasonal Flexibility in Memberships:** Introduce short-term or flexible membership plans to attract casual riders during warmer months, fostering engagement and eventual conversion to annual memberships.

- **Increased Availability of Electric Bikes:** Scale up the availability and promotion of electric bikes, as their popularity continues to rise, particularly among casual users.

By implementing these targeted strategies, Cyclistic can effectively bridge the gap between casual and annual riders, improve user retention, and drive profitability, positioning itself for sustainable business growth in the competitive bike-share industry.

# Users
* **Name** - text
* **Phone_Number** - text
* **Language** - text
* **Issue** - text
* **Issue_Desc** - text
* **Availability** - timestamp with timezone
* **UserID** - PKEY integer

# Volunteers
* **Vol_ID** - PKEY integer
* **Name** text
* **Language** text
* **Start_Time** timestamp with timezone
* **Stop_Time** timestamp with timezone

# Appointments
* **Start_Time** timestamp with time zone
* **End_Time** timestamp with time zone
* **Name** text
* **Volunteer_Name** text
* **Issue** text
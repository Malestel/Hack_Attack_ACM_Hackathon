# API Documentation
## Appointments
*HTTP GET* `/api/appointment/{id}`

**Response** (200)
```json
[
    {
        "insert":"stuff",
        "here":"for",
        "good":"return"
    }
]
```
**Response** (404)
```
Appointment not found
```
-----------
*HTTP GET* `/api/appointment`

**Response** (200)
```json
    [
        {
            "insert":"stuff",
            "here":"for",
            "good":"return"
        },
        {
            "insert":"stuff",
            "here":"for",
            "good":"return"
        },
        ...
    ]
```
-----------
*HTTP POST* `/api/appointment`

**Request**
```json
{
    "Start_Time": timestamp-tz,
    "End_Time": timestamp-tz,
    "User_ID": integer (Users Key),
    "Volunteer_ID": integer (Volunteers Key)
}
```
**Response** (200)
```json
{
    "location":"/api/appointment/{id}"
}
```
-----------
*HTTP DELETE* `/api/appointment/{id}`

*Response* (200)
```
"OK"
```
*Response* (404)
```
Appointment Not Found
```
-----------
## Users
*HTTP GET* `/api/user/{id}`

# Users
* **Name** - text
* **Phone_Number** - text
* **Language** - text
* **Issue** - text
* **Issue_Desc** - text
* **Availability** - timestamp with timezone
* **UserID** - PKEY integer
**Response** (200)
```json
[
    {
        "Name": string,
        "Phone_Number": string,
        "Language":string,
        "Issue": string,
        "Issue_Desc": string,
        "Availability": timestamp-tz
    }
]
```
-----------
*HTTP GET* `/api/appointment`

**Response** (200)
```json
    [
        {
            "Name": string,
            "Phone_Number": string,
            "Language":string,
            "Issue": string,
            "Issue_Desc": string,
            "Availability": timestamp-tz
        },
        {
            "Name": string,
            "Phone_Number": string,
            "Language":string,
            "Issue": string,
            "Issue_Desc": string,
            "Availability": timestamp-tz
        },
        ...
    ]
```
-----------
*HTTP POST* `/api/appointment`

**Request**
```json
{
    "Name": string,
    "Phone_Number": string,
    "Language":string,
    "Issue": string,
    "Issue_Desc": string,
    "Availability": timestamp-tz
}
```
**Response** (200)
```json
{
    "location":"/api/appointment/{id}"
}
```
-----------
*HTTP DELETE* `/api/appointment/{id}`

*Response* (200)
```
"OK"
```
*Response* (404)
```
Appointment Not Found
```

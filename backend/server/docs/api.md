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
*HTTP GET* `/api/user`

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
*HTTP POST* `/api/user`

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
    "location":"/api/user/{id}"
}
```
-----------
*HTTP DELETE* `/api/user/{id}`

*Response* (200)
```
"OK"
```
*Response* (404)
```
User Not Found
```
-----------
## Volunteers
*HTTP GET* `/api/user/{id}`

```json
[
    {
        "Name": string,
        "Language":string,
        "Start_Time": timestamp-tz,
        "Stop_Time": timestamp-tz
    }
]
```
-----------
*HTTP GET* `/api/volunteer`

**Response** (200)
```json
    [
        {
            "Name": string,
            "Language":string,
            "Start_Time": timestamp-tz,
            "Stop_Time": timestamp-tz
        },
        {
            "Name": string,
            "Language":string,
            "Start_Time": timestamp-tz,
            "Stop_Time": timestamp-tz
        },
        ...
    ]
```
-----------
*HTTP POST* `/api/volunteer`

**Request**
```json
{
    "Name": string,
    "Language":string,
    "Start_Time": timestamp-tz,
    "Stop_Time": timestamp-tz
}
```
**Response** (200)
```json
{
    "location":"/api/volunteer/{id}"
}
```
-----------
*HTTP DELETE* `/api/volunteer/{id}`

*Response* (200)
```
"OK"
```
*Response* (404)
```
Volunteer Not Found
```

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
    "insert":"stuff",
    "here":"for",
    "good":"return"
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

# Ticket Booking API

## Features:

```
- An endpoint to book a ticket using a user’s name, phone number, and timings.
- An endpoint to update a ticket timing.
- An endpoint to view all the tickets for a particular time.
- An endpoint to delete a particular ticket.
- An endpoint to view the user’s details based on the ticket id.
- Marks a ticket as expired if there is a diff of 8 hours between the ticket timing and current time.
- For a particular timing, a maximum of 20 tickets can be booked.
- REST API
- Database : SQLAlchemy
- Automatically delete all the tickets which are expired or not valid for the current time.
- Test cases included for all the endpoints.

```

## Dependencies

- Python
- Flask
- flask_sqlalchemy

## Installation

- **cd** into project root
- Creating a virtual environment is recommended. Following command can be used to create a virtual environment.

```
python -m venv env
```

- Install all the requirements using the below command.

```
pip install -r requirements.txt
```

## Usage

Run the flask server as follows

```
flask run
OR
python3 app.py
```

This will setup a local server on http://127.0.0.1:5000<br />
Following routes are allowed on the API

To run Unit Tests:
```
python3 test.py
```

- **GET** / is used to **get all tickets**, **get user details**, **get tickets for particular timing**
- **POST** is used to **book ticket**
- **DELETE** is used to **delete a ticket**

### Booking a ticket
Ticket can be booked by giving a POST request to ` /book ` route with following parameters.<br />
The format for timing is HH:MM. For example, to be book ticket for 7:00PM, the timing parameter will be 19:00
```
{
    "user_name": "Username",
    "phone": "Phone Number",
    "timings": "Show time to be booked"
}
```
An **expiresAt** key is attached to every successful booking which is the time 8 hours from the ticket time. The ticket is automatically marked expired and deleted when current time reaches expiresAt.
#### Example
[]("./images/ticketBooking.png")


### Updating ticket timing
Ticket timing can be updated by giving a GET request to ` ticket/<id> ` route without any parameters.<br />

#### Example
[]("./images/deleteTicket.png")

### Get ticket details by ID
To get detail of a particular ticket, give a GET request to ` ticket/<id> ` route.<br />
```
{
    "ticket_id": "ID of the ticket to be updated",
}
```
#### Example
[]("./images/getUserDetailFromTicketID.png")

### Get ticket details by Timing
To get detail of all the tickets for particular time, give a GET request to ` /tickets/<time> ` route.<br />

#### Example
[]("./images/getAllTicketsOnParticularTime.png")

### Deleting a ticket
Tickets can be deleted by giving a DELETE request to ` /ticket/<id> ` route with following parameters.<br />

#### Example
[]("./images/deleteTicket.png")

## Testing
Unit tests have been written and tested for all these cases. All the test related code can be found in ` test.py ` file. Below is the test report.<br/>
<br />
[]("./images/unitTestResult.png")

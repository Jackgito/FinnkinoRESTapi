## Movie Ticket Booking System

This project implements a simple movie ticket booking system with two components:

- **booking_client.py:** This Python script acts as the client application, allowing users to view available shows and book tickets.
- **theater_api.py:** This Flask application implements the server-side API responsible for managing show information and handling booking requests.

**Features:**

- **Client:**
    - View available shows
    - Book tickets for a specific show
- **Server:**
    - Expose API endpoints for show information and booking
    - Manage show information and bookings

**Requirements:**

- Python 3.x
- requests library (client)
- Flask web framework (server)

**Installation:**

1. Open a terminal window.
2. Install both libraries using pip:

```bash
pip install requests Flask
```

**Running:**

1. **Server:**
    - Start the server by running `python theater_api.py` in the root directory.
2. **Client:**
    - Run the script `python booking_client.py` in the root directory. This will:
        - List available shows
        - Prompt for user input (show ID, number of tickets, user ID)
        - Attempt to book tickets and display the result

**API:**

- `/api/shows`: Get list of available shows (GET) (theater_api.py)
- `/api/bookings`: Book tickets (POST) (theater_api.py)
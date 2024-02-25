import requests

BASE_URL = "http://127.0.0.1:5000/api"

def get_available_shows():
    url = f"{BASE_URL}/shows"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch available shows. Status code: {response.status_code}")
        return None

def book_ticket(show_id, num_tickets, user_id):
    url = f"{BASE_URL}/bookings"
    data = {
        "show_id": show_id,
        "num_tickets": num_tickets,
        "user_id": user_id
    }

    response = requests.post(url, json=data)

    if response.status_code == 201:
        print(f"Booking successful! Booking ID: {response.json()['booking_id']}")
    else:
        print(f"Failed to book tickets. Status code: {response.status_code}")

# Example usage
available_shows = get_available_shows()

if available_shows:
    for show in available_shows['shows']:
        print(f"Show ID: {show['id']}, Movie: {show['movie']}, Time: {show['time']}")

    show_id = int(input("Enter the Show ID to book tickets: "))
    num_tickets = int(input("Enter the number of tickets: "))
    user_id = input("Enter your user ID: ")

    book_ticket(show_id, num_tickets, user_id)

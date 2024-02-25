from flask import Flask, jsonify, request, abort

app = Flask(__name__)

shows = [
    {"id": 1, "movie": "Inception", "time": "2024-02-25T18:00:00"},
    {"id": 2, "movie": "The Matrix", "time": "2024-02-25T20:30:00"},
]

bookings = []

@app.route('/api/shows', methods=['GET'])
def get_shows():
    return jsonify({"shows": shows})

@app.route('/api/bookings', methods=['POST'])
def book_ticket():
    if not request.json or 'show_id' not in request.json or 'num_tickets' not in request.json or 'user_id' not in request.json:
        abort(400)

    show_id = request.json['show_id']
    num_tickets = request.json['num_tickets']
    user_id = request.json['user_id']

    show = next((s for s in shows if s['id'] == show_id), None)

    if not show:
        abort(404, f"Show with ID {show_id} not found.")

    if num_tickets <= 0:
        abort(400, "Number of tickets should be greater than 0.")

    if num_tickets > 10:
        abort(400, "You cannot book more than 10 tickets at once.")

    # Assume a simple booking ID for demonstration purposes
    booking_id = len(bookings) + 1
    booking = {"booking_id": booking_id, "show": show, "num_tickets": num_tickets, "user_id": user_id}
    bookings.append(booking)

    return jsonify({"booking_id": booking_id}), 201

if __name__ == '__main__':
    app.run(debug=True)

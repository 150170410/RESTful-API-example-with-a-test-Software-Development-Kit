from flask import Flask, jsonify, abort, make_response, request


app = Flask(__name__)

# Mock database
clients = [
    {
        'id': 1,
        'first_name': 'Bob',
        'last_name': 'Clark',
        'phone_number': '123-123-1234',
        'email': 'bob@example.com'
    },
    {
        'id': 2,
        'first_name': 'Matt',
        'last_name': 'Robertson',
        'phone_number': '125-125-1235',
        'email': 'matt@example.com'
    }
]


@app.route('/application/api/clients', methods=['GET'])
def get_clients():
    return jsonify({'clients': clients})


@app.route('/application/api/clients/<int:client_id>', methods=['GET'])
def get_client(client_id):
    client = [client for client in clients if client['id'] == client_id]
    if len(client) == 0:
        abort(404)
    return jsonify({'client': client[0]})


@app.route('/application/api/clients', methods=['POST'])
def create_client():
    if not request.json:
        abort(400)
    client = {
        'id': clients[-1]['id'] + 1,
        'first_name': request.json.get('first_name'),
        'last_name': request.json.get('last_name'),
        'phone_number': request.json.get('phone_number'),
        'email': request.json.get('email')
    }
    clients.append(client)
    return jsonify("Successfully added client")


@app.route('/application/api/clients/<int:client_id>', methods=['PUT'])
def update_client(client_id):
    client = [client for client in clients if client['id'] == client_id]

    client[0]['first_name'] = request.json.get('first_name', client[0]['first_name'])
    client[0]['last_name'] = request.json.get('last_name', client[0]['last_name'])
    client[0]['phone_number'] = request.json.get('phone_number', client[0]['phone_number'])
    client[0]['email'] = request.json.get('email', client[0]['email'])

    # return jsonify({'client': client[0]})
    return jsonify("Successfully updated client")


@app.route('/application/api/clients/<int:client_id>', methods=['DELETE'])
def delete_client(client_id):
    client = [client for client in clients if client['id'] == client_id]
    if len(client) == 0:
        abort(404)
    clients.remove(client[0])

    return jsonify("Successfully deleted client")


@app.errorhandler(404)
def not_found_error(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)


if __name__ == "__main__":
    app.run(debug=True)

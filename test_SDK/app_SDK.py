import requests
import json

local_host = 'http://127.0.0.1:5000/'

class ClientInterface:
    def get_clients(self):
        """
        Retrieves all clients in database with a GET request.
        """

        url = local_host + 'application/api/clients'
        response_data = requests.get(url)

        if response_data.ok:
            data = json.loads(response_data.content)
            for key, value in data.items():
                print(key, value)
        else:
            response_data.raise_for_status()

    def get_client(self, client_id):
        """
        Retrieves a specific client from database with provided client id
        with a GET request.

        :param client_id: Value of the client id the user wants to delete
        """

        url = local_host + 'application/api/clients/' + str(client_id)
        response_data = requests.get(url)

        if response_data.ok:
            data = json.loads(response_data.content)
            for key, value in data.items():
                print(key, value)
        else:
            response_data.raise_for_status()

    def create_client(self, first_name, last_name, phone_number, email):
        """
        Creates a new client in the database with a POST request.

        :param first_name: First name of client to be added
        :param last_name: Last name of client to be added
        :param phone_number: Phone number of client to be added
        :param email: Email address of client to be added
        """

        url = local_host + 'application/api/clients'
        client_data = {}
        client_data['first_name'] = str(first_name)
        client_data['last_name'] = str(last_name)
        client_data['phone_number'] = str(phone_number)
        client_data['email'] = str(email)
        response_data = requests.post(url, json=client_data)

        if response_data.ok:
            data = json.loads(response_data.content)
            print(data)
        else:
            response_data.raise_for_status()

    def update_client(self, client_id, first_name=None, last_name=None,
                      phone_number=None, email=None):
        """
        Updates an existing client's data with a PUT request.

        :param client_id: Specified id of client to be modified
        :param first_name: Updated first name of client
        :param last_name: Updated last name of client
        :param phone_number: Updated phone number of client
        :param email: Updated email address of client
        """

        url = local_host + 'application/api/clients/' + str(client_id)
        client_data = {}
        if first_name != None:
            client_data['first_name'] = first_name
        if last_name != None:
            client_data['last_name'] = last_name
        if phone_number != None:
            client_data['phone_number'] = phone_number
        if email != None:
            client_data['email'] = email
        response_data = requests.put(url, json=client_data)

        if response_data.ok:
            data = json.loads(response_data.content)
            print(data)
        else:
            response_data.raise_for_status()

    def delete_client(self, client_id):
        """
        Deletes an existing client from database with a DELETE request.

        :param client_id: Id of existing client to be deleted
        """

        url = local_host + 'application/api/clients/' + str(client_id)
        response_data = requests.delete(url)

        if response_data.ok:
            data = json.loads(response_data.content)
            print(data)
        else:
            response_data.raise_for_status()

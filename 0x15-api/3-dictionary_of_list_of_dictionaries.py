#!/usr/bin/python3

"""
Using what you did in the task #0, extend your Python script to export data in
the JSON format.
"""

import json
import requests

URL = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    user_response = requests.get('{}/users'.format(URL)).json()
    todo_response = requests.get('{}/todos'.format(URL)).json()
    data = {}

    for user in user_response:
        id = user.get('id')
        username = user.get('username')

        todo = list(filter(lambda x: x.get('userId') == id, todo_response))
        user = list(map(lambda x: {
            'username': username,
            'task': x.get('title'),
            'completed': x.get('completed')
        }, todo))

        data['{}'.format(id)] = user

    with open('todo_all_employees.json', 'w') as filename:
        json.dump(data, filename)

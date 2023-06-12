#!/usr/bin/python3

"""
Using what you did in the task #0, extend your Python script to export data in
the json format.
"""

import json
import re
import requests
import sys


URL = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            user_response = requests.get('{}/users/{}'.format(URL, id)).json()
            todo_response = requests.get('{}/todos'.format(URL)).json()
            username = user_response.get('username')

            todo = list(filter(lambda x: x.get('userId') == id, todo_response))

            with open('{}.json'.format(id), 'w') as filename:
                data = list(map(lambda x: {
                    "task": x.get("title"),
                    "completed": x.get("completed"),
                    "username": username
                }, todo))

                data = {"{}".format(id): data}
                json.dump(data, filename)

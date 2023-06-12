#!/usr/bin/python3

"""
A script to request info from a REST API. The todo list progress of the
employee will be displayed
"""

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
            username = user_response.get('name')

            todo = list(filter(lambda x: x.get('userId') == id, todo_response))
            todo_total = len(todo)
            completed = list(filter(lambda x: x.get('completed'), todo))
            completed_total = len(completed)

            print('Employee {} is done with tasks ({}/{}):'
                  .format(username, completed_total, todo_total))

            for complete_task in completed:
                print('\t {}'.format(complete_task.get('title')))

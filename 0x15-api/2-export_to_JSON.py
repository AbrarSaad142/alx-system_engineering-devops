#!/usr/bin/python3
"""For a given employee ID, returns information about
their TODO list progress"""

import json
import requests
import sys

if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"

    user_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    params = {"userId": user_id}
    todos_response = requests.get(url + "todos", params=params)
    todos = todos_response.json()
    data_to_export = {user_id: []}
    for todo in todos:
        task_info = {"task": todo.get("title"),
                     "completed": todo.get("completed"),
                     "username": user.get("username")}
        data_to_export[user_id].append(task_info)
    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)

#!/usr/bin/python3
"""For a given employee ID, returns information about
their TODO list progress"""

import json
import requests

if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"

    users = requests.get(url + "users").json()
    data_to_export = {}
    for user in users:
        user_id = user["id"]
        todos_response = requests.get(url + f"todos?userId={user_id}")
        todos = todos_response.json()
        data_to_export[user_id] = []
        for todo in todos:
            task_info = {"task": todo.get("title"),
                         "completed": todo.get("completed"),
                         "username": user.get("username")}
            data_to_export[user_id].append(task_info)
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)

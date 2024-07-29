#!/usr/bin/python3
""" gather data from an API """
import requests
import sys


def get_data(employee_id):
    try:
        user_url = (
            "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
        )
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        user_data = user_response.json()

        employee_name = user_data.get("name")

        todo_url = (
            "https://jsonplaceholder.typicode.com/todos?userId={}".format(
                employee_id)
        )
        todo_response = requests.get(todo_url)
        todo_response.raise_for_status()
        todo_data = todo_response.json()

        total_tasks = len(todo_data)
        completed = [task for task in todo_data if task.get("completed")]
        num_of_completed = len(completed)

        print("Employee {} is done with tasks({}/{}):"
              .format(employee_name, num_of_completed, total_tasks))
        for task in completed:
            print("\t {}".format(task.get('title')))
    except requests.exceptions.RequestException as e:
        pass


if __name__ == '__main__':
    employee_id = sys.argv[1]

    if not employee_id.isdigit():
        sys.exit()

    get_data(int(employee_id))

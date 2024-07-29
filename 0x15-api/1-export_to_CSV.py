#!/usr/bin/python3
""" gather data from an API """
import requests
import sys
import csv


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

            filename = "{}.csv".format(employee_id)
            with open(filename, mode='w', newline='') as csv_file:
                fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                              "TASK_TITLE"]
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

                writer.writeheader()
                for task in todo_data:
                    writer.writerow({
                        "USER_ID": employee_id
                        "USERNAME": employee_name
                        "TASK_COMPLETED_STATUS": task.get("completed"),
                        "TASK_TITLE": task.get("title")
                    })
    except requests.exceptions.RequestException as e:
        pass


if __name__ == '__main__':
    employee_id = sys.argv[1]

    if not employee_id.isdigit():
        sys.exit()

    get_data(int(employee_id))

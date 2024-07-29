#!/usr/bin/python3
""" gather data from an API """
import csv
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

        filename = "{}.csv".format(employee_id)
        with open(filename, mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

            for task in todo_data:
                writer.writerow({
                    employee_id,
                    employee_name,
                    task.get("completed"),
                    task.get("title")
                })
    except requests.exceptions.RequestException as e:
        pass


if __name__ == '__main__':
    employee_id = sys.argv[1]

    if not employee_id.isdigit():
        sys.exit()

    get_data(int(employee_id))

#!/usr/bin/python3
# csv exported
import csv
from requests import get
from sys import argv


def csvWrite(user):
    """ Writing to csv """
    data = get('https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        user)).json()
    name = get('https://jsonplaceholder.typicode.com/user/{}'.format(
        user)).json().get('username')
    employee_data = open('{}.csv'.format(user), 'w')
    seawrite = csv.writer(employee_data, quoting=csv.QUOTE_ALL)
    for line in data:
        linemate = [line.get('used_Id'), name,
                    line.get('completed'), line.get('title')]
        seawrite.writerow(linemate)
    employee_data.close()
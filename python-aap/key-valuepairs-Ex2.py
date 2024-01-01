import csv
import os

csv_file_path = 'dictionary_info.csv'


if not os.path.isfile(csv_file_path):
   
    with open(csv_file_path, 'w', newline='') as csv_file:
        header = ['First name', 'Last name', 'Job title', 'Company']
        csv_writer = csv.DictWriter(csv_file, fieldnames=header)
        csv_writer.writeheader()

user_info = {}

user_info['First name'] = input("Enter your first name: ")
user_info['Last name'] = input("Enter your last name: ")
user_info['Job title'] = input("Enter your job title: ")
user_info['Company'] = input("Enter your company: ")

with open(csv_file_path, 'a', newline='') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=user_info.keys())

    csv_writer.writerow(user_info)

print("Information has been written to the CSV file.")

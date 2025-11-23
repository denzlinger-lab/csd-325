# Abram Denzlinger
# November 19, 2025
# 8.2 - json practice

# This program reads data from a json file
# and prints it in a specified format.
# It adds a new record, indicates which records
# are existing and which are new, and then
# prompts the user via GUI pop up to save or
# discard the changes.

import tkinter as tk
from tkinter import messagebox
import json

"""
# reads data from json file
# returns a list of dictionaries, or an empty list
# if file missing or invalid
"""
def load_students_from_json():
    file_path = "students.json"
    try:
        with open(file_path, 'r') as file:
            class_list = json.load(file)
        return class_list
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from the file '{file_path}'. Check the file format.")
        return None

def save_students_to_json(students_data_list):
    """
    Saves the list of student data back to the file,
    overwriting previous content
    """
    file_path = "students.json"
    try:
        # Opens in write mode, uses indent=4 for readability
        with open(file_path, 'w') as file:
            json.dump(students_data_list, file, indent=4)
        print(f"\nSuccessfully saved updated list to '{file_path}'.")
    except IOError as e:
        print(f"Error saving file: {e}")

def print_student_in_class(class_list_data, original_length):
    """
    Loops through the list, formats the output, and indicates
    if the record was part of the original list or the new list
    """
    if not class_list_data: return

    for index, student in enumerate(class_list_data):
        # Compares index to original length to determine status
        if index < original_length:
            status = "(Student in original list)"
        else:
            status = "(New student in updated list)"

        last_name = student['L_Name']
        first_name = student['F_Name']
        student_id = student['Student_ID']
        email = student['Email']

        # Formats the output and indicates status
        output_line = f"{last_name}, {first_name} : ID = {student_id} , Email = {email} {status}"
        print(output_line)

# Main Program

# Load data from JSON into a list
students_data = load_students_from_json()
# Record the count of items originally in the file
initial_count = len(students_data)

# Define new student as a dictionary and append to list in memory
new_student = {
    "L_Name": "Denzlinger",
    "F_Name": "Abram",
    "Student_ID": "12345",
    "Email": "adenzlinger@my365.bellevue.edu"
}
students_data.append(new_student)

# Display all records, showing changes
print_student_in_class(students_data, initial_count)

# GUI confirmation pop up via Tkinter, prompt user to save
root = tk.Tk()
root.withdraw() # hide empty window

result = messagebox.askyesno("Save Changes?", "The student list has been modified in memory. Do you want to save these changes to students.json?")

# Execute user's choice from GUI pop up
if result:
    save_students_to_json(students_data)
else:
    print(".\n-> Save cancelled via GUI dialog. The original file was not changed.")
root.destroy()


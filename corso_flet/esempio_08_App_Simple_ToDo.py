# Example 8: Building a Simple To-Do App
# This example combines multiple controls and event handlers to create an interactive application.

import flet as ft

def main(page: ft.Page):
    page.title = "My To-Do List"

    # Step 1: Create an input field for a new task
    new_task_input = ft.TextField(hint_text="What needs to be done?", expand=True)

    # Step 2: Create a column to display tasks
    tasks_view = ft.Column()

    # Step 3: Define the function to add a task
    def add_task(e):
        if new_task_input.value: # If the input field is not empty
            task_checkbox = ft.Checkbox(
                label=new_task_input.value # Checkbox text is the task text
            )
            tasks_view.controls.append(task_checkbox) # Add the checkbox to the tasks list
            new_task_input.value = "" # Clear the input field
            page.update() # Update the page
    # Step 4: Create a button to add a task
    add_button = ft.FloatingActionButton(
        icon=ft.icons.ADD,
        on_click=add_task
    )

    # Step 5: Add the elements to the page
    page.add(
        ft.Row(
            [
                new_task_input, # Input field
                add_button # Add button
            ],
            alignment=ft.MainAxisAlignment.START # Align to the start of the row
        ),
        tasks_view # Column to display tasks
    )

    page.update()

ft.app(target=main)

""""
Step-by-step explanation:

new_task_input = ft.TextField(...): Field for task text input.
expand=True allows it to take all available space in the Row.
tasks_view = ft.Column(): An empty Column where tasks will be dynamically added.
def add_task(e): Handler for the "Add" button.
if new_task_input.value: Check if the user entered something.
task_checkbox = ft.Checkbox(...): Create a new Checkbox for each task.
tasks_view.controls.append(task_checkbox): Key point:
Dynamically adding an element to the controls list of a column.
new_task_input.value = "": Clear the input field.
page.update(): Update the UI.
add_button = ft.FloatingActionButton(...):
A floating action button with an icon.
page.add(ft.Row [...]), tasks_view):
Add the input field and button to a Row (so they are on the same line),
then the Column for tasks below them.
"""
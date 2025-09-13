# Example 10: Changing Page Theme (Dark/Light Mode Toggle)
# This example shows how to programmatically switch between
# light and dark themes for your application.

import flet as ft

def main(page: ft.Page):
    page.title = "Theme Toggle"

    # Step 1: Set the initial page theme (e.g., light)
    page.theme_mode = ft.ThemeMode.LIGHT
    page.update() # Update to apply initial theme

    # Step 2: Define the function to toggle the theme
    def toggle_theme(e):
        # If current theme is light, switch to dark, otherwise switch to light
        page.theme_mode = ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        e.control.text = "Light Theme" if page.theme_mode == ft.ThemeMode.DARK else "Dark Theme" # Update button
        page.update() # Update the page

    # Step 3: Create a button to toggle the theme
    theme_toggle_button = ft.ElevatedButton(
        text ="Dark Theme", # initial button text
        on_click=toggle_theme
    )

    # Step 4: Add the elements to the page
    page.add(
        ft.Text("Click the button to toggle the theme", size=20),
        theme_toggle_button
    )
    page.update()

ft.app(target=main)


"""
Step-by-step explanation:

page.theme_mode = ft.ThemeMode.LIGHT: Set the initial theme mode of the page.
ft.ThemeMode provides constants for LIGHT and DARK modes.
page.update(): Update to apply the initial theme immediately.
def toggle_theme(e): Button handler.
page.theme_mode = ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.
LIGHT: This is a ternary operator. It checks the current theme:
if LIGHT, it sets to DARK, otherwise it sets to LIGHT.
e.control.text = ...:
Update the text on the button itself so it reflects which theme the button will switch to next.
page.update(): Update the UI to display the theme changes and button text.
theme_toggle_button = ft.ElevatedButton(...): Create the button.
Conclusion (In English):
The Flet library opens up immense possibilities for creating cross-platform applications in pure Python,
without the need to learn other languages or UI frameworks.
You've seen how easy it is to create interactive elements,
manage layout, handle events, and even dynamically change the state of your application.
"""

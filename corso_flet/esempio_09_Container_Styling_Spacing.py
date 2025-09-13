# Example 9: Container for Styling and Spacing
# A Container is a versatile control that can hold other controls and apply styles like background,
# padding, and margins to them.

import flet as ft

def main(page: ft.Page):
    page.title = "Container Example"

    # Step 1: Create a text control inside the container
    contained_text = ft.Text("Text in Container", color=ft.colors.WHITE)

    # Step 2: Create a Container and add the text control to it
    my_container = ft.Container(
        content=contained_text, # Content of the container
        padding=20, # Internal padding
        margin=ft.margin.only(top=50, left=50), # External margins (only top and left)
        bgcolor=ft.colors.BLUE_GREY_700, # Background color
        width=250,
        height=100,
        alignment=ft.alignment.center, # Alignment of content within the container
        border_radius=ft.border_radius.all(15), # Rounded corners
        ink=True, # Inkwell effect on tap
        on_click=lambda e: print("Container clicked!"), # Click handler
    )

    # Step 3: Add the container to the page
    page.add(my_container)
    page.update()

ft.app(target=main)

"""
Step-by-step explanation:

contained_text = ft.Text(...): Create a regular text control that will be inside the container.
my_container = ft.Container(...): Create a Container.
content: Accepts a single control to be placed inside the container.
padding: Internal padding (space between content and container's border).
margin: External margins (space around the container).
ft.margin.ONLY allows setting margins for individual sides.
bgcolor: Background color of the container. Flet provides many predefined colors via ft.colors.
width, height: Dimensions of the container.
alignment: Alignment of the content within the container.
border_radius: Rounded corners.
ink=True, on_click: Containers can also be interactive and react to taps.
page.add(my_container): Add the container to the page.

"""
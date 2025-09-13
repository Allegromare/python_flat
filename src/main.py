'''
import flet as ft
import os

def main(page: ft.Page):
    counter = ft.Text("0", size=50, data=0)

    def increment_click(e):
        counter.data += 1
        counter.value = str(counter.data)
        counter.update()
    def exit_app(e):
        os._exit(0)

    page.add(ft.Text("Hello, World!"))
    page.add(ft.IconButton(ft.Icons.EXIT_TO_APP, on_click=exit_app))

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, on_click=increment_click
    )
    page.add(
        ft.SafeArea(
            ft.Container(
                counter,
                alignment=ft.alignment.center,
            ),
            expand=True,
        )
    )


ft.app(main)
'''

import flet as ft

class Task(ft.UserControl):
    def __init__(self, task_name: str, task_status: str, task_delete, on_task_drag):
        super().__init__()
        self.task_name = task_name
        self.task_status = task_status
        self.task_delete = task_delete
        self.on_task_drag = on_task_drag

    def build(self):
        self.task_text = ft.Text(self.task_name, size=16)
        self.edit_button = ft.IconButton(
            icon=ft.icons.EDIT,
            on_click=self.edit_clicked,
            icon_color=ft.colors.BLUE,
            tooltip="Modifica attività"
        )
        self.delete_button = ft.IconButton(
            icon=ft.icons.DELETE,
            on_click=self.delete_clicked,
            icon_color=ft.colors.RED,
            tooltip="Elimina attività"
        )

        self.view_mode = ft.Row(
            controls=[
                self.task_text,
                ft.Row(
                    controls=[
                        self.edit_button,
                        self.delete_button,
                    ]
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )

        self.edit_field = ft.TextField(value=self.task_name, on_blur=self.save_clicked)
        self.save_button = ft.IconButton(icon=ft.icons.SAVE, on_click=self.save_clicked, icon_color=ft.colors.GREEN)
        self.edit_mode = ft.Row(
            visible=False,
            controls=[
                self.edit_field,
                self.save_button
            ]
        )

        self.draggable_task = ft.Draggable(
            group="task",
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        self.view_mode,
                        self.edit_mode
                    ]
                ),
                padding=10,
                bgcolor=ft.colors.WHITE,
                border_radius=5,
            ),
            on_drag_start=self.on_drag_start
        )

        return self.draggable_task

    def edit_clicked(self, e):
        self.view_mode.visible = False
        self.edit_mode.visible = True
        self.update()

    def save_clicked(self, e):
        self.task_name = self.edit_field.value
        self.task_text.value = self.task_name
        self.view_mode.visible = True
        self.edit_mode.visible = False
        self.update()

    def delete_clicked(self, e):
        self.task_delete(self)

    def on_drag_start(self, e: ft.DragStartEvent):
        self.on_task_drag(self)

class KanbanColumn(ft.UserControl):
    def __init__(self, title: str, on_task_drag_reorder):
        super().__init__()
        self.title = title
        self.tasks = ft.Column(spacing=10)
        self.on_task_drag_reorder = on_task_drag_reorder

    def build(self):
        self.add_task_field = ft.TextField(
            label="Nuova attività...",
            on_submit=self.add_task_clicked
        )
        self.add_button = ft.IconButton(
            icon=ft.icons.ADD,
            on_click=self.add_task_clicked,
            tooltip="Aggiungi attività"
        )

        self.drag_target = ft.DragTarget(
            group="task",
            content=self.tasks,
            on_accept=self.handle_drag_accept,
            on_will_accept=self.handle_drag_will_accept,
            on_leave=self.handle_drag_leave
        )

        return ft.Container(
            content=ft.Column([
                ft.Row([ft.Text(self.title, size=20, weight=ft.FontWeight.BOLD), self.add_button]),
                self.add_task_field,
                self.drag_target
            ]),
            padding=10,
            bgcolor=ft.colors.BLUE_GREY_100,
            border_radius=5,
            expand=True
        )

    def add_task(self, task: Task):
        self.tasks.controls.append(task)
        self.update()

    def add_task_clicked(self, e):
        if self.add_task_field.value:
            new_task = Task(self.add_task_field.value, self.title, self.delete_task, self.set_dragged_task)
            self.tasks.controls.append(new_task)
            self.add_task_field.value = ""
            self.update()

    def delete_task(self, task: Task):
        self.tasks.controls.remove(task)
        self.update()

    def handle_drag_accept(self, e: ft.DragTargetAcceptEvent):
        src_id = e.src_id
        dragged_task_instance = self.page.controls[0].get_dragged_task()

        if dragged_task_instance:
            dragged_task_instance.task_status = self.title
            self.tasks.controls.append(dragged_task_instance)
            self.drag_target.border = None
            self.on_task_drag_reorder(dragged_task_instance.task_status)
        self.update()

    def handle_drag_will_accept(self, e: ft.DragTargetAcceptEvent):
        self.drag_target.border = ft.border.all(2, ft.colors.BLACK45)
        self.update()

    def handle_drag_leave(self, e):
        self.drag_target.border = None
        self.update()

    def set_dragged_task(self, task: Task):
        self.page.controls[0].set_dragged_task(task)
        # Rimuovi l'attività dalla colonna di origine
        for col in self.page.controls[0].controls[0].controls:
            if isinstance(col, KanbanColumn):
                if task in col.tasks.controls:
                    col.tasks.controls.remove(task)
                    col.update()
                    break

class KanbanBoard(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.columns = [
            KanbanColumn("Da fare", self.on_task_drag_reorder),
            KanbanColumn("In corso", self.on_task_drag_reorder),
            KanbanColumn("Fatto", self.on_task_drag_reorder)
        ]
        self.dragged_task = None

    def build(self):
        return ft.Row(
            controls=self.columns,
            vertical_alignment=ft.CrossAxisAlignment.START,
            expand=True,
        )

    def set_dragged_task(self, task: Task):
        self.dragged_task = task

    def get_dragged_task(self):
        return self.dragged_task

    def on_task_drag_reorder(self, target_column_title: str):
         # Qui potresti implementare la logica per riordinare
         # le attività all'interno della colonna di destinazione
         # dopo un'operazione di trascinamento e rilascio.
         pass


def main(page: ft.Page):
    page.title = "Bacheca Kanban Flet"
    page.window_width = 1200
    page.window_height = 800

    kanban_board = KanbanBoard()

    page.add(kanban_board)

if __name__ == "__main__":
    ft.app(target=main)
"""
gui/layout.py

Shared UI components.
"""

from nicegui import ui


def add_navigation():
    """
    Shared navigation row.
    """

    with ui.row():

        ui.button(
            "Dashboard",
            on_click=lambda:
                ui.navigate.to("/")
        )

        ui.button(
            "Authors",
            on_click=lambda:
                ui.navigate.to("/authors")
        )

        ui.button(
            "Documents",
            on_click=lambda:
                ui.navigate.to("/documents")
        )

        ui.button(
            "Compare Documents",
            on_click=lambda:
                ui.navigate.to(
                    "/compare-documents"
                )
        )
        
        ui.button(
            "Compare Sample",
            on_click=lambda:
                ui.navigate.to("/compare-sample")
        )

        ui.button(
            "Compare Authors",
            on_click=lambda:
                ui.navigate.to("/compare-authors")
        )

        ui.button(
            "Corpus Explorer",
            on_click=lambda:
                ui.navigate.to("/corpus")
        )


def page_header(title):
    """
    Standard page structure.
    """

    add_navigation()

    ui.separator()

    ui.label(title).classes(
        "text-2xl"
    )

    ui.separator()

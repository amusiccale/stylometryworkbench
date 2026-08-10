"""
gui/authors.py

Author management page.
"""

from nicegui import ui

from gui.layout import page_header

from models.author import (
    create_author,
    delete_author,
    list_authors,
)


def authors_page():

    page_header("Authors")

    #
    # Search
    #

    search_input = ui.input(
        label="Search Authors"
    )

    ui.separator()

    #
    # Create Author
    #

    with ui.row():

        id_input = ui.input(
            label="Author ID"
        )

        name_input = ui.input(
            label="Display Name"
        )

        def add_author():

            try:

                create_author(
                    int(id_input.value),
                    name_input.value,
                )

                id_input.set_value("")
                name_input.set_value("")

                refresh()

            except Exception as exc:

                ui.notify(
                    str(exc),
                    color="negative",
                )

        ui.button(
            "Create Author",
            on_click=add_author,
        )

    ui.separator()

    #
    # Author List
    #

    author_container = ui.column()

    def remove_author(author):

        try:

            delete_author(
                author.author_id
            )

            refresh()

        except Exception as exc:

            ui.notify(
                str(exc),
                color="negative",
            )

    def refresh():

        author_container.clear()

        search_text = (
            search_input.value or ""
        ).lower()

        with author_container:

            for author in list_authors():

                display_name = (
                    author.display_name or ""
                )

                if (
                    search_text
                    and search_text
                    not in display_name.lower()
                ):
                    continue

                with ui.row():

                    ui.label(
                        f"{author.author_id}"
                    )

                    ui.label(
                        display_name
                    )

                    ui.button(
                        "Delete",
                        color="negative",
                        on_click=lambda
                        a=author:
                        remove_author(a),
                    )

    search_input.on(
        "update:model-value",
        lambda e: refresh()
    )

    refresh()

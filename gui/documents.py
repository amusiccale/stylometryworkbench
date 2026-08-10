"""
gui/documents.py

Document management page.
"""

from pathlib import Path

from nicegui import ui

from gui.layout import page_header

from models.author import list_authors
from models.document import create_document

from ingest.txt_loader import load_txt
from ingest.docx_loader import load_docx
from datetime import datetime

def generate_filename(extension):
    """
    Generate fallback filename.
    """

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    return f"document_{timestamp}.{extension}"

def documents_page():

    page_header("Documents")

    #
    # Author Selector
    #

    authors = list_authors()

    author_choices = {
        str(author.author_id):
        f"{author.author_id} - "
        f"{author.display_name}"
        for author in authors
    }

    author_select = ui.select(
        author_choices,
        label="Author",
    )

    ui.separator()

    #
    # Paste Text
    #

    ui.label("Paste Text")

    text_input = ui.textarea().props(
        "rows=12"
    )

    filename_input = ui.input(
        label="Filename"
    )

    def save_pasted_text():

        if not author_select.value:

            ui.notify(
                "Select an author first",
                color="negative",
            )

            return

        create_document(
            author_id=int(
                author_select.value
            ),
            filename=(
                filename_input.value
                or "pasted_text.txt"
            ),
            text=text_input.value or "",
        )

        text_input.set_value("")
        filename_input.set_value("")

        ui.notify(
            "Document saved",
            color="positive",
        )

    ui.button(
        "Save Pasted Text",
        on_click=save_pasted_text,
    )

    ui.separator()

    #
    # TXT Upload
    #

    ui.label("Upload TXT")

    async def handle_txt_upload(event):
        print()
        print("EVENT TYPE:", type(event))
        print("DIR:")
        print(dir(event))
        print()

        if not author_select.value:

            ui.notify(
                "Select an author first",
                color="negative",
            )

            return

        filename = getattr(
            getattr(event, "file", None),
            "name",
            None,
        )

        if not filename:
            filename = generate_filename("txt")

        temp_path = f"_upload_{filename}"

        with open(
            temp_path,
            "wb",
        ) as file:

            content = await event.file.read()

            file.write(content)

        text = load_txt(temp_path)

        create_document(
            author_id=int(
                author_select.value
            ),
            filename=filename,
            text=text,
        )

        Path(temp_path).unlink(
            missing_ok=True
        )

        ui.notify(
            "TXT uploaded",
            color="positive",
        )

    ui.upload(
        label="Choose TXT File",
        on_upload=handle_txt_upload,
    ).props(
        'accept=".txt"'
    )

    ui.separator()

    #
    # DOCX Upload
    #

    ui.label("Upload DOCX")

    async def handle_docx_upload(event):
        print()
        print("EVENT TYPE:", type(event))
        print("DIR:")
        print(dir(event))
        print()
            
        if not author_select.value:

            ui.notify(
                "Select an author first",
                color="negative",
            )

            return

        filename = getattr(
            getattr(event, "file", None),
            "name",
            None,
        )

        if not filename:
            filename = generate_filename("docx")

        temp_path = f"_upload_{filename}"

        with open(
            temp_path,
            "wb",
        ) as file:

            content = await event.file.read()

            file.write(content)

        text = load_docx(temp_path)

        create_document(
            author_id=int(
                author_select.value
            ),
            filename=filename,
            text=text,
        )

        Path(temp_path).unlink(
            missing_ok=True
        )

        ui.notify(
            "DOCX uploaded",
            color="positive",
        )

    ui.upload(
        label="Choose DOCX File",
        on_upload=handle_docx_upload,
    ).props(
        'accept=".docx"'
    )

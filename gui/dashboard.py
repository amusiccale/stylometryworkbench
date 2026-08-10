"""
gui/dashboard.py
"""

from nicegui import ui

from gui.layout import page_header

from models.author import list_authors
from models.document import list_documents


def dashboard_page():

    page_header(
        "Stylometric Fingerprint Workbench"
    )

    authors = list_authors()

    documents = list_documents()

    corpus_words = sum(
        document.word_count
        for document in documents
    )

    with ui.row():

        ui.card().classes(
            "p-4"
        )

        with ui.card():

            ui.label("Authors")

            ui.label(
                str(len(authors))
            )

        with ui.card():

            ui.label("Documents")

            ui.label(
                str(len(documents))
            )

        with ui.card():

            ui.label(
                "Corpus Words"
            )

            ui.label(
                str(corpus_words)
            )

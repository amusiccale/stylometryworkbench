from nicegui import ui
from database.db import (
    initialize_database,
)

initialize_database()
from config import APP_PORT

##ui.label("Stylometric Fingerprint Workbench")
##ui.label("SFW v0.1 - Development Build")
##
##ui.run(
##    title="Stylometric Fingerprint Workbench",
##    port=APP_PORT,
##)

from gui.dashboard import (
    dashboard_page
)

from gui.authors import (
    authors_page,
)

from gui.documents import (
    documents_page,
)

from gui.compare_sample import (
    compare_sample_page,
)

from gui.compare_authors import (
    compare_authors_page,
)

from gui.corpus_explorer import (
    corpus_explorer_page,
)
from gui.compare_documents import (
    compare_documents_page,
)

@ui.page("/")
def index():

    dashboard_page()

@ui.page("/authors")
def authors():

    authors_page()

@ui.page("/documents")
def documents():

    documents_page()

@ui.page("/compare-documents")
def compare_documents_route():

    compare_documents_page()

@ui.page("/compare-sample")
def compare_sample():

    compare_sample_page()


@ui.page("/compare-authors")
def compare_authors():

    compare_authors_page()

@ui.page("/corpus")
def corpus():

    corpus_explorer_page()

ui.run(
    title=(
        "Stylometric "
        "Fingerprint Workbench"
    )
)

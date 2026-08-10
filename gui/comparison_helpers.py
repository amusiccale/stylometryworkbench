"""
gui/comparison_helpers.py
"""

from models.author import list_authors


def author_choices():

    return {
        str(author.author_id):
        f"{author.author_id} - "
        f"{author.display_name}"
        for author in list_authors()
    }

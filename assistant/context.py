from models.author import (
    list_authors,
)


def author_context():

    authors = list_authors()

    lines = []

    for author in authors:

        lines.append(
            f"{author.author_id}: "
            f"{author.display_name}"
        )

    return "\n".join(lines)

from models.author import list_authors


def build_author_lookup():

    lookup = {}

    for author in list_authors():

        #
        # Numeric ID
        #

        lookup[
            str(author.author_id).lower()
        ] = author.author_id

        #
        # Author 7
        #

        lookup[
            f"author {author.author_id}".lower()
        ] = author.author_id

        #
        # Display name
        #

        if author.display_name:

            lookup[
                author.display_name.lower()
            ] = author.author_id

    return lookup

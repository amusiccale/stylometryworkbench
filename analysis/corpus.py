from models.author import list_authors
from models.fingerprint import load_fingerprint


def get_corpus_fingerprints():

    results = []

    for author in list_authors():

        fp = load_fingerprint(
            author.author_id
        )

        if fp is None:
            continue

        results.append(
            {
                "author_id":
                    author.author_id,

                "label":
                    author.display_name,

                "vector":
                    fp.vector,
            }
        )

    return results

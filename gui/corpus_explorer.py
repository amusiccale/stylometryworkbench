"""
gui/corpus_explorer.py
"""

from nicegui import ui

from gui.layout import page_header

from analysis.corpus import (
    get_corpus_fingerprints,
)

from analysis.similarity import (
    cosine_similarity,
)

from analysis.clustering import (
    generate_pca_coordinates,
    generate_umap_coordinates,
)

from visualization.heatmap import (
    create_similarity_heatmap,
)

from visualization.pca import (
    create_pca_plot,
)

from visualization.umap import (
    create_umap_plot,
)


def corpus_explorer_page():

    page_header("Corpus Explorer")

    corpus = get_corpus_fingerprints()

    if len(corpus) < 2:

        ui.label(
            "Need at least two authors with "
            "fingerprints to explore corpus."
        )

        return

    labels = [
        author["label"]
        for author in corpus
    ]

    vectors = [
        author["vector"]
        for author in corpus
    ]

    #
    # Similarity Heatmap
    #

    ui.label(
        "Similarity Heatmap"
    ).classes(
        "text-xl"
    )

    matrix = []

    for vec_a in vectors:

        row = []

        for vec_b in vectors:

            row.append(
                cosine_similarity(
                    vec_a,
                    vec_b,
                )
            )

        matrix.append(row)

    heatmap = create_similarity_heatmap(
        matrix,
        labels,
    )

    ui.plotly(
        heatmap
    ).classes(
        "w-full"
    )

    ui.separator()

    #
    # PCA
    #

    ui.label(
        "PCA Visualization"
    ).classes(
        "text-xl"
    )

    pca_coords = (
        generate_pca_coordinates(
            vectors,
            labels,
        )
    )

    if pca_coords:

        pca_fig = create_pca_plot(
            pca_coords
        )

        ui.plotly(
            pca_fig
        ).classes(
            "w-full"
        )

    else:

        ui.label(
            "Not enough data "
            "for PCA."
        )

    ui.separator()

    #
    # UMAP
    #

    ui.label(
        "UMAP Visualization"
    ).classes(
        "text-xl"
    )

    umap_coords = (
        generate_umap_coordinates(
            vectors,
            labels,
        )
    )

    if umap_coords:

        umap_fig = create_umap_plot(
            umap_coords
        )

        ui.plotly(
            umap_fig
        ).classes(
            "w-full"
        )

    else:

        ui.label(
            "Not enough data "
            "for UMAP."
        )

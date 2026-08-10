"""
gui/compare_documents.py
"""

from nicegui import ui

from gui.layout import page_header

from models.document import (
    list_documents,
)

from analysis.feature_categories import (
    features_from_categories,
    all_features,
)

from analysis.document_comparison import (
    compare_documents,
    build_document_vector,
)

from analysis.feature_differences import (
    calculate_feature_differences,
)

from visualization.radar import (
    create_radar_chart,
)

from visualization.differences import (
    create_difference_plot,
)

from analysis.feature_differences import (
    calculate_feature_differences,
)

def document_choices():

    return {
        str(doc.document_id):
        f"{doc.document_id} - {doc.filename}"
        for doc in list_documents()
    }


def compare_documents_page():

    page_header(
        "Compare Documents"
    )

    scaling_mode = ui.select(
        [
            "raw",
            "log",
            "relative",
            "log_relative",
        ],
        label="Chart Scaling",
        value="log_relative",
    )

    with ui.column().classes(
        "w-full"
    ):
        ui.label(
            "Feature Categories"
        )

        selected_categories = ui.select(
            [
                "lexical",
                "structural",
                "function_words",
                "character",
                "punctuation",
                "pos",
            ],
            label="Categories",
            multiple=True,
            value=[
                "lexical",
                "structural",
                "function_words",
                "character",
                "punctuation",
                "pos",
            ],
        )

        ui.separator()

        with ui.expansion(
            "Advanced Feature Selection"
            ):
            feature_state = {
                feature:
                ui.checkbox(
                    feature,
                    value=True,
                )
                for feature in all_features()
            }
        
        ui.separator()

        choices = document_choices()

        document_a = ui.select(
            choices,
            label="Document A",
        )

        document_b = ui.select(
            choices,
            label="Document B",
        )

        ui.separator()

        result_container = ui.column().style(
            "width: 100%;"
        )

        def run_comparison():

            result_container.clear()

            if (
                not document_a.value
                or not document_b.value
            ):
                return

            selected_features = [
                feature
                for feature, checkbox
                in feature_state.items()
                if checkbox.value
            ]

            result = compare_documents(
                int(document_a.value),
                int(document_b.value),
                method="cosine",
                selected_features=
                    selected_features,
            )

            vec_a = build_document_vector(
                int(document_a.value)
            )

            vec_b = build_document_vector(
                int(document_b.value)
            )

            differences = (
                calculate_feature_differences(
                    vec_a,
                    vec_b,
                    selected_features,
                )
            )

            with result_container:

                ui.label(
                    f"Similarity: "
                    f"{result['similarity']:.4f}"
                )

                ui.label(
                    f"Distance: "
                    f"{result['distance']:.4f}"
                )

                ui.separator()

                radar_a = create_radar_chart(
                    vec_a,
                    f"Document {document_a.value}",
                    normalization=scaling_mode.value,
                )

                radar_b = create_radar_chart(
                    vec_b,
                    f"Document {document_b.value}",
                    normalization=scaling_mode.value,
                )

                ui.plotly(
                    radar_a
                ).classes(
                    "w-full"
                )

                ui.plotly(
                    radar_b
                ).classes(
                    "w-full"
                )

                ui.separator()

                difference_fig = (
                    create_difference_plot(
                        differences,
                        normalization=
                            scaling_mode.value,
                    )
                )

                ui.plotly(
                    difference_fig
                ).classes(
                    "w-full"
                )

        ui.button(
            "Compare Documents",
            on_click=run_comparison,
        )

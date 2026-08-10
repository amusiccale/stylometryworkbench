"""
gui/compare_authors.py
"""

from nicegui import ui

from gui.layout import page_header

from gui.comparison_helpers import (
    author_choices,
)

from models.fingerprint import (
    load_fingerprint,
)

from analysis.similarity import (
    similarity_result,
)

from analysis.feature_categories import (
    features_from_categories,
)

from analysis.feature_categories import (
    features_from_categories,
    all_features,
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

def compare_authors_page():
    
    page_header(
        "Compare Authors"
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
        
    with ui.column().classes("w-full"):
                    
        #
        # Feature Categories
        #

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

        #
        # Author Selectors
        #

        choices = author_choices()

        author_a = ui.select(
            choices,
            label="Author A",
        )

        author_b = ui.select(
            choices,
            label="Author B",
        )

        ui.separator()

        result_container = ui.column().style(
            "width: 100%;"
        )
        
        def run_comparison():

            result_container.clear()

            if (
                not author_a.value
                or not author_b.value
            ):
                return

            fp_a = load_fingerprint(
                int(author_a.value)
            )

            fp_b = load_fingerprint(
                int(author_b.value)
            )

            selected_features = [
                feature
                for feature, checkbox
                in feature_state.items()
                if checkbox.value
            ]

            result = similarity_result(
                int(author_a.value),
                int(author_b.value),
                fp_a.vector,
                fp_b.vector,
                method="cosine",
                selected_features=
                    selected_features,
            )

            differences = (
                calculate_feature_differences(
                    fp_a.vector,
                    fp_b.vector,
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

                fig_a = create_radar_chart(
                    fp_a.vector,
                    f"Author {author_a.value}",
                    normalization=
                        scaling_mode.value,
                )

                fig_b = create_radar_chart(
                    fp_b.vector,
                    f"Author {author_b.value}",
                    normalization=
                        scaling_mode.value,
                )

                ui.plotly(
                    fig_a
                ).classes(
                    "w-full"
                )

                ui.plotly(
                    fig_b
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
            "Compare",
            on_click=run_comparison,
        )

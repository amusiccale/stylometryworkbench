"""
gui/compare_sample.py
"""

from nicegui import ui

from gui.layout import page_header

from analysis.attribution import (
    attribute_text,
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
from exports.html_report import (
    export_html_report,
)


def compare_sample_page():

    page_header("Compare Sample")

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

        sample_text = ui.textarea(
            label="Sample Text"
        ).props(
            "rows=15"
        )

        result_container = ui.column().style(
            "width: 100%;"
        )

        latest_result = None


        def export_report():

            if latest_result is None:

                ui.notify(
                    "Run attribution first."
                )

                return

            output_path = (
                "attribution_report.html"
            )

            export_html_report(
                latest_result,
                output_path,
            )

            ui.notify(
                f"Exported: {output_path}"
            )

        def run_attribution():
            nonlocal latest_result
 
            result_container.clear()

            selected_features = [
                feature
                for feature, checkbox
                in feature_state.items()
                if checkbox.value
            ]

            result = attribute_text(
                sample_text.value or "",
                selected_features=selected_features,
            )

            latest_result = result
            
            
            with result_container:

                ui.label(
                    f"Predicted Author: "
                    f"{result['predicted_author']}"
                )

                ui.label(
                    f"Confidence: "
                    f"{result['confidence']}%"
                )

                ui.separator()

                for rank in result["rankings"]:

                    ui.label(
                        f"{rank['author_id']} | "
                        f"{rank['display_name']} | "
                        f"{rank['score']:.4f}"
                    )

        ui.button(
            "Run Attribution",
            on_click=run_attribution,
        )

        ui.button(
            "Export HTML Report",
            on_click=export_report,
        )

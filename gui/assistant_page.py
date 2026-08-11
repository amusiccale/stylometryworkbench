"""
gui/assistant_page.py
"""

from nicegui import ui

from gui.layout import (
    page_header,
)

from assistant.intents import (
    identify_intent,
)

from assistant.executor import (
    execute_intent,
    format_author_comparison,
    format_document_comparison,
    format_author_list,
    format_document_list,
)

from assistant.explainer import (
    explain_author_comparison,
    explain_document_comparison,
)

from visualization.radar import (
    create_radar_chart,
)

from visualization.differences import (
    create_difference_plot,
)


def assistant_page():

    page_header(
        "Workbench Assistant"
    )

    with ui.column().classes(
        "w-full"
    ):

        ui.label(
            "*Experimental Natural-Language Interface, requires local LLM endpoint* (localhost:5001/v1)"
        )

        ui.label(
            "Try: compare authors, compare documents, list documents, list authors"
        )

        question = ui.textarea(
            label="Question"
        ).props(
            "rows=6"
        )

        result_container = ui.column().classes(
            "w-full"
        )

        def ask():

            result_container.clear()

            try:

                intent = identify_intent(
                    question.value or ""
                )

                result = execute_intent(
                    intent
                )

                #
                # Compare Authors
                #

                if (
                    result.get("intent")
                    == "compare_authors"
                ):

                    formatted = (
                        format_author_comparison(
                            result
                        )
                    )

                    explanation = (
                        explain_author_comparison(
                            result
                        )
                    )

                    with result_container:

                        ui.markdown(
                            formatted
                            + "\n\n---\n\n"
                            + "## Interpretation\n\n"
                            + explanation
                        )


                    if (
                        "fingerprint_a" in result
                    ):
                        radar_a = (
                            create_radar_chart(
                                result["fingerprint_a"],
                                result["author_a_name"],
                                normalization="log_relative",
                            )
                        )

                        ui.separator()

                        ui.plotly(
                            radar_a
                        ).classes(
                            "w-full"
                        )

                        radar_b = (
                            create_radar_chart(
                                result["fingerprint_b"],
                                result["author_b_name"],
                                normalization="log_relative",
                            )
                        )

                        ui.plotly(
                            radar_b
                        ).classes(
                            "w-full"
                        )

                        difference_fig = (
                            create_difference_plot(
                                result["all_differences"],
                                normalization="log_relative",
                            )
                        )

                        ui.separator()

                        ui.plotly(
                            difference_fig
                        ).classes(
                            "w-full"
                        )
                #
                # Compare Documents
                #

                elif (
                    result.get("intent")
                    == "compare_documents"
                ):

                    formatted = (
                        format_document_comparison(
                            result
                        )
                    )

                    explanation = (
                        explain_document_comparison(
                            result
                        )
                    )

                    with result_container:

                        ui.markdown(
                            formatted
                            + "\n\n---\n\n"
                            + "## Interpretation\n\n"
                            + explanation
                        )

                        #
                        # Radar A
                        #

                        radar_a = (
                            create_radar_chart(
                                result["vector_a"],
                                f"Document {result['document_a']}",
                                normalization="log_relative",
                            )
                        )

                        ui.separator()

                        ui.plotly(
                            radar_a
                        ).classes(
                            "w-full"
                        )

                        #
                        # Radar B
                        #

                        radar_b = (
                            create_radar_chart(
                                result["vector_b"],
                                f"Document {result['document_b']}",
                                normalization="log_relative",
                            )
                        )

                        ui.plotly(
                            radar_b
                        ).classes(
                            "w-full"
                        )

                        #
                        # Difference Chart
                        #

                        difference_fig = (
                            create_difference_plot(
                                result["all_differences"],
                                normalization="log_relative",
                            )
                        )

                        ui.plotly(
                            difference_fig
                        ).classes(
                            "w-full"
                        )

                #
                # List Authors
                #

                elif (
                    result.get("intent")
                    == "list_authors"
                ):

                    with result_container:

                        ui.markdown(
                            format_author_list(
                                result
                            )
                        )

                #
                # List Documents
                #

                elif (
                    result.get("intent")
                    == "list_documents"
                ):

                    with result_container:

                        ui.markdown(
                            format_document_list(
                                result
                            )
                        )

                #
                # Fallback
                #

                else:

                    with result_container:

                        ui.markdown(
                            str(result)
                        )

            except Exception as exc:

                result_container.clear()

                with result_container:

                    ui.markdown(
                        f"### Error\n\n```\n{exc}\n```"
                    )

        ui.button(
            "Ask",
            on_click=ask,
        )

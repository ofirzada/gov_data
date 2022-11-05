import altair as alt
import pandas as pd
import streamlit as st


def get_chart(source, x="TimePeriod", y="Value", color="path_name", title=None):
    hover = alt.selection_single(
        fields=[x],
        nearest=True,
        on="mouseover",
        empty="none",
    )

    lines = (
        alt.Chart(source)
        .mark_line()
        .encode(x=x, y=y,color=color)
    )

    # Draw points on the line, highlight based on selection, color based on delta
    points = lines.transform_filter(hover).mark_circle(size=65)

    # Draw an invisible rule at the location of the selection
    tooltips = (
        alt.Chart(source)
        .mark_rule(opacity=0)
        .encode(
            x=x,
            y=y,
            tooltip=[x, y,alt.Tooltip("path_name", title="path_name"),alt.Tooltip("units", title="יחידות מידע")],
        )
        .add_selection(hover)
    )

    return (lines + points + tooltips).interactive()

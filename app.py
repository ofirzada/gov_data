from datetime import date, datetime
import visualHandler.graphs as grh
import visualHandler.table as tbl
import altair as alt
import pandas as pd
import streamlit as st
import subject_hanlder.fatch_data_from_subject as sh



import asyncio
from dataHandler import path_data


def plot_all_data(
        source, x="TimePeriod", y="Value", group="path", axis_scale="linear"
):
    brush = alt.selection_interval(encodings=["x"], empty="all")

    click = alt.selection_multi(encodings=["color"])

    lines = (
        (
            alt.Chart(source)
            .mark_line(point=True)
            .encode(
                x=x,
                y=alt.Y(y, scale=alt.Scale(type=f"{'linear'}")),
                color=group,
                tooltip=[
                    "TimePeriod",
                    "Value",
                    "unit.name"

                ],
            )
        )
        .add_selection(brush)
        .properties(width=550)
        .transform_filter(click)
    )

    bars = (
        alt.Chart(source)
        .mark_bar()
        .encode(
            y=group,
            color=group,
            x=alt.X("downloads:Q", scale=alt.Scale(type=f"{'linear'}")),
            tooltip=["TimePeriod", "Value"],
        )
        .transform_filter(brush)
        .properties(width=550)
        .add_selection(click)
    )

    return lines & bars




def get_name(list, path):
    for items in list:
        if items['path'] == path:
            return items['name']


async def get_main_subjects(level=1, subject=None):
    get_subjects = await sh.get_subjects(level=level, subject=subject)
    option_list = list(map(lambda d: d['path'], get_subjects))
    return st.selectbox(
        "נושאים בתוך קומת המידע", options=option_list, format_func=lambda x: get_name(get_subjects, x)
    )


async def main():
    # Note that page title/favicon are set in the __main__ clause below,
    # so they can also be set through the mega multipage app (see ../pandas_app.py).
    data_paths = []
    data_from_subject = []
    with st.form("my_form"):

        col1, col2 = st.columns(2)
        with col1:
            subject = await get_main_subjects()

        with col2:
            level = st.selectbox(
                "level_of_data", [2, 3, 4],

            )

        submitted = st.form_submit_button("Submit")
        if submitted:
            try:
                data_path = await get_main_subjects(level=level, subject=subject)
                title = f"subject {subject} level {level}".format(subject=subject, level=level)
                data_paths.append(list(data_path))
                data_from_subject = await path_data.get_all_data_from_subject(data_paths)


            except Exception as e:
                print(e)
                st.write("data not found")


    st.header("data")

    if len(data_from_subject) >= 1:

        chart = grh.get_chart(data_from_subject[0], title=title)
        st.altair_chart(chart,use_container_width=True)
        tbl.get_table(data_from_subject[0])



st.set_page_config(layout="wide", page_icon="💬", page_title="data app")

st.title("apis data")
st.write(
    " "
    "data from the `apis api` where all the goverment data can be accessed."
)

asyncio.run(main())

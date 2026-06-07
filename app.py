
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Smart Analytics Tool",
    layout="wide"
)

st.title("📊 Smart Analytics Tool")

st.write("Upload a CSV file to begin analysis.")

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.success("Dataset uploaded successfully!")

    st.write(
        f"Rows: {df.shape[0]} | Columns: {df.shape[1]}"
    )

    st.header("Dataset Preview")

    st.dataframe(df.head())

    st.header("Dataset Information")

    info_df = pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str)
    })

    st.dataframe(info_df)

    st.header("Missing Value Analysis")

    missing_df = pd.DataFrame({
        "Column": df.columns,
        "Missing Values": df.isnull().sum().values
    })

    st.dataframe(missing_df)

    total_missing = df.isnull().sum().sum()

    st.metric(
        "Total Missing Values",
        total_missing
    )

    st.header("Statistical Summary")

    numeric_df = df.select_dtypes(
        include=["number"]
    )

    if not numeric_df.empty:
        st.dataframe(
            numeric_df.describe()
        )
    else:
        st.warning(
            "No numeric columns available."
        )

    st.header("Visualization 1: Histogram")

    numeric_cols = df.select_dtypes(
        include=["number"]
    ).columns.tolist()

    if len(numeric_cols) > 0:

        hist_col = st.selectbox(
            "Select Column for Histogram",
            numeric_cols
        )

        fig1 = px.histogram(
            df,
            x=hist_col
        )

        st.plotly_chart(
            fig1,
            use_container_width=True
        )

    st.header("Visualization 2: Scatter Plot")

    if len(numeric_cols) >= 2:

        x_col = st.selectbox(
            "X Axis",
            numeric_cols,
            key="scatter_x"
        )

        y_col = st.selectbox(
            "Y Axis",
            numeric_cols,
            key="scatter_y"
        )

        fig2 = px.scatter(
            df,
            x=x_col,
            y=y_col
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    st.header("Visualization 3: Bar Chart")

    categorical_cols = df.select_dtypes(
        include=["object"]
    ).columns.tolist()

    if len(categorical_cols) > 0:

        cat_col = st.selectbox(
            "Select Category",
            categorical_cols
        )

        value_counts = (
            df[cat_col]
            .value_counts()
            .reset_index()
        )

        value_counts.columns = [
            cat_col,
            "Count"
        ]

        fig3 = px.bar(
            value_counts,
            x=cat_col,
            y="Count"
        )

        st.plotly_chart(
            fig3,
            use_container_width=True
        )

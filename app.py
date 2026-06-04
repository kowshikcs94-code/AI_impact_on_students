import streamlit as st
import pandas as pd
import plotly.express as px

# Page Config
st.set_page_config(
    page_title="AI Student Impact Dashboard",
    page_icon="🎓",
    layout="wide"
)

# Load Data
@st.cache_data
def load_data():
    return pd.read_csv("data/ai_student_impact_dataset.csv")

df = load_data()

# Title
st.title("🎓 AI Student Impact Dashboard")
st.markdown("Analyze the impact of AI on students.")

# Sidebar Filters
st.sidebar.header("Filters")

if "Gender" in df.columns:
    gender = st.sidebar.multiselect(
        "Gender",
        df["Gender"].unique(),
        default=df["Gender"].unique()
    )
    df = df[df["Gender"].isin(gender)]

# KPI Cards
col1, col2, col3 = st.columns(3)

col1.metric("Total Students", len(df))

if "Age" in df.columns:
    col2.metric(
        "Average Age",
        round(df["Age"].mean(), 1)
    )

if "Study_Hours_Per_Week" in df.columns:
    col3.metric(
        "Avg Study Hours",
        round(df["Study_Hours_Per_Week"].mean(), 1)
    )

st.divider()

# Chart 1
numeric_cols = df.select_dtypes(include="number").columns

if len(numeric_cols) > 0:
    st.subheader("Numeric Feature Distribution")

    selected_col = st.selectbox(
        "Select Feature",
        numeric_cols
    )

    fig = px.histogram(
        df,
        x=selected_col,
        title=f"{selected_col} Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# Chart 2
if len(numeric_cols) >= 2:
    st.subheader("Relationship Analysis")

    x_col = st.selectbox(
        "X Axis",
        numeric_cols,
        index=0
    )

    y_col = st.selectbox(
        "Y Axis",
        numeric_cols,
        index=1
    )

    fig = px.scatter(
        df,
        x=x_col,
        y=y_col,
        title=f"{x_col} vs {y_col}"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# Data Preview
st.subheader("Dataset Preview")

st.dataframe(
    df.head(),
    use_container_width=True
)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from io import BytesIO
import warnings
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="Aplikasi EDA Lengkap",
    page_icon="🔍",
    layout="wide"
)

# -------------------------------
# 1. TITLE & SUBHEADER
# -------------------------------
st.markdown("""
<h1 style='text-align: center;'>
🕵️ A COMPLETE EXPLORATORY DATA ANALYSIS TOOL 🕵️‍♀️
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<div style="display:flex; justify-content:center;">
    <div style="
        background-color:#E6F6F7;
        padding:20px;
        border-radius:12px;
        border:1px solid #d0eaea;
        box-shadow: 0 2px 6px rgba(0,0,0,0.05);
        width:100%;
        text-align:center;
    ">
        <h4 style="margin-bottom:10px;">Understand Your Data Instantly</h4>
        <p style="margin:0; font-size:15px; line-height:1.6;">
            This application allows you to perform <b>Exploratory Data Analysis (EDA)</b> by simply uploading your dataset. 
            EDA is the process of examining, summarizing, and visualizing data to discover patterns, detect issues, 
            and gain meaningful insights before further analysis or modeling.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------
# CREATE SIDEBAR NAVIGATION
#---------------------------------------------
st.sidebar.title("EDA Dashboard")
menu = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📌 Dataset Overview",
        "🔍 Data Preview",
        "📄 Dataset Information",
        "⚠️ Missing Values",
        "📊 Statistical Summary",
        "📈 Data Visualization",
        "🧠 Analysis"
    ]
)

# -------------------------------
# 2. FILE UPLOAD
# -------------------------------
file = st.file_uploader("Upload your file (CSV,Excel or Json)", type=["csv", "xlsx", "json"])

if file is not None:

    # Read file
    if file.name.endswith(".csv"):
        df = pd.read_csv(file)

    elif file.name.endswith(".xlsx"):
        df = pd.read_excel(file)

    elif file.name.endswith(".json"):
        try:
            df = pd.read_json(file)
        except ValueError:
            file.seek(0)
            df = pd.json_normalize(pd.read_json(file))

    st.success("File uploaded successfully!")
    st.caption(f"Detected file type: {file.type}")

    # ---------------- HOME ----------------
    if menu == "🏠 Home":
        # ---------------- HERO SECTION ----------------
        st.markdown("""
        <div style="padding:25px; border-radius:12px; background:linear-gradient(90deg,#E6F6F7,#F0F9FF);">
            <h2 style="margin-bottom:5px;">📊 Data Analysis Made Simple</h2>
            <p style="margin:0; font-size:16px;">
                Upload your dataset and instantly explore insights, detect issues, and visualize patterns — all in one place.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # ---------------- FEATURE CARDS ----------------

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("""
            <div style="
            padding:15px;
            border-radius:10px;
            background-color:#F8FAFC;
            border:1px solid #e5e7eb;
            height:150px;
            display:flex;
            flex-direction:column;
            justify-content:space-between;
            ">
                <h4>📌 Overview</h4>
                <p style="font-size:14px;">Quickly understand dataset size, missing values, and duplicates.</p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div style="
    padding:15px;
    border-radius:10px;
    background-color:#F8FAFC;
    border:1px solid #e5e7eb;
    height:150px;
    display:flex;
    flex-direction:column;
    justify-content:space-between;
">
                <h4>⚠️ Missing Values</h4>
                <p style="font-size:14px;">Identify missing data and potential data issues.</p>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div style="
    padding:15px;
    border-radius:10px;
    background-color:#F8FAFC;
    border:1px solid #e5e7eb;
    height:150px;
    display:flex;
    flex-direction:column;
    justify-content:space-between;
">
                <h4>🔍 Data Preview</h4>
                <p style="font-size:14px;">View your data structure and inspect rows easily.</p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div style="
    padding:15px;
    border-radius:10px;
    background-color:#F8FAFC;
    border:1px solid #e5e7eb;
    height:150px;
    display:flex;
    flex-direction:column;
    justify-content:space-between;
">
                <h4>📈 Visualization</h4>
                <p style="font-size:14px;">Create charts like histogram, scatter plot, and heatmap.</p>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown("""
            <div style="
    padding:15px;
    border-radius:10px;
    background-color:#F8FAFC;
    border:1px solid #e5e7eb;
    height:150px;
    display:flex;
    flex-direction:column;
    justify-content:space-between;
">
                <h4>📊 Statistics</h4>
                <p style="font-size:14px;">Get numerical and categorical summaries instantly.</p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div style="
    padding:15px;
    border-radius:10px;
    background-color:#F8FAFC;
    border:1px solid #e5e7eb;
    height:150px;
    display:flex;
    flex-direction:column;
    justify-content:space-between;
">
                <h4>🧠 Analysis</h4>
                <p style="font-size:14px;">Generate quick insights and understand your data better.</p>
            </div>
            """, unsafe_allow_html=True)

        # ---------------- QUICK STATS ----------------
        st.markdown("### 📊 Quick Snapshot")

        if file is not None:
            col1, col2, col3, col4 = st.columns(4)

            col1.metric("Rows", df.shape[0])
            col2.metric("Columns", df.shape[1])
            col3.metric("Missing", df.isnull().sum().sum())
            col4.metric("Duplicates", df.duplicated().sum())

        else:
            st.info("Upload a dataset to see a quick summary here.")

        st.markdown("<br>", unsafe_allow_html=True)

        # ---------------- GET STARTED ----------------
        st.markdown("""
        <div style="padding:15px; border-radius:10px; background-color:#F0F9FF; border:1px solid #dbeafe;">
            <h4>🚀 Get Started</h4>
            <p style="font-size:14px;">
                1. Upload your dataset<br>
                2. Explore the <b>Overview</b><br>
                3. Visualize your data<br>
                4. Gain insights from Analysis
            </p>
        </div>
        """, unsafe_allow_html=True)
    # -------------------------------
    # 3. DATASET OVERVIEW
    # -------------------------------
    elif menu == "📌 Dataset Overview":
        st.header("📌 Dataset Overview")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Total Rows", df.shape[0])
        col2.metric("Total Columns", df.shape[1])
        col3.metric("Missing Values", df.isnull().sum().sum())
        col4.metric("Duplicate Rows", df.duplicated().sum())

    # -------------------------------
    # 4. DATA PREVIEW
    # -------------------------------
    elif menu == "🔍 Data Preview":
        st.header("🔍 Data Preview")
        st.dataframe(df.head())

    # -------------------------------
    # 5. DATASET INFORMATION
    # -------------------------------
    elif menu == "📄 Dataset Information":
        st.header("📄 Dataset Information")

        buffer = pd.DataFrame({
            "Column Name": df.columns,
            "Data Type": df.dtypes.astype(str),
            "Non-Null Count": df.count().values
        })

        st.dataframe(buffer)

    # -------------------------------
    # 6. MISSING VALUES TABLE
    # -------------------------------
    elif menu == "⚠️ Missing Values":
        st.header("⚠️ Missing Values")

        missing = df.isnull().sum()
        missing_df = pd.DataFrame({
            "Column": missing.index,
            "Missing Count": missing.values
        })

        st.dataframe(missing_df[missing_df["Missing Count"] > 0])

    # -------------------------------
    # 7. STATISTICAL SUMMARY (NUMERICAL)
    # -------------------------------
    elif menu == "📊 Statistical Summary":
        st.header("📊 Statistical Summary (Numerical Features)")
        st.dataframe(df.describe())

    # -------------------------------
    # 8. STATISTICAL SUMMARY (NON-NUMERICAL)
    # -------------------------------
    
        st.header("🔤 Statistical Summary (Categorical Features)")
        st.dataframe(df.describe(include=['object']))

    # -------------------------------
    # 9. DATA VISUALIZATION
    # -------------------------------
    elif menu == "📈 Data Visualization":
        st.header("📈 Data Visualization")

        chart_type = st.selectbox(
            "Choose Chart Type",
            ["Histogram", "Scatter Plot", "Bar Chart", "Heatmap"]
        )

        numeric_columns = df.select_dtypes(include=['number']).columns
        all_columns = df.columns

        if chart_type == "Histogram":
            col = st.selectbox("Select column", numeric_columns)
            fig, ax = plt.subplots()
            ax.hist(df[col].dropna())
            ax.set_title(f"Histogram of {col}")
            st.pyplot(fig)

        elif chart_type == "Scatter Plot":
            col1 = st.selectbox("X-axis", numeric_columns)
            col2 = st.selectbox("Y-axis", numeric_columns)
            fig, ax = plt.subplots()
            ax.scatter(df[col1], df[col2])
            ax.set_xlabel(col1)
            ax.set_ylabel(col2)
            st.pyplot(fig)

        elif chart_type == "Bar Chart":

            col = st.selectbox("Select column", df.columns)

            value_counts = df[col].value_counts().head(10)

            fig, ax = plt.subplots(figsize=(10, 5))

            x_positions = range(len(value_counts))

            ax.bar(x_positions, value_counts.values)

            ax.set_xticks(x_positions)
            ax.set_xticklabels(value_counts.index, rotation=45, ha='right')

            ax.set_title(f"Bar Chart of {col}")

            plt.tight_layout()

            st.pyplot(fig)

        elif chart_type == "Heatmap":

            st.write("Select columns for heatmap (recommended for large datasets)")

            numeric_cols = df.select_dtypes(include=['number']).columns.tolist()

            selected_cols = st.multiselect(
                "Choose columns",
                numeric_cols,
                default=numeric_cols[:10]  # show first 10 by default
            )

            if len(selected_cols) > 1:
                corr = df[selected_cols].corr()

                fig, ax = plt.subplots(figsize=(10, 6))

                sns.heatmap(
                    corr,
                    annot=True if len(selected_cols) <= 10 else False,
                    cmap="coolwarm",
                    ax=ax
                )

                ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
                plt.tight_layout()

                st.pyplot(fig)
            else:
                st.warning("Please select at least 2 columns.")

    # -------------------------------
    # 10. ANALYSIS SECTION
    # -------------------------------
    elif menu == "🧠 Analysis":
        st.header("🧠 Analysis")

        st.write("Here are some quick insights:")

        st.write("👉 Dataset has", df.shape[0], "rows and", df.shape[1], "columns.")

        if df.isnull().sum().sum() > 0:
            st.warning("There are missing values in the dataset. Consider cleaning them.")
        else:
            st.success("No missing values detected.")

        if df.duplicated().sum() > 0:
            st.warning("Duplicate rows found. Consider removing duplicates.")
        else:
            st.success("No duplicate rows found.")

    else:
        st.info("Please upload a CSV, Excel or Json file to begin.")
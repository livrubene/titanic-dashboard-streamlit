import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

plt.style.use('ggplot')

# Load data
df = pd.read_csv("Titanic-Dataset.csv")

# Page config
st.set_page_config(page_title="Titanic Explorer", layout="wide")

st.title("🚢 Titanic Data Explorer")
st.markdown("Explore passenger data from the Titanic dataset using filters.")

# Sidebar filters
st.sidebar.header("🔎 Filters")

# Gender
gender = st.sidebar.selectbox("Select Gender", ["All"] + sorted(df["Sex"].dropna().unique()))

# Passenger Class
pclass = st.sidebar.selectbox("Select Passenger Class", ["All"] + sorted(df["Pclass"].dropna().unique()))

# Age range
age_min, age_max = int(df["Age"].min()), int(df["Age"].max())
age_range = st.sidebar.slider("Select Age Range", age_min, age_max, (age_min, age_max))

# Siblings/Spouses Aboard (number input with stepper)
sibsp = st.sidebar.number_input(
    "Siblings/Spouses Aboard", 
    min_value=int(df["SibSp"].min()), 
    max_value=int(df["SibSp"].max()), 
    value=int(df["SibSp"].min()), 
    step=1
)

# Dashboard credit
st.sidebar.markdown("---")
st.sidebar.caption("📊 Dashboard created by **Liva Rubene**")

# Apply filters
filtered_df = df.copy()
if gender != "All":
    filtered_df = filtered_df[filtered_df["Sex"] == gender]
if pclass != "All":
    filtered_df = filtered_df[filtered_df["Pclass"] == pclass]

filtered_df = filtered_df[
    (filtered_df["Age"] >= age_range[0]) & 
    (filtered_df["Age"] <= age_range[1]) & 
    (filtered_df["SibSp"] == sibsp)
]

# Display filtered data
st.dataframe(filtered_df, use_container_width=True)

# Pie chart: Survival rate
st.subheader("🧍 Survival Distribution")
survival_counts = filtered_df["Survived"].value_counts().sort_index()
survival_labels = ["Did Not Survive", "Survived"]

fig_pie = px.pie(
    names=survival_labels,
    values=survival_counts.values,
    title="Survival Rate",
    color=survival_labels,
    color_discrete_map={
        "Survived": "green",
        "Did Not Survive": "darkred"
    }
)
st.plotly_chart(fig_pie)

# Bar chart: Survival by Embarkation Port
st.subheader("💬 Survival by Embarkation Port")
port_survival = filtered_df.groupby(["Embarked", "Survived"]).size().reset_index(name="Count")
port_survival["Survived"] = port_survival["Survived"].map({0: "Did Not Survive", 1: "Survived"})

fig_bar = px.bar(
    port_survival,
    x="Embarked",
    y="Count",
    color="Survived",
    barmode="group",
    title="Survival Count by Embarkation Port",
    color_discrete_map={
        "Survived": "green",
        "Did Not Survive": "darkred"
    }
)
st.plotly_chart(fig_bar)

# Raw data toggle
st.subheader("🧾 Raw Data")
if st.checkbox("Show raw data"):
    st.write(df)

# titanic-dashboard-streamlit

🚢 Titanic Data Explorer (Streamlit App)
This is a beginner-friendly interactive Streamlit app that lets you explore the Titanic dataset. Use filters like gender, age, class, and siblings/spouses aboard to discover survival insights and port-based trends.

🔍 Features
- Filter passengers by gender, age range, class, and family aboard
- Explore survival distribution with a pie chart
- View survival stats by port of embarkation
- View filtered data table and toggle raw data
- Built using Streamlit, Plotly, pandas, and Matplotlib

📁 Project Structure
- app-core.py – Main Streamlit app
- Titanic-Dataset.csv – The dataset used in the app
- requirements.txt – Python dependencies
- README.md – Project overview and instructions
- .gitignore – Exclude unnecessary files from the repo

🚀 How to Run Locally
1. Install Python 3.10+
2. Install required libraries:
   ```bash
   pip install -r requirements.txt
Run the app: 
streamlit run app-core.py

Open your browser to the localhost URL 

About This Project
This project is part of my learning journey in data storytelling and analytics. I’m experimenting with tools like Streamlit, Power BI, Shiny, and AI to bring data to life in engaging ways.

This dashboard focuses on the Titanic dataset—a classic case in data science—to help beginners explore real-world data visually. It's simple, interactive, and informative.

💡 My Approach
I started by loading the Titanic dataset using pandas.read_csv() and inspecting it. I used Streamlit's sidebar to create simple filters - gender, age, class, and number of siblings/spouses aboard.

Once filtered, the app displays:

A table of filtered passengers

A pie chart showing survival distribution using Plotly

A grouped bar chart of survival by embarkation port

A raw data toggle for full transparency

This app shows how you can build a clean, interactive data dashboard with minimal code. I used Plotly to create modern, responsive visuals, and set a global ‘ggplot’ style with matplotlib for consistent formatting. 
This app shows how you can build a data dashboard with minimal code while giving users meaningful interaction with historical data.


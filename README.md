🌍 Climate Change Trend Analyzer 📌 Overview

The Climate Change Trend Analyzer is a machine learning-based web application that analyzes historical temperature data of Indian cities and predicts future temperature trends.

This project allows users to explore climate patterns interactively by selecting a city and viewing both historical data and future predictions. It helps in understanding short-term climate behavior and raises awareness about climate change.

🚀 Features 🌆 City-based data filtering 📊 Historical temperature visualization 🔮 Future temperature prediction (tomorrow + 5-day intervals) 📈 Graphical representation (line & bar charts) 🌡️ Current temperature display ⚡ Interactive user interface

🛠️ Technologies Used Python Pandas Matplotlib Scikit-learn Streamlit

🧠 Machine Learning Model Algorithm Used: Linear Regression Input Feature: Days (time progression) Target Variable: Temperature The model learns patterns from historical data and predicts future temperature values.

📂 Dataset Indian Cities Daily Weather Data (2000–2024) Key columns used: City Date Temperature

⚙️ System Workflow User selects a city from the dropdown Data is filtered based on the selected city Preprocessing is performed (date conversion, feature creation) Machine learning model is trained Future predictions are generated Results are displayed using graphs and values

💻 Installation & Setup

Clone the repository git clone https://github.com/your-username/climate-analyzer.git cd climate-analyzer
Install dependencies pip install pandas matplotlib scikit-learn streamlit
Run the application streamlit run app.py 📸 Output 📈 Future prediction graph 📊 Historical temperature graph 🔢 Predicted temperature values 🌡️ Current temperature metric
🎯 Objectives Analyze temperature trends in Indian cities Provide short-term climate predictions Build an interactive ML-based web application Increase awareness about climate change 👥 Team Members Zuweina Shaikh Hiya Bhanushali Mahee Jain Sakshi Mudale Harshita Bhagat

📌 Future Enhancements Use advanced models (LSTM / Time Series) Add more weather parameters (humidity, pressure) Improve UI with interactive charts (Plotly) Add multi-city comparison

📄 License This project is for educational purposes.

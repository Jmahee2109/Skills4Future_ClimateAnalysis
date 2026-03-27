import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.linear_model import LinearRegression
import datetime

# ================================
# Page Config
# ================================
st.set_page_config(page_title="Climate Analyzer", layout="wide")

# ================================
# Background Styling
# ================================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #e0f7fa, #ffffff);
}
</style>
""", unsafe_allow_html=True)

# ================================
# Title
# ================================
st.title("🌍 Climate Change Trend Analyzer")
st.subheader("📊 AI Climate Decision Support System")

st.markdown("""
### 📌 Project Description
This project analyzes historical temperature data and predicts future climate trends 
using Machine Learning (Linear Regression). It also provides climate risk detection 
and AI-based recommendations for different weather conditions.
""")

# ================================
# Load Dataset
# ================================
df = pd.read_csv("india_2000_2024_daily_weather.csv")

df = df[['city', 'date', 'temperature_2m_max']]
df.columns = ['City', 'Date', 'Temperature']

df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
df = df.dropna()

# Feature Engineering
df['Days'] = (df['Date'] - df['Date'].min()).dt.days
df['Temp_Change'] = df.groupby('City')['Temperature'].diff()

# ================================
# Sidebar
# ================================
st.sidebar.markdown("## ⚙️ Controls Panel")
st.sidebar.success("AI Climate System 🌍")

city = st.sidebar.selectbox("Select City", sorted(df['City'].unique()))
days_range = st.sidebar.slider("Select Future Days", 5, 60, 30)

# ================================
# Filter Data
# ================================
city_df = df[df['City'] == city]

# ================================
# Model
# ================================
X = city_df[['Days']]
y = city_df['Temperature']

model = LinearRegression()
model.fit(X, y)

score = model.score(X, y)
st.sidebar.write(f"Model Accuracy: {score:.2f}")

# ================================
# Predictions
# ================================
last_day = city_df['Days'].max()

future_steps = [1] + list(range(5, days_range + 5, 5))

future_days = pd.DataFrame({
    'Days': [last_day + i for i in future_steps]
})

predictions = model.predict(future_days)

# ================================
# Current Temperature
# ================================
latest_temp = city_df.iloc[-1]['Temperature']
st.metric("🌡️ Current Temperature", f"{latest_temp:.2f} °C")

# ================================
# Layout
# ================================
col1, col2 = st.columns(2)

# ================================
# LEFT SIDE
# ================================
with col1:
    st.subheader("📈 Future Prediction Graph")

    fig, ax = plt.subplots()
    ax.plot(future_steps, predictions, marker='o')
    ax.set_xlabel("Days Ahead")
    ax.set_ylabel("Temperature (°C)")
    st.pyplot(fig)

    st.subheader("📊 Historical Temperature Trend")

    hist_df = city_df.tail(10)

    fig2, ax2 = plt.subplots()
    ax2.bar(hist_df['Date'].astype(str), hist_df['Temperature'])
    plt.xticks(rotation=45)
    st.pyplot(fig2)

# ================================
# RIGHT SIDE
# ================================
with col2:
    st.subheader("🔮 Prediction Values")

    for step, pred in zip(future_steps, predictions):
        if step == 1:
            st.success(f"Tomorrow: {pred:.2f} °C")
        else:
            st.success(f"After {step} days: {pred:.2f} °C")

# ================================
# 📅 Future Date Prediction
# ================================
st.subheader("📅 Future Date Prediction")

target_date = st.date_input("Select a future date")

if target_date:
    days_input = (target_date - df['Date'].min()).days
    pred_temp = model.predict([[days_input]])[0]

    st.metric("🌡 Estimated Temperature", f"{pred_temp:.2f} °C")
    st.caption("⚠ Approximate prediction based on trend")

# ================================
# 🌍 Climate Classification
# ================================
st.subheader("🌍 Climate Condition")

if latest_temp >= 35:
    climate = "Extreme Heat 🔥"
elif latest_temp >= 30:
    climate = "Hot ☀"
elif latest_temp >= 25:
    climate = "Warm 🌤"
elif latest_temp >= 20:
    climate = "Pleasant 🌿"
elif latest_temp >= 10:
    climate = "Cool 🍃"
else:
    climate = "Cold ❄"

st.markdown(f"## {climate}")

# ================================
# ⚠ Risk Detection
# ================================
st.subheader("⚠ Climate Risk Level")

if latest_temp >= 35:
    risk = "High Risk 🔥"
elif latest_temp <= 10:
    risk = "Cold Risk ❄"
elif latest_temp >= 30:
    risk = "Moderate Risk ⚠"
else:
    risk = "Low Risk 🌿"

st.write(f"Risk Level: {risk}")

# ================================
# 📊 Risk Index
# ================================
st.subheader("📊 AI Climate Risk Index")

risk_index = ((latest_temp + 5) / 50) * 100
st.progress(int(risk_index))
st.write(f"Risk Score: {risk_index:.1f} / 100")

# ================================
# 💡 Smart Suggestions
# ================================
st.subheader("💡 AI Climate Suggestions")

if latest_temp >= 35:
    st.error("🔥 Extreme Heat")
    st.write("• Stay hydrated 💧")
    st.write("• Use sunscreen 🧴")
    st.write("• Avoid afternoon sun ☀")

elif latest_temp >= 30:
    st.warning("☀ Hot Weather")
    st.write("• Wear light clothes")
    st.write("• Drink water 💧")

elif latest_temp >= 25:
    st.info("🌤 Warm Weather")
    st.write("• Comfortable outdoors")

elif latest_temp >= 20:
    st.success("🌿 Pleasant Weather")
    st.write("• Ideal for outdoor activities")

elif latest_temp >= 10:
    st.warning("🍃 Cool Weather")
    st.write("• Wear light jacket 🧥")

else:
    st.error("❄ Cold Weather")
    st.write("• Wear warm clothes 🧥")

# ================================
# 📈 Feature Engineering Display
# ================================
st.subheader("📈 Temperature Change Trend")
st.line_chart(city_df['Temp_Change'].fillna(0))

# ================================
# Footer
# ================================
st.markdown("---")
st.caption("AI Climate Decision Support System 🌍")
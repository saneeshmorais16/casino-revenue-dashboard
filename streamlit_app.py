import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv(r"C:\Users\sanee\AppData\Local\Programs\Python\Python313\casino-revenue-dashboard\data\casino_revenue_data.csv")


st.title("🎰 Casino Revenue Dashboard")
st.markdown("This dashboard analyzes simulated casino game revenue data.")

# Game selection
game_filter = st.selectbox("Select a Game", df['game'].unique())

# Filtered data
filtered_df = df[df['game'] == game_filter]

# Summary stats
st.subheader(f"Summary for {game_filter}")
st.write(filtered_df.describe())

# Revenue over time
st.subheader("Revenue Over Time")
df['timestamp'] = pd.to_datetime(df['timestamp'])
revenue_time = df[df['game'] == game_filter].groupby(df['timestamp'].dt.date)['revenue'].sum()

fig, ax = plt.subplots(figsize=(10, 5))
revenue_time.plot(ax=ax)
ax.set_title(f"Daily Revenue for {game_filter}")
ax.set_xlabel("Date")
ax.set_ylabel("Revenue")
st.pyplot(fig)

# Total revenue by shift
st.subheader("Total Revenue by Shift")
shift_revenue = df[df['game'] == game_filter].groupby('shift')['revenue'].sum().sort_values()

fig2, ax2 = plt.subplots(figsize=(6, 4))
shift_revenue.plot(kind='barh', color='skyblue', ax=ax2)
ax2.set_xlabel("Revenue")
ax2.set_title("Revenue by Shift")
st.pyplot(fig2)

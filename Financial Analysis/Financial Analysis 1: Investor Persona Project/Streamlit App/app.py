import streamlit as st
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# 🔹 Inject custom CSS styling
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# 🔹 Load and clean data
@st.cache_data
def load_data():
    df = pd.read_csv("Final Data.csv")
    df.columns = [col.strip().replace("(", "").replace(")", "").replace("[", "").replace("]", "") for col in df.columns]
    features = [
        'Age', 'Best Option: Mutual Funds', 'Best Option: Equity Market',
        'Best Optioin: Debentures', 'Best Option: Government Bonds',
        'Best Option: Fixed Deposits', 'Best Option: Public Provident Fund',
        'Best Option: Gold'
    ]
    return df[features]

# 🔹 Load data and train KMeans model
df = load_data()
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_scaled)

# 🔹 Streamlit UI
st.title("💼 Investor Persona Predictor")

st.markdown("Use the sliders to input your age and investment preferences (1 = Most Preferred, 7 = Least Preferred):")

# 🔹 Input sliders
age = st.slider("Age", 18, 65, 30)
mutual = st.slider("Mutual Funds", 1, 7, 4)
equity = st.slider("Equity Market", 1, 7, 4)
debentures = st.slider("Debentures", 1, 7, 4)
bonds = st.slider("Government Bonds", 1, 7, 4)
fds = st.slider("Fixed Deposits", 1, 7, 4)
ppf = st.slider("Public Provident Fund", 1, 7, 4)
gold = st.slider("Gold", 1, 7, 4)

# 🔹 Make prediction
user_input = np.array([[age, mutual, equity, debentures, bonds, fds, ppf, gold]])
user_scaled = scaler.transform(user_input)
cluster = kmeans.predict(user_scaled)[0]

# 🔹 Map cluster to persona
def get_persona(c):
    return {
        0: "🧠 Cautious Young Investor",
        1: "🚀 Aggressive Growth Seeker",
        2: "📈 Experienced Risk-Balancer"
    }.get(c, "Unknown")

# 🔹 Show result
st.subheader("🔍 Your Predicted Investor Persona:")
st.success(get_persona(cluster))

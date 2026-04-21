import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px  # Added Plotly

# --- Configuration ---
st.set_page_config(page_title="VC Portfolio OS", layout="wide")
DB_PATH = "portfolio.db"

# --- Helper Functions ---
import numpy as np
# ... (your other imports) ...

def load_data():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM portfolio_metrics", conn)
    conn.close()
    
    # 1. Clean MRR
    df['mrr'] = df['mrr'].astype(str).str.replace('$', '').str.replace('k', '000', case=False).str.replace('Unknown', '0')
    df['mrr'] = pd.to_numeric(df['mrr'], errors='coerce')
    
    # Fill NaN MRR with unique random values between 100 and 100,000
    mrr_nans = df['mrr'].isna()
    df.loc[mrr_nans, 'mrr'] = np.random.randint(100, 100001, size=mrr_nans.sum())
    
    # 2. Clean Runway
    df['runway_months'] = pd.to_numeric(df['runway_months'], errors='coerce')
    
    # Fill NaN Runway with unique random values between 0 and 18
    runway_nans = df['runway_months'].isna()
    df.loc[runway_nans, 'runway_months'] = np.random.randint(0, 19, size=runway_nans.sum())
    
    # Add Risk Category
    df['Risk Level'] = df['runway_months'].apply(lambda x: 'High Risk (<6 mo)' if x < 6 else 'Stable (6+ mo)')
    
    return df

if "messages" not in st.session_state:
    st.session_state.messages = []

df = load_data()

# ==========================================
# UI LAYOUT
# ==========================================
st.title("📊 Centralised Founder Database")
st.markdown("---")

# 1. TOP ROW: Macros and Graphs
st.subheader("Portfolio Health")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Total Portfolio MRR", value=f"${df['mrr'].sum():,.0f}")
with col2:
    st.metric(label="Avg Runway", value=f"{df['runway_months'].mean():.1f} Months")
with col3:
    st.metric(label="Startups at Risk (<6mo)", value=len(df[df['runway_months'] < 6]))

st.write("") # Spacer

# Plotly Graphs Row
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    # Scatter Plot: MRR vs Runway
    fig_scatter = px.scatter(
        df, x="runway_months", y="mrr", color="Risk Level",
        hover_name="startup_name", size="mrr",
        color_discrete_map={"High Risk (<6 mo)": "#ff4b4b", "Stable (6+ mo)": "#00cc96"},
        title="Risk Matrix: MRR vs. Runway",
        labels={"runway_months": "Runway (Months)", "mrr": "Monthly Recurring Revenue ($)"}
    )
    # Add quadrants
    fig_scatter.add_vline(x=6, line_dash="dash", line_color="gray")
    st.plotly_chart(fig_scatter, use_container_width=True)

with chart_col2:
    # Histogram: Runway Distribution
    fig_hist = px.histogram(
        df, x="runway_months", nbins=10, 
        title="Runway Distribution Across Portfolio",
        labels={"runway_months": "Runway (Months)"},
        color_discrete_sequence=["#636EFA"]
    )
    st.plotly_chart(fig_hist, use_container_width=True)

st.markdown("---")

# 2. MIDDLE ROW: Feed and Company Specifics
col_feed, col_company = st.columns([1, 1])

with col_feed:
    st.subheader("Recent Updates")
    st.dataframe(df[['startup_name', 'mrr', 'runway_months', 'key_challenge']], use_container_width=True, height=300)

with col_company:
    st.subheader("Company Deep Dive")
    if not df.empty:
        selected_startup = st.selectbox("Select a Startup", df['startup_name'].unique())
        startup_data = df[df['startup_name'] == selected_startup].iloc[0]
        
        st.write(f"**Reported MRR:** ${startup_data['mrr']:,.0f}")
        st.write(f"**Runway:** {startup_data['runway_months']} months")
        st.error(f"**Current Blocker:** {startup_data['key_challenge']}")
        
        with st.expander("View Raw Source Email"):
            st.text(startup_data['raw_text'])

st.write("")
st.write("")

# 3. BOTTOM ROW: Persistent RAG Chat
st.markdown("### 💬 Ask the Database")
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("E.g., Which startups are struggling with hiring right now?"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # For now, a mock response. You will wire your RAG function here.
    mock_response = f"Simulated RAG response analyzing the vector database for: '{prompt}'"
    with st.chat_message("assistant"):
        st.markdown(mock_response)
    st.session_state.messages.append({"role": "assistant", "content": mock_response})
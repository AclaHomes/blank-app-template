# bank_tools_dashboard.py
import streamlit as st

# --- App Config ---
st.set_page_config(
    page_title="Bank Tools Dashboard",
    page_icon="🏦",
    layout="wide",
)

# --- Sidebar Navigation ---
st.sidebar.title("🏦 Bank Tools App")
menu = st.sidebar.radio(
    "Choose a section:",
    [
        "🏠 Home",
        "📊 Pricing Model",
        "💰 Deposit Opportunities",
        "📑 Financials",
        "🛠️ Other Tools",
        "⚙️ Admin"
    ]
)

# --- Home Page ---
if menu == "🏠 Home":
    st.title("🏦 Bank Tools Dashboard")
    st.markdown(
        """
        Welcome to your **Bank Tools App**.  
        This dashboard is the central hub where you can access all your tools:

        - 📊 Loan Pricing Model  
        - 💰 Deposit Opportunity Reviews  
        - 📑 Financials  
        - 🛠️ Custom Apps  

        Use the sidebar to navigate between tools.  
        """
    )

# --- Pricing Model Placeholder ---
elif menu == "📊 Pricing Model":
    st.title("📊 Loan Pricing Model")
    st.info("This is a placeholder. Paste your pricing model app code here later.")

# --- Deposit Opportunities Placeholder ---
elif menu == "💰 Deposit Opportunities":
    st.title("💰 Deposit Opportunity Review")
    st.info("This is a placeholder. Paste your deposit memo generator here later.")

# --- Financials Placeholder ---
elif menu == "📑 Financials":
    st.title("📑 Company Financials")
    st.info("This is a placeholder. Add your financials uploader/analysis here later.")

# --- Other Tools Placeholder ---
elif menu == "🛠️ Other Tools":
    st.title("🛠️ Other Tools")
    st.info("This is a placeholder for any additional apps you want to integrate.")

# --- Admin Placeholder ---
elif menu == "⚙️ Admin":
    st.title("⚙️ Admin & Settings")
    st.info("This is a placeholder for settings, user accounts, or admin functions.")


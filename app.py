import streamlit as st
import pandas as pd

# CUSTOM STYLING

st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

h1 {
    color: #0f172a;
}

h2, h3 {
    color: #1e293b;
}

.stButton>button {
    background-color: #0f172a;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
}

.stTextInput>div>div>input {
    border-radius: 10px;
}

.stTextArea textarea {
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# ============================================
# PAGE CONFIGURATION
# ============================================

st.set_page_config(
    page_title="Finguard Finance & Compliance App",
    page_icon="🛡️",
    layout="wide"
)

# ============================================
# APP TITLE
# ============================================

st.title("🛡️ Finguard Finance & Compliance App")

st.markdown("""
### Fraud Detection & Complaint Resolution System For Opay, Moniepoint, Palmpay

Built for:
- Fraud Detection
- Compliance Monitoring
- Customer Complaint Resolution
- Fintech Risk Intelligence
""")

# ============================================
# SIDEBAR
# ============================================

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go To",
    [
        "Dashboard",
        "Fraud Detection",
        "Complaint Resolution",
        "Compliance Center"
    ]
)

# ============================================
# DASHBOARD PAGE
# ============================================

if page == "Dashboard":

    st.subheader("📊 Executive Dashboard")

    # METRICS
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Transactions Today", "1,240")
    col2.metric("Fraud Alerts", "12")
    col3.metric("Pending Complaints", "5")
    col4.metric("High Risk Transactions", "7")

    st.divider()

    # SAMPLE TRANSACTION DATA
    data = {
        "Txn ID": [
            "TX001",
            "TX002",
            "TX003",
            "TX004",
            "TX005"
        ],

        "User": [
            "Matthew",
            "John",
            "Grace",
            "Daniel",
            "Esther"
        ],

        "Amount": [
            5000,
            900000,
            12000,
            450000,
            7000
        ],

        "Status": [
            "Success",
            "Suspicious",
            "Success",
            "Suspicious",
            "Success"
        ],

        "Risk": [
            "Low",
            "High",
            "Low",
            "High",
            "Low"
        ]
    }

    df = pd.DataFrame(data)

    st.subheader("💳 Transaction Monitoring Table")

    st.dataframe(
        df,
        use_container_width=True
    )

    st.divider()

    st.subheader("📈 Risk Statistics")

    chart_data = pd.DataFrame({
        "Risk Level": ["Low", "Medium", "High"],
        "Transactions": [850, 300, 90]
    })

    st.bar_chart(
        chart_data.set_index("Risk Level")
    )

    st.success("✅ System Monitoring Active")


# ============================================
# FRAUD DETECTION PAGE
# ============================================

elif page == "Fraud Detection":

    st.subheader("🚨 AI Fraud Detection Engine")

    amount = st.number_input(
        "Enter Transaction Amount (₦)",
        min_value=0
    )

    frequency = st.number_input(
        "Number of Transactions in Last Hour",
        min_value=0
    )

    location = st.selectbox(
        "Transaction Location",
        [
            "Lagos",
            "Abuja",
            "Port Harcourt",
            "Kano",
            "Unknown"
        ]
    )

    if st.button("Analyze Transaction"):

        if amount > 500000:
            st.error(
                "🚨 HIGH FRAUD RISK DETECTED"
            )

            st.write("""
Reasons:
- Unusually high transaction value
- Possible rapid movement of funds
- Requires compliance review
            """)

        elif frequency > 10:
            st.warning(
                "⚠️ Suspicious Rapid Transactions Detected"
            )

            st.write("""
Possible fraud pattern:
- Multiple rapid transactions
- Potential bot activity
- Requires investigation
            """)

        elif location == "Unknown":
            st.warning(
                "⚠️ Unknown transaction location detected"
            )

        else:
            st.success(
                "✅ Transaction appears safe"
            )

# ============================================
# COMPLAINT RESOLUTION PAGE
# ============================================

elif page == "Complaint Resolution":

    st.subheader("💬 AI Complaint Resolution Agent")

    customer_name = st.text_input(
        "Customer Name"
    )

    complaint = st.text_area(
        "Describe Your Complaint"
    )

    if st.button("Submit Complaint"):

        st.info(
            "🤖 AI Agent is reviewing complaint..."
        )

        # SIMPLE AI LOGIC
        complaint_lower = complaint.lower()

        if "reversal" in complaint_lower:

            st.success("""
Transaction Issue Identified:
- Delayed reversal detected

AI Recommendation:
- Expected reversal within 30 minutes
- Escalate if unresolved after 24 hours
            """)

        elif "debit" in complaint_lower:

            st.success("""
Issue Identified:
- Unauthorized debit complaint

AI Recommendation:
- Freeze suspicious account temporarily
- Send to fraud investigation unit
            """)

        elif "transfer" in complaint_lower:

            st.success("""
Issue Identified:
- Transfer processing issue

AI Recommendation:
- Network timeout suspected
- Verify recipient bank response
            """)

        else:

            st.success("""
Complaint received successfully.

AI Recommendation:
- Ticket generated
- Compliance team notified
- Await further review
            """)

# ============================================
# COMPLIANCE CENTER
# ============================================

elif page == "Compliance Center":

    st.subheader("🛡️ Compliance Monitoring Center")

    st.write("""
This section helps compliance officers monitor:
- Suspicious transactions
- AML risks
- Rapid transfers
- Customer complaint trends
""")

    compliance_data = pd.DataFrame({

        "Alert Type": [
            "AML Alert",
            "Rapid Transfers",
            "Unauthorized Debit",
            "High Volume Transfer"
        ],

        "Cases": [
            4,
            7,
            2,
            3
        ]
    })

    st.table(compliance_data)

    st.warning("""
⚠️ Compliance Notice:
7 transactions require manual compliance review.
""")

    st.success("""
✅ Compliance monitoring system operational.
""")
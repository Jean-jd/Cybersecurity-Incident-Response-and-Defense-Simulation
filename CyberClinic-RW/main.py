
import streamlit as st
import csv
from datetime import datetime

LOG_FILE = "logs.txt"

# === Load Threat Responses from CSV ===
def load_threat_responses():
    responses = {}
    try:
        with open('threats.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                responses[row['threat'].strip().lower()] = row['response']
    except FileNotFoundError:
        st.error("Threat database file 'threats.csv' not found! Please generate it first.")
    return responses

THREAT_RESPONSES = load_threat_responses()

def get_response_for_threat(threat):
    return THREAT_RESPONSES.get(threat.strip().lower(), "No specific response available. Follow general incident response procedures.")

# === Logging Functions ===
def log_action(category, entry):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] {category} - {entry}\n"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_line)

def read_logs():
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            return f.readlines()
    except FileNotFoundError:
        return []

# === Streamlit UI ===
st.set_page_config(page_title="CyberShield-RW", layout="wide")
st.title("CyberShield-RW: Incident Response & Defense Toolkit")

menu = [
    "Threat Modeling", 
    "Defense Strategy", 
    "Incident Response Plan", 
    "Risk Management (NIST)",
    "Problem Solving Log", 
    "Communication Strategy", 
    "Download Report"
]
choice = st.sidebar.selectbox("Navigate", menu)

if choice == "Threat Modeling":
    st.header("Threat Modeling")

    threat_list = sorted(THREAT_RESPONSES.keys())
    threat_display_names = [t.title() for t in threat_list]  # capitalize for display

    with st.form(key="threat_form"):
        asset = st.text_input("Asset (e.g., Database Server)")
        selected_index = st.selectbox("Select Threat", range(len(threat_display_names)), format_func=lambda x: threat_display_names[x])
        threat = threat_list[selected_index]
        vulnerability = st.text_input("Vulnerability (e.g., Unvalidated Input)")
        submit = st.form_submit_button("Add to Threat Model")

        if submit:
            response = get_response_for_threat(threat)
            entry = f"Asset: {asset}, Threat: {threat.title()}, Vulnerability: {vulnerability} | Suggested Response: {response}"
            log_action("Threat Modeling", entry)
            st.success("Threat model entry logged.")
            st.subheader("Suggested Response Actions")
            st.code(response)

elif choice == "Defense Strategy":
    st.header("Defense Strategy")
    with st.form(key="defense_form"):
        defense_layer = st.selectbox("Defense Layer", ["Network", "Application", "Endpoint", "User Training"])
        strategy = st.text_area("Defense Strategy Details")
        submit = st.form_submit_button("Save Defense Strategy")
        if submit:
            entry = f"Layer: {defense_layer}, Strategy: {strategy}"
            log_action("Defense Strategy", entry)
            st.success("Defense strategy logged.")

elif choice == "Incident Response Plan":
    st.header("Incident Response Guide")
    with st.form(key="response_form"):
        phase = st.radio("Phase", ["Detection", "Containment", "Eradication", "Recovery"])
        action_taken = st.text_area(f"Action taken during {phase} phase")
        submit = st.form_submit_button("Log Action")
        if submit:
            entry = f"Phase: {phase}, Action: {action_taken}"
            log_action("Incident Response", entry)
            st.success("Incident response action logged.")

elif choice == "Risk Management (NIST)":
    st.header("Risk Management (NIST Framework)")
    st.write("Enter risk assessment details and mitigation plans below.")
    with st.form(key="risk_form"):
        risk_description = st.text_area("Risk Description")
        mitigation_plan = st.text_area("Mitigation Plan")
        submit = st.form_submit_button("Log Risk Management Entry")
        if submit:
            entry = f"Risk: {risk_description}, Mitigation: {mitigation_plan}"
            log_action("Risk Management", entry)
            st.success("Risk management entry logged.")

elif choice == "Communication Strategy":
    st.header("Communication Strategy")
    st.write("Document communication protocols for internal and external stakeholders.")
    with st.form(key="comm_form"):
        audience = st.text_input("Audience (e.g., Internal Team, Public, Management)")
        message = st.text_area("Communication Message / Protocol")
        submit = st.form_submit_button("Log Communication Strategy")
        if submit:
            entry = f"Audience: {audience}, Message: {message}"
            log_action("Communication Strategy", entry)
            st.success("Communication strategy logged.")

elif choice == "Problem Solving Log":
    st.header("Problem Solving Log")
    logs = read_logs()
    if not logs:
        st.info("No logs have been recorded yet.")
    else:
        st.write("All logged actions so far:")
        for log_entry in logs:
            st.write(log_entry.strip())

elif choice == "Download Report":
    st.header("Download Incident Report")
    logs = read_logs()
    if not logs:
        st.info("No logs to download.")
    else:
        report = "".join(logs)
        st.download_button(label="Download Log Report", data=report, file_name="cybershield_report.txt")
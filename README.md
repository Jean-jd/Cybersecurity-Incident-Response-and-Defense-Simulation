CyberShield-RW

Overview

CyberShield-RW is a Streamlit-based web application that helps cybersecurity professionals and learners simulate and manage incident response operations. It mimics real-world Security Operations Center (SOC) workflows. The app assists in identifying threats, logging response actions, assessing risks with NIST controls, and generating professional reports.

Inspiration

CyberShield-RW was created in response to the increasing threat landscape and the limited availability of accessible tools for organized incident response. By following the NIST Incident Response Framework, it offers a practical learning and operational platform.

Features

- Threat Modeling: Identify assets, threats, and vulnerabilities with guided response actions.

- Incident Response Plan: Log actions across phases: Detection, Containment, Eradication, and Recovery.

- Risk Management: Use NIST controls and calculate real-time risk scores.

- Problem Solving Log: Document decisions and root cause analyses.

- Communication Strategy: Create internal and public communication templates.

- Report Generation: Download a detailed incident report.

Built With

- Languages: Python 3.13

- Frameworks/Libraries: Streamlit, Pandas, SQLite3

- Platform: Kali Linux

- Database: SQLite

- Version Control: GitHub

- Inspiration Tools: Metasploit, Nmap, OWASP ZAP, Nikto (conceptual reference)

Installation

git clone https://github.com/Jean-jd/cybershield-rw.git
cd  cybershield-rw 
python3 -m venv cyberenv  
source cyberenv/bin/activate  
pip install -r requirements.txt  
streamlit run main.py  

How to Use It

- Launch App: After running the app, it opens in your browser.

- Select a Threat: Enter or choose a known threat (e.g., “Phishing”, “DDoS”) to get a detailed response guide.

- Log Incident Steps:  

  - Fill in Detection, Containment, Eradication, and Recovery actions.  

  - Each entry saves in the app’s internal log.  

- Calculate Risk: Go to the Risk Management tab, input control effectiveness, and see your risk score.

- Problem-Solving Log: Document any issues encountered, root causes, and solutions.

- Communication: Write internal and public response messages for the incident.

- Export: Download a report summarizing all actions and findings for audit or sharing.

What We Learned

- How to build modular and scalable apps with Streamlit

- Applying NIST Risk Management in a functional tool

- Focusing on human-centered design for professional use

Future Improvements

- AI-powered threat detection

- Role-based access for multiple users

- PDF/Excel report export

- Integration with external incident systems

License

MIT License

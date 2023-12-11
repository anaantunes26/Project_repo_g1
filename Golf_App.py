import streamlit as st

class GolfApp:
    def __init__(self):
        self.accounts = []
        self.courses = []

    def load_accounts(self):
        # Muster-Accounts
        self.accounts = [
            {"Benutzername": "casual_golfer123", "E-Mail": "casualgolfer123@example.com", "Passwort": "Golfer123!", "Mitgliedschaft": "Basic"},
            {"Benutzername": "golf_enthusiast45", "E-Mail": "golfenthusiast45@example.com", "Passwort": "GreenSwing45@", "Mitgliedschaft": "Premium"},
            {"Benutzername": "pro_golfer89", "E-Mail": "progolfer89@example.com", "Passwort": "ProPassion89$", "Mitgliedschaft": "Elite"}
        ]
        st.write("Accounts wurden geladen!")

    def load_courses(self):
        # Golfplätze in der Schweiz
        self.courses = [
            {"Name": "Swiss Alps Golf Club", "Ort": "Crans-Montana", "Beschreibung": "Ein atemberaubender Golfplatz in den Schweizer Alpen mit Panoramablicken und anspruchsvollen Löchern."},
            {"Name": "Lake Geneva Golf Resort", "Ort": "Genf", "Beschreibung": "Ein exklusiver Golfplatz am Genfer See mit Blick auf das Wasser und eine perfekte Kombination aus Herausforderung und Schönheit."},
            {"Name": "Zurich Valley Golf Club", "Ort": "Zürich", "Beschreibung": "Ein moderner Golfplatz in der Nähe von Zürich, der eine erstklassige Spielumgebung mit hochwertigen Einrichtungen bietet."}
        ]
        st.write("Golfplätze wurden geladen!")

# Erstellen einer Instanz der GolfApp
golf_app = GolfApp()

# Laden von Accounts und Golfplätzen
golf_app.load_accounts()
golf_app.load_courses()

# Anzeige der geladenen Daten in Streamlit
st.write("### Geladene Muster-Accounts:")
for account in golf_app.accounts:
    st.write(f"**Benutzername:** {account['Benutzername']}, **E-Mail:** {account['E-Mail']}, **Mitgliedschaft:** {account['Mitgliedschaft']}")

st.write("### Geladene Golfplätze in der Schweiz:")
for course in golf_app.courses:
    st.write(f"**Name:** {course['Name']}, **Ort:** {course['Ort']}")
    st.write(f"**Beschreibung:** {course['Beschreibung']}")
    st.write("---")


SOLLTE IN FABIO.py reingetan werden:

# FABIO.py

from Golf_App import GolfApp  # Importing the GolfApp class from Golf_App.py

# Create an instance of GolfApp
golf_app = GolfApp()

# Load data or perform actions from Golf_App.py
if st.button("Load Data"):
    golf_app.load_accounts()
    golf_app.load_courses()

# Display the loaded data in Streamlit
st.write("Geladene Muster-Accounts:")
for account in golf_app.accounts:
    st.write(f"**Benutzername:** {account['Benutzername']}, **E-Mail:** {account['E-Mail']}, **Mitgliedschaft:** {account['Mitgliedschaft']}")

st.write("Golfplätze in der Schweiz:")
for course in golf_app.courses:
    st.write(f"**Name:** {course['Name']}, **Ort:** {course['Ort']}")
    st.write(f"**Beschreibung:** {course['Beschreibung']}")
    st.markdown("---")

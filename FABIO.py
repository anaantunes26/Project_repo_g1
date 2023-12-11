import streamlit as st

st.title("Welcome to the Golf App!")

menu_choice = st.sidebar.radio("Menu", ["Home", "Register", "Login", "Exit"])

if menu_choice == "Home":
    st.write("This is the home page.")

elif menu_choice == "Register":
    st.subheader("Registration:")
    first_name = st.text_input("Enter your first name:")
    last_name = st.text_input("Enter your last name:")
    handicap = st.number_input("Enter your handicap:", min_value=0, step=1)
    username = st.text_input("Enter your username:")
    password = st.text_input("Enter your password:", type="password", key="register_password")
    account_type = st.radio("Register as user or admin?", ["User", "Admin"])
    is_admin = account_type == "Admin"

    if st.button("Register"):
        golf_app.accounts.append(golf_app.create_account(first_name, last_name, handicap, username, password, is_admin))
        golf_app.save_accounts()

elif menu_choice == "Login":
    st.subheader("Login:")
    username = st.text_input("Enter your username:")
    password = st.text_input("Enter your password:", type="password", key="login_password")

    if st.button("Login"):
        if golf_app.login(username, password):
            st.success("Login successful.")
            if golf_app.current_user.is_admin:
                st.sidebar.success("Logged in as Admin")
            else:
                st.sidebar.success("Logged in as User")
        else:
            st.error("Invalid username or password. Please try again.")

elif menu_choice == "Exit":
    # Save the courses before exiting
    golf_app.save_courses()
    st.balloons()
    st.write("Goodbye!")
    st.stop()

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
            {"Swiss Alps Golf Club", "Crans-Montana", "Beschreibung:" "Ein atemberaubender Golfplatz in den Schweizer Alpen mit Panoramablicken und anspruchsvollen Löchern."},
            {"Lake Geneva Golf Resort", "Genf", "Beschreibung:" "Ein exklusiver Golfplatz am Genfer See mit Blick auf das Wasser und eine perfekte Kombination aus Herausforderung und Schönheit."},
            {"Zurich Valley Golf Club", "Zürich", "Beschreibung:" "Ein moderner Golfplatz in der Nähe von Zürich, der eine erstklassige Spielumgebung mit hochwertigen Einrichtungen bietet."}
        ]
        st.write("Golfplätze wurden geladen!")

# Erstellen einer Instanz der GolfApp
golf_app = GolfApp()

# Laden von Accounts und Golfplätzen
golf_app.load_accounts()
golf_app.load_courses()

# Anzeige der geladenen Daten in Streamlit
st.write("Muster-Accounts:")
for account in golf_app.accounts:
    st.header(f"**Benutzername:** {account['Benutzername']}, **E-Mail:** {account['E-Mail']}, **Mitgliedschaft:** {account['Mitgliedschaft']}")

st.write("Golfplätze in der Schweiz:")
for course in golf_app.courses:
    st.write(f"**Name:** {course['Name']}, **Ort:** {course['Ort']}")
    st.write(f"**Beschreibung:** {course['Beschreibung']}")
    st.markdown("---")
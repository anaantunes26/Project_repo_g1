import streamlit as st

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

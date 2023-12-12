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
    first_name = st.text_input("Enter your first name:")
    last_name = st.text_input("Enter your last name:")
    handicap = st.number_input("Enter your handicap:", min_value=0, step=1)
    username = st.text_input("Enter your username:")
    password = st.text_input("Enter your password:", type="password")
    account_type = st.radio("Register as user or admin?", ["User", "Admin"])
    is_admin = account_type == "Admin"

    if golf_app.create_account(first_name, last_name, handicap, username, password, is_admin):
        golf_app.save_accounts()
        st.success("Registration successful!")
    else:
        st.error("Username already exists. Please choose a different one.")

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
    GolfApp.save_courses()
    st.balloons()
    st.write("Goodbye!")
    st.stop()

if golf_app.current_user:
    st.sidebar.subheader(f"Logged in as: {golf_app.current_user.username}")

    if golf_app.current_user.is_admin:
        st.sidebar.info("Admin actions:")
        admin_choice = st.sidebar.radio("Select an action", ["Add Golf Course", "Delete Golf Course", "Logout"])

        if admin_choice == "Add Golf Course":
            st.subheader("Add Golf Course:")
            course_name = st.text_input("Enter the name of the course:")
            holes = []
            for i in range(1, 19):
                st.write(f"Enter details for Hole {i}:")
                par = st.number_input(f"Par for Hole {i}:", min_value=1, step=1)
                stroke_index = st.number_input(f"Stroke Index for Hole {i}:", min_value=1, step=1)
                holes.append({"hole_number": i, "par": par, "stroke_index": stroke_index})
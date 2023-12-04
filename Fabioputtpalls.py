import streamlit as st

class Hole:
    def __init__(self, hole_number, par, stroke_index):
        self.hole_number = hole_number
        self.par = par
        self.stroke_index = stroke_index

    def __str__(self):
        return f"Hole {self.hole_number} - Par: {self.par}, Stroke Index: {self.stroke_index}"

# ... (die anderen Klassen bleiben unverändert)

class GolfApp:
    # ... (die restlichen Methoden und Eigenschaften bleiben unverändert)

def main():
    golf_app = GolfApp()

    # Lade vorhandene Konten und Kurse
    golf_app.load_accounts()
    golf_app.load_courses()

    st.title("Golf App")

    while True:
        st.write("\nWelcome to the Golf App!")
        choice = st.radio("Select an option:", ('Register', 'Login', 'Exit'))

        if choice == 'Register':
            st.write("Registration:")
            first_name = st.text_input("Enter your first name:")
            last_name = st.text_input("Enter your last name:")
            handicap = st.number_input("Enter your handicap:", min_value=0)
            username = st.text_input("Enter your username:")
            password = st.text_input("Enter your password:", type="password")
            account_type = st.selectbox("Register as user or admin?", ('user', 'admin'))
            is_admin = account_type == 'admin'
            account = Account(first_name, last_name, handicap, username, password, is_admin)
            golf_app.accounts.append(account)
            golf_app.save_accounts()
        elif choice == 'Login':
            st.write("Login:")
            username = st.text_input("Enter your username:")
            password = st.text_input("Enter your password:", type="password")
            if golf_app.login(username, password):
                if golf_app.current_user.is_admin:
                    golf_app.admin_actions()
                else:
                    golf_app.user_actions()
            else:
                st.write("Invalid username or password. Please try again.")
        elif choice == 'Exit':
            golf_app.save_courses()
            st.write("Goodbye!")
            break

if __name__ == "__main__":
    main()

import streamlit as st

class Hole:
    # Hole-Klasse bleibt unverändert

# Die restlichen Klassen bleiben auch unverändert

class GolfApp:
    # GolfApp-Klasse bleibt unverändert

    def user_actions(self):
        while True:
            st.write("\nUser Menu:")
            user_choice = st.selectbox("Select an option:", ('Choose a Golf Course', 'Enter Scores', 'Calculate Total Score', 'Compete with Other Users', 'Logout'))

            if user_choice == 'Choose a Golf Course':
                course = self.get_course_choice()
                self.play_golf(course)
            elif user_choice == 'Enter Scores':
                if not self.current_user:
                    st.write("Please login first.")
                else:
                    course = self.get_course_choice()
                    self.play_golf(course)
            elif user_choice == 'Calculate Total Score':
                if not self.current_user:
                    st.write("Please login first.")
                else:
                    st.write(f"Total Score: {self.calculate_total_score()}")
            elif user_choice == 'Compete with Other Users':
                if not self.current_user:
                    st.write("Please login first.")
                else:
                    self.compete_with_users()
            elif user_choice == 'Logout':
                break
            else:
                st.write("Invalid choice. Please enter a valid option.")

    # Die restlichen Methoden bleiben unverändert

def main():
    golf_app = GolfApp()

    # Lade vorhandene Konten und Kurse
    golf_app.load_accounts()
    golf_app.load_courses()

    st.title("Welcome to the Golf App!")

    while True:
        choice = st.radio("Select an option:", ('Register', 'Login', 'Exit'))

        if choice == 'Register':
            st.write("Registration:")
            first_name = st.text_input("Enter your first name:")
            last_name = st.text_input("Enter your last name:")
            handicap = st.number_input("Enter your handicap:", min_value=0)
            username = st.text_input("Enter your username:")
            password = st.text_input("Enter your password:", type="password")
            account_type = st.selectbox("Register as user or admin?", ('user', 'admin'))
            is_admin = account_type == 'admin'
            account = Account(first_name, last_name, handicap, username, password, is_admin)
            golf_app.accounts.append(account)
            golf_app.save_accounts()
        elif choice == 'Login':
            st.write("Login:")
            username = st.text_input("Enter your username:")
            password = st.text_input("Enter your password:", type="password")
            if golf_app.login(username, password):
                if golf_app.current_user.is_admin:
                    golf_app.admin_actions()
                else:
                    golf_app.user_actions()
            else:
                st.write("Invalid username or password. Please try again.")
        elif choice == 'Exit':
            golf_app.save_courses()
            st.write("Goodbye!")
            break

if __name__ == "__main__":
    main()

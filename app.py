import streamlit as st  

class Hole:
    def __init__(self, hole_number, par, stroke_index):
        self.hole_number = hole_number
        self.par = par
        self.stroke_index = stroke_index

    def __str__(self):
        return f"Hole {self.hole_number} - Par: {self.par}, Stroke Index: {self.stroke_index}"


class Player:
    def __init__(self, name, handicap):
        self.name = name
        self.handicap = handicap
        self.scores = {}  # Dictionary to store scores for each round

    def play_round(self, course):
        round_scores = {}
        print(f"\nPlaying at {course.name}...")
        for hole in course.holes:
            print(hole)
            strokes = int(input(f"Enter strokes for Hole {hole.hole_number}: "))
            round_scores[hole.hole_number] = strokes

        round_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.scores[round_date] = {"course": course.name, "scores": round_scores}
        print("\nRound completed!")

    def show_previous_rounds(self):
        if not self.scores:
            print("No previous rounds.")
            return

        print("\nPrevious Rounds:")
        print("{:<20} {:<20} {:<20}".format("Course", "Score", "Date"))
        for date, data in self.scores.items():
            total_score = sum(data["scores"].values())
            print("{:<20} {:<20} {:<20}".format(data["course"], total_score, date))

    def compete_with_friend(self, friend):
        print("\nComparing with your friend...")
        user_scores = self.scores.values()
        friend_scores = friend.scores.values()

        if not user_scores or not friend_scores:
            print("No rounds to compare.")
            return

        user_total = sum(sum(round["scores"].values()) for round in user_scores)
        friend_total = sum(sum(round["scores"].values()) for round in friend_scores)

        print(f"{self.name}'s total score: {user_total}")
        print(f"{friend.name}'s total score: {friend_total}")

    def __str__(self):
        return f"{self.name} - Handicap: {self.handicap}"


class Course:
    def __init__(self, name, holes):
        self.name = name
        self.holes = holes


class Account:
    def __init__(self, first_name, last_name, handicap, username, password, is_admin=False):
        self.first_name = first_name
        self.last_name = last_name
        self.handicap = handicap
        self.username = username
        self.password = password
        self.is_admin = is_admin
        self.player = Player(f"{first_name} {last_name}", handicap)

class GolfApp:
    def __init__(self):
        self.accounts = []
        self.current_user = None
        self.courses = []  # List to store available golf courses

    def save_accounts(self, filename='accounts.txt'):
        with open(filename, 'w') as file:
            for account in self.accounts:
                file.write(f"{account.first_name},{account.last_name},{account.handicap},{account.username},{account.password},{account.is_admin}\n")

    def load_accounts(self, filename='accounts.txt'):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    first_name, last_name, handicap, username, password, is_admin = data
                    handicap = int(handicap)
                    is_admin = is_admin.lower() == 'true'
                    account = Account(first_name, last_name, handicap, username, password, is_admin)
                    self.accounts.append(account)
        except FileNotFoundError:
            pass

    def save_courses(self, filename='courses.txt'):
        with open(filename, 'w') as file:
            for course in self.courses:
                file.write(f"{course.name}\n")
                for hole in course.holes:
                    file.write(f"{hole.hole_number},{hole.par},{hole.stroke_index}\n")

    def load_courses(self, filename='courses.txt'):
        try:
            with open(filename, 'r') as file:
                line_iter = iter(file)
                while True:
                    try:
                        course_name = next(line_iter).strip()
                        holes = []
                        for _ in range(18):
                            hole_data = next(line_iter).strip().split(',')
                            hole_number, par, stroke_index = map(int, hole_data)
                            holes.append(Hole(hole_number, par, stroke_index))
                        course = Course(course_name, holes)
                        self.courses.append(course)
                    except StopIteration:
                        break
        except FileNotFoundError:
            pass

    def create_account(self):
        print("Registration:")
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        handicap = int(input("Enter your handicap: "))
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        account_type = input("Register as user or admin? (user/admin): ").lower()
        is_admin = account_type == 'admin'
        account = Account(first_name, last_name, handicap, username, password, is_admin)
        self.accounts.append(account)

    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        for account in self.accounts:
            if account.username == username and account.password == password:
                self.current_user = account
                return True
        return False

class GolfCourse:
    def __init__(self, name):
        self.name = name

class GolfCourseAdmin:
    def __init__(self):
        self.courses = []
        self.admin_choice = None  # Variable to store admin choice

    def create_custom_course(self):
        name = st.text_input("Enter the name of the new golf course:")
        return GolfCourse(name)

    def admin_actions(self):
        st.title("Admin Menu")
        self.admin_choice = st.selectbox("Select an action:",
                                         ("Select an action", "Add Golf Course", "Delete Golf Course", "Logout"))

        if self.admin_choice == "Add Golf Course":
            st.subheader("Add Golf Course")
            course = self.create_custom_course()
            self.courses.append(course)
            st.success(f"Golf Course '{course.name}' added.")

        elif self.admin_choice == "Delete Golf Course":
            st.subheader("Delete Golf Course")
            if len(self.courses) == 0:
                st.warning("No golf courses available to delete.")
            else:
                st.write("Available Golf Courses:")
                selected_course = st.selectbox("Select a course to delete:",
                                              [course.name for course in self.courses],
                                              key="delete_course")  # Unique key for this selectbox
                course_to_delete = next((course for course in self.courses if course.name == selected_course), None)
                if course_to_delete:
                    self.courses.remove(course_to_delete)
                    st.success(f"Golf Course '{course_to_delete.name}' deleted.")
                else:
                    st.error("Course not found.")

        elif self.admin_choice == "Logout":
            pass  # Logout action placeholder

        else:
            st.warning("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    admin = GolfCourseAdmin()
    admin.admin_actions()

def user_actions(golf_club):
    while True:
        st.subheader("User Menu:")
        st.write("1. Let's play!")
        st.write("2. Show previous games")
        st.write("3. Compete with your puttpals")
        st.write("4. Logout")
        user_choice = st.text_input("Enter your choice (1-4): ")

        if user_choice == '1':
            if not golf_club.current_user or not golf_club.current_user.player:
                st.write("Please login first.")
            else:
                golf_club.play_golf()
        elif user_choice == '2':
            if not golf_club.current_user or not golf_club.current_user.player:
                st.write("Please login first.")
            else:
                golf_club.current_user.player.show_previous_rounds()
        elif user_choice == '3':
            if not golf_club.current_user or not golf_club.current_user.player:
                st.write("Please login first.")
            else:
                friend_username = st.text_input("Enter the username of your friend: ")
                friend = next((account for account in golf_club.accounts if account.username == friend_username), None)
                if friend and friend.is_admin:
                    st.write("Cannot compete with an admin.")
                elif friend:
                    golf_club.current_user.player.compete_with_friend(friend.player)
                else:
                    st.write(f"No user found with the username '{friend_username}'.")
        elif user_choice == '4':
            break
        else:
            st.write("Invalid choice. Please enter a valid option.")

# Create an instance of your GolfClub class
golf_club = GolfClub()

# Run Streamlit
if __name__ == '__main__':
    st.title("Golf Club App")
    user_actions(golf_club)

    class GolfClub:
    def __init__(self, name, location, description):
        self.name = name
        self.location = location
        self.description = description

# Erstellen von Instanzen für drei Golfclubs in der Schweiz
golfclub_1 = GolfClub(
    name="Golfclub Davos",
    location="Davos, Graubünden",
    description="Ein renommierter Golfclub in den Schweizer Alpen mit einem 18-Loch-Meisterschaftsplatz."
)

golfclub_2 = GolfClub(
    name="Golfclub Bad Ragaz",
    location="Bad Ragaz, St. Gallen",
    description="Ein exklusiver Golfclub mit einem 36-Loch-Platz, der sich in der Nähe der Alpen befindet."
)

golfclub_3 = GolfClub(
    name="Golfclub Genève",
    location="Genf",
    description="Ein eleganter Golfclub mit Blick auf den Genfer See, bekannt für seinen anspruchsvollen 18-Loch-Kurs."
)

# Zugriff auf Informationen der Golfclubs
print("Golfclub 1:", golfclub_1.name, "in", golfclub_1.location)
print("Beschreibung:", golfclub_1.description)
print("-----")
print("Golfclub 2:", golfclub_2.name, "in", golfclub_2.location)
print("Beschreibung:", golfclub_2.description)
print("-----")
print("Golfclub 3:", golfclub_3.name, "in", golfclub_3.location)
print("Beschreibung:", golfclub_3.description)

class GolfClub:
    def __init__(self, name, location, description):
        self.name = name
        self.location = location
        self.description = description

# Erstellen von Instanzen für drei Golfclubs in der Schweiz
golfclub_1 = GolfClub(
    name="Golfclub Davos",
    location="Davos, Graubünden",
    description="Ein renommierter Golfclub in den Schweizer Alpen mit einem 18-Loch-Meisterschaftsplatz."
)

golfclub_2 = GolfClub(
    name="Golfclub Bad Ragaz",
    location="Bad Ragaz, St. Gallen",
    description="Ein exklusiver Golfclub mit einem 36-Loch-Platz, der sich in der Nähe der Alpen befindet."
)

golfclub_3 = GolfClub(
    name="Golfclub Genève",
    location="Genf",
    description="Ein eleganter Golfclub mit Blick auf den Genfer See, bekannt für seinen anspruchsvollen 18-Loch-Kurs."
)

# Streamlit-Anwendung zur Anzeige der Golfclub-Informationen
st.title("Schweizer Golfclubs")

# Funktion, um Golfclub-Informationen anzuzeigen
def show_golfclub_info(golfclub):
    st.subheader(golfclub.name)
    st.write("Ort:", golfclub.location)
    st.write("Beschreibung:", golfclub.description)
    st.write("----")

# Anzeige der Informationen zu den erstellten Golfclubs
st.header("Informationen zu den Golfclubs:")
show_golfclub_info(golfclub_1)
show_golfclub_info(golfclub_2)
show_golfclub_info(golfclub_3)

    description="Ein eleganter Golfclub mit Blick auf den Genfer See, bekannt für seinen anspruchsvollen 18-Loch-Kurs."
)

# Streamlit-Anwendung zur Anzeige der Golfclub-Informationen
st.title("Schweizer Golfclubs")

# Funktion, um Golfclub-Informationen anzuzeigen
def show_golfclub_info(golfclub):
    st.subheader(golfclub.name)
    st.write("Ort:", golfclub.location)
    st.write("Beschreibung:", golfclub.description)
    st.write("----")

# Anzeige der Informationen zu den erstellten Golfclubs
st.header("Informationen zu den Golfclubs:")
show_golfclub_info(golfclub_1)
show_golfclub_info(golfclub_2)
show_golfclub_info(golfclub_3)
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
        self.scores = {}

    def play_hole(self, hole, strokes):p
        self.scores[hole.hole_number] = strokes

    def calculate_total_score(self):
        return sum(self.scores.values())

    def __str__(self):
        return f"{self.name} - Handicap: {self.handicap}, Total Score: {self.calculate_total_score()}"

class Course:
    def __init__(self, name, holes):
        self.name = name
        self.holes = holes

def get_player_info():
    name = st.text_input("Enter player's name:")
    handicap = st.number_input("Enter your handicap:", min_value=0)
    return Player(name, handicap)

def create_custom_course():
    course_name = st.text_input("Enter the name of the course:")
    holes = []
    for i in range(1, 19):
        st.write(f"Enter details for Hole {i}:")
        par = st.number_input(f"Par for Hole {i}:", min_value=1)
        stroke_index = st.number_input(f"Stroke Index for Hole {i}:", min_value=1)
        holes.append(Hole(i, par, stroke_index))
    return Course(course_name, holes)

def get_course_choice():
    st.write("Choose a golf course:")
    st.write("1. Ostschweizerischer Golfclub Niederbüren")
    st.write("2. Golfclub Appenzell")
    st.write("3. Golfpark Waldkirch")
    st.write("4. Create a new course")
    choice = st.selectbox("Enter your choice (1-4):", ('1', '2', '3', '4'))
    
    if choice == '1':
        predefined_holes = [Hole(1, 5, 13), Hole(2, 4, 9), ...]  # Define holes here
        return Course("Ostschweizerischer Golfclub Niederbüren", predefined_holes)
    # Rest of the code remains the same for other choices

def main():
    st.title("Golf Score Tracker")
    course = get_course_choice()
    players = []

    while True:
        player = get_player_info()
        players.append(player)

        for hole in course.holes:
            st.write(hole)
            strokes = st.number_input(f"Enter strokes for Hole {hole.hole_number}:")
            player.play_hole(hole, strokes)

        another_player = st.radio("Is there another player?", ('Yes', 'No'))
        if another_player == 'No':
            break

    players.sort(key=lambda x: x.calculate_total_score())
    st.header(f"Results at {course.name}:")
    for player in players:
        st.write(player)

if __name__ == "__main__":
    main()




from golf_app import current_user  # Stelle sicher, dass der Import korrekt ist

if hasattr(golf_app, 'current_user') and golf_app.current_user:
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

            if st.button("Add Golf Course"):
                golf_app.courses.append(golf_app.create_custom_course(course_name, holes))
                golf_app.save_courses()

        elif admin_choice == "Delete Golf Course":
            st.subheader("Delete Golf Course:")
            if not golf_app.courses:
                st.warning("No courses available for deletion.")
            else:
                course_options = [course.name for course in golf_app.courses]
                course_to_delete = st.selectbox("Select a course to delete:", course_options)
                if st.button("Delete Course"):
                    golf_app.courses = [course for course in golf_app.courses if course.name != course_to_delete]
                    golf_app.save_courses()
                    st.success(f"Golf Course '{course_to_delete}' deleted.")

        elif admin_choice == "Logout":
            golf_app.current_user = None
            st.success("Logged out.")
            st.sidebar.warning("Admin logged out.")

    else:  # User actions
        st.sidebar.info("User actions:")
        user_choice = st.sidebar.radio("Select an action", ["Let's play!", "Show previous games", "Compete with your puttpals", "Logout"])

        if user_choice == "Let's play!":
            st.subheader("Let's play!")
            if not golf_app.courses:
                st.warning("No courses available. Please add a course first.")
            else:
                course_options = [course.name for course in golf_app.courses]
                selected_course = st.selectbox("Select a course to play:", course_options)

                if st.button("Play"):
                    course = next(course for course in golf_app.courses if course.name == selected_course)
                    golf_app.current_user.player.play_round(course)
                    golf_app.save_accounts()

        elif user_choice == "Show previous games":
            st.subheader("Show previous games:")
            golf_app.current_user.player.show_previous_rounds()

        elif user_choice == "Compete with your puttpals":
            st.subheader("Compete with your puttpals:")
            friend_username = st.text_input("Enter the username of your friend:")
            friend = next((account for account in golf_app.accounts if account.username == friend_username), None)

            if st.button("Compete"):
                if friend and friend.is_admin:
                    st.error("Cannot compete with an admin.")
                elif friend:
                    golf_app.current_user.player.compete_with_friend(friend.player)
                else:
                    st.warning(f"No user found with the username '{friend_username}'.")
                    st.warning("Please enter a valid username.")

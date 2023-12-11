class Course:
    def __init__(self, name, holes):
        self.name = name
        self.holes = holes

class GolfRound:
    def __init__(self, course, player):
        self.course = course
        self.player = player
        self.strokes_by_hole = {}
        self.points_by_hole = {}

    def play_hole(self, hole, strokes):
        hole_number = hole.hole_number

        if 1 <= strokes <= 10:
            self.strokes_by_hole[hole_number] = strokes
            self.calculate_points_by_hole(hole, strokes)
        else:
            st.warning("Please enter a stroke value between 1 and 10.")

    def calculate_points_by_hole(self, hole, strokes):
        hole_number = hole.hole_number
        handicap = self.player.handicap

        # Calculate points logic here
        # ...

def create_golf_round(course):
    name = st.text_input("Enter player's name:", key="player_name")
    handicap = st.number_input("Enter your handicap:", min_value=0, step=1, key="player_handicap")
    player = Player(name, handicap)
    return GolfRound(course, player)

def create_custom_course():
    course_name = st.text_input("Enter the name of the course:", key="course_name")
    holes = []
    for i in range(1, 19):
        st.write(f"Enter details for Hole {i}:")
        par = st.number_input(f"Par for Hole {i}:", min_value=3, step=1, key=f"hole_{i}_par")
        stroke_index = st.number_input(f"Stroke Index for Hole {i}:", min_value=1, step=1, key=f"hole_{i}_stroke")
        holes.append(Hole(i, par, stroke_index))
    return Course(course_name, holes)

def get_course_choice():
    st.write("Choose a golf course:")
    course_options = {
        "Ostschweizerischer Golfclub Niederbüren": [
            (1, 5, 13), (2, 4, 9),  # ... (hole_number, par, stroke_index)
        ],
        # Define other course options similarly...
    }
    choice = st.selectbox("Select a course:", list(course_options.keys()) + ["Create a new course"])

    if choice == "Create a new course":
        return create_custom_course()
    else:
        holes_data = course_options.get(choice, [])
        predefined_holes = [Hole(*hole_data) for hole_data in holes_data]
        return Course(choice, predefined_holes)

def main():
    st.title("Golf Round Tracker")
    course = get_course_choice()

    rounds = []
    while True:
        golf_round = create_golf_round(course)
        rounds.append(golf_round)

        for hole in course.holes:
            st.write(hole)

            strokes = st.number_input(f"Enter strokes for Hole {hole.hole_number}:", min_value=1, max_value=10, key=f"hole_{hole.hole_number}_strokes")
            golf_round.play_hole(hole, strokes)

        another_player = st.radio("Is there another player?", ('Yes', 'No'), key="another_player_radio")
        if another_player == 'No':
            break

    rounds.sort(key=lambda x: x.calculate_total_points(), reverse=True)

    st.write(f"\nResults at {course.name}:")
    for rnd in rounds:
        st.write(rnd.player)  # Display player info
        # Display other round information as needed

if __name__ == "__main__":
    main()

import streamlit as st

class Course:
    def __init__(self, name, holes):
        self.name = name
        self.holes = holes

class Player:
    def __init__(self, name, handicap):
        self.name = name
        self.handicap = handicap

class GolfRound:
    def __init__(self, course, player):
        self.course = course
        self.player = player
        self.strokes_by_hole = {}
        self.points_by_hole = {}

    def play_hole(self, hole, strokes):
        # TODO: Implement solid validations for strokes - 1 max. 10?
        self.strokes_by_hole[hole.hole_number] = strokes
        self.calculate_points_by_hole(hole, strokes)

    def calculate_points_by_hole(self, hole, strokes):
        self.points_by_hole[hole.hole_number] = hole.calculate_points(self.player.handicap, strokes)

    def calculate_total_strokes(self):
        return sum(self.strokes_by_hole.values())

    def calculate_total_points(self):
        return sum(self.points_by_hole.values())

    def __str__(self):
        return f"{self.player.name} - Handicap: {self.player.handicap}, Total Strokes: {self.calculate_total_strokes()}, Total Points: {self.calculate_total_points()}"

def main():
    st.title('Golf Round Tracker')

    # Create Course
    course_name = st.text_input('Course Name:')
    num_holes = st.number_input('Number of Holes:', min_value=1, max_value=18, value=18)
    holes = [f'Hole {i+1}' for i in range(num_holes)]
    course = Course(course_name, holes)

    # Create Player
    player_name = st.text_input('Player Name:')
    player_handicap = st.number_input('Player Handicap:', min_value=0, max_value=36, value=0)
    player = Player(player_name, player_handicap)

    # Create Golf Round
    golf_round = GolfRound(course, player)

    # Play Hole
    hole_to_play = st.selectbox('Select Hole to Play:', holes)
    strokes = st.number_input('Strokes:', min_value=1, max_value=10, value=1)
    
    if st.button('Play Hole'):
        hole_number = int(hole_to_play.split(' ')[1])  # Extract hole number from hole string
        hole = Course(course_name, holes)
        golf_round.play_hole(hole, strokes)

        # Display Player Info and Round Summary
        st.write(f"Player: {golf_round.player.name}")
        st.write(f"Handicap: {golf_round.player.handicap}")
        st.write(f"Total Strokes: {golf_round.calculate_total_strokes()}")
        st.write(f"Total Points: {golf_round.calculate_total_points()}")

if __name__ == "__main__":
    main()
import streamlit as st

class Player:
    def __init__(self, name, handicap):
        self.name = name
        self.handicap = handicap

    def __str__(self):
        return f"{self.name} - Handicap: {self.handicap}"

def main():
    st.title("Player Information")

    # Input for player's name and handicap
    player_name = st.text_input("Enter player's name:")
    player_handicap = st.number_input("Enter player's handicap:", min_value=0, step=1)

    # Create a Player object using the input values
    player = Player(player_name, player_handicap)

    # Display the player information
    st.write("Player Information:")
    st.write(str(player))

if __name__ == "__main__":
    main()

class Hole:
    def __init__(self, hole_number, par, stroke_index):
        self.hole_number = hole_number
        self.par = par
        self.stroke_index = stroke_index 

def main():
    st.title("Golf Hole Information")

    hole_number = st.number_input("Enter hole number:", min_value=1, step=1)
    par = st.number_input("Enter par for the hole:", min_value=3, step=1)
    stroke_index = st.number_input("Enter stroke index for the hole:", min_value=1, step=1)

    # Create a Hole object using the input values
    hole = Hole(hole_number, par, stroke_index)

    # Display the hole information
    st.write("Hole Information:")
    st.write(f"Hole Number: {hole.hole_number}")
    st.write(f"Par: {hole.par}")
    st.write(f"Stroke Index: {hole.stroke_index}")

if __name__ == "__main__":
    main()

class Hole:
    def __init__(self, hole_number, par, stroke_index):
        self.hole_number = hole_number
        self.par = par
        self.stroke_index = stroke_index 

    def calculate_net_strokes(self, handicap, strokes):
        stroke_deduction = 1 if self.stroke_index <= handicap else 0

        if handicap > 18 and self.stroke_index <= (handicap - 18):
            stroke_deduction += 1

        net_strokes = strokes - stroke_deduction
        return net_strokes

import streamlit as st

class Hole:
    def __init__(self, hole_number, par, stroke_index):
        self.hole_number = hole_number
        self.par = par
        self.stroke_index = stroke_index 

    def calculate_net_strokes(self, handicap, strokes):
        stroke_deduction = 1 if self.stroke_index <= handicap else 0

        if handicap > 18 and self.stroke_index <= (handicap - 18):
            stroke_deduction += 1

        net_strokes = strokes - stroke_deduction
        return net_strokes

def main():
    st.title("Net Strokes Calculator")

    hole_number = st.number_input("Enter hole number:", min_value=1, step=1, key="hole_number_input")
    par = st.number_input("Enter par for the hole:", min_value=3, step=1, key="par_input")
    stroke_index = st.number_input("Enter stroke index for the hole:", min_value=1, step=1, key="stroke_index_input")
    handicap = st.number_input("Enter player's handicap:", min_value=0, step=1, key="handicap_input")

    hole = Hole(hole_number, par, stroke_index)

    strokes = st.number_input("Enter strokes for the hole:", min_value=1, step=1, key="strokes_input")

    net_strokes = hole.calculate_net_strokes(handicap, strokes)

    st.write(f"Net strokes for Hole {hole_number}: {net_strokes}")

if __name__ == "__main__":
    main()

class GolfCalculator:
    def calculate_stableford_points(self, par, net_strokes):
        """Calculate Stableford points."""
        return max(0, 2 + (par - net_strokes))

    def calculate_points(self, handicap, strokes, par):
        # get the net strokes
        net_strokes = self.calculate_net_strokes(handicap, strokes)

        # calculate and display Stableford points
        points = self.calculate_stableford_points(par, net_strokes)

        return points

    def calculate_net_strokes(self, handicap, strokes):
        # Implement logic to calculate net strokes based on handicap and strokes
        # For example:
        net_strokes = strokes - handicap
        return net_strokes

def main():
    st.title('Stableford Points Calculator')

    # Create an instance of the GolfCalculator class
    golf_calc = GolfCalculator()

    # Input fields
    handicap = st.number_input('Handicap:', min_value=0, max_value=50, value=0)
    strokes = st.number_input('Strokes:', min_value=0, max_value=200, value=0)
    par = st.number_input('Par:', min_value=3, max_value=10, value=4)

    # Calculate points
    if st.button('Calculate'):
        points = golf_calc.calculate_points(handicap, strokes, par)
        st.success(f'Stableford Points: {points}')

if __name__ == "__main__":
    main()

class GolfHole:
    def __init__(self, hole_number, par, stroke_index):
        self.hole_number = hole_number
        self.par = par
        self.stroke_index = stroke_index

    def __str__(self):
        return f"Hole {self.hole_number} - Par: {self.par}, Stroke Index: {self.stroke_index}"

def main():
    st.title('Golf Hole Information')

    hole_number = st.number_input('Hole Number:', min_value=1, max_value=18, value=1)
    par = st.number_input('Par:', min_value=3, max_value=5, value=4)
    stroke_index = st.number_input('Stroke Index:', min_value=1, max_value=18, value=1)

    golf_hole = GolfHole(hole_number, par, stroke_index)

    if st.button('Display Hole Info'):
        info = str(golf_hole)
        st.success(info)

if __name__ == "__main__":
    main()

class Course:
    def __init__(self, name, holes):
        self.name = name
        self.holes = holes

class GolfRound:
    def __init__(self, course, player):
        self.course = course
        self.player = player
        self.strokes_by_hole = {}
        self.points_by_hole = {}

def main():
    st.title('Golf Round Tracker')

    # Create Course
    course_name = st.text_input('Course Name:')
    num_holes = st.number_input('Number of Holes:', min_value=1, max_value=18, value=18)
    holes = [f'Hole {i+1}' for i in range(num_holes)]
    course = Course(course_name, holes)

    # Create Golf Round
    player_name = st.text_input('Player Name:')
    golf_round = GolfRound(course, player_name)

    # Display Course and Player Info
    st.write(f"Course: {golf_round.course.name}")
    st.write(f"Player: {golf_round.player}")

if __name__ == "__main__":
    main()



NEEUUUU

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

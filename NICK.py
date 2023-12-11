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

import streamlit as st

class Hole:
    def __init__(self, hole_number, par, stroke_index):
        self.hole_number = hole_number
        self.par = par
        self.stroke_index = stroke_index

    def calculate_points(self, handicap, strokes):
        # Implement Stableford point calculation here
        # Use the provided formula
        return max(0, 2 + (self.par - strokes))

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

def create_golf_round(course):
    name = st.text_input("Enter player's name:")
    handicap = st.number_input("Enter your handicap:", min_value=0, max_value=36)
    player = Player(name, handicap)
    return GolfRound(course, player)

def create_custom_course():
    course_name = st.text_input("Enter the name of the course:")
    holes = []
    for i in range(1, 19):
        st.write(f"Enter details for Hole {i}:")
        par = st.number_input(f"Hole {i} - Par:", min_value=3, max_value=5)
        stroke_index = st.number_input(f"Hole {i} - Stroke Index:", min_value=1, max_value=18)
        holes.append(Hole(i, par, stroke_index))
    return Course(course_name, holes)

def main():
    st.title("Golf Round Tracker")

    course = get_course_choice()

    rounds = []
    while True:
        golf_round = create_golf_round(course)
        rounds.append(golf_round)

        for hole in course.holes:
            st.write(hole)

            # Ask the player to enter the strokes for the hole and save the result
            strokes = st.number_input(f"Enter strokes for Hole {hole.hole_number}:", min_value=1, max_value=10)
            golf_round.play_hole(hole, strokes)

        another_player = st.radio("Is there another player?", ("Yes", "No"))
        if another_player == 'No':
            break

rounds.sort(key=lambda x: x.calculate_total_points(), reverse=True)

st.write(f"\nResults at {course.name}:")
for golf_round in rounds:
    st.write(golf_round)



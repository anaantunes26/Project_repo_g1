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

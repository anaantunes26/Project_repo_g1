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




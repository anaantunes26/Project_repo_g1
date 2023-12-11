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


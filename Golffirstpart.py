import streamlit as st

st.write ("class Hole:
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

  def play_hole(self, hole, strokes):
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
  name = input("Enter player's name: ")
  handicap = int(input("Enter your handicap: "))
  return Player(name, handicap)

def create_custom_course():
  course_name = input("Enter the name of the course: ")
  holes = []
  for i in range(1, 19):
      print(f"Enter details for Hole {i}:")
      par = int(input("Par: "))
      stroke_index = int(input("Stroke Index: "))
      holes.append(Hole(i, par, stroke_index))
  return Course(course_name, holes)

def get_course_choice():
  print("Choose a golf course:")
  print("1. Ostschweizerischer Golfclub Niederbüren")
  print("2. Golfclub Appenzell")
  print("3. Golfpark Waldkirch")
  print("4. Create a new course")
  choice = input("Enter your choice (1-4): ")")
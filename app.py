import streamlit as st  

class Player:
  def __init__(self, name, handicap):
      self.name = name
      self.handicap = handicap

  def __str__(self):
      return f"{self.name} - Handicap: {self.handicap}, Total Strokes: {self.calculate_total_strokes()}"

class Hole:
  def __init__(self, hole_number, par, stroke_index):
      self.hole_number = hole_number
      self.par = par
      self.stroke_index = stroke_index

  def calculate_net_strokes(self, handicap, strokes):
    """Calculate net strokes based on the SI and the HCP."""

    # determine the strokes we are allowed to subtract
    stroke_deduction = 1 if self.stroke_index <= handicap else 0

    # for handicaps greater than 18, check if we need to give an additional stroke
    if handicap > 18 and self.stroke_index <= (handicap - 18):
      stroke_deduction += 1

    # calculate the net strokes
    net_strokes = strokes - stroke_deduction
    return net_strokes

  def calculate_stableford_points(self, net_strokes):
    """Calculate Stableford points."""
    return max(0, 2 + (self.par - net_strokes))

  def calculate_points(self, handicap, strokes):
    # get the net strokes
    net_strokes = self.calculate_net_strokes(handicap, strokes)

    # calculate and display Stableford points
    points = self.calculate_stableford_points(net_strokes)

    return points

  def __str__(self):
      return f"Hole {self.hole_number} - Par: {self.par}, Stroke Index: {self.stroke_index}"

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
      # TODO: implement solid validations for strokes - 1 max. 10?
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
  name = input("Enter player's name: ")
  handicap = int(input("Enter your handicap: "))
  player = Player(name, handicap)
  return GolfRound(course, player)

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
  choice = input("Enter your choice (1-4): ")

  if choice == '1':
      predefined_holes = [Hole(1, 5, 13), Hole(2, 4, 9), Hole(3, 4, 1), Hole(4, 5, 3), Hole(5, 3, 11), Hole(6, 4, 17), Hole(7, 4, 7), Hole(8, 3, 15), Hole(9, 4, 5), Hole(10, 3, 8), Hole(11, 4, 18), Hole(12, 4, 12), Hole(13, 4, 6), Hole(14, 4, 2), Hole(15, 5, 16), Hole(16, 3, 10), Hole(17, 4, 4), Hole(18, 5, 14)]
      return Course("Ostschweizerischer Golfclub Niederbüren", predefined_holes)
  elif choice == '2':
      predefined_holes = [Hole(1, 3, 15), Hole(2, 4, 13), Hole(3, 5, 5), Hole(4, 4, 7), Hole(5, 4, 3), Hole(6, 5, 9), Hole(7, 3, 17), Hole(8, 5, 1), Hole(9, 4, 11), Hole(10, 3, 14), Hole(11, 4, 12), Hole(12, 3, 18), Hole(13, 5, 2), Hole(14, 4, 4), Hole(15, 4, 6), Hole(16, 4, 8), Hole(17, 4, 10), Hole(18, 3, 16)]
      return Course("Golfclub Appenzell", predefined_holes)
  elif choice == '3':
      predefined_holes = [Hole(1, 4, 13), Hole(2, 4, 3), Hole(3, 3, 11), Hole(4, 5, 5), Hole(5, 3, 17), Hole(6, 4, 1), Hole(7, 4, 9), Hole(8, 4, 7), Hole(9, 5, 15), Hole(10, 5, 6), Hole(11, 3, 16), Hole(12, 4, 4), Hole(13, 4, 14), Hole(14, 3, 10), Hole(15, 4, 12), Hole(16, 4, 2), Hole(17, 3, 18), Hole(18, 5, 8)]
      return Course("Golfpark Waldkirch", predefined_holes)
  else:
      return create_custom_course()

def main():
  course = get_course_choice()

  rounds = []
  while True:
      golf_round = create_golf_round(course)
      rounds.append(golf_round)

      for hole in course.holes:
          print(hole)

          # Ask the player to enter the strokes for the hole and save the result
          strokes = int(input(f"Enter strokes for Hole {hole.hole_number}: "))
          golf_round.play_hole(hole, strokes)

          # Now we can calculate the stableford score for the player for this hole
          # player.calculate_stableford_score(hole)


      another_player = input("Is there another player? (yes/no): ").lower()
      if another_player != 'yes':
          break

  rounds.sort(key=lambda x: x.calculate_total_points(), reverse=True)

  print(f"\nResults at {course.name}:")
  for round in rounds:
      print(round)

if __name__ == "__main__":
  main()
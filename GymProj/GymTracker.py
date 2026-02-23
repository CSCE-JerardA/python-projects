## Jerard Austin

from abc import ABC

class Exercise:
    def __init__(self, exercise_name: str, part_of_body: str, time_minutes: int):

        self.exercise_name = exercise_name
        self.part_of_body = part_of_body
        self.time_seconds = time_minutes

    
    def __str__(self):
        return f"{self.exercise_name}: {self.part_of_body} for {self.time_seconds} minutes."


    




class WorkoutSession:
    def __init__(self, reps: int, lift_sets: int):
        self.reps = reps
        self.lift_sets = lift_sets

    def __str__(self):
        return f"{self.reps} for {self.lift_sets} sets"


    def calcProgression(self):

        

        
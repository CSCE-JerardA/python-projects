## Jerard Austin 2026

from abc import ABC

class Exercise:
    def __init__(self, exercise_name: str, part_of_body: str, time_minutes: int, is_complete: bool):

        self.exercise_name = exercise_name
        self.part_of_body = part_of_body
        self.time_seconds = time_minutes
        self.is_complete = is_complete
    
    def mark_done(self):

        if self.is_complete == True:
            print(f"{self.exercise_name} was completed!")
        else:
            print("This exercise hasn't been completed!")


    
    def __str__(self):
        return f"{self.exercise_name}: {self.part_of_body} for {self.time_seconds} minutes."


    

class Workout:
    def __init__(self, reps: int, lift_sets: int, date: int, exercises: list):
        self.exercises = []
        self.date = date
        self.reps = reps
        self.lift_sets = lift_sets
        


    def __str__(self):
        return f"{self.reps} for {self.lift_sets} sets"


    def addExercise(self, exercise):
        self.exercise = exercise
        self.exercises.append(exercise)
        print(f"{self.exerc} was added to your Exercise List")


    def workoutProgress(self):

        if not self.exercises:
            print("No exercises here yet")
            return 0
        
        completed_e = 0
        total_exercises = len(self.exercises)


        for workout in self.exercises:
            if workout.is_complete == True:
                completed_e += 1

        progress_percent = (completed_e / total_exercises) * 100

        print("You are {progress_percent} done with your workout!")

        return progress_percent






class User:
    def __init__(self, userName: str, day: str):

        self.name = userName
        self.day = day

    def createWorkoutDay(self):

        if self.day == "Monday":
            print("Chest Day!")

        elif self.day == "Tuesday":
            print("Back Day!")

        elif self.day == "Wednesday":
            print("Leg Day!")

        elif self.day == "Thursday":
            print("Cardio Day!")

        elif self.day == "Friday":
            print("Core Day")

        else:
            print("Please rest today :)")


    def assigning(self, work: Workout, name_of_exercise: str):

        self.name_of_exercise = name_of_exercise
        self.work = work


        for workout in work.exercises:
            print(f"Hello {self.name}, today were working on {self.name_of_exercise}!")
            workout.mark_done()

        print(f"{self.name_of_exercise} was not found")




jcWorkout = Workout("Hitting Legs")

e1 = Exercise("Squats", "Legs", 10, True)
e2 = Exercise("Deadlift", "Legs", 6, False)

jcWorkout.addExercise(e1)
jcWorkout.addExercise(e2)

jerard = User("Jerard", "Wednesday")

jerard.assigning("Bulgarian Split Squats")
jerard.assigning("Calve Raises")
jerard.assigning("Seated Hamstring Curls")

new_progress = jcWorkout.workoutProgress()
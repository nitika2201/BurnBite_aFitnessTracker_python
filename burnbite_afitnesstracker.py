import tkinter as tk
from tkinter import messagebox, simpledialog
from collections import defaultdict

class FitnessTracker:
    def __init__(self):
        self.workouts = []
        self.meals = []
        self.badges = defaultdict(int)

    def add_workout(self, date, exercise, duration, calories):
        workout = {
            'date': date,
            'exercise': exercise,
            'duration': duration,
            'calories': calories
        }
        self.workouts.append(workout)
        self.check_badges()

    def add_meal(self, date, meal, calories):
        self.meals.append({'date': date, 'meal': meal, 'calories': calories})

    def get_workouts(self):
        return self.workouts

    def get_meals(self):
        return self.meals

    def total_calories(self):
        return sum(workout['calories'] for workout in self.workouts)

    def check_badges(self):
        if len(self.workouts) >= 5:
            self.badges['Workout Warrior'] += 1
        if self.total_calories() >= 500:
            self.badges['Calorie Crusher'] += 1

    def get_badges(self):
        return {badge: count for badge, count in self.badges.items() if count > 0}

class FitnessApp:
    def __init__(self, root):
        self.tracker = FitnessTracker()
        self.root = root
        self.root.title("Fitness Tracker")
        self.root.configure(bg="#f0f0f0")

        # Create and place widgets
        tk.Label(root, text="Date (YYYY-MM-DD)", bg="#f0f0f0").grid(row=0, column=0)
        self.date_entry = tk.Entry(root, font=('Arial', 14), width=30)
        self.date_entry.grid(row=0, column=1)

        tk.Label(root, text="Exercise", bg="#f0f0f0").grid(row=1, column=0)
        self.exercise_entry = tk.Entry(root, font=('Arial', 14), width=30)
        self.exercise_entry.grid(row=1, column=1)

        tk.Label(root, text="Duration (mins)", bg="#f0f0f0").grid(row=2, column=0)
        self.duration_entry = tk.Entry(root, font=('Arial', 14), width=30)
        self.duration_entry.grid(row=2, column=1)

        tk.Label(root, text="Calories", bg="#f0f0f0").grid(row=3, column=0)
        self.calories_entry = tk.Entry(root, font=('Arial', 14), width=30)
        self.calories_entry.grid(row=3, column=1)

        self.add_button = tk.Button(root, text="Add Workout", command=self.add_workout, bg="#4CAF50", fg="white", font=('Arial', 12))
        self.add_button.grid(row=4, column=0, columnspan=2, pady=5)

        tk.Label(root, text="Meal", bg="#f0f0f0").grid(row=5, column=0)
        self.meal_entry = tk.Entry(root, font=('Arial', 14), width=30)
        self.meal_entry.grid(row=5, column=1)

        tk.Label(root, text="Meal Calories", bg="#f0f0f0").grid(row=6, column=0)
        self.meal_calories_entry = tk.Entry(root, font=('Arial', 14), width=30)
        self.meal_calories_entry.grid(row=6, column=1)

        self.add_meal_button = tk.Button(root, text="Add Meal", command=self.add_meal, bg="#2196F3", fg="white", font=('Arial', 12))
        self.add_meal_button.grid(row=7, column=0, columnspan=2, pady=5)

        self.view_button = tk.Button(root, text="View Workouts", command=self.view_workouts, bg="#FFC107", fg="black", font=('Arial', 12))
        self.view_button.grid(row=8, column=0, columnspan=2, pady=5)

        self.view_meals_button = tk.Button(root, text="View Meals", command=self.view_meals, bg="#FFC107", fg="black", font=('Arial', 12))
        self.view_meals_button.grid(row=9, column=0, columnspan=2, pady=5)

        self.calories_button = tk.Button(root, text="Total Calories Burned", command=self.show_total_calories, bg="#FF5722", fg="white", font=('Arial', 12))
        self.calories_button.grid(row=10, column=0, columnspan=2, pady=5)

        self.badges_button = tk.Button(root, text="View Badges", command=self.show_badges, bg="#9C27B0", fg="white", font=('Arial', 12))
        self.badges_button.grid(row=11, column=0, columnspan=2, pady=5)

    def add_workout(self):
        date = self.date_entry.get()
        exercise = self.exercise_entry.get()
        try:
            duration = int(self.duration_entry.get())
            calories = int(self.calories_entry.get())
            self.tracker.add_workout(date, exercise, duration, calories)
            messagebox.showinfo("Success", "Workout added!")
            self.clear_entries()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for duration and calories.")

    def add_meal(self):
        date = self.date_entry.get()
        meal = self.meal_entry.get()
        try:
            meal_calories = int(self.meal_calories_entry.get())
            self.tracker.add_meal(date, meal, meal_calories)
            messagebox.showinfo("Success", "Meal added!")
            self.clear_entries()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for meal calories.")

    def view_workouts(self):
        workouts = self.tracker.get_workouts()
        if not workouts:
            messagebox.showinfo("Workouts", "No workouts logged yet.")
            return
        
        workout_info = "\n".join(
            f"Date: {w['date']}, Exercise: {w['exercise']}, Duration: {w['duration']} mins, Calories: {w['calories']}"
            for w in workouts
        )
        messagebox.showinfo("Workout History", workout_info)

    def view_meals(self):
        meals = self.tracker.get_meals()
        if not meals:
            messagebox.showinfo("Meals", "No meals logged yet.")
            return
        
        meal_info = "\n".join(
            f"Date: {m['date']}, Meal: {m['meal']}, Calories: {m['calories']}"
            for m in meals
        )
        messagebox.showinfo("Meal History", meal_info)

    def show_total_calories(self):
        total = self.tracker.total_calories()
        messagebox.showinfo("Total Calories", f"Total calories burned: {total}")

    def show_badges(self):
        badges = self.tracker.get_badges()
        if not badges:
            messagebox.showinfo("Badges", "No badges earned yet.")
            return

        badge_info = "\n".join(f"{badge}: {count}" for badge, count in badges.items())
        messagebox.showinfo("Earned Badges", badge_info)

    def clear_entries(self):
        self.date_entry.delete(0, tk.END)
        self.exercise_entry.delete(0, tk.END)
        self.duration_entry.delete(0, tk.END)
        self.calories_entry.delete(0, tk.END)
        self.meal_entry.delete(0, tk.END)
        self.meal_calories_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = FitnessApp(root)
    root.mainloop()

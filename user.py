from habit import Habit
from habitdb import HabitDatabase
from datetime import datetime
class User:
    def __init__(self, user_id, username, habit_db):
        """
        Initializes a new User instance.

        Parameters:
            user_id (str): The unique identifier for the user, it is 8 character long.
            username (str): The username associated with the user.
            habit_db (HabitDatabase): An instance of the HabitDatabase class for database operations.
        """
        self.user_id = user_id
        self.username = username
        self.habits = []  # List to store Habit instances associated with the user
        self.habit_db = habit_db

        # Load habits from the database when a User instance is created
        self.load_habits()


    def get_user_habit(self):
        """

        get all habits associated with user, and return as a list of habit objects
        """
        return self.habits
    def load_habits(self):
        """
        Loads habits associated with the user from the database.
        """
        self.habits = self.habit_db.get_all_user_habits(self.user_id)

    def add_habit(self, task, frequency, target_days=None):
        """
        Adds a new habit for the user.

        Parameters:
            task (str): The task or description of the habit.
            frequency (str): The frequency of the habit (e.g., "daily" or "weekly").
            target_days (list): List of days for weekly habits (default is None).


        Returns:
            Habit: An instance of the Habit class representing the new habit.
        """
        habit_id = self.habit_db.add_habit(self.user_id, task, frequency, target_days)
        new_habit = Habit(habit_id,task, frequency, target_days)
        self.habits.append(new_habit)
        return new_habit


    def mark_habit_completed(self, habit_id, completion_date=None):
        """
        Marks a habit as completed for the user.

        Parameters:
            habit_id (str): The ID of the habit to mark as completed.
            completion_date (str): The completion date in the format "%Y-%m-%d" (default is None,
                                   uses the current date).
        """
        habit = next((h for h in self.habits if h.habit_id == habit_id), None)
        print('got here')
        print(habit)
        print(habit.habit_id)

        if habit.is_due_today():
            completion_date = datetime.now().strftime("%Y-%m-%d")
            habit.mark_completion(completion_date)
            self.habit_db.mark_habit_completed(self.user_id, habit_id, completion_date)

    def is_due_today(self, habit_id):
        """
        Checks if a habit is due to be completed today for the user.

        Parameters:
            habit_id (str): The ID of the habit to check.

        Returns:
            bool: True if the habit is due today, False otherwise.
        """
        habit = next((h for h in self.habits if h.habit_id == habit_id), None)
        if habit:
            return habit.is_due_today()
        return False

    def view_progress(self):
        """
        Retrieves the user's habit progress.

        Returns:
            dict: A dictionary containing the user's habit progress.
        """
        progress = {}
        for habit in self.habits:
            progress[habit.task] = {
                'completed_dates': list(habit.completed_dates),
                'longest_streak': habit.get_longest_streak(self.user_id)
            }
        return progress

    def __str__(self):
        """
        Returns a string representation of the User instance.

        Returns:
            str: String representation of the User.
        """
        return f"User {self.user_id}: {self.username}"



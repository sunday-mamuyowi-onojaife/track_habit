from datetime import datetime

class Habit:
    def __init__(self, habit_id, task, frequency, target_days=None,completed_dates=None):
        """
        Initializes a new Habit instance.

        Parameters:
            habit_id (str): The unique identifier for the habit, it is 14 characters long.
            task (str): The name or description of the habit.
            frequency (str): The frequency of the habit (e.g., "daily" or "weekly").
            target_days (list): List of days for weekly habits (default is None).

            completed_dates (list): Set of dates when the habit was completed (default is None).
        """
        self.habit_id = habit_id
        self.task = task
        self.frequency = frequency
        self.target_days = target_days if target_days else []

        self.completed_dates = completed_dates if completed_dates else []

    def mark_completion(self, completion_date=None):
        """
        Marks the habit as completed on the given date.

        Parameters:
            completion_date (str): The completion date in the format "%Y-%m-%d" (default is None,
                                   uses the current date).
        """
        if not completion_date:
            completion_date = datetime.now().strftime("%Y-%m-%d")
        self.completed_dates.append(completion_date)

    def is_due_today(self):
        """
        Checks if the habit is due to be completed today.

        Returns:
            bool: True if the habit is due today, False otherwise.
        """
        if self.frequency == "Daily":
            return True
        elif self.frequency == "Weekly":
            today = datetime.now().strftime("%A")
            return today in self.target_days
        else:
            return False




    def __str__(self):
        """
        Returns a string representation of the Habit instance.

        Returns:
            str: String representation of the Habit.
        """
        return f"HabitID: {self.habit_id}, Habit : {self.task}, Frequency: {self.frequency}, " \
               f"Target Days: {self.target_days}"



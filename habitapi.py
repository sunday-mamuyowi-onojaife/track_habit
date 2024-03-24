from datetime import datetime

class HabitAPI:
    def __init__(self, habit_db, user=None):
        self.user = user
        self.habit_db = habit_db
#########################################################################################
    def login(self,email,password):
        return self.habit_db.login(email,password)

#########################################################################################
    def register_user(self,emaill,usernamee,passwordd):
        li=self.habit_db.create_user(emaill,usernamee,passwordd)
        return li[0]




###########################################################################################
    def get_list_of_user_habits(self,userid):
        return self.habit_db.list_of_a_user_habits(userid)
#############################################################################################
    def get_habit_all_days_and_fulfilled(self,habit_id):
        return self.habit_db.get_habit_all_days(habit_id)
###############################################################################################
    def add_habit(self,user_id,task,frequency,target_days=None):

        return self.habit_db.add_habit(user_id, task, frequency,target_days)

##################################################################################################
    def list_of_a_user_habits(self, user_id):
        return self.habit_db.list_of_a_user_habits( user_id)

 ###############################################################################################

    def check_if_task_needs_to_be_mark(self,habit_id,present_day):
        return self.habit_db.check_if_task_needs_to_be_mark(habit_id,present_day)

 ##################################################################################################

    def mark_habit_completed(self, user_id, habit_id, completion_date):

        return self.habit_db.mark_habit_completed(user_id, habit_id, completion_date)
    #######################################################################################

    def weekly_list_of_a_user_habits(self, user_id):
        return self.habit_db.weekly_list_of_a_user_habits(user_id)

    def daily_list_of_a_user_habits(self, user_id):
        return self.habit_db.daily_list_of_a_user_habits(user_id)

    def all_habit_longest_streak(self,user_id):
        return self.habit_db.all_habit_longest_streak(user_id)

    def habit_longest_streak(self,habit_id):
        return self.habit_db.habit_longest_streak(habit_id)

    def stop_habit(self, habit_id):
        return self.habit_db.stop_habit(habit_id)


    def check_if_habit(self, user_id, habit_id, completion_date):
        return self.habit_db.check_if_habit(user_id, habit_id, completion_date)
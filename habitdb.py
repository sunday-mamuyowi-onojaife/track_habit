import mysql.connector
from habit import Habit
import random
import datetime
from streak import Streak
class HabitDatabase:
    def __init__(self):
        """
        initialize the database connection using the required credentials.
        """
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.database = "habit_tracker"
        self.connection = None

    def connect(self):
        """
        create the connection needed to connect to the mysql database

        """
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

    def disconnect(self):
        """

        This closes the connection when the connection is no longer needed
        """
        if self.connection:
            self.connection.close()

    def execute_query(self, query, data=None):
        """
        This is the engine that executes all the sql query

        Parameters:
            query (str): The query string to be executed.

            data (str): Accept associated data to execute alongside the query (default is None).

        """
        cursor = self.connection.cursor()
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result
    def login(self,email,passwordd):
        details = []

        query = "SELECT user_id,user_name FROM userz WHERE email = %s and pazzword = %s"
        data = (email,passwordd)
        result = self.execute_query(query, data)

        if len(result) ==0:

            details.append('INCORRECT')

            return details
        else:
            for row in result:
                details.append(row[0])
                details.append(row[1])
                details.append(email)
        return details

    def create_user(self,emaill,usernamee,passwordd):
        email=[]
        username=[]
        e_present=False
        u_present=False
        query = "SELECT email,user_name FROM userz"

        result = self.execute_query(query)
        for row in result:
            a=row[0]
            b=row[1]
            email.append(a.lower())
            username.append(b.lower())
        if emaill.lower() in email:
            e_present = True

        if usernamee.lower() in username:
            u_present = True
        if e_present == False and u_present == False:

            a = random.randint(1000, 9999)
            b = random.randint(1000, 9999)
            c=str(a)+str(b)
            query = "INSERT INTO userz (user_id,email, user_name, pazzword) VALUES (%s, %s, %s, %s)"
            data = (c, emaill,usernamee , passwordd)
            self.execute_query(query, data)
            self.connection.commit()
            from user import User
            userr=User(c,usernamee,self )
            return [userr]
        else:
            return ['Cant']

    def get_all_user_habits(self, user_id):
        user_habits=[]

        query = "SELECT habit_id,task,frequency,period FROM habit WHERE user_id = %s ORDER BY ordering_time DESC"
        data = (user_id,)
        result = self.execute_query(query, data)

        for row in result:
            #print(row[3])
            strr=row[3]
            target_dayz = list(strr.split(" "))
            habitidz=row[0]
            completion_list=[]
            query2 = "SELECT completion_date FROM completed_habits WHERE habit_id = %s"
            data2 = (habitidz,)
            result2 = self.execute_query(query2, data2)
            for roww in result2:
                completion_list.append(str(roww[0]))

            h=Habit(row[0],row[1],row[2],target_dayz,completion_list)
            #print(h)
            user_habits.append(h)


        return user_habits

    def completed_Date(self,habitID):
        completed_date = []

        query = "SELECT completion_date FROM completed_habits WHERE habit_id = %s"
        data = (habitID,)
        result = self.execute_query(query, data)
        for row in result:

            completed_date.append(str(row[0]))
        return completed_date



    def add_habit(self, user_id, task, frequency, target_days=None):

        if not target_days:
            period = 'Everyday'
        else:
            period = ' '.join(target_days)


        a = random.randint(1000000, 9999999)  # 7 digits
        b = random.randint(1000000, 9999999)  # 7 digits
        hid = str(a) + str(b)
        query = "INSERT INTO habit (habit_id,user_id, task, frequency, period) VALUES (%s, %s, %s, %s, %s)"
        data = (hid,user_id, task, frequency,period )
        self.execute_query(query, data)
        self.connection.commit()
        return hid

    def stop_habit(self,habit_id):
        query = "UPDATE habit set statuz='STOPPED',stop_date=NOW() WHERE habit_id = %s"
        data = (habit_id,)
        self.execute_query(query, data)
        self.connection.commit()
        return('ok')


    def mark_habit_completed(self, user_id, habit_id, completion_date):
        checker=self.check_if_habit(user_id,habit_id,completion_date)

        if checker:
            a = random.randint(1000000, 9999999)  # 7 digits
            b = random.randint(1000000, 9999999)  # 7 digits
            hid = str(a) + str(b)
            query = "INSERT INTO completed_habits (complete_id,user_id, habit_id, completion_date) VALUES (%s, %s, %s,%s)"
            data = (hid,user_id, habit_id, completion_date)
            self.execute_query(query, data)
            self.connection.commit()
            return 'Just Marked'
        else:
            return 'Marked'


    def check_if_habit(self,user_id,habit_id,completion_date):
        query = "SELECT completion_date FROM completed_habits WHERE user_id = %s and habit_id=%s and completion_date=%s"
        data = (user_id,habit_id,completion_date)
        result = self.execute_query(query, data)

        if len(result)>0:
            return False
        else:
            return True




    def list_of_tracked_habit(self,user_id):
        list_of_habit = []

        query = "SELECT habit_id,task,frequency,period,start_date FROM habit WHERE user_id = %s and statuz='IN_PROGRESS' ORDER BY ordering_time DESC"
        data = (user_id,)
        result = self.execute_query(query, data)
        lenn=len(result)
        if lenn==0:
            return [89]
        for row in result:
            #print(f'habit_id {row[0]}, task {row[1]}, frequency {row[2]}')

            h=Habit(row[0],row[1],row[2],target_days=row[3])
            list_of_habit.append(str(h))
        return list_of_habit



    def get_habit_all_days(self,habit_id):

        all_days = []
        start_date=''
        freq=''
        period=''
        stop_date=''
        statuz = ''
        days=[]
        days_fulfilled=[]

        query = "SELECT start_date,frequency,period,statuz,stop_date FROM habit WHERE habit_id = %s ORDER BY ordering_time DESC"
        data = (habit_id,)
        result = self.execute_query(query, data)
        for row in result:
            start_date = row[0]
            freq = row[1]
            period = row[2]
            stop_date = str(row[4])
            statuz = row[3]

        print(freq)
        if freq=='Daily':
            days=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']

        if freq=='Weekly':
            days=list(period.split(" "))


       # z = datetime.datetime.today().strftime('%Y-%m-%d')

        presentday = datetime.datetime.today()
        tomorrow = presentday + datetime.timedelta(1)
        d=str(tomorrow)
        dd=d[:10]


        changingDaay = ''

        today = dd.replace('-', '')

        start_date=str(start_date)
        #start_date=str('2023-12-14')
        start_date = start_date.replace('-', '')
        print(statuz)
        if statuz=='STOPPED':
            today=stop_date.replace('-', '')

        print(f'start_date:::{start_date}')
        while changingDaay != start_date:

            date_obj = datetime.datetime.strptime(today, '%Y%m%d')
            a = date_obj + datetime.timedelta(days=-1)

            name_of_day = a.strftime('%A')
            # print(name_of_day)
            year_month_day = a.strftime('%Y-%m-%d')
            # print(year_month_day)
            if name_of_day in days:
                all_days.append(year_month_day)
            k = year_month_day.replace('-', '')
            today = k
            changingDaay = today



        query = "SELECT completion_date FROM completed_habits WHERE habit_id = %s"
        data = (habit_id,)
        result = self.execute_query(query, data)
        for row in result:
            days_fulfilled.append(str(row[0]))

        #all_days holds all possible days
        print(f'Total days passed: {all_days}')
        print(f'Days fullfilled: {days_fulfilled}')



        return (all_days,days_fulfilled)


    def list_of_a_user_habits(self, user_id):
        list_of_habit=[]

        query = "SELECT habit_id,task,frequency,period,statuz,start_date FROM habit WHERE user_id = %s ORDER BY ordering_time DESC"
        data = (user_id,)
        result = self.execute_query(query, data)

        for row in result:
            dict={}
            dict['habit_id']=row[0]
            dict['task'] = row[1]
            dict['frequency'] = row[2]
            dict['period'] = row[3]
            dict['status'] = row[4]
            dict['start_date'] = str(row[5])
            list_of_habit.append(dict)


        return list_of_habit



    def check_if_task_needs_to_be_mark(self,habit_id,present_day):
        query = "SELECT frequency,period FROM habit WHERE habit_id = %s"
        data = (habit_id,)
        result = self.execute_query(query, data)
        period=''
        for row in result:
            period=row[0]
            if row[0]=='Daily':
                period='Sunday Monday Tuesday Wednesday Thursday Friday Saturday'
            if row[0]=='Weekly':
                period=row[1]

        status = False

        if present_day in period:

            status = True
        else:
            return ['Not one of task days']

        if status:
            today = datetime.datetime.today()
            d = str(today)
            d = d[:10]


            get_all_marked_date = []

            query = "SELECT completion_date FROM completed_habits WHERE habit_id = %s"
            data = (habit_id,)
            result = self.execute_query(query, data)
            for row in result:
                get_all_marked_date.append(str(row[0]))

            if len(get_all_marked_date) == 0:
                #'No date marked yet, checked box should be visible'
                return '678'
            if d in get_all_marked_date:
                #'It has been marked already, checked box should not be visible'
                return '677'
            else:
                #'It needs to be marked, checked box should be visible'
                return '678'




    def weekly_list_of_a_user_habits(self, user_id):
        list_of_habit=[]

        query = "SELECT habit_id,task,frequency,period,statuz,start_date FROM habit WHERE user_id = %s and frequency='Weekly' ORDER BY ordering_time DESC"
        data = (user_id,)
        result = self.execute_query(query, data)

        for row in result:
            dict={}
            dict['habit_id']=row[0]
            dict['task'] = row[1]
            dict['frequency'] = row[2]
            dict['period'] = row[3]
            dict['status'] = row[4]
            dict['start_date'] = str(row[5])
            list_of_habit.append(dict)


        return list_of_habit



    def daily_list_of_a_user_habits(self, user_id):
        list_of_habit=[]

        query = "SELECT habit_id,task,frequency,period,statuz,start_date FROM habit WHERE user_id = %s and frequency='Daily' ORDER BY ordering_time DESC"
        data = (user_id,)
        result = self.execute_query(query, data)

        for row in result:
            dict={}
            dict['habit_id']=row[0]
            dict['task'] = row[1]
            dict['frequency'] = row[2]
            dict['period'] = row[3]
            dict['status'] = row[4]
            dict['start_date'] = str(row[5])
            list_of_habit.append(dict)


        return list_of_habit

    def convert_str_list(self,string):
        li = list(string.split(" "))
        return li
    def all_habit_longest_streak(self,user_id):

        dictt={}
        dictt2 = {}

        temp=[]
        period=[]
        query = "SELECT habit_id,frequency,period,task,statuz,start_date FROM habit WHERE user_id = %s"
        data = (user_id,)
        result = self.execute_query(query, data)
        for row in result:

            dictt2[row[0]]=[row[0],row[3],row[2],row[1],str(row[5]),row[4]]

            queryy = "SELECT completion_date FROM completed_habits WHERE habit_id = %s"

            dataa = (row[0],)
            resultt = self.execute_query(queryy, dataa)
            temp.clear()
            for roww in resultt:
                if row[1]=='Daily':
                    period = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
                else:
                    period=self.convert_str_list(row[2])


                temp.append(str(roww[0]))
                s = Streak(period, temp)

            dictt[row[0]] = s.longest_streakz()


        val=[]
        val.append(dictt)
        val.append(dictt2)

        return val


    def habit_longest_streak(self,habit_id):

        dictt={}
        dictt2 = {}

        temp=[]
        period=[]
        query = "SELECT habit_id,frequency,period,task,statuz,start_date FROM habit WHERE habit_id = %s"
        data = (habit_id,)
        result = self.execute_query(query, data)
        for row in result:

            dictt2[row[0]]=[row[0],row[3],row[2],row[1],str(row[5]),row[4]]

            queryy = "SELECT completion_date FROM completed_habits WHERE habit_id = %s"

            dataa = (row[0],)
            resultt = self.execute_query(queryy, dataa)
            temp.clear()
            for roww in resultt:
                if row[1]=='Daily':
                    period = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
                else:
                    period=self.convert_str_list(row[2])


                temp.append(str(roww[0]))
                s = Streak(period, temp)

            dictt[row[0]] = s.longest_streakz()


        val=[]
        val.append(dictt)
        val.append(dictt2)

        return val

from datetime import datetime
class Streak:
    def __init__(self,period,fulfilled):
        self.period=period
        self.fulfilled=fulfilled
        self.period=self.impose_order()


    def impose_order(self):
        days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        the_order = ['', '', '', '', '', '', '']
        k = 0
        for i in days:
            for j in self.period:
                if i == j:
                    the_order[k] = i

            k = k + 1
        for i in the_order:
            if i == '':
                the_order.remove('')

        return  the_order



    def orderr(self,d1, d2):
        # order=['Monday','Wednesday','Friday','Saturday']
        order = self.period

        ind1 = order.index(d1)
        ind2 = order.index(d2)
        dif = ind2 - ind1

        if ind2 == 0 and ind1 == len(order) - 1:
            return True
        if dif == 1:
            return True
        else:
            return False
        return False

    def if_they_are_same_week_range(self,day1, day2):
        dictt = {}

        dayy1 = datetime.strptime(day1, "%Y-%m-%d").date()
        dayy2 = datetime.strptime(day2, "%Y-%m-%d").date()
        wn1 = dayy1.strftime("%V")  # the week
        wn2 = dayy2.strftime("%V")  # the week

        dow = dayy1.strftime("%A")
        dow2 = dayy2.strftime("%A")

        t1 = dayy1.timetuple()
        t2 = dayy2.timetuple()

        t11 = t1[7]
        t22 = t2[7]

        dictt['day1'] = [wn1, dow, t11]
        dictt['day2'] = [wn2, dow2, t22]
        return dictt

    def get_streak(self,a, b):
        dict = self.if_they_are_same_week_range(a, b)
        day1 = dict['day1']
        day2 = dict['day2']
        # print(day1[1])
        # print(day2[1])

        if self.orderr(day1[1], day2[1]):

            dif2 = abs(int(day1[2]) - int(day2[2]))
            if dif2 < 7:
                return True
            else:
                return False
        else:

            return False

    def longest_streakz(self):
        dictt = {}
        p = 0
        temp = set()
        # print(dates)
        current_streak = 0
        longest_streak = 0
        a = 0
        r = len(self.fulfilled) - 1
        for i in self.fulfilled:
            # print(i,a)

            if a == r:
                break
            else:
                # print(dates[a],dates[a+1])
                if self.get_streak(self.fulfilled[a], self.fulfilled[a + 1]):
                    current_streak += 1
                    temp.add(self.fulfilled[a])
                    temp.add(self.fulfilled[a + 1])

                    aa = temp.copy()
                    dictt[p] = aa




                else:
                    p = p + 1
                    temp.clear()
                    current_streak = 0

                longest_streak = max(longest_streak, current_streak)

            a = a + 1
        # j=list(temp)
        # jj=sorted(j)
        # print(jj)
        long = longest_streak + 1
        lon_arr = []

        for value in dictt.values():
            li = list(value)
            if len(li) == long:
                lon_arr = li

        return sorted(lon_arr)

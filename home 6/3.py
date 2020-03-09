class Worker:
    name = " "
    surname = " "
    position = " "
    wage = 0
    bonus = 0
    _income = {"wage": wage, "bonus": bonus}
class Position(Worker):
    def worker_info(self,name,surname,wage,bonus):
        get_full_name = str(name)+" " + str(surname)
        get_total_income = {"wage": wage, "bonus": bonus}
        all_cash = wage + bonus
        print(get_full_name +" "+str(get_total_income)+" ЗП: "+str(all_cash) )
w = Position()
w.worker_info("Sam","Kim",5000,1500)
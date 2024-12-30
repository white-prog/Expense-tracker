


class Expense:
    def __init__(self):
        self.expenses = []
    def add_expense(self,description,amount):
        from datetime import date
        Id = len(self.expenses) + 1
        date = date.today()
        try:
            self.expenses.append([Id,date,description,int(amount)])
        except:
            print("Inputs are not valid!")
        
    def update_expense(self,Id,description,amount):
        from datetime import date
        try:
            self.expenses[Id - 1][1] = date.today()
            self.expenses[Id - 1][2] = description
            self.expenses[Id - 1][3] = int(amount)
        except:
            print("Inputs are not valid!")
    def delete_expense(self,Id):
        try:
            self.expenses.remove(self.expenses[Id - 1])
        except:
            print("Id not found")
    def view_expenses(self):
        headers = ['ID','DATE','DESCRIPTION','AMOUNT']
        for elements in headers:
            print(elements,end = "     ")
        print()
        print("------------------------------------------------------------")
        for expense in self.expenses:
            for value in expense:
                print(value,end = "     ")
            print()
    def view_summary(self):
        total = 0
        for expense in self.expenses:
            total += expense[3]
        print(f"Total expense : {total}")
    def view_summary_for_month(self,month):
        total = 0
        for expense in self.expenses:
            dt = expense[1].split('-')
            if dt[1] == month:
                    total += expense[3]
        print(f"Total expense in {month} : {total}")
    def get_csv(self):
        import csv
        copy_expenses = self.expenses
        copy_expenses.insert(0,['ID','DATE','DESCRIPTION','AMOUNT'])
        with open('expenses.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(copy_expenses)

def main():
    

    expense_first = Expense()
    expense_first.add_expense("Food",60)
    expense_first.view_expenses()
    expense_first.get_csv()

if __name__ == "__main__":
    main()





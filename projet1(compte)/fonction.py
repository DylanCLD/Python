class Employee:
    def __init__(self, first_name, last_name, monthly_salary, is_commercial=False):
        self.first_name = first_name
        self.last_name = last_name
        self.monthly_salary = monthly_salary
        self.is_commercial = is_commercial

    def annual_salary(self):
        return self.monthly_salary * (13 if self.is_commercial else 12)

    def __str__(self):
        role = "commercial" if self.is_commercial else ""
        return f"firstName : {self.first_name:<10} lastName : {self.last_name:<10} mSal : {self.monthly_salary:<5} {role}"


class Factory:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def calculate_annual_cost(self):
        total_salaries = sum(emp.annual_salary() for emp in self.employees)
        return total_salaries * 1.70  

    def average_salary(self):
        if not self.employees:
            return 0
        total_salaries = sum(emp.annual_salary() for emp in self.employees)
        return total_salaries / len(self.employees)

    def display_info(self):
        annual_cost = self.calculate_annual_cost()
        avg_salary = self.average_salary()
        print(f"---> Firm: {self.name} AnnualCost: {annual_cost:.2f} AverageSal: {avg_salary:.2f}\n")
        for emp in self.employees:
            print(emp)

    def save_employees_to_file(self, filename="employees.txt"):
        with open(filename, "w") as file:
            for emp in self.employees:
                file.write(f"{emp}\n")
        print(f"Les informations des employés ont été enregistrées dans le fichier '{filename}'.")

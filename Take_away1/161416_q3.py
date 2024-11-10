class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"Employee ID: {self.employee_id}, Name: {self.name}, Salary: {self.salary}")

    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"Updated salary for {self.name} to {self.salary}")


class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Added {employee.name} to {self.department_name} department.")

    def calculate_total_salary_expenditure(self):
        total_salary = sum(employee.salary for employee in self.employees)
        print(f"Total salary expenditure for {self.department_name} department: {total_salary}")
        return total_salary

    def display_all_employees(self):
        print(f"Employees in {self.department_name} department:")
        for employee in self.employees:
            employee.display_details()

    def interactive_mode(self):
        while True:
            action = input("Choose an action: [1] Add employee, [2] Display total salary expenditure, [3] Display all employees, [4] Exit: ")
            if action == '1':
                name = input("Enter employee's name: ")
                employee_id = input("Enter employee's ID: ")
                salary = float(input("Enter employee's salary: "))
                employee = Employee(name, employee_id, salary)
                self.add_employee(employee)
            elif action == '2':
                self.calculate_total_salary_expenditure()
            elif action == '3':
                self.display_all_employees()
            elif action == '4':
                print("Exiting interactive mode.")
                break
            else:
                print("Invalid option. Please try again.")


if __name__ == "__main__":
    department_name = input("Enter department name: ")
    department = Department(department_name)
    department.interactive_mode()

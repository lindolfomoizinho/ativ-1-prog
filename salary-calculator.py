def calculate_total_salary(base_salary, total_sales, commission_percentage):
    commission = total_sales * (commission_percentage / 100)
    return  base_salary + commission

base_salary = float(input("Enter the employee's base salary: "))

total_sales = float(input("Enter the total sales amount: "))

commission_percentage = float(input("Enter the commission percentage: "))


total_salary = calculate_total_salary(base_salary, total_sales, commission_percentage)

print(f"The total salary of the employee is: ${total_salary:.2f}")
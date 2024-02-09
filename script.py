from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# load in financial data
financial_data = pd.read_csv('financial_data.csv')

# code goes here
print(financial_data.head())

month = financial_data['Month'] 
revenue = financial_data['Revenue'] 
expenses = financial_data['Expenses'] 
plt.plot(month, revenue)
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.title('Revenue')
plt.tight_layout()
plt.show()
plt.clf()

plt.plot(month, expenses)
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.title('Expenses')
plt.tight_layout()
plt.show()
plt.clf()


expense_overview = pd.read_csv('expenses.csv')
print(expense_overview)

expense_categories = ['Salaries', 'Advertising', 'Office Rent', 'Other']
proportions = [0.62, 0.15, 0.15, 0.08]
plt.pie(proportions, labels= expense_categories, autopct='%0.f%%')
plt.axis('equal')
plt.title('Expences Categories')
plt.tight_layout()
plt.legend()
plt.show()

employees_cut  = 'Salaries'

employees = pd.read_csv('employees.csv',encoding='latin-1')
# print(employees.head())
sorted_productivity = employees.sort_values(by=['Productivity'])
# print(sorted_productivity)
employees_cut = sorted_productivity.head(100)
# print(employees_cut)

transformation = 'standardization'

commute_times  = sorted_productivity['Commute Time']
commute_times_log = np.log(commute_times)
print(commute_times.describe())

plt.clf()

plt.hist(commute_times_log)
plt.title('Employee Commute Times')
plt.xlabel('Commute Time')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

scaler = StandardScaler()
income_product = ['Salary', 'Productivity']
scaler = StandardScaler()
for item in income_product:
  employees[item] = scaler.fit_transform(employees[[item]])
plt.scatter(employees.Salary, employees.Productivity)
plt.show()
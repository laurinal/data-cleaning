# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 11:00:18 2023

@author: iyino
"""

import pandas as pd
data = { "name": ['John', 'Mary', 'Bob', 'Sarah', 'Tom', 'Lisa'],
        "department":['IT', 'Marketing', 'Sales', 'IT', 'Finance', 'Marketing'],
        "age":[30, 40, 25, 35, 45, 28],
        "gender": ['Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
        "salary": [50000, 60000, 45000, 55000, 70000, 55000],
        "experience": [3, 7, 2, 5, 10, 4]}

employee_df = pd.DataFrame(data)

first_3_rows = employee_df.iloc[:3] 

Marketing_department = employee_df.loc[employee_df["department"] =="Marketing"]
print(Marketing_department)

age_gender_first_4_rows = employee_df.iloc[:4, [2,3]]

male_salary_experience = employee_df.loc[employee_df["gender"]=="Male", ["salary"]==["experience"]]
print(male_salary_experience)
 
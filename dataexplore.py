import pandas as pd
#Create a sample TXT file (CSV style for easy parsing)
with open("employees.txt", "w") as f:
    f.write("ID,Name,Department,Salary,JoiningDate\n")
    f.write("101,varun,CONSULTING,500000,2020-01-15\n")
    f.write("102,sundar,DIRECTOR,600000,2019-07-23\n")
    f.write("103,ravi,DIRECTOR,5500000,2021-03-10\n")
    f.write("104,pradeep,MANAGER,6500000,2018-11-05\n")
    f.write("105,ashish,DIRECTOR,5200000,2022-06-18\n")

#Read TXT into pandas DataFrame
df = pd.read_csv("employees.txt")
print(df)

#Explore Data
print(df.info(), "\n")
print(df.describe(include="all"), "\n")

#Data Cleaning
df["JoiningDate"] = pd.to_datetime(df["JoiningDate"])  
print("Data after converting JoiningDate:\n", df.dtypes, "\n")

#Filtering & Selecting
print("Employees with Salary > 50k:\n", df[df["Salary"] > 50000], "\n")
print("Name Salary\n", df[["Name", "Salary"]], "\n")

#Grouping & Aggregation
print("Average Salary by Department:\n", df.groupby("Department")["Salary"].mean(), "\n")
print("Count of Employees per Department:\n", df["Department"].value_counts(), "\n")

#Sorting
print("Employees sorted by Salary (Descending):\n", df.sort_values("Salary", ascending=False), "\n")

#Adding & Modifying Columns
df["Bonus"] = df["Salary"] * 0.10
print("Added Bonus Column:\n", df, "\n")

df["Seniority"] = (pd.Timestamp("2025-10-03") - df["JoiningDate"]).dt.days // 365
print("Added Seniority Column (Years):\n", df, "\n")

#Merging / Joining
dept_managers = pd.DataFrame({
    "Department": ["HR", "IT", "Finance"],
    "Manager": ["Sophia", "Liam", "Olivia"]
})
merged_df = pd.merge(df, dept_managers, on="Department", how="left")
print("Merged Data with Managers:\n", merged_df, "\n")

#Pivot Table
pivot = pd.pivot_table(df, values="Salary", index="Department", aggfunc="mean")
print("Pivot Table - Avg Salary per Department:\n", pivot, "\n")

#Export to CSV / Excel
df.to_csv("cleaned_employees.csv", index=False)
df.to_excel("cleaned_employees.xlsx", index=False)
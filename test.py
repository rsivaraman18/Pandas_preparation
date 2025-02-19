import pandas as pd
data  = pd.read_csv("student_sample.csv")
df = pd.DataFrame(data)

# print(df)
# print(df.head())
# print(df['Name'])
# print(df[['Name','Maths']])
# print(df['Name']=='Surya')

# print(df[df['Name']=='Surya'])
# # print(df[(df['Name'] == 'Priya') | (df['Name'] == 'Surya')])
# print(df.isna())  # Check missing values
# print(df.isna().sum())  # Count missing values per column

# new_record = df.fillna({'Name':'No Name', 'Age': "No Age"})
# print(new_record)

# df_filled = df.fillna({"Age": df["Age"].mean(), "Salary": df["Salary"].median()})
# print(df_filled)

# df_dropped = df.dropna()  # Drops rows where any column has NaN
# print(df_dropped)

# df_filled = df.fillna("Empty ")
# print(df_filled)


# print(df.tail(3))
# df_unique = df.drop_duplicates()
# print(df_unique.tail(3))



# df["Name"] = df["Name"].replace({"Arjun": "KKKKJK", "Bob": "Robert"})
# print(df.head(5))

# df = df.replace({"India": "Country"})
# print(df.tail(5))

# print(df[df["Name"].str.contains("Ramesh",na=False)])

# df["Name"] = df["Name"].str.replace("Bobby", "Ramesh")
# print(df.tail(5))

# df[["First_Name", "Last_Name"]] = df["Full_Name"].str.split(" ", expand=True)
# print(df)

# df["Category"] = df["Age"].map(lambda x: "Young" if x < 30 else "Old")
# print(df.head())


# df["Category"] = pd.Categorical(df["Category"])
# print(df.head(3))
# print(df.dtypes)

# df["total"] = [ [100], [200], [300], [140], [160],  ]
# df = df.drop(columns=['English'])
# df = df.drop(columns=['English','Location'])

# df["Age_Squared"] = df["Age"].apply(lambda x: x ** 2)
# # df["Age_Category"] = df["Age"].map(lambda x: "Young" if x < 30 else "Old")
# df_numeric = df[["Age_Squared"]].applymap(lambda x: x / 10)  # Works on all elements
# print(df_numeric.head(3))

# df = df.sort_values("Name",ascending=False)
# df = df.sort_values(["Name","Maths"],ascending=False)
# df = df.sort_values(by=["Name","Location"],ascending=False)


# df_sorted_index = df.sort_index([2])
# print(df_sorted_index)
# print(df.head(3))


df = pd.DataFrame({
    "Department": ["HR", "IT", "IT", "HR", "Finance"],
    "Salary": [50000, 70000, 80000, 55000, 60000]
})

grouped = df.groupby("Department")
print(grouped)
# grouped = df.groupby("Department").agg({"Salary": ["mean", "sum"]})







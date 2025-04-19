import pandas as pd
df = pd.read_csv("emp.csv")
print(df)
sorted_values= df.sort_values(by =['deptno','salary'], ascending=[True,False])
print(sorted_values)
sort_by_index= df.sort_index(ascending = False)
print(sort_by_index)
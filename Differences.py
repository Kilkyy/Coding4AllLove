import pandas as pd

# Load the first Excel file
df1 = pd.read_excel("file1.xlsx")

# Load the second Excel file
df2 = pd.read_excel("file2.xlsx")

# Compare the two dataframes and store the differences in a new dataframe
df_diff = df1.merge(df2, indicator=True, how='outer').query("_merge != 'both'")

# Drop the merge column
df_diff.drop(columns=['_merge'], inplace=True)

# Save the differences to a new Excel file
df_diff.to_excel("differences.xlsx", index=False)


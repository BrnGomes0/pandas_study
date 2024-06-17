# Imports the libraries
import pandas as pd

# Creating a connection with .xlsx
data_frame = pd.read_excel("C:/Users/GOB8CA/Documents/studyPandas/tables/table_excel.xlsx", sheet_name="Call List")

# Removing the duplicates rowns
data_frame.drop_duplicates(inplace=True)

# Drop the column
data_frame.drop(columns="Not_Useful_Column", inplace=True)

# Removing the spaces in left and right (both)
# data_frame["Last_Name"].str.strip()

# Removing left spaces -> lstrip()
# data_frame["Last_Name"].str.lstrip()

# Remoging right spaces -> rstrip()
# data_frame["Last_Name"].str.rstrip()

# First Way
# Removing with a char with strip
# data_frame["Last_Name"] = data_frame["Last_Name"].str.lstrip("...")
# data_frame["Last_Name"] = data_frame["Last_Name"].str.lstrip("/")
# data_frame["Last_Name"] = data_frame["Last_Name"].str.rstrip("_")

# Second Way (with list of char)
data_frame["Last_Name"] = data_frame["Last_Name"].str.strip("._/")

# Removing the chars
# It is a regular expression that matches any character that is not a letter (upper or lower case) or a digit (0 to 9).
# The ^ inside the brackets [] reverses the pattern, that is, it selects all characters that are not letters or digits.
# Regex=True, for To interpret the logic for replace
data_frame["Phone_Number"] = data_frame["Phone_Number"].str.replace("[^a-zA-Z0-9]", "", regex=True)


data_frame["Phone_Number"] = data_frame["Phone_Number"].apply(lambda x: str(x))
data_frame["Phone_Number"] = data_frame["Phone_Number"].apply(lambda x: x[0:3] + "-" + x[3:6] + "-" +  x[6:10])

data_frame["Phone_Number"] = data_frame["Phone_Number"].str.replace("nan--", "")
data_frame["Phone_Number"] = data_frame["Phone_Number"].str.replace("Na--", "")


# Creating a new column for the field
data_frame[["Street_Address", "State", "Zip_Code"]] = data_frame["Address"].str.split(',',n=2, expand=True)
data_frame["Street_Address"] = data_frame["Street_Address"].str.replace("N/a", "")

# Deleted all fields with None (is used for replace Not a Number (NaN) values in the Column (Zip_Code), and replace for a empty String (""))
data_frame["State"] = data_frame["State"].fillna("")
data_frame["Zip_Code"] = data_frame["Zip_Code"].fillna("")

# The all data_frame
# data_frame.fillna("")

# Drop the column Address
data_frame.drop(columns="Address", inplace=True)

data_frame["Paying Customer"] = data_frame["Paying Customer"].str.replace("Yes", "Y")
data_frame["Paying Customer"] = data_frame["Paying Customer"].str.replace("No", "N")
data_frame["Paying Customer"] = data_frame["Paying Customer"].str.replace("N/a", "")

data_frame["Do_Not_Contact"] = data_frame["Do_Not_Contact"].str.replace("Yes", "Y")
data_frame["Do_Not_Contact"] = data_frame["Do_Not_Contact"].str.replace("No", "N")
data_frame["Do_Not_Contact"] = data_frame["Do_Not_Contact"].fillna("")

for x in data_frame.index:
    if data_frame.loc[x, "Do_Not_Contact"] == "Y":
        data_frame.drop(x, inplace=True )

for x in data_frame.index:
    if data_frame.loc[x, "Phone_Number"] == "":
        data_frame.drop(x, inplace=True )

# data_frame.reset_index(drop=True)
# data_frame = data_frame.dropna(subset="Phone_Number", inplace=True)


print(data_frame)  
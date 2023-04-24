import pandas as pd




def basic_cleaning_1 (df):
    """
    This function drops missing values and duplicates rows; 
    and sets each column name to lowercase and strips whitespaces from left and right.
    """
    
    # 1. Modify the dataframe
        # 1.1 Lowercase and remove leading and trailing whitespaces:
    df.columns = [i.lower().replace(" ", "_") for i in df.columns.str.strip()]
        # 1.2 Drop null values:
    df.dropna(how="all", inplace = True)
        # 1.3 Drop duplicates:
    df.drop_duplicates(inplace=True)
    
    return df


def basic_cleaning_2 (df):
    """
    This function drops the selected columns useless for the analysis.
    """
    
    # 1. Modify the dataframe
        # 1.1 Drop selected columns useless for the analysis:
    df.drop(columns=["case_number", "investigator_or_source", "pdf", "href_formula", "href", "case_number.1", "case_number.2", "original_order", "unnamed:_22", "unnamed:_23"], axis = 1, inplace = True)
    
    return df


def cleaning_question_1 (df):
    """
    This function drops: 
    """
    
    # 1. Modify the dataframe:
        # 1.1 Drop null values:
    df = df[["activity", "fatal_(y/n)"]].dropna(how="all")    
        # 1.2 Cast values into string:
    df = df.astype(dtype=str)    
    
    # 2. Modify the column "activity":
        # 2.1 Set values to lowercase:
    df["activity"] = [i.lower() for i in df["activity"]]
        # 2.2 Filter to keep only the rows where the "activity" column contains the words "swim" or "surf" 
    df = df[df["activity"].str.contains("swim|surf") == True]
        # 2.3 Create new column called "activity_swim_surf", with values of "swim" or "surf" depending on whether the word "swim" is present in the "activity" column or not. 
    df["activity_swim_surf"] = df["activity"].apply(lambda x:"swim" if "swim" in x else "surf")
    
    # 3. Modify the column "fatal_(y/n)"
        # 3.1 Set values to lowercase and remove leading and trailing whitespaces:
    df["fatal_(y/n)"] = [i.lower() for i in df["fatal_(y/n)"].str.strip()]
        # 3.2 Filter to exclude those rows where the value in the "fatal_(y/n)" column is "UNKNOWN":
    df = df[df["fatal_(y/n)"] != "UNKNOWN"]
 
    return df



def cleaning_question_2 (df):
    """
    This function drops: 
    """
    
    # 1. Modify the dataframe:
        # 1.1 Drop null values:
    df = df[["age", "fatal_(y/n)"]].dropna(how="any")
        # 1.2 Cast values into string:
    df = df.astype(dtype=str)

    # 2. Modify the column "age":
        # 2.1 Chek age values whose length is greater than 2 (means data entry error):
    for i in df["age"]:
        if len(i) > 2:
            print(i)
        # 2.2 Set values to lowercase and remove leading and trailing whitespaces.
    df["age"] = [i.lower() for i in df["age"].str.strip()]
        # 2.3 Update the "age" column by extracting the first two characters if the string has more than two characters and contains an "s", otherwise it leaves the original value unchanged (eg. 30s, 40s, etc.)
    df["age"] = df["age"].apply(lambda x : x[0:2] if len(x) == 3 and "s" in x else x)
        # 2.4 Update the "age" column by replacing the substring "teen" with "15".
    df["age"] = df["age"].str.replace("teen", "15")
        # 2.5 Update the "age" column by removing whitespaces and extracting the first two characters from the string if it contains "or".
    df["age"] = df["age"].apply(lambda x : x.strip()[0:2] if "or" in x else x)
        # 2.6 Update the "age" column by removing whitespaces and extracting the first two characters from the string if it contains "to".
    df["age"] = df["age"].apply(lambda x : x.strip()[0:2] if "to" in x else x)
        # 2.7 Filter rows where the "age" column contains "&" because as it is referring to more than one person we assume it is not valid data.
    df = df[df["age"].str.contains("&")==False]
        # 2.8 Manual replacements.
    df["age"] = df["age"].str.replace("15s", "15")
    df["age"] = df["age"].str.replace(">50", "50")
    df["age"] = df["age"].str.replace("18 months", "1")
    df["age"] = df["age"].str.replace("mid-30s", "35")
    df["age"] = df["age"].str.replace("20?", "20")
    df["age"] = df["age"].str.replace("60's", "60")
    df["age"] = df["age"].str.replace("mid-20s", "20")
    df["age"] = df["age"].str.replace("ca. 33", "33")
    df["age"] = df["age"].str.replace("2½", "2")
        # 2.9 Set the remaining values to "excluded values", because their weight is not significant.
    df["age"] = df["age"].apply(lambda x : "excuded values" if len(x) > 2 else x)
        # 2.10 Convert the "age" column to numeric data type.
    df["age"] = pd.to_numeric(df["age"], errors='coerce')

    # 3. Modify the column "fatal_(y/n)":
        # 3.1 Remove leading and trailing whitespaces.
    df["fatal_(y/n)"] = df["fatal_(y/n)"].str.strip()
        # 3.2 Filter to exclude rows where the "fatal_(y/n)" column contains the value "UNKNOWN", "M" or "2017".
    df = df[df["fatal_(y/n)"] != "UNKNOWN"]
    df = df[df["fatal_(y/n)"] != "M"]
    df = df[df["fatal_(y/n)"] != "2017"]
        # 3.3 Updates the "fatal_(y/n)" column by replacing "Y" with "Yes" and "N" with "No".
    df["fatal_(y/n)"] = df["fatal_(y/n)"].str.replace("Y", "Yes")
    df["fatal_(y/n)"] = df["fatal_(y/n)"].str.replace("N", "No")

    return df




def cleaning_question_3 (df):
    """
    This function drops: 
    """
    
    # 1. Modify the dataframe:
        # 1.1 Drop null values:
    df = df[["year"]].dropna(how="all")        
        # 1.2 Cast values into string:
    df = df.astype(dtype=str)
        # 1.3 Filter the "year" column into include only rows where the values start with "1" or "2".
    df = df[df["year"].str.startswith(('1', '2'))]
        # 1.4 Converts the "year" column to numeric type.
    df['year'] = pd.to_numeric(df['year'], errors='coerce')
        # 1.5 Remove rows whose year is previous to 1800 since the number of sharck attacks is not significant.
    df = df[df['year'] > 1800]

    return df

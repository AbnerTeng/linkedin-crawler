import pandas as pd

def get_full_df(path3):
    df1 = pd.read_csv('job_df.csv')
    df2 = pd.read_csv('descrip_df.csv')

    try:
        big_df = pd.concat([df1, df2], axis = 1)
        big_df.head()
        big_df.to_csv(path3, index = False, encoding = "utf-8-sig")

    except:
        print("Dimension Error: Please check the dimension of the two dataframes")

    

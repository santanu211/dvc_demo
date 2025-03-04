import pandas as pd
import numpy as np
import os


df=pd.read_csv(r"c:\Users\Admin\Downloads\student_data_100.csv")
print(df.head(1))

df=df.drop(["Student_ID","Gender","Major","Age"],axis=1)
print(df.head(1))

if "Credits_Completed" in df.columns:
    # Drop NaN values before filtering
    df = df[df["Credits_Completed"].notnull()]
    
    # Apply filter
    df = df[df["Credits_Completed"] > 60]



df.to_csv(os.path.join("data","student.csv"))

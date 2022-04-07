import pandas as pd
df=pd.read_csv("C:\\Users\\banga\\gitremoterepo\\Ex-02_DS_Outlier\\weight.csv")
df
df.drop("Gender",axis=1,inplace=True)
df
# df=df.drop("Gender",axis=1,inplace=True)
df.boxplot()
from scipy import stats
import numpy as np
z=np.abs(stats.zscore(df))
z
df
df1=df.copy()
df1=df1[(z<3).all(axis=1)]
df1.boxplot()
df1
#interquartile method
          df2=df.copy()
q1=df2.quantile(0.25)
q3=df2.quantile(0.75)
IQR=q3-q1
          IQR
IQR.Height
df2_new=df2[((df2>=q1-1.5*IQR)&(df2<=q3+1.5*IQR)).all(axis=1)]
df2



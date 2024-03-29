# -*- coding: utf-8 -*-
"""FMLBasePlot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rzLQqR8_XpGA2nz40gmsv_DF5O1JJ29O
"""

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("/content/dev.results.summary.txt", sep= " ", names = ["log3C", "d", "acc", "std"])
df['std'] = df['std'].fillna(0)
df['error'] = 1- df['acc']
df['upper_bound'] = df['std'] + df['error']
df['lower_bound'] = - df['std'] +df['error']

df

for n, df_n in df.groupby('d'):
    ax = plt.gca()
    df = df.sort_values(by = 'log3C')
    df_n.plot(kind='line',x='log3C',y='error',ax = ax)
    df_n.plot(kind='line',x='log3C',y='upper_bound', color='grey' ,ax = ax)
    df_n.plot(kind='line',x='log3C',y='lower_bound', color='grey',ax = ax)
    
    plt.xlabel("k: C = 3^k")
    plt.ylabel("Cross Validation Error")
    plt.title("d = "+ str(n))
    
    plt.savefig("d"+ str(n)+".png")
    plt.show()
    # print(df_n)
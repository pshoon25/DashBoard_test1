import pandas as pd
import numpy as np

df = pd.read_csv('이지체인_기간별_')

df.head()

# df['취소일자'].isnull()

# a = []
# for i in df['취소일자'].isnull() :
#     if i == True :
#         a.append(df['취소일자'])
#     else :
#         a.append(df['구매일자'])


# print(a)
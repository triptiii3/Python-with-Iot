from matplotlib import pyplot as plt
import numpy as np
import math

# x=np.arange(0,math.pi*2,0.05)
# y=np.tan(x)
# plt.plot(x,y)
# plt.xlabel("angle")
# plt.ylabel("sine")
# plt.title('sine wave')
# plt.show()

# fig,a=plt.subplots(2,2)
# x=np.arange(1,5)
# a[0][0].plot(x,x*x)
# a[0][0].set_title('square')
# a[0][1].plot(x,np.sqrt(x))
# a[0][1].set_title('square root')
# a[1][0].plot(x,np.exp(x))
# a[1][0].set_title('exp')
# a[1][1].plot(x,np.log10(x))
# a[1][1].set_title('log')
# plt.show()

# fig=plt.figure()
# ax=fig.add_axes([0,0,1,1])
# langs=['C','C++','Java','Python','PHP']
# students=[23,17,35,29,12]
# ax.bar(langs,students)
# plt.show()

# import pandas as pd
# ts=pd.Series(np.random.randn(1000),index=pd.date_range('1/1/2000',periods=1000))
# df=pd.DataFrame(np.random.randn(1000,4),
#                 index=ts.index,columns=list('ABCD'))
# df=df.cumsum()
# plt.figure()
# df.plot()
# plt.show()

import seaborn as sns
import pandas as pd
df = pd.read_csv("C:/Users/Tripti/Downloads/Titanic/tested.csv")
# # sns.heatmap(df.corr(),annot=True,cmap='coolwarm',linewidths=2)
# # sns.distplot(df['name'],bins=50,kde=False,vertical=True)
# plt.show()

# y=list(df.Age)
# print(y)
# plt.boxplot(y)
# plt.show()

# sns.barplot(y=df['Age'])
# plt.show()

# sns.boxplot(y=df['Age'],color='g')
# plt.show()

# sns.countplot(df[''])

# sns.violinplot(x=df['Survived'],y=df['Age'],width=0.5)

sns.stripplot(x=df['Survived'],y=df['Age'],jitter=False)
plt.show()





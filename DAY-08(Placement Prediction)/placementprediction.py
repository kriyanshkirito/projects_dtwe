# %%
import numpy as np
import pandas as pd

# %%
df=pd.read_csv(r"C:\Users\hp\Downloads\placement.csv")

# %%
df.head()

# %%
df.shape

# %%
# this is very less size so our model would not be predict new values greatly ,i take this small dataset becuse today i have not get more free time 

# %%
df.drop(columns=['Unnamed: 0'],inplace=True)

# %%
df.head()

# %%
import matplotlib.pyplot as plt;
import seaborn as sns

# %%
sns.scatterplot(x=df['cgpa'],y=df['iq'],hue=df['placement'])

# %%
df['cgpa'].skew()

# %%
df['iq'].skew()

# %%
df['placement'].skew()

# %%
X=df.iloc[:,0:2]
y=df.iloc[:,-1]

# %%
X

# %%
from sklearn.model_selection import train_test_split

# %%
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

# %%
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression

# %%



# %%
# model2.fit(X_train,y_train)

# %%


# %%


# %%


# %%
trf1=ColumnTransformer([('cgpa',StandardScaler(),[0]),
                      ('iq',StandardScaler(),[1]) ])
trf2=LogisticRegression()


# %%
pickle.dump(pipe,open('pipe.pkl','wb'))

# %%
pipe=Pipeline([
    ('trf1',trf1),
    ('trf2',trf2)
])

# %%
pipe.fit(X_train,y_train)

# %%
y_pred=pipe.predict(X_test)

# %%
from sklearn.metrics import accuracy_score

# %%
accuracy_score(y_test,y_pred)

# %%
import pickle

# %%
pickle.dump(pipe,open('pipe.pkl','wb'))

# %%
test_input=np.array([6,130]).reshape(1,2)

# %%
pipe.predict(test_input)

# %%




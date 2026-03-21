
# In[1]:
# we are going to make model which can predict if we advertise any specific product on social media does it affect and people purchased the product

# In[2]:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

# In[3]:
df2=pd.read_csv(r"C:\Users\hp\Downloads\Social_Network_Ads.csv")

# In[4]:
df2.sample(5)

# In[5]:
df1=df2.rename(columns={'Purchased':'Purchased After Watching Ads'})

# In[6]:
df=df1.drop(['User ID'],axis=1)

# In[7]:


# In[8]:


# In[9]:
df.head()

# In[10]:
df.shape

# In[11]:
df.isnull().sum()   #  no null values so ok

# In[12]:


# In[13]:
X=df.iloc[:,0:3]

# In[14]:
y=df.iloc[:,-1]

# In[15]:
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

# In[16]:
X_train

# In[17]:
y_test

# In[18]:
KBins_age=KBinsDiscretizer(n_bins=10,encode='ordinal',strategy='quantile')
KBins_salary=KBinsDiscretizer(n_bins=10,encode='ordinal',strategy='quantile')

# In[19]:
trf1=ColumnTransformer([('first',KBins_age,[1]),
                       ('second',KBins_salary,[2])
                       ])

# In[20]:
trf1.transformers

# In[21]:
trf2=ColumnTransformer([
    ('Gender',OneHotEncoder(sparse_output=False,handle_unknown='ignore'),[0])
])

# In[22]:
trf3=DecisionTreeClassifier()

# In[23]:
# if we use pipeline then we need one .pkl file not two but if not we need two one for tranformation and other for model 
# thts why we use pipeline

# In[24]:
from sklearn.pipeline import Pipeline

# In[25]:
pipe=Pipeline([
    ('trf1',trf1),
    ('trf2',trf2),
    ('trf3',trf3)
])

# In[26]:
pipe.named_steps

# In[27]:
pipe.fit(X_train,y_train)

# In[28]:
y_pred=pipe.predict(X_test)

# In[29]:
print(y_pred)

# In[30]:
test_input=np.array([['Female',40,80000]],dtype=object)

# In[31]:
print(pipe.predict(test_input))

# In[32]:
# our model is ready but we want to draw corrleation matricx of all becuse previosuly gender was not one hot encoded so we not use so now we are using it

# In[33]:
import pickle

# In[34]:
pickle.dump(pipe,open('pipe.pkl','wb'))

# In[35]:

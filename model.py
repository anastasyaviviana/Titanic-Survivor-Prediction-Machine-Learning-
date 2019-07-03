#DATASET TITANIC SEABORN WITH LOGISTIC REGRESSION
import pandas as pd
import numpy as np
import seaborn as sns

df=sns.load_dataset('titanic')
df=df.drop(['class','deck','embarked','alive','alone'],axis=1)        #drop variabel 
df=df.dropna(axis=0)                                                  #drop na values

# sklearn one hot encoding
# labelling
from sklearn.preprocessing import LabelEncoder
label=LabelEncoder()
df['sex']=label.fit_transform(df['sex'])                        #['female' 'male']
print(label.classes_)   #check label class of dummy
df['embark_town']=label.fit_transform(df['embark_town'])        #['Cherbourg' 'Queenstown' 'Southampton']
print(label.classes_)
df['who']=label.fit_transform(df['who'])                        #['child' 'man' 'woman']
print(label.classes_)

var_x=df.drop(['survived'],axis=1).values
print(pd.DataFrame(var_x))
var_y=df['survived']

# one hot encoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

coltrans=ColumnTransformer(
    [('one_hot_encoder',OneHotEncoder(categories='auto'),[1,6,8])],remainder='passthrough'
)
var_x=np.array(coltrans.fit_transform(var_x))
print(pd.DataFrame(var_x).head())

#splitting
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(var_x,var_y,test_size=0.1)

#logistic regression
from sklearn.linear_model import LogisticRegression
model=LogisticRegression(solver='liblinear',multi_class='auto')
model.fit(xtrain,ytrain)

#predict all data
df['predict']=model.predict(var_x)      #variabel prediksi
print(df.head())
print('Score model = {}%'.format(round(model.score(xtest,ytest)*100,2)))

#save model
import joblib
joblib.dump(model,'modeltitanic')

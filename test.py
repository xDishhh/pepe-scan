**Lab_sheet-1**
**Example:1**
students=[{"name":"Alice","age":18},{"name":"Bob","age":20},{"name":"Charlie","age":19},{"name":"David","age":21},{"name":"Eve","age":18},]
total_age=0
for student in students:
  total_age+=student["age"]

average_age=total_age/len(students)

print(f"The average age of the students is : {average_age:.2f}")

youngest_student=min(students,key=lambda x:x["age"])
oldest_student=max(students,key=lambda x:x["age"])

print(f"The youngest student is {youngest_student['name']} with age {youngest_student['age']}")
print(f"The youngest student is {oldest_student['name']} with age {oldest_student['age']}")
**Example:2**
ages=[25,30,22,28,35]
names=["Alice","Bob","Carol","David","Eve"]
total_age=sum(ages)
num_people=len(ages)
average_age=total_age/num_people
print("Average age:",average_age)
**Example:3**
books=[{"title":"Harry Potter","author":"J.K. Rowling","genre":"Fantasy","year":1997},
       {"title":"To Kill a Mockingbird","author":"Harper Lee","genre":"Fiction","year":1960},
       {"title":"1984","author":"George Orwell","genre":"Dystopian","year":1949},
       {"title":"The Great Gatsby","author":"F. Scott Fitgerald","genre":"Classic","year":1925}]

print("Book info")

for book in books:
  print("Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}, Year: {book['year']}")
  total_year = 0

for book in books:
  total_year += book['year']
  average_year = total_year / len(books)
  print(f"Average Publication Year of Books: {average_year:.2f}")
  count_classic_books = 0

for book in books:
  if book['genre'] == 'Classic':
    count_classic_books += 1
    print(f"Number of Books in the 'Classic' Genre: {count_classic_books}")
------------------------------------------------------------------------------------------------------------------------------------
**Lab_sheet-2**
from sklearn import tree
from pandas import read_csv
import os
import numpy as np
df=read_csv("diabetes.csv")
x=np.array(df.drop(["Outcome"],1))
y=np.array(df["Outcome"])
y
print(df.head(10))
print(df.isnull().sum())
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy='mean')
meanx=imputer.fit_transform(x)
meanx
from sklearn.preprocessing import MinMaxScaler, StandardScaler
minmax_scaler=MinMaxScaler()
x_minmax=minmax_scaler.fit_transform(x)
x_minmax
zscore_scaler=StandardScaler()
z_zscore=zscore_scaler.fit_transform(x)
z_zscore
from sklearn.preprocessing import RobustScaler
robust_scaler=RobustScaler()
x_robust=robust_scaler.fit_transform(x)
x_robust
------------------------------------------------------------------------------------------------------------------------------------
**Lab_sheet-3**
from sklearn import tree
from pandas import read_csv
import os
import numpy as np
df = read_csv("sales_data_sample.csv")
df.head()
df.info()
x=np.array(df.drop(["SALES"],1))
y=np.array(df["SALES"])
df.describe()
df.shape
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.3, random_state=100)
from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(x_train, y_train)
y_pred=model.predict(x_test)
y_pred
test=np.array([3,7,2003,10134,41,94,74])
reshaped_test=test.reshape(1,-1)
reshaped_test
y_pred=model.predict(reshaped_test)
y_pred
intercept=model.intercept_
coefficients=model.coef_
print("intercept",intercept)
print("coefficents",coefficients)
------------------------------------------------------------------------------------------------------------------------------------
**Lab_sheet-4**
from sklearn import tree
from pandas import read_csv
import os
import numpy as np
df=read_csv("/content/diabetes.csv")

x=np.array(df.drop(["Outcome"],1))
y=np.array(df["Outcome"])
df.head()
from sklearn.feature_selection import SelectKBest, chi2, RFE
k_best=SelectKBest(score_func=chi2,k=5)
x_kbest=k_best.fit_transform(x,y)
x_kbest
from sklearn.ensemble import RandomForestClassifier
estimator = RandomForestClassifier(random_state=42)
rfe=RFE(estimator,n_features_to_select=4,step=1)
x_rfe=rfe.fit_transform(x,y)
x_rfe
rf_model=RandomForestClassifier(random_state=42)
rf_model.fit(x,y)
feature_importances=rf_model.feature_importances_
sorted_indices=np.argsort(feature_importances)[::-1]
top_features_indices=sorted_indices[:4]
x_rf_importance=x[:,top_features_indices]
x_rf_importance
------------------------------------------------------------------------------------------------------------------------------------
**Labsheet-5**

from pandas import read_csv
import numpy as np
df=read_csv("diabetes.csv")
df
x=np.array(df.drop(["Outcome"],1))
y=np.array(df["Outcome"])
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=100)
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
x_train=scaler.fit_transform(x_train)
x_test=scaler.transform(x_test)
x_train
from sklearn.linear_model import LogisticRegression
logistic_regression=LogisticRegression()
logistic_regression.fit(x_train,y_train)
y_pred=logistic_regression.predict(x_test)
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
accuracy=accuracy_score(y_test,y_pred)
print(accuracy*100,"%")
matrix=confusion_matrix(y_test,y_pred)
print(matrix)

report=classification_report(y_test,y_pred)
print(report)
------------------------------------------------------------------------------------------------------------------------------------
**Lab_sheet-6**
from sklearn import tree
from pandas import read_csv
import numpy as np
df=read_csv("glass.csv")
df
x=np.array(df.drop(["Type"],1))
y=np.array(df["Type"])
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=100)
from sklearn.linear_model import LogisticRegression
logistic_regression=LogisticRegression()
logistic_regression.fit(x_train,y_train)
y_pred=logistic_regression.predict(x_test)
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
accuracy=accuracy_score(y_test,y_pred)
print(accuracy*100,"%")
lr=LogisticRegression(multi_class='auto',max_iter=1000)
param_grid = {
    'C':[0.001,0.01,0.1,1,10,100],
    'penalty':['l1','l2'],
    'solver':['lbfgs','liblinear','saga']
}
from sklearn.model_selection import GridSearchCV
grid_search = GridSearchCV(lr,param_grid,cv=5,verbose=1)
grid_search.fit(x_train,y_train)
best_params = grid_search.best_params_
best_params
best_logistic_regression = LogisticRegression(
    multi_class='auto',
    max_iter = 1000,
    C=best_params['C'],
    penalty=best_params['penalty'],
    solver=best_params['solver']
)
best_logistic_regression.fit(x_train,y_train)
y_pred = best_logistic_regression.predict(x_test)
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

accuracy = accuracy_score(y_test,y_pred)
print(accuracy*100,"%")
------------------------------------------------------------------------------------------------------------------------------------
**Lab_sheet-7**

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from pandas import read_csv

df=read_csv("/content/PIMA_diabetes.csv")

x=np.array(df.drop(["Outcome"],1))
y=np.array(df["Outcome"])

df.head()

print(np.shape(x))
print(np.shape(y))

scaler=StandardScaler()
x_scaled=scaler.fit_transform(x)

x_scaled

n_components=2
pca=PCA(n_components=n_components)
x_pca=pca.fit_transform(x_scaled)

np.shape(y)

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn import tree
model=tree.DecisionTreeClassifier()

model=tree.DecisionTreeClassifier(criterion="entropy",splitter="random",min_samples_split=4)

x_train,x_test,y_train,y_test=train_test_split(x_pca,y,test_size=0.4,random_state=100)

model=model.fit(x_train,y_train)

y_pred=model.predict(x_test)
print("accuracy:",accuracy_score(y_test,y_pred)*100)
------------------------------------------------------------------------------------------------------------------------------------
**Labsheet-8**

from google.colab import drive
drive.mount('/content/drive/')

import cv2
import numpy as np
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input,decode_predictions
from tensorflow.keras.preprocessing import image

model=ResNet50(weights='imagenet')

img_path='/content/drive/MyDrive/Ml/1.jpeg'
img=image.load_img(img_path,target_size=(224,224))
img_array=image.img_to_array(img)
img_array=np.expand_dims(img_array,axis=0)
img_array=preprocess_input(img_array)
predictions=model.predict(img_array)

decoded_predictions=decode_predictions(predictions)

for i,(imagenet_id,label,score) in enumerate(decoded_predictions[0]):
  print(f"{i+1}:{label}({score:.2f})")

img=cv2.imread(img_path)
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

for _,label,score in decoded_predictions[0]:
  if score>0.5:
    print(f"Object:{label},Score:{score}")
    cv2.putText(img,f"{label}:{score:.2f}",(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2,cv2.LINE_AA)

import matplotlib.pyplot as plt
plt.imshow(img)
plt.axis('off')
plt.show()
------------------------------------------------------------------------------------------------------------------------------------
**Labsheet-9**
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt

(train_images,train_labels),(test_images,test_labels)=mnist.load_data()

train_images,test_images=train_images/255.0,test_images/255.0

model=keras.Sequential([layers.Flatten(input_shape=(28,28)),
                        layers.Dense(128,activation='relu'),
                        layers.Dropout(0.2),
                        layers.Dense(10,activation='softmax')])

model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

model.fit(train_images,train_labels,epochs=20)

test_loss,test_acc=model.evaluate(test_images,test_labels)
print(f"Test accuracy:{test_acc}")

predictions=model.predict(test_images)

n=10
plt.figure(figsize=(15,3))
for i in range(n):
  plt.subplot(1,n,i+1)
  plt.imshow(test_images[i],cmap='gray')
  plt.title(f'Pred:{tf.argmax(predictions[i])},True:{test_labels[i]}')
plt.show()

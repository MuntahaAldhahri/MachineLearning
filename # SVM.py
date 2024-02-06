# SVM

#-------------------------------------------------------------
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#-------------------------------------------------------------
# Importing the dataset
dataset = pd.read_csv('customer_data.csv')

# Dependent & Independent:
# Independent varible(Features) = Demographic information "spending, purchase frequency"
X = dataset[['purchase_frequency','age']].values
# Dependent varible(Target) = loyal customer.
y = dataset['loyalty'].values

#-------------------------------------------------------------
# Data cleaning 
# replace any missing value in spending with median of spending
median_spending = np.median(y)
y = (y > median_spending).astype(int)

#-------------------------------------------------------------
# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)


#-------------------------------------------------------------
# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#-------------------------------------------------------------
#-------------------------------------------------------------
# Training the SVM model on the training set
from sklearn.svm import SVC
classifier = SVC(kernel='rbf', random_state=42)
classifier.fit(X_train, y_train)

#-------------------------------------------------------------
# Predicting the Test set results
y_pred = classifier.predict(X_test)

#-------------------------------------------------------------
# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print("\n ********** SVM **********")
print(f"Classification matrix: \n{cm} \n")

Ac= classifier.score(X_test, y_test)
print(f"Accuracy: {Ac} \n")

#-------------------------------------------------------------
# Visualising sets
# Visualising the Training set results
from matplotlib.colors import ListedColormap
X_set, y_set = X_train, y_train
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('SVM (Training set)')
plt.xlabel('purchase_frequency')
plt.ylabel('loyalty')
plt.legend()
plt.show()


# Visualising the Test set results
from matplotlib.colors import ListedColormap
X_set, y_set = X_test, y_test
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('SVM (Testing set)')
plt.xlabel('purchase_frequency')
plt.ylabel('loyalty')
plt.legend()
plt.show()
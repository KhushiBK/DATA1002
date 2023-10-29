import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.model_selection import train_test_split

df = pd.read_csv('Integrated datasets - edit.csv')
X = df[["Time asleep (seconds)"]]      # slice dataFrame to extract input variables
y = df["Sleep Quality"]        # slice dataFrame to extract target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = LogisticRegression(solver='liblinear').fit(X_train, y_train)

y_pred = clf.predict(X_test)
y_pred_proba = clf.predict_proba(X_test)

print('----- Sample case -----')
last_sample = X_test.loc[list(X_test.index)[-1]]
print("Time asleep:", last_sample)
last_sample_proba = y_pred_proba[-1]
print('Probability of class 1:', last_sample_proba[0])
print('Predicted class:',y_pred[-1])
print('Actual class:', y_test.loc[list(y_test.index)[-1]])
print('-----------------------')

print('Calculate the accuracy using the test data')
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

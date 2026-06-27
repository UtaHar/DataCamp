# All required libraries are imported here for you.
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

# Load the dataset
crops = pd.read_csv("soil_measures.csv")

# Write your code here
# Exploratory analysis
print(crops.head())
print(crops.info())
print(crops.describe().T)
crops['crop'].value_counts(normalize=True)

# split dataset, train model, predict test set, evaluate model performance
X = crops.drop('crop', axis=1).values
y = crops['crop'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
feature_dict = {}
for i in [0, 1, 2, 3]:
    feature = ['N','P','K','ph'][i]
    logreg = LogisticRegression(multi_class = 'multinomial')
    # The subsetting with brackets didn't work. 
    # The reshape command transforms a list to a list of single element lists,
    # thus a 2D array. 
    logreg.fit(X_train[0:len(X_train), i].reshape(-1, 1), y_train)
    y_pred = logreg.predict(X_test[0:len(X_test), i].reshape(-1, 1))
    feature_performance = metrics.f1_score(y_test, y_pred, average = "weighted")
    feature_dict[feature] = feature_performance
print(f'F1-score for {feature_dict}')

# Picking the best predictive feature score.
best_key = ""
best_value = 0
for key in feature_dict:
    value = feature_dict[key]
    if value > best_value:
        best_value = value
        best_key = key
best_predictive_feature = {best_key: best_value}
print(best_predictive_feature)
print('Potassium is the best feature to evaluate, which crops to pick.')

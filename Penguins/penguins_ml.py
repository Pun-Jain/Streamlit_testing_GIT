import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle
# Create a dataframe
penguin_df=pd.read_csv('penguins.csv')
# Drop all the null values
penguin_df.dropna(inplace=True)
# Seperate Features and the output
output=penguin_df['species']
features=penguin_df[['island','bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g','sex']]
# Convert all the categorical variables to Dummy Columns
features=pd.get_dummies(features)
# Factorize the output values from text to numbers 
print(features.head())
# output,uniques=pd.factorize(output)
# # create a test train split
# x_train, x_test, y_train, y_test = train_test_split(features, output,test_size=0.8)
# # name and chose the model that you want to use
# rfc=RandomForestClassifier(random_state=15)
# # Train the model on the training data
# rfc.fit(x_train.values,y_train)
# # Calculate the predicted values through the model on the test data
# y_pred=rfc.predict(x_test.values)
# # calculate the accuracy score of your predicted values by comparing them with the test values
# score=accuracy_score(y_pred,y_test)
# print(f'Our accuracy score for this model is {score}')
# rf_pickle=open('rf_penguin.pickle','wb')
# pickle.dump(rfc,rf_pickle)
# rf_pickle.close()
# output_pickle=open('output_penguin.pickle','wb')
# pickle.dump(uniques,output_pickle)
# output_pickle.close()





# print('Here are our output variables')
# print(output.head())
# print('Here are our features')
# print(features.head())

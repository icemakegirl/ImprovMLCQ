import pandas as pd
from joblib import load

# Load the data
data = pd.read_csv('out.csv')

# model name
model_name = 'model_featureenvy2.pkl'  # Replace with the desired model name

# Select features based on the model
if model_name == 'model_longmethod2.pkl':
    features = data[['type','ck_method_uniquewordsqty','ck_method_assignmentsqty','watching','background','loc','commits','ck_class_numbersqty','smell_designite_num_aglomeration','number_of_contributors','longmethod_label']]
elif model_name == 'model_featureenvy2.pkl':
    features = data[['type','ck_method_parametersqty','smell_designite_num_aglomeration','ck_class_fanin','ck_method_assignmentsqty','watching','background','loc','commits','number_of_contributors','featureenvy_label']]
elif model_name == 'model_dataclass2.pkl':
    features = data[['stars','number_of_contributors','type','smell_pmd','ck_method_stringliteralsqty','smell_pmd_dataclass','smell_designite_num_aglomeration','background','loc','commits','dataclass_label']]
elif model_name == 'model_blob3.pkl':
    features = data[[['type','smell_pmd','smell_pmd_blob','smell_designite_num_aglomeration','background','ck_method_uniquewordsqty','ck_method_loc','loc','commits','stars','blob_label']]
else:
    print('replace the desired model name')



# Load the data
model = load(model_name)

# Make predictions
predictions = model.predict(features)

# Save the results
output = pd.DataFrame({'Type Name': data['Type Name'], 'Prediction': predictions})
output.to_csv('prediction_results.csv', index=False)

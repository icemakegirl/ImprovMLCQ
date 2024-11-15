import pandas as pd
from joblib import load

# Load the data
data = pd.read_csv('out.csv')

# model name
model_name = 'model_featureenvy2.pkl'  # Replace with the desired model name

# Select features based on the model
if model_name == 'model_longmethod2.pkl':
    features = data[['ck_method_stringliteralsqty','ck_method_uniquewordsqty','smell_designite_longmethod','ck_method_parametersqty','ck_class_lcom','loc','commits','ck_method_cbo','smell_designite_num_aglomeration','ck_method_fanin','longmethod_label']]
elif model_name == 'model_featureenvy2.pkl':
    features = data[['stars','ck_method_parametersqty','smell_designite_num_aglomeration','ck_method_returnsqty','smell_pmd_num_aglomeration','ck_method_cbo','ck_class_lcom','loc','commits','number_of_contributors','featureenvy_label']]
elif model_name == 'model_dataclass2.pkl':
    features = data[['ck_method_returnsqty','number_of_contributors','ck_class_lcom','ck_method_fanout','ck_method_parametersqty','ck_method_fanin','smell_designite_num_aglomeration','watching','loc','commits','dataclass_label']]
elif model_name == 'model_blob3.pkl':
    features = data[[['ck_method_returnsqty','ck_method_cbo','smell_pmd_blob','smell_designite_num_aglomeration','smell_pmd_num_aglomeration','ck_method_uniquewordsqty','number_of_contributors','loc','commits','stars','blob_label']]
else:
    print('replace the desired model name')



# Load the data
model = load(model_name)

# Make predictions
predictions = model.predict(features)

# Save the results
output = pd.DataFrame({'type': data['type'], 'Prediction': predictions})
output.to_csv('prediction_results.csv', index=False)

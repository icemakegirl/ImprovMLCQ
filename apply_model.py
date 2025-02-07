import pandas as pd
from joblib import load

# Load the data
data = pd.read_csv('out_clean.csv')

# model name
model_name = 'models_multilabel_FS2.pkl'  # Replace with the desired model name

# Select features based on the model
features = data[['longmethod_label', 'featureenvy_label','ck_method_cbo','ck_class_cbo','ck_class_fanin']]



# Load the data
model = load(model_name)

# Make predictions
predictions = model.predict(features)

# Save the results
output = pd.DataFrame({'type': data['type'], 'Prediction': predictions})
output.to_csv('prediction_results.csv', index=False)

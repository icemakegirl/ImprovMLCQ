from sklearn.preprocessing import LabelEncoder
import pandas as pd

# Load File
df = pd.read_csv('out.csv')

# Label Encoding
label_encoder = LabelEncoder()

df['ck_method_constructor']= label_encoder.fit_transform(df['ck_method_constructor'])
df['ck_method_hasjavadoc']= label_encoder.fit_transform(df['ck_method_hasjavadoc'])
df['type']= label_encoder.fit_transform(df['type'])
df['smell_organic']= label_encoder.fit_transform(df['smell_organic'])
df['smell_pmd']= label_encoder.fit_transform(df['smell_pmd'])
f['background']= label_encoder.fit_transform(df['background'])

df.to_csv('out.csv', index=False)
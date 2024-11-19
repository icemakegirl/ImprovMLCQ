# ImproveMLCQ

### Tools

We use three tools do classify code smells: PMD, Organic, Designate.
Before using these tools, the user must copy all the project's .java to a single root folder. This folder will be used by the tools to label the code smells.
The tools were used to extend the MLCQ with metrics and code smells labeling .ck .
To run the tools we need to download all the projects that are in our ImproveMLCQ dataset locally.
The path_with_the_files is the path of the projects that were downloaded to run the tools.

#### PMD
WEBSITE: [https://pmd.github.io/](https://pmd.github.io/)

To use the PMD tool, the user must download it from the website and perform the following steps:

1. Extract the file to, for example, C:\pmd-bin-7.0.0-rc4
2. Run the command line:"<path_to_pmd.bat_bin_folder_in_root_pmd_folder> check -d <path_with_the_files> -R rulesets/java/design.xml -f csv -r <path_to_csv_file/report.csv>"

After executing the command line, the "report.csv" file is created. It contains the data for extracting the following features: smell_pmd_num_agglomeration and smell_pmd_longmethod.
### Organic
WEBSITE: [https://github.com/opus-research/organic](https://github.com/opus-research/ancient-organic)

To use the Organic tool and obtain the data, the user must access the OPUS repository through the link and download the .jar file and perform the following steps:

1. Run the command line:"java -jar <path_to_organic-v0.1.2.jar> -src <path_with_the_files> -sf output.json"

After executing the command line, the "output.json" file is created. It contains the data for extracting the following features: smell_organic_featureenvy and smell_organic_longmethod.

#### Designite
WEBSITE: https://www.designite-tools.com/

The Designate tool has several versions, the one needed to obtain the data is DesignateJava and can be obtained at website.
To use Designite we require a student license because Designite is a paid tool.

With DesignateJava.jar, run the following command:

1. Run the command line:"java -jar <path_to_the_DesigniteJava.jar> -i <path_with_the_files> -o <path_out_with_the_smells>"

After executing the command line, Designate generates several outputs, but for model training, only the following were used: ImplementationSmells.csv and DesignSmells.csv.

Through these two csvs, we will obtain data to extract the following features: smell_designite_longmethod, smell_designite_num_agglomeration and smell_designite_agglomeration.

### Data
link out.csv and out_with_labelEncoding: https://zenodo.org/records/12602468

The out.csv file is the extension we make of MLCQ by adding the tool analysis, and this file is used within "apply_model.py" to use the models
We create data dictionaries that contain all the features: FS1, FS2, FS3 and the definition of each of these features.
Also contains the files of the top 10 features used for FS3 for each code smell.
To access these files, go to the Features folder.

The label encoding technique was used to transform the columns: which came in text formats into numeric data.
You can run the code below and modify the out.csv to apply this label encoding technique or download the out_with_labelEncoding.csv file that already comes with this labeling assigned

```
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
```
### Research Questions

To answer the research questions, we used the notebooks available in the repository.
For RQ1 we used the notebook: colab notebooks/RQ_1.ipynb
For RQ2 we used the notebook: colab notebooks/RQ_2.ipynb
For RQ3 we create 3 notebooks, each of these 3 for 1 feature selection: colab notebooks/RQ_3_fs1.ipynb, colab notebooks/RQ_3_fs2.ipynb and colab notebooks/RQ_3_fs3.ipynb.

### Using the model

To use the model, open the code "apply_model.py" and edit the model name for which model you will use (model_featureenvy2.pkl, model_longmethod2.pkl, model_dataclass2.pkl or model_blob2.pkl). Run the code.
The number 2 in the nomenclature represents the models that we extracted when we ran FS2, we are using them because they were the ones that had the best results in the experiments


```Python
model_name = 'model_featureenvy2.pkl' 
```

The model is loaded and makes predictions, generating a "prediction_results.csv" file with the prediction of whether or not it has the model's code smell for each java file.

## Comments

If you have difficulty running any of the codes, use the notebooks available in the colab notebooks folder.
In notebooks there will be 3 lines to install the main libraries that will be used to train the model: pycaret, dataframe-image and optuna.
The lines below this until before the settings of the first smell long method are responsible for loading and checking the file and excluding features that are not necessary for the feature selection.
It is necessary to run this part from importing the libraries to filtering the columns when running the code for each smell

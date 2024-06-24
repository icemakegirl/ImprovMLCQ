# ImproveMLCQ
# ML Model for Code Smell Long Method, Feature Envy, DataClass and Blob Detection in Open-Source Projects on GitHub

### Ferramentas

Before using the tools, the user must copy all .java files to a single folder.

#### PMD

To use the PMD tool and obtain the data, the user must download it from the website https://pmd.github.io/ and then perform the following steps:

1. Extract the file to, for example, C:\pmd-bin-7.0.0-rc4
2. Run the command line:
3. "<path_to_pmd.bat_bin_folder_in_root_pmd_folder> check -d <path_to_the_folder_with_codes> -R rulesets/java/design.xml -f csv -r <path_to_csv_file/report.csv>"

After executing the command line, the "report.csv" file is created. It contains the data for extracting the following features: smell_PMD_num_agglomeration and smell_PMD_longmethod.
### Organic

To use the Organic tool and obtain the data, the user must access the OPUS repository through the link https://github.com/opus-research/organic and download the .jar file.

To run the tool, you must execute the following command:

– "java -jar <path_to_organic-v0.1.2.jar> -src <PATH_PROS_CODE_FILES> -sf output.json"

The "output.json" file is created. It contains the data for extracting the following features: smell_organic_featureenvy and smell_organic_longmethod.

#### Designate

The Designate tool has several versions, the one needed to obtain the data is DesignateJava and can be obtained at https://www.designite-tools.com/.

With DesignateJava.jar, run the following command:

– "java -jar <path_to_the_DesigniteJava.jar> -i <path_with_the_files> -o <path_out_with_the_smells>"

Designate generates several outputs, but for model training, only the following were used: ImplementationSmells.csv and DesignSmells.csv.

Through these two csvs, we will obtain data to extract the following features: smell_Designite_longmethod, smell_Designite_num_agglomeration and smell_Designite_agglomeration.

### Data

The out.csv file contains the tool analyzes along with the MLCQ dataset, and this file is used within "apply_model.py" to use the models

### Using the model

To use the model, open the code "apply_model.py" and edit the model name for which model you will use (model_featureenvy3.pkl, model_longmethod3.pkl, model_dataclass3.pkl or model_blob3.pkl). Run the code.

```Python
model_name = 'model_featureenvy3.pkl' # Replace with the desired model name
```

The model is loaded and makes predictions, generating a "prediction_results.csv" file with the prediction of whether or not it has the model's code smell for each java file.

## Comments

If you have difficulty running any of the codes, use Google Colab.

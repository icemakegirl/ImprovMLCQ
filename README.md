# ImproveMLCQ

### Tools
Code-smell metric-based tools 
We use three tools do classify code smells: PMD, Organic, Designate.
Before using these tools, the user must copy all .java files from a project to a single folder.

#### PMD
website: https://pmd.github.io/
To use the PMD tool, the user must download it from the website and perform the following steps:

1. Extract the file to, for example, C:\pmd-bin-7.0.0-rc4
2. Run the command line:"<path_to_pmd.bat_bin_folder_in_root_pmd_folder> check -d <path_to_the_folder_with_codes> -R rulesets/java/design.xml -f csv -r <path_to_csv_file/report.csv>"

After executing the command line, the "report.csv" file is created. It contains the data for extracting the following features: smell_pmd_num_agglomeration and smell_pmd_longmethod.
### Organic
OPUS repository: https://github.com/opus-research/organic
To use the Organic tool and obtain the data, the user must access the OPUS repository through the link and download the .jar file and perform the following steps:

1. Run the command line:"java -jar <path_to_organic-v0.1.2.jar> -src <PATH_PROS_CODE_FILES> -sf output.json"

After executing the command line, the "output.json" file is created. It contains the data for extracting the following features: smell_organic_featureenvy and smell_organic_longmethod.

#### Designate
website: https://www.designite-tools.com/
The Designate tool has several versions, the one needed to obtain the data is DesignateJava and can be obtained at website.

With DesignateJava.jar, run the following command:

1. Run the command line:"java -jar <path_to_the_DesigniteJava.jar> -i <path_with_the_files> -o <path_out_with_the_smells>"

After executing the command line, Designate generates several outputs, but for model training, only the following were used: ImplementationSmells.csv and DesignSmells.csv.

Through these two csvs, we will obtain data to extract the following features: smell_designite_longmethod, smell_designite_num_agglomeration and smell_designite_agglomeration.

### Data

The out.csv file is the extension we make of MLCQ by adding the tool analysis, and this file is used within "apply_model.py" to use the models
We create data dictionaries that contain all the features: FS1, FS2, FS3 and the definition of each of these features.
Also contains the files of the top 10 features used for FS3 for each code smell.
To access these files, go to the Features folder

### Using the model

To use the model, open the code "apply_model.py" and edit the model name for which model you will use (model_featureenvy2.pkl, model_longmethod2.pkl, model_dataclass2.pkl or model_blob2.pkl). Run the code.
The number 2 in the nomenclature represents the models that we extracted when we ran FS2, we are using them because they were the ones that had the best results in the experiments


```Python
model_name = 'model_featureenvy2.pkl' 
```

The model is loaded and makes predictions, generating a "prediction_results.csv" file with the prediction of whether or not it has the model's code smell for each java file.

## Comments

If you have difficulty running any of the codes, use the notebooks available in the colab notebooks folder.

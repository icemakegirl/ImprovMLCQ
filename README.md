# ImprovMLCQ
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.16748784.svg)](https://doi.org/10.5281/zenodo.16748784)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Abstract
This repository contains the implementation and datasets for "ImprovMLCQ: Improving Machine Learning Code Quality Detection through Enhanced Feature Selection and Multi-label Classification". The project extends the MLCQ dataset with code smell detection using PMD, Organic, and Designite tools, implementing both Machine Learning and Deep Learning approaches for multi-label code smell classification.

Access full paper [here](SBCARS_2025___ImprovMLCQ.pdf)

## Repository Structure

```
ImprovMLCQ/
├── README.md                           # Main documentation
├── LICENSE                             # MIT License
├── SBCARS_2025___ImprovMLCQ.pdf       # Research paper
├── apply_model.py                      # Script to use trained models
├── label_encoder.py                    # Label encoding utilities
├── resource_skills.txt                 # Resource requirements guide
├── colab notebooks/                    # Jupyter notebooks for experiments
│   ├── RQ_1.ipynb                     # Research Question 1 analysis
│   ├── RQ_2.ipynb                     # Research Question 2 analysis
│   ├── EDA_Improv.ipynb               # Exploratory Data Analysis
│   ├── DeepLearningMultilabel_FS1.ipynb    # Deep Learning with Feature Selection 1
│   ├── DeepLearningMultilabel_FS2.ipynb    # Deep Learning with Feature Selection 2
│   ├── DeepLearningMultilabel_FS3.ipynb    # Deep Learning with Feature Selection 3
│   ├── MachineLearningMultilabelRQ_3_fs1_out_clean.ipynb  # ML with FS1
│   ├── MachineLearningMultilabelRQ_3_fs2_out_clean.ipynb  # ML with FS2
│   └── MachineLearningMultilabelRQ_3_fs3_out_clean.ipynb  # ML with FS3
└── results/                           # Experimental results
    ├── DeepLearning All Smells.csv    # Deep Learning results summary
    ├── smell_classification_report_FS1_Multilabel.xlsx  # FS1 results
    ├── smell_classification_report_FS2_Multilabel.xlsx  # FS2 results
    └── smell_classification_report_FS3_Multilabel.xlsx  # FS3 results
```

### External Dependencies (Download Required)
```
External Data (Zenodo):
├── out.csv                            # Original extended MLCQ dataset
├── out_with_labelEncoding.csv         # Label encoded dataset
├── out_clean.csv                      # Cleaned dataset (recommended)
└── Features/                          # Feature definitions and rankings
    ├── features_all_features.csv      # Complete feature dictionary
    └── top5_features_code_smells.csv  # Top 5 features per smell
```

### Generated Outputs (After Execution)
```
Generated Files:
├── models_multilabel_FS1.pkl         # Trained ML models (FS1)
├── models_multilabel_FS2.pkl         # Trained ML models (FS2)
├── models_multilabel_FS3.pkl         # Trained ML models (FS3)
└── prediction_results.csv            # Model predictions
```

**Key Directories:**
- **`colab notebooks/`**: All Jupyter notebooks for reproducing experiments
- **`results/`**: Pre-computed experimental results and reports
- **Root files**: Main scripts, documentation, and paper

**External Data**: Must be downloaded from [Zenodo](https://zenodo.org/records/14834187) before running experiments.

## Creating the ImprovMLCQ Dataset

**For Advanced Users Only** - This section describes how to recreate the dataset from scratch. **Most users should skip this section** and proceed directly to [Reproducing Results](#reproducing-results).

### Tools Required

We use three tools to classify code smells: PMD, Organic, Designite.
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
#### Organic
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
link out.csv and out_with_labelEncoding: [Link Zenodo](https://zenodo.org/records/14834187)
The out.csv file is the extension we make of MLCQ by adding the tool analysis, and this file is used within "apply_model.py" to use the models
We create data dictionaries that contain all the features: FS1, FS2, FS3 and the definition of each of these features.
Also contains the files of the top 10 features used for FS3 for each code smell.
To access these files, go to the Features folder.

**For Basic Reproduction**: Use the pre-processed `out_clean.csv` file (recommended).

**For Advanced Users Only**: The label encoding technique was used to transform the columns which came in text formats into numeric data. You can run the code below and modify the out.csv to apply this label encoding technique, or download the out_with_labelEncoding.csv file that already comes with this labeling assigned

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
df['background']= label_encoder.fit_transform(df['background'])

df.to_csv('out.csv', index=False)
```

we clean the dataset and call it out_clean.csv. 
The data preprocessing phase started with the removal of columns containing more than 50% values. 
A review of missing records was conducted, and all empty fields were imputed with a value of 0.
Duplicate rows were removed
We run the Machine Learning and Deep Learning algorithms using out_clean.csv. This file can also be found at: [Link Zenodo](https://zenodo.org/records/14834187)
You can dowload this code label enconder 
### Features
Inside the feature folder is the .csv file features - all_features.csv and a file called top5 features code smells. On the y-axis are the names of the most relevant features, in order of importance from top to bottom. The x-axis indicates the weight of each feature for each smell.

### Packages
scikit-learn, numpy, optuna, pycaret, os, ydata_profiling and os

### Dataset Cleaning
Before running the models, it is necessary to clean and standardize the data. Execute the file **"EDA_Improv.ipynb"**, and among its results, you should use the file **"out_clean.csv"** for model execution.
## Reproducing Results

### Prerequisites
1. Download the dataset files from [Zenodo](https://zenodo.org/records/14834187):
   - `out.csv`
   - `out_with_labelEncoding.csv` 
   - `out_clean.csv`
2. Have a Google account to access Google Colab
3. Upload files to a folder in colab

### Step-by-Step Guide

#### 1. Initial Setup (Required for ALL notebooks)
1. **Open the notebook** in Google Colab
2. **Change the notebooks** path to where you stored the datasets out and out_clean
3. **If you upload the file to Colab**, ignore the first line about importing the dataset from a path dnd when reading the dataset, remove the content from: df = pd.read_csv('/out_clean.csv', index_col=0)
   - Click on the folder icon in the left sidebar
   - Upload `out_clean.csv` (recommended for model execution)
   - Or upload `out.csv` if you want to apply label encoding

4. **Install required libraries**:
   - For **Machine Learning notebooks** only, run these lines at the beginning:
   ```python
   !pip install pycaret
   !pip install dataframe-image
   !pip install optuna
   ```
   - For **Deep Learning notebooks**, no additional library installation is required
5. **Run the initial setup section** - this includes:
   - Importing all necessary libraries
   - Loading and checking the dataset file
   - Excluding features that are not necessary for feature selection
   - **Important**: Always run this section completely before proceeding to smell-specific analysis

#### 2. Notebook Descriptions

**Data Preparation:**
- **`EDA_Improv.ipynb`**: Exploratory Data Analysis and dataset cleaning. Generates the `out_clean.csv` file used by all other notebooks. Includes data profiling, missing value analysis, and preprocessing steps.

**Research Questions:**

**RQ1 - Statistical Analysis:**
- **`RQ_1.ipynb`**: Analyzes code smell distribution across the dataset. Provides descriptive statistics, correlation analysis, and visualization of code smell patterns in Java projects.

**RQ2 - Feature Selection Comparison:**
- **`RQ_2.ipynb`**: Compares different feature selection methods (FS1, FS2, FS3). Evaluates the effectiveness of each approach and identifies the most relevant features for code smell detection.

**RQ3 - Model Training and Evaluation (6 notebooks):**

*Deep Learning Approaches:*
- **`DeepLearningMultilabel_FS1.ipynb`**: Neural network training using all features (FS1). Implements multi-label classification with deep learning models.
- **`DeepLearningMultilabel_FS2.ipynb`**: Neural network training using statistically selected features (FS2). Optimized feature set for better performance.
- **`DeepLearningMultilabel_FS3.ipynb`**: Neural network training using top-ranked features (FS3). Uses the most important features identified through feature importance analysis.

*Machine Learning Approaches:*
- **`MachineLearningMultilabelRQ_3_fs1_out_clean.ipynb`**: Traditional ML algorithms (Random Forest, SVM, XGBoost) using all features (FS1). Includes hyperparameter tuning with Optuna.
- **`MachineLearningMultilabelRQ_3_fs2_out_clean.ipynb`**: Traditional ML algorithms using statistically selected features (FS2). Compares performance across different algorithms.
- **`MachineLearningMultilabelRQ_3_fs3_out_clean.ipynb`**: Traditional ML algorithms using top-ranked features (FS3). Focuses on the most predictive features for optimal performance.


## Reproducibility

All experiments can be fully reproduced using the provided Jupyter notebooks:

- **RQ1**: Statistical analysis of code smell distribution
- **RQ2**: Comparative analysis of feature selection methods
- **RQ3**: Machine Learning and Deep Learning model training and evaluation

### Expected Results:
- Trained models saved as `.pkl` files
- Performance metrics and comparison tables
- Feature importance rankings
- Visualization plots and confusion matrices

### Using the model

To use the model, open the code "apply_model.py" and edit the model name for which model you will use (models_multilabel_FS2.pkl and models_multilabel_FS3.pkl). Run the code.
The number 2 in the nomenclature represents the models that we extracted when we ran FS2, we are using them because they were the ones that had the best results in the experiments


```Python
model_name = 'models_multilabel_FS2.pkl' 
```

The model is loaded and makes predictions, generating a "prediction_results.csv" file with the prediction of whether or not it has the model's code smell for each java file.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



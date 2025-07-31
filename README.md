# Healthcare Disease Prediction Project

## Overview
The Healthcare Disease Prediction project aims to develop machine learning models for predicting various diseases based on patient data. This project utilizes several datasets to train and evaluate models, providing insights into healthcare analytics.

## Note: for details on the model comparison please refer to reports/ and healthcare-disease-prediction/notebooks/04_evaluation.ipynb

## Project Structure
- **data/**: Contains all datasets used in the project.
  - **raw/**: Original datasets used for the project.
  - **processed/**: Cleaned and preprocessed datasets ready for analysis.
  - **external/**: External data sources that complement the primary datasets.
  
- **notebooks/**: Jupyter notebooks for different stages of the project.
  - **01_eda.ipynb**: Exploratory Data Analysis.
  - **02_preprocessing.ipynb**: Data preprocessing steps.
  - **03_modeling.ipynb**: Building and training machine learning models.
  - **04_evaluation.ipynb**: Evaluating model performance.

- **src/**: Source code for the project.
  - **data/**: Scripts for loading and preprocessing data.
  - **features/**: Scripts for feature engineering and selection.
  - **models/**: Implementations of machine learning models and training routines.
  - **visualization/**: Utility scripts for creating visualizations and plots.

- **models/**: Directory for saving trained machine learning models.

- **reports/**: Generated analysis reports, including findings and visualizations.

- **requirements.txt**: Lists the dependencies required for the project.

- **README.md**: Documentation for the project.

- **.gitignore**: Specifies files and directories to be ignored by version control.


## Usage Guidelines
- Use the Jupyter notebooks in the `notebooks/` directory to explore the data, preprocess it, build models, and evaluate their performance.
- The source code in the `src/` directory can be modified for custom data processing and model training routines.
- Save trained models in the `models/` directory for future use.

## Model Performance & Medical Interpretation

Four machine learning models were evaluated for diabetes prediction using patient data. The table below summarizes their performance across key metrics:

| Model         | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|---------------|----------|-----------|--------|----------|---------|
| RandomForest  | 0.95     | 0.95      | 0.91   | 0.93     | 0.98    |
| DecisionTree  | 0.88     | 0.82      | 0.85   | 0.83     | 0.87    |
| KNN           | 0.79     | 0.75      | 0.62   | 0.68     | 0.87    |
| SVM           | 0.81     | 0.79      | 0.64   | 0.70     | 0.89    |

RandomForest stands out as the most effective model, achieving the highest scores in both recall and ROC-AUC. In a healthcare context, recall is especially important because it reflects the model’s ability to correctly identify patients with diabetes. Missing a diagnosis can have serious consequences, so models with higher recall are preferred for clinical screening.

DecisionTree offers interpretability, which is valuable for understanding how predictions are made, but its overall performance is lower than RandomForest. KNN and SVM show reduced recall, indicating a higher risk of missed diagnoses. These models may be less suitable for deployment in a clinical setting where sensitivity is critical.

Selecting a model for healthcare applications involves more than just accuracy; it requires careful consideration of how the model balances false positives and false negatives. Based on these results, RandomForest is recommended for initial diabetes screening, with further validation and monitoring to ensure patient safety and regulatory compliance.

**Ethical Note:**  
Models with low recall risk missing patients who need care. We recommend RandomForest for initial screening, with further clinical validation.

## Reports & Visualizations

All key findings and visualizations are available in the `reports/` directory:

- **Model Comparison:** See `model_comparison.png` for a visual summary of all models.
- **Feature Importance:** `feature_importance.png` and `shap_summary.png` highlight which patient features most influence predictions.
- **Patient-Level Explanations:** SHAP force plots (viewable in the notebook) show how individual predictions are made.

## Ethical & Clinical Considerations

This project prioritizes sensitivity (recall) to minimize missed diagnoses, and uses interpretable models and explanations to support clinical trust. All results should be validated with domain experts before deployment.


## Next Steps

The next phase will focus on deploying the best-performing model as an API or web application for real-world use.

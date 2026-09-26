# 🏥 Medical Insurance Cost Prediction

A Machine Learning project that predicts an individual's estimated medical insurance cost based on demographic and health-related factors.

## 📌 Project Overview

The goal of this project is to develop a machine learning model that estimates medical insurance charges using features such as age, BMI, number of children, smoking status, gender, and region.

The project follows a complete Machine Learning workflow — from dataset exploration and preprocessing to model training, evaluation, and deployment.

## 🎯 Problem Statement

Medical insurance costs can vary depending on several factors such as age, BMI, smoking status, number of children, gender, and geographical region.

This project uses Multiple Linear Regression to predict the estimated insurance cost for a given customer profile.

## 📊 Dataset

The project uses the **Medical Cost Personal Dataset** from Kaggle.

**Dataset:** https://www.kaggle.com/datasets/mirichoi0218/insurance

The dataset contains 1,338 records and 7 original columns:

- `age`
- `sex`
- `bmi`
- `children`
- `smoker`
- `region`
- `charges`

## 🧹 Data Preprocessing

The following preprocessing steps were performed:

- Checked for missing values
- Identified duplicate records
- Removed duplicate records
- Identified categorical variables
- Applied One-Hot Encoding to categorical variables
- Prepared the final dataset for machine learning

**Categorical variables:**
- `sex`
- `smoker`
- `region`

After preprocessing, the model used 8 input features.

## 📈 Exploratory Data Analysis

Several visualizations were created to understand relationships between insurance charges and important variables:

- Age vs. Medical Insurance Charges
- BMI vs. Medical Insurance Charges
- Smoking Status vs. Medical Insurance Charges
- Correlation analysis

One key observation: smoking status showed a strong positive correlation with insurance charges in this dataset.

## 🤖 Machine Learning Model

**Algorithm:** Multiple Linear Regression

The dataset was split into:

- 80% Training Data
- 20% Testing Data

The model was trained using the training set and evaluated using the testing set.

## 📊 Model Evaluation

| Metric   | Result        |
|----------|--------------:|
| MAE      | 4,177.05      |
| MSE      | 35,478,020.68 |
| RMSE     | 5,956.34      |
| R² Score | 0.807         |

The model achieved an **R² score of approximately 0.807** on the test set.

## 💻 Prediction Application

A Streamlit web application was developed where users can enter:

- Age
- Gender
- BMI
- Number of Children
- Smoking Status
- Region

The application then predicts the estimated medical insurance cost.

## 🧪 Test Cases

| Test Case    | Age | Gender | BMI | Children | Smoker | Region    | Predicted Cost |
|--------------|----:|--------|----:|---------:|--------|-----------|----------------:|
| Test Case 1  | 30  | Female | 25  | 0        | No     | Northeast | $4,321.21       |
| Test Case 2  | 45  | Male   | 32  | 2        | Yes    | Southeast | $33,478.60      |

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit
- Google Colab
- GitHub

## 📁 Project Structure

```text
medical-insurance-cost-prediction/
│
├── app.py
├── train_model.py
├── insurance_model.pkl
├── insurance.csv
└── README.md
```

## ▶️ How to Run Locally


**1. Clone the repository**

```bash
git clone https://github.com/YOUR-USERNAME/medical-insurance-cost-prediction.git
```

**2. Move into the project directory**

```bash
cd medical-insurance-cost-prediction
```

**3. Install the required libraries**

```bash
pip install pandas numpy scikit-learn matplotlib seaborn streamlit joblib
```

**4. Run the application**

```bash
python -m streamlit run app.py
```

The application will open in your browser.

## ⚠️ Limitations

- The model is trained on a relatively small dataset.
- Predictions are estimates and should not be treated as actual insurance quotations.
- Linear Regression assumes a linear relationship between the input features and insurance charges.
- Additional features could potentially improve prediction performance.

## 👩‍💻 Author

**Mahnoor Hassan**
Software Engineering Student

# Heart Disease Prediction App

This repository contains a machine learning-powered web application for predicting heart disease risk based on user input data. The app is built with Python, Streamlit, and scikit-learn.

## Table of Contents

- [Overview](#overview)
- [Demo](#demo)
- [Features](#features)
- [Dataset](#dataset)
- [Model](#model)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Heart Disease Prediction App uses a trained machine learning model to estimate the likelihood of heart disease for a user, based on several health-related parameters. The app is easy to use and provides instant feedback.

## Demo

To run the app locally, execute:

```bash
streamlit run app.py
```

## Features

- Interactive web interface for user input.
- Predicts risk of heart disease instantly.
- Uses a machine learning model trained on real-world heart disease data.
- Provides clear feedback: "Heart Disease Detected" or "No Heart Disease Detected".

## Dataset

The model is trained on preprocessed heart disease datasets:

- `heart dataset.csv`: Original dataset with numeric/encoded values.
- `heart diseases data.csv`: Cleaned dataset with descriptive categorical values.

Both datasets include features such as age, chest pain type, heart pain, exercise pain, oldpeak, number of blood vessels, blood disorder, and target (presence/absence of heart disease).

## Model

The model is based on a scikit-learn pipeline (see `m_heart.ipynb` for training details). It includes preprocessing steps and a classifier (e.g., Decision Tree). The trained pipeline is serialized into `model.pkl`.

## Usage

1. Clone this repository.
2. Ensure Python 3.7+ is installed.
3. Install required dependencies (see below).
4. Run the app with Streamlit:

   ```bash
   streamlit run app.py
   ```

5. Enter your health information in the web interface and click "Predict" to get results.

## Dependencies

- Python 3.7+
- pandas
- numpy
- scikit-learn
- streamlit
- pickle

Install dependencies with:

```bash
pip install pandas numpy scikit-learn streamlit
```

## File Structure

```
- `README.md - Project documentation and introduction.`  
- `app.py - Main application script; runs the web or backend app.`  
- `heart dataset.csv - Dataset file containing heart-related data for analysis or model training.`  
- heart diseases data.csv - Another dataset file, possibly with different or additional heart disease data.  
- m_heart.ipynb - Jupyter Notebook; contains code, analysis, and visualizations for the heart disease project.  
- model.pkl - Serialized (pickled) machine learning model for heart disease prediction.  
- requirements.txt - List of Python dependencies needed to run the project.
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is open-source and available under the MIT License.

---

**Disclaimer:** This app is for educational purposes only and should not be used for real medical diagnosis.

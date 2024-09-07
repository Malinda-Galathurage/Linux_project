Titanic Survival Prediction Project

Project Overview

This project aims to predict the survival of passengers on the Titanic using machine learning models. 
Two algorithms were implemented: Logistic Regression by Malinda and Decision Tree Classifier by Vithya.


- Malinda
- Vithyashini


 Project Structure
- `data/`: Contains the input datasets and the output predictions.
- `code/`: Contains the scripts for data collection, preprocessing, model training, evaluation, and deployment.
- `models/`: Contains the saved models (e.g., malinda_model.pkl, vithya_model.pkl).
- `documentation/`: Contains project-related documentation, including this README.

Data Description

The dataset consists of various features, including:
- PassengerId: Unique ID of the passenger
- Pclass: Ticket class (1st, 2nd, or 3rd)
- Sex: Gender of the passenger
- Age: Age of the passenger
- Survived: Target variable (1 for survived, 0 for not)

 Modeling

Two machine learning models were implemented:
- Logistic Regression (Malinda): This model is a commonly used classifier for binary classification problems.
- Decision Tree (Vithya): This model is simple to interpret and can handle both numerical and categorical data.

After evaluating the models, we found the following:
- Logistic Regression achieved an accuracy of 0.81.
- Decision Tree achieved an accuracy of 0.94.

 Conclusion

Both models performed well, but the Decision tree model slightly outperformed the Logistic regression model.


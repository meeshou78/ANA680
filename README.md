# Assignment2
This dataset has approximately 683 patient data having 10 features and 1 class label describing whether the patient has cancer or not. Each row describes one patient, and the class column describes if the patient tumor is benign (label = 2) or malignant (label = 4). 
For this dataset, build all the classification models (using Python and Scikit-learn) given below (no need to visualize) and tabulate the accuracy and confusion matrix obtained for each. Split the dataset such that the test data size is 25% of the total dataset.
Make sure to code each classification model in a separate python file. Then, you can tabulate the accuracy and confusion matrix in a Word document table. Finally, submit all the python files and Word documents.
            a. Logistic Regression 
            b. KNN (k = 5)
            c. Linear SVM (kernel = linear)
            d. Kernel SVM (kernel = rbf)
            e. Naïve Bayes
            f. Decision Tree
            g. Random Forest (estimators = 10)
            f. XGBoost
# Assignment3
You are provided with a bank customers dataset (Churn_Modelling.csv) with about 10,000 customer information that can be used to decide whether the customer is likely to churn. 
There are multiple features. 
Identify which features are significant in determining whether the customer will churn. 
The last column, “Exited,” tells whether the customer stayed with the bank (Exited = 0) or left the bank (Exited = 1). 
Write a python code to design a three-layered ANN classifier that can predict whether the customer will churn for the test data set, which is 20% of the total dataset. 
Print the confusion matrix and accuracy, and then, submit the python code.
Be sure to encode the categorical data and perform the feature scaling. 
Use ‘relu’ activation for the first and second layers and ‘sigmoid’ for the last dense layer. 
For compiling, use ‘adam’ optimizer; and loss should be ‘binary_crossentropy’ as this is a binary classification problem.

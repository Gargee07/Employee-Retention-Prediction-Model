
# Employee-Retention-Prediction-Mode

A machine learning model to predict employee retention by analyzing factors such as demographics, job role, satisfaction levels etc. The goal is to create a predictive tool that can forecast the likelihood of an employee leaving the company or staying in company.




## Machine Learning Model

The final model is made using Random Forest Classifier . After analyzing the dataset, performing feature engineering, and conducting numerical analysis of the data, it was determined that the problem falls under a classification task. Various classification algorithms, including logistic regression, k-nearest neighbors (KNN), decision tree classifier, and random forest classifier, were compared based on their testing accuracy scores. Among these, the random forest classifier emerged as the most suitable model.



        Classifier               Accuracy (%)
	Logistic Regression      77.000000
	KNN                      97.222222
	Decision Tree            97.888889
	Random Forest            98.977778


## Deployment

The machine learning model is deployed using Flask, a Python web framework known for its simplicity and flexibility in building web applications. For the user interface, HTML (Hypertext Markup Language) is employed to structure web pages, while CSS (Cascading Style Sheets) is used for styling and layout design

To deploy this project run

```bash
  pip install flask
```




## Screenshots


![image 1](https://drive.google.com/file/d/12mO99e4xjuRxIGVNwGi1Rij-L60ItyI7/view?usp=sharing)

![image 2](https://drive.google.com/file/d/1Lfs5E-c1rcqHDl1NpOJAu6o7wcyKox8i/view?usp=drive_link)

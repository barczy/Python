import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import mlflow
from mlflow.models import infer_signature
mlflow.set_tracking_uri('http://127.0.0.1/5000')

# load datasets
X,y = datasets.load_iris(return_X_y=True)
# split data traning and test sets
X_train, X_test, y_train, y_test=train_test_split(X,y, test_size=0.20)
# define model hiper parameter
params = {"penalty": "l2", "solver":"lbfgs", "max_iter": 1000, "random_state": 8888}
# train modell
lr = LogisticRegression(**params)
lr.fit(X_train, y_train)

# prediction on the test set
y_pred = lr.predict(X_test)
y_pred

accuracy = accuracy_score(y_test, y_pred)
print(accuracy)

# MLFlow tracking
mlflow.set_tracking_uri(uri='http://127.0.0.1:5000')
# create new experiment
mlflow.set_experiment("MLFlow Quickstart")

with mlflow.start_run():
    mlflow.log_params(params)
    mlflow.log_metric("accuracy", accuracy)
    mlflow.set_tag("Training info", "Basic LR model for iris data")
    signature = infer_signature(X_train, lr.predict(X_train))
    model_info = mlflow.sklearn.log_model(
        sk_model=lr,
        artifact_path="iris_model2",
        signature=signature,
        input_example = X_train,
        registered_model_name="tracking-quickstart"
    )


params = {"solver":"newton-cg", "max_iter": 1000, "random_state": 8888}
# train modell
lr = LogisticRegression(**params)
lr.fit(X_train, y_train)

# prediction on the test set
y_pred = lr.predict(X_test)
y_pred

accuracy = accuracy_score(y_test, y_pred)
print(accuracy)


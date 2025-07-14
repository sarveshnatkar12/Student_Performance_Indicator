import os
import sys
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
import warnings
from sklearn.exceptions import FitFailedWarning
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FitFailedWarning)


from src.exception import CustomException
from src.logger import logging

def save_object(file_path, obj):
    """
    Saves any Python object (like a model or preprocessor) to the given file path using pickle.
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

        logging.info(f"Object saved at: {file_path}")

    except Exception as e:
        raise CustomException(e, sys)

def load_object(file_path):
    """
    Loads a pickled object (like a model or preprocessor) from the given file path.
    """
    try:
        with open(file_path, "rb") as file_obj:
            logging.info(f"Object loaded from: {file_path}")
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)

def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    """
    Trains and evaluates multiple models using GridSearchCV. Returns a report of model test scores.
    """
    try:
        report = {}

        for model_name, model in models.items():
            logging.info(f"Evaluating model: {model_name}")
            model_params = param.get(model_name, {})

            # Perform GridSearchCV if parameters are specified
            if model_params:
                gs = GridSearchCV(model, model_params, cv=3, n_jobs=-1, verbose=0)
                gs.fit(X_train, y_train)
                model = gs.best_estimator_
                logging.info(f"Best params for {model_name}: {gs.best_params_}")
            else:
                model.fit(X_train, y_train)

            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            logging.info(f"{model_name} R2 Score -> Train: {train_model_score:.4f}, Test: {test_model_score:.4f}")
            report[model_name] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)

import joblib
import pandas as pd
import pytest
 
# Define path to our model
MODEL_DIR = "models"
 
def test_model_correctness():
    clf = joblib.load(f"{MODEL_DIR}/model.pkl")
    data = {
        "MSSubClass": 60,
        "MSZoning": "RL",
        "LotArea": 7844,
        "LotConfig": "Inside",
        "BldgType": "1Fam",
        "OverallCond": 7,
        "YearBuilt": 1978,
        "YearRemodAdd": 1978,
        "Exterior1st": "HdBoard",
        "BsmtFinSF2": 0,
        "TotalBsmtSF": 672
    }
    # Compare with a tolerance: exact float equality breaks across library versions / CPUs
    assert clf.predict(pd.DataFrame(data, index=[0]))[0] == pytest.approx(157551.3761237591, rel=1e-6)
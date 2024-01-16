from dscigametrics.stat_summary import *
import pytest
import pandas as pd
import numpy as np

campaign_id = 219011657
start_date = 20220810
end_date = 20220811
data = pd.read_csv('tests/ga_metrics_test_data.csv')

output = stat_summary(data, campaign_id, start_date, end_date)

def test_mean():
    assert output.iloc[0, 0] == (0.9 + 0.8) /2
def test_std():
    assert np.isclose(output.iloc[2, 0], np.std([0.9, 0.8]), rtol=1e-05, atol=1e-08, equal_nan=False).all()
from dscigametrics.stat_summary import *
import pytest
import pandas as pd
import numpy as np

campaign_id = 219011657
start_date = 20220810
end_date = 20220811
test_data_path = 'tests/ga_metrics_test_data.csv'
data = pd.read_csv(test_data_path)

output = stat_summary(data, campaign_id, start_date, end_date)

def test_mean():
    assert output.iloc[0, 0] == (0.9 + 0.8) /2, f"The mean value is wrong with test data: {test_data_path}"

def test_std():
    assert np.isclose(output.iloc[2, 0], np.std([0.9, 0.8]), rtol=1e-05, atol=1e-08, equal_nan=False).all(), f"The standard deviation value is wrong with test data: {test_data_path}"

def test_input_type_error():
    with pytest.raises(TypeError):
        stat_summary('data', campaign_id, start_date, end_date)

def test_all_zero():
    data['totals.visits'] = 0
    output = stat_summary(data, campaign_id, start_date, end_date)
    assert (output['conversion_rate'] == 0).all(), "When 'totals.visits' are zeros, wrong value of conversion rate."
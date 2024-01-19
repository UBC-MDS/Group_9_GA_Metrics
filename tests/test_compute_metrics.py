from src.dscigametrics.compute_metrics import compute_metrics
import pytest
import pandas as pd

df = pd.read_csv('ga_metrics_test_data_small.csv')

def test_metric_computation():
    actual =  compute_metrics(df, 123851219, 20220801, 20220801)
    expected = {'conversion rate': 0.2,
                'new to return rate': 0.9,
                'total transaction revenue': 356.0,
                'average transaction revenue': 35.6}
    assert actual == expected, 'Metrics were not computed correctly!'

def test_data_check():
    with pytest.raises(TypeError, match='Your data argument must be a pandas dataframe'):
        compute_metrics(0, 123851219, 20220801, 20220801)

def test_ID_check():
    with pytest.raises(TypeError, match='The campaign ID should be an integer'):
        compute_metrics(df, '45', 20220801, 20220801)

def test_start_date_check():
    with pytest.raises(TypeError, match='Dates are entered as integers. 1st August, 2022 should be 20220801'):
        compute_metrics(df, 123851219, '20220801', 20220801)

def test_end_date_check():
    with pytest.raises(TypeError, match='Dates are entered as integers. 1st August, 2022 should be 20220801'):
        compute_metrics(df, 123851219, 20220801, '20220801')

def test_df_size_check():
    with pytest.raises(ValueError, match='There is no data matching your query'):
        compute_metrics(df, 0, 20220801, 20220801)
from dscigametrics.daily_plot import *
import pytest
import pandas as pd
import numpy as np

campaign_id = 219011657
start_date = 20220801
end_date = 20220820
data = pd.read_csv('tests/ga_metrics_test_data.csv')

output = daily_plot(data, campaign_id, start_date, end_date)

# Test for correct return type
def test_daily_plot_returns_chart():
    result = daily_plot(data, campaign_id, start_date, end_date)
    assert isinstance(result, alt.Chart), "`create_scatter_plot` should return an Altair Chart object"

# Test for correct error handling for incorrect object type (not a pandas data frame)
def test_daily_plot_returns_chart():
    with pytest.raises(TypeError):
        daily_plot(23455, campaign_id, start_date, end_date)

# Test for correct error handling for incorrect object type (not a integer)
def test_daily_plot_returns_chart():
    with pytest.raises(TypeError):
        daily_plot(data, 'campaign_id', start_date, end_date)

# Test for correct error handling for incorrect object type (not a integer)
def test_daily_plot_returns_chart():
    with pytest.raises(TypeError):
        daily_plot(data, campaign_id, 'start_date', end_date)

# Test for correct error handling for incorrect object type (not a integer)
def test_daily_plot_returns_chart():
    with pytest.raises(TypeError):
        daily_plot(data, campaign_id, start_date, 'end_date')

# Test for correct handling of negative width and height
def test_daily_plot_returns_chart():
    with pytest.raises(ValueError):
        daily_plot(data, campaign_id, start_date, end_date, -400, 400)
    with pytest.raises(ValueError):
        daily_plot(data, campaign_id, start_date, end_date, 400, -400)


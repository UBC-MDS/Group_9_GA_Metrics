import pytest
import pandas as pd
from dscigametrics.find_campaigns import find_campaigns



def test_find_campaigns():
    
    data = pd.read_csv('tests/ga_metrics_test_data.csv')

    # Test with invalid date format
    with pytest.raises(ValueError) as excinfo:
        find_campaigns(data, 'invalid-date', 20220825, [219011657, 140569061, 215934049, 123851219], 'conversion_rate')
    assert "Invalid start_date or end_date format" in str(excinfo.value)

    # Test with invalid metric
    with pytest.raises(ValueError) as excinfo:
        find_campaigns(data, 20220801, 20220825, [219011657, 140569061, 215934049, 123851219], 'invalid_metric')
    assert "metric must be one of" in str(excinfo.value)

    # Test with incorrect type for campaign_ids
    with pytest.raises(TypeError) as excinfo:
        find_campaigns(data, 20220801, 20220825, 'not-a-list', 'conversion_rate')
    assert "campaign_ids must be a list of integers" in str(excinfo.value)

    # Test with start date later than end date
    with pytest.raises(ValueError) as excinfo:
        find_campaigns(data, 20220825, 20220801, [219011657, 140569061, 215934049, 123851219], 'conversion_rate')
    assert "Start date must be earlier than end date" in str(excinfo.value)

    # Test An ID not in the data frame
    nonexistent_campaign_id = 99999 
    with pytest.raises(ValueError) as excinfo:
        find_campaigns(data, 20220801, 20220825, [nonexistent_campaign_id], 'conversion_rate')
    assert f"Campaign ID {nonexistent_campaign_id} not found in data" in str(excinfo.value)

    # Test the result is as expeced
    start_date = 20220801
    end_date =  20220825
    campaign_ids = [219011657, 140569061, 215934049, 123851219]
    metric = 'conversion_rate'
    result = find_campaigns(data, start_date, end_date, campaign_ids, metric)

    # Check if the result is a dictionary
    assert isinstance(result, dict)
    
    # Check the structure and values of the output
    expected_output = {
        'best_campaign': {'id': 123851219, 'value': 0.116},
        'worst_campaign': {'id': 219011657, 'value': 0.056}}
    
    assert result == expected_output
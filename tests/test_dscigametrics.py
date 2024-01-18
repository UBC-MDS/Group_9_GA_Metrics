import pytest
import pandas as pd
from dscigametrics.find_campaigns import find_campaigns



def test_find_campaigns():
    
    data = pd.read_csv('tests/toy_data_test.csv')

    # Test with invalid date format
    with pytest.raises(ValueError) as excinfo:
        find_campaigns(data, 'invalid-date', '2023-12-31', [100, 101], 'conversion_rate')
    assert "Invalid start_date or end_date format" in str(excinfo.value)

    # Test with invalid metric
    with pytest.raises(ValueError) as excinfo:
        find_campaigns(data, '2023-01-01', '2023-12-31', [100, 101], 'invalid_metric')
    assert "metric must be one of" in str(excinfo.value)

    # Test with incorrect type for campaign_ids
    with pytest.raises(TypeError) as excinfo:
        find_campaigns(data, '2023-01-01', '2023-12-31', 'not-a-list', 'conversion_rate')
    assert "campaign_ids must be a list of integers" in str(excinfo.value)


if __name__ == "__main__":
    pytest.main()

    # Test with start date later than end date
    with pytest.raises(ValueError) as excinfo:
        find_campaigns(data, '2024-01-01', '2023-12-31', [100, 101], 'conversion_rate')
    assert "Start date must be earlier than end date" in str(excinfo.value)

    # Test An ID not in the data frame
    nonexistent_campaign_id = 9999  
    with pytest.raises(ValueError) as excinfo:
        find_campaigns(data, '2023-01-01', '2023-12-31', [nonexistent_campaign_id], 'conversion_rate')
    assert f"Campaign ID {nonexistent_campaign_id} not found in data" in str(excinfo.value)

    # Test the result is as expeced
    start_date = '2023-01-01'
    end_date = '2023-12-31'
    campaign_ids = [100, 101, 102, 103, 104]
    metric = 'conversion_rate'
    result = find_campaigns(data, start_date, end_date, campaign_ids, metric)

    # Check if the result is a dictionary
    assert isinstance(result, dict)
    
    # Check the structure and values of the output
    expected_output = {
        'best_campaign': {'id': 104, 'value': 0.25},
        'worst_campaign': {'id': 100, 'value': 0.15384615384615385}
    }
    assert result == expected_output
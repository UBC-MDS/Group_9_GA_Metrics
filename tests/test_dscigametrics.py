from dscigametrics import dscigametrics
import pytest
import pandas as pd
from dscigametrics.find_campaigns import find_campaigns
# from dscigametrics.compute_metrics import compute_metrics


def test_find_campaigns():
    
    data = pd.read_csv('toy_data_large.csv')

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

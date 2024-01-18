
import pandas as pd
import numpy as np
from compute_metrics_temp import compute_metrics

def find_campaigns(data, start_date, end_date, campaign_ids, metric):
    """Analyzes and identifies the best and worst performing marketing campaigns based on a selected metric 

    Parameters
    ----------
    data : dataframe
        Dataframe containing information from google analytics
    start_date : datetime
        The start date for the analysis period.
    end_date : datetime
        The end date for the analysis period.
    campaign_ids : list of str
        A list of campaign IDs to be analyzed.
    metric : str
        The name of the metric to be used for evaluating campaign performance. 

    Returns
    -------
    dict
        A dictionary containing two key-value pairs - 'best_campaign' and 'worst_campaign'.

    Examples
    --------
    >>> output_dict = find_best_and_worst_campaigns(data, 11111111, 20170817, 20170820, 'conversion_rate')
    """
    if not isinstance(start_date, (str, pd.Timestamp)) or not isinstance(end_date, (str, pd.Timestamp)):
        raise ValueError("start_date and end_date must be strings or pandas Timestamps")

    try:
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)
    except ValueError:
        raise ValueError("Invalid start_date or end_date format")

    if not isinstance(campaign_ids, list) or not all(isinstance(x, int) for x in campaign_ids):
        raise TypeError("campaign_ids must be a list of integers")

    valid_metrics = ['new_to_return_rate', 'conversion_rate', 'total_transaction_revenue', 'average_transaction_revenue']
    if not isinstance(metric, str) or metric not in valid_metrics:
        raise ValueError(f"metric must be one of {valid_metrics}")

    campaign_metrics = {}
    for cid in campaign_ids:
        metrics = compute_metrics(data, cid, start_date, end_date)
        campaign_metrics[cid] = metrics.get(metric, 0)

    best_campaign = max(campaign_metrics, key=campaign_metrics.get)
    worst_campaign = min(campaign_metrics, key=campaign_metrics.get)

    return {
        'best_campaign': {'id': best_campaign, 'value': campaign_metrics[best_campaign]},
        'worst_campaign': {'id': worst_campaign, 'value': campaign_metrics[worst_campaign]}
    }
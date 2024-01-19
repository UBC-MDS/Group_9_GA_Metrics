
import pandas as pd
import numpy as np


def find_campaigns(data, start_date, end_date, campaign_ids, metric):
    """Analyzes and identifies the best and worst performing marketing campaigns based on a selected metric 

    Parameters
    ----------
    data : dataframe
        Dataframe containing information from google analytics
    start_date : int or timestamp
        The start date for the analysis period.
    end_date : int or timestamp
        The end date for the analysis period.
    campaign_ids : list of int
        A list of campaign IDs to be analyzed.
    metric : str
        The name of the metric to be used for evaluating campaign performance. 

    Returns
    -------
    dict
        A dictionary containing two key-value pairs - 'best_campaign' and 'worst_campaign'.

    Examples
    --------
    >>> output_dict = find_best_and_worst_campaigns(data, '2023-01-01', '2023-12-31', [100, 101, 102, 103, 104], 'conversion_rate')
    {'best_campaign': {'id': 104, 'value': 0.25}, 'worst_campaign': {'id': 100, 'value': 0.15384615384615385}}

    """
    if not isinstance(start_date, (int, pd.Timestamp)) or not isinstance(end_date, (int, pd.Timestamp)):
        raise ValueError("start_date and end_date must be int or pandas Timestamps")

    if not isinstance(campaign_ids, list) or not all(isinstance(x, int) for x in campaign_ids):
        raise TypeError("campaign_ids must be a list of integers")

    valid_metrics = ['return_rate', 'conversion_rate', 'total_trans_revenue', 'avg_trans_revenue']
    if not isinstance(metric, str) or metric not in valid_metrics:
        raise ValueError(f"metric must be one of {valid_metrics}")
    
    
    if start_date > end_date:
        raise ValueError("Start date must be earlier than end date")

    start_date = pd.to_datetime(start_date, format='%Y%m%d')
    end_date = pd.to_datetime(end_date, format='%Y%m%d')
    toy_data = data[['trafficSource.adwordsClickInfo.campaignId', 'date', 'totals.newVisits', 'totals.transactions', 'totals.visits', 'totals.transactionRevenue']]
    toy_data = toy_data.fillna(0.0)
    toy_data.columns = ['campaignId', 'date', 'newVisits', 'transactions', 'visits', 'transactionRevenue' ]
    toy_data['date'] = pd.to_datetime(toy_data['date'], format='%Y%m%d')
    filtered_data = toy_data[(toy_data['date'] >= start_date) & (toy_data['date'] <= end_date)]
    
    campaign_metrics = {}
    for cid in campaign_ids:
        metrics = {}
        data = filtered_data[filtered_data['campaignId'] == cid]
        metrics['return_rate'] = data['newVisits'].mean()
        metrics['conversion_rate'] = sum(data['transactions']) / sum(data['visits'])
        metrics['total_trans_revenue']  = data['transactionRevenue'].sum()
        metrics['avg_trans_revenue']  = data['transactionRevenue'].mean()
        campaign_metrics[cid] = metrics.get(metric, 0)

    best_campaign = max(campaign_metrics, key=campaign_metrics.get)
    worst_campaign = min(campaign_metrics, key=campaign_metrics.get)

    return {
        'best_campaign': {'id': best_campaign, 'value': campaign_metrics[best_campaign]},
        'worst_campaign': {'id': worst_campaign, 'value': campaign_metrics[worst_campaign]}
    }

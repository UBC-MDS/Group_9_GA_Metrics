import pandas as pd
import numpy as np


def compute_metrics(data, campaign_id, start_date, end_date):
    """Computes the key metrics.

    Computes four metrics from Google Analytics data: 
        1. New to return rate
        2. Conversion rate
        3. Total transaction revenue
        4. Average transaction revenue

    Parameters
    ----------
    data : dataframe
        Dataframe containing information from google analytics
    campaign_id : int
        The campaign ID of the campaign in question
    start_date : int
        Date when campaign started
    end_date : int
        Date when campaign ended

    Returns
    -------
    string
        A body of text stating the four computed metrics

    Example
    -------
    >>> compute_metrics(df, 11111111, 20230101, 20231231)
        "New to return rate: 1.3
        Conversion rate: 0.23
        Total transaction revenue: $100
        Average transaction revenue: $2.33"
    """
    
    data['startDate'] = pd.to_datetime(data['startDate'])
    data['endDate'] = pd.to_datetime(data['endDate'])

    filtered_data = data[(data['campaignId'] == campaign_id) & 
                         (data['startDate'] >= start_date) & 
                         (data['endDate'] <= end_date)]

    new_visitors = filtered_data['visitNumber'] == 1
    returning_visitors = filtered_data['visitNumber'] > 1
    new_to_return_rate = new_visitors.sum() / returning_visitors.sum() if returning_visitors.sum() > 0 else 0

    conversions = filtered_data['transactionId'].notna()
    conversion_rate = conversions.sum() / len(filtered_data) if len(filtered_data) > 0 else 0

    total_transaction_revenue = filtered_data['transactionRevenue'].sum()
    average_transaction_revenue = filtered_data['transactionRevenue'][conversions].mean() if conversions.sum() > 0 else 0

    return {
        'new_to_return_rate': new_to_return_rate,
        'conversion_rate': conversion_rate,
        'total_transaction_revenue': total_transaction_revenue,
        'average_transaction_revenue': average_transaction_revenue
    }

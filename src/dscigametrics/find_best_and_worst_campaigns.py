def find_best_and_worst_campaigns(data, start_date, end_date, campaign_ids, metric):
    """Analyzes the extreme performing values of marketing campaigns.

    Analyzes and identifies the best and worst performing marketing campaigns based on a selected metric from Google Analytics data over a specified date range.

    Parameters
    ----------
    data : pandas.DataFrame
        A DataFrame containing campaign data. Expected to include columns for dates, campaign IDs, and various metrics like visits, transactions, and revenue.
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
    

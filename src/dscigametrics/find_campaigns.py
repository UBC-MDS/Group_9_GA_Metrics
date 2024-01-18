def find_best_and_worst_campaigns(data, start_date, end_date, campaign_ids, metric):
    """Analyzes and identifies the best and worst performing marketing campaigns based on a selected metric 

    Parameters
    ----------
    data : dataframe
        Dataframe containing information from google analytics
    start_date : string
        The start date for the analysis period.
    end_date : string
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
    

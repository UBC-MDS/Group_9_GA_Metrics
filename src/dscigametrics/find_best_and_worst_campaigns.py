def find_best_and_worst_campaigns(df, start_date, end_date, campaign_ids, metric):
    '''

    Analyzes and identifies the best and worst performing marketing campaigns based on a selected metric from Google Analytics data over a specified date range.

    Parameters
    ----------
    df : pandas.DataFrame
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
    ----------
    dict
        A dictionary containing two key-value pairs - 'best_campaign' and 'worst_campaign'.


    '''
    

def find_best_and_worst_campaigns(df, start_date, end_date, campaign_ids, metric):
    '''

    Analyzes and identifies the best and worst performing marketing campaigns based on a selected metric from Google Analytics data over a specified date range.

    This function calculates performance metrics for each specified campaign within the date range and then determines the best and worst performing campaigns based on the specified metric.

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
        The name of the metric to be used for evaluating campaign performance. This should be one of the keys returned by the 'calculate_campaign_metrics' function, such as 'conversion_rate', 'total_transaction_revenue', etc.

    Returns
    ----------
    dict
        A dictionary containing two key-value pairs - 'best_campaign' and 'worst_campaign'. Each is a dictionary itself, containing the 'campaign_id' and its corresponding 'metrics', which include the performance metrics calculated for that campaign.


    '''
    
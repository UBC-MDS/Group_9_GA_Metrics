def find_best_and_worst_campaigns(df, start_date, end_date, campaign_ids, metric):
    """
    Analyzes marketing campaign performance over a specified date range and identifies the best and worst performing campaigns based on a selected metric.

    This function iterates over a list of campaign IDs, calculates performance metrics for each campaign within the given date range, and then determines the best and worst performing campaigns based on the specified metric.

    Parameters:
    df (pandas.DataFrame): A DataFrame containing campaign data. Expected to include columns for dates, campaign IDs, and various metrics like visits, transactions, and revenue.
    start_date (datetime): The start date for the analysis period.
    end_date (datetime): The end date for the analysis period.
    campaign_ids (list of str): A list of campaign IDs to be analyzed.
    metric (str): The name of the metric to be used for evaluating campaign performance. This should be one of the keys returned by the 'calculate_campaign_metrics' function, such as 'conversion_rate', 'total_transaction_revenue', etc.

    Returns:
    dict: A dictionary containing two key-value pairs - 'best_campaign' and 'worst_campaign'. Each is a dictionary itself, containing the 'campaign_id' and its corresponding 'metrics', which include the performance metrics calculated for that campaign.

    Example usage:
    campaign_ids = ['campaign1', 'campaign2', 'campaign3'];
    result = find_best_and_worst_campaigns(df, pd.to_datetime('2022-01-01'), pd.to_datetime('2022-03-31'), campaign_ids, 'conversion_rate');
    print(result)
    """

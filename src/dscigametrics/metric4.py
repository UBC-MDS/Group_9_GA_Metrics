def find_best_and_worst_campaigns(df, start_date, end_date, campaign_ids, metric):
    """
    Analyzes marketing campaign performance over a specified date range and identifies the best and worst performing campaigns based on a selected metric.

    This function iterates over a list of campaign IDs, calculates performance metrics for each campaign within the given date range, and then determines the best and worst performing campaigns based on the specified metric.

    Parameters:
    df (pandas.DataFrame): A DataFrame containing campaign data. Expected to include columns for dates, campaign IDs, and various metrics like visits, transactions, and revenue.
    start_date (datetime): The start date for the analysis period.
    end_date (datetime): The end date for the analysis period.

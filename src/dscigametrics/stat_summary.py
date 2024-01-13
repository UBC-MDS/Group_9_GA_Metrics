def stat_summary(data, campaign_id, start_date, end_date):
    """Return statistics summary of metrics.
    
    Return a pandas dataframe presenting the statistics summary of the four metric, where the metrics are:
            1. New to return rate
            2. Conversion rate
            3. Total transaction revenue
            4. Average transaction revenue

    Parameters
    ----------
    data : dataframe
        Dataframe containing information from google analytics.
    campaign_id : int
        The unique id of the campaign.
    start_date : int
        The campaign start date.
    end_date : int
        The campaign end date.
    
    Returns
    -------
    summary_table : pd.DataFrame
        A pandas dataframe contains the mean, median and standard deviation of the four metrics.
        Four metrics:
            1. New to return rate
            2. Conversion rate
            3. Total transaction revenue
            4. Average transaction revenue 
    
    Example
    -------
    >>> summary = stat_summary(data, 11111111, 20170817, 20170820)
    >>> print(summary)
                    return   conversion   ttl_revenue   avg_revenue
        Mean         0.01        0.05         250           100
        Median       0.02        0.04         238           120
        SD           1.43        0.66         1.62          0.77
    """

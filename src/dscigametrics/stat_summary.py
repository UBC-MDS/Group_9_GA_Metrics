def stat_summary(campaign_id, start_date, end_date):
    """
    Return statistics summary of metrics.

    Parameters
    ----------
    campaign_id : int
        The unique id of the campaign.
    start_date : int
        The campaign start date.
    end_date : int
        The campaign end date.

    Returns
    -------
    summary_table : pd.DataFrame
        A pandas dataframe contains the overall statistic summary of the four metrics.
    mean : dict
        Mean values of the four metrics. Should look like `{'return': 0.01, 'conversion': 0.05, ...}
    median : dict
        Median values of the four metrics.
    sd : dict
        Standard deviations of the four metrics.
    """

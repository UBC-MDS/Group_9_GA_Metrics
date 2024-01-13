def daily_plot(data, campaign_id, start_date, end_date):
    """Creating time-series chart

    Returns a time-series chart that visualises daily performance of a campaign
    in a period.

    Parameters
    ----------
    data : dataframe
        Dataframe containing information from google analytics
    campaign_id : int
        The unique id of the campaign.
     start_date : int
        The campaign start date.
    end_date : int
        The campaign end date.
        
    Returns
    -------
    plot
        A plot that visualize data points of four metrics.
            Four metrics:
                1. New to return rate
                2. Conversion rate
                3. Total transaction revenue
                4. Average transaction revenue 

    Examples
    --------
    >>> daily_plot(df, 452349492, 20220401, 20220430)
    """
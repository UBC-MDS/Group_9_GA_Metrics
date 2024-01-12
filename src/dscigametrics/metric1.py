def compute_metrics(data, campaign, start_date, end_date):
    '''
    Computes four metrics from Google Analytics data: 
        1. New to return rate
        2. Conversion rate
        3. Total transaction revenue
        4. Average transaction revenue

    Parameters
    ----------

    data : dataframe
        Dataframe containing information from google analytics
    campaign : int or double
        The campaign ID of the campaign in question
    start_date : int
        Date when campaign started
    end_date : int
        Date when campaign ended

    Returns
    -------

    string
    A body of text stating the four computed metrics

    Examples
    --------
    >>> from dscigametrics import compute_metrics(df, 123, 2023-01-01, 2023-12-31)
    >>> "New to return rate: 1.3 \n 
    Conversion rate: 0.23 \n 
    Total transaction revenue: $100 \n 
    Average transaction revenue: $2.33"

    '''
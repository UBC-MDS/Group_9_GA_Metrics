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
    campaign : int
        The campaign ID of the campaign in question
    start_date : int
        Date when campaign started
    end_date : int
        Date when campaign ended

    Returns
    -------

    string
    A body of text stating the four computed metrics
    '''
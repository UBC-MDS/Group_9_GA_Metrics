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
        ----------
            summary_table : pd.DataFrame
                A pandas dataframe contains the mean, median and standard deviation of the four metrics.
                Four metrics:
                    1. New to return rate
                    2. Conversion rate
                    3. Total transaction revenue
                    4. Average transaction revenue 
    
    """

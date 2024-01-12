def stat_summary(metric, verbose = True):
    """Return statistics summary of metrics

    Parameters
    ----------
    metric : pd.Series
        Serveral data points represent `metrics` of different time.
    verbose : boolean
        Whether or not print out the statistics summary result.

    Returns
    -------
    mean
        Mean value of the data points.
    median
        Median value of the data points.
    sd
        Standard deviation of the data points.
    """
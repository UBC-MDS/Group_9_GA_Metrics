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

    Examples
    --------
    >>> mean, median, sd = summary_metric2(metric2, verbose = True)
    """
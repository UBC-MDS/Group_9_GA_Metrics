# dscigametrics

`dscigametrics` enables users to easily compute four important metrics:

1. Ratio of new to returning visitors: measures the ratio of new users to returning users of each campaign in certain period. 
2. Conversion rate: measures the percentage of users who complete a specific desired action of each campaign in certain period.
3. Total transaction revenue: measures total transaction revenue of each campaign in certain period.
4. Average transaction revenue: measures average transaction revenue of each campaign in certain period.

## Fuctions in the package

The package also provides convenience functions to compute summary statistics, produce visualizations of the data and find the best and worst campaign:

1. `compute_metrics` summarises general performance of campaign based on four metrics.
2. `stat_summary` summarises variance of campaign performance based on four metrics.
3. `daily_plot` visualises performance changes of campaign based on four metrics.
4. `find_best_and_worst_campaigns` identifies the best and worst performing campaigns based on a selected metric.

## Where this package fits in

The popularity and influence of Google Analytics means that there is already a decent number of related python packages, such as googleanalytics, which can be found on PyPI: [https://pypi.org/project/googleanalytics/]. However the majority of these packages provide functionality that allows developers to interact with the Google Analytics API, which presupposes a fairly high level of technical skill. Our package is intended to help users with a novice familiarity with python by operating directly on downloaded GA data sets instead.

## Installation

```bash
$ pip install dscigametrics
```

## Main Contributor

Beth Ou-Yang, Ian MacCarthy, Yili Tang, Weilin Han

## Contributing

Contributions are welcome and greatly appreciated! If you're interested in contributing to this project, take a look at the [contributor guide](contributing.md).

## License

`dscigametrics` was created by DSCI524 Cohort8 Group9. It is licensed under the terms of the MIT license.

## Credits

`dscigametrics` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).

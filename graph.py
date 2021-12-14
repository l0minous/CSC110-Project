"""CSC110 Fall 2020 Project, Toronto Living Cost Calculator Display Graphs

This Python module contains the program to display the graph.

Copyright and Usage Information
===============================
This file is provided solely for the personal and private use of The Department of Computer Science
at the University of Toronto St. George campus. All forms of distribution of this code, whether
as given or with any changes, are expressly prohibited.

This file is Copyright (c) 2021 Derrick Ken Willis, Sebastian Noel Lie, Diler Zaza and
Humraj Bhoday.
"""
from matplotlib import pyplot as plt


def display_month_to_gap(dict_1: dict) -> None:
    """Displays information of a graph from function month_to_gap"""
    plt.close()
    y = [dict_1[x] for x in dict_1]
    plt.plot(list(dict_1), y)
    plt.xticks(rotation=90)
    plt.xlabel('Months')
    plt.ylabel('Difference Between Wage and Living Cost')
    plt.title('Affordability Over Time Period')
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    import python_ta
    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()
    python_ta.check_all(config={
        'allowed-io': ['load_rent', 'load_electricity_costs', 'load_weekly_wages',
                       'load_water_rates'],
        'extra-imports': ['python_ta.contracts', 'matplotlib'],
        'max-line-length': 100,
        'max-args': 6,
        'max-locals': 25,
        'disable': ['R1705'],
    })

"""CSC110 Fall 2020 Project, Loading Data from CSV Files

This Python module contains the program to load data from the csv files.

Copyright and Usage Information
===============================
TODO
"""
import csv


def load_rent() -> list[list[str, int]]:
    """Returns a list of a lists where each inner list element is a row of the average_rent.csv file

    The data in average_rent.csv is in a csv format with 2 columns. The first column corresponds to
    the month. The second column correspond to the average house rent for a one bedroom apartment
    in Toronto.
    """
    # ACCUMULATOR row_so_far: Accumulator where each element is a list of the month and rent cost
    row_so_far = []
    filename = "data/average_rent.csv"
    with open(filename) as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)  # skip the header

        for row in reader:
            assert len(row) == 2, 'Expected every row to contain 2 elements.'
            # row is a list of strings
            rent_for_month = [row[0], float(row[1])]
            row_so_far.append(rent_for_month)

    return row_so_far


def load_electricity_costs() -> list[list]:
    """Returns a list of lists where each inner list element is a row of the electricity_costs.csv
    file

    The data in electricity_costs.csv is in a csv format with 2 columns. The first column
    corresponds to the date. The second column correspond to the date's electricity rate in Toronto.
    """
    # ACCUMULATOR row_so_far: Accumulator where each element is a list of the month and rent cost
    row_so_far = []
    filename = "data/electricity_costs.csv"
    with open(filename) as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)  # skip the header

        for row in reader:
            assert len(row) == 2, 'Expected every row to contain 2 elements.'
            # row is a list of strings
            rate_for_month = [row[0], float(row[1])]
            row_so_far.append(rate_for_month)

    return row_so_far


def load_weekly_wages() -> list[list]:
    """Returns a list of lists where each inner list element is a row of the weekly_wages.csv
    file

    The data in weekly_wages.csv is in a csv format with 23 columns. The first column corresponds to
    the industry. The rest of the columns correspond to the industry's wage in Toronto
    """
    # ACCUMULATOR row_so_far: Accumulator where each element is a list of the month and rent cost
    row_so_far = []
    filename = "data/weekly_wages.csv"
    with open(filename) as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)  # skip the header

        for row in reader:
            assert len(row) == 23, 'Expected every row to contain 2 elements.'
            # row is a list of strings
            rate_for_month = []
            rate_for_month.append(row[0])
            for i in range(1, 23):
                rate_for_month.append(float(row[i]))
            row_so_far.append(rate_for_month)

    return row_so_far


def load_water_rates() -> list[list]:
    """Returns a list of lists where each inner list element is a row of the water_rates.csv
    file

    The data in water_rates.csv is in a csv format with 2 columns. The first column corresponds to
    the year. The second columns corresponds to the water rate per gallon in Toronto for that year.
    """
    # ACCUMULATOR row_so_far: Accumulator where each element is a list of the month and rate.
    row_so_far = []
    filename = "data/water_rates.csv"
    with open(filename) as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)  # skip the header

        for row in reader:
            assert len(row) == 2, 'Expected every row to contain 2 elements.'
            # row is a list of strings
            rate_for_month = [row[0], float(row[1])]
            row_so_far.append(rate_for_month)

    return row_so_far


def load_all() -> dict[str, list]:
    """Returns a dictionary mapping the type of data to list of data from all the csv files"""
    # ACCUMULATOR row_so_far: Accumulator that maps type of csv data to data in list form.
    all_data = {'rent': load_rent(), 'electricity': load_electricity_costs(),
                'wages': load_weekly_wages(), 'water': load_water_rates()}
    return all_data


if __name__ == '__main__':
    import python_ta
    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()
    python_ta.check_all(config={
        'allowed-io': ['load_rent', 'load_electricity_costs', 'load_weekly_wages',
                       'load_water_rates'],
        'extra-imports': ['python_ta.contracts', 'csv'],
        'max-line-length': 100,
        'max-args': 6,
        'max-locals': 25,
        'disable': ['R1705'],
    })

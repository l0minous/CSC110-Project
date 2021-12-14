"""CSC110 Fall 2020 Project, Toronto Living Cost Calculator Calculations

This Python module contains the program to perform calculations on data.

Copyright and Usage Information
===============================
This file is provided solely for the personal and private use of The Department of Computer Science
at the University of Toronto St. George campus. All forms of distribution of this code, whether
as given or with any changes, are expressly prohibited.

This file is Copyright (c) 2021 Derrick Ken Willis, Sebastian Noel Lie, Diler Zaza and
Humraj Bhoday.
"""
import load_data


def get_difference(occupation: str, month_gap: dict, start: str, end: str) -> dict:
    """
    Returns a dictionary with tuples which contain the previous month and the current month as the
    keys and tuples containing the numeric change in the difference between the monthly wages and
    the cost of housing as the value pairs.
    """
    # ACCUMULATOR dict_difference: Accumulator where each key-value pair holds data on the difference between monthly
    # wages and the cost of housing for the months between the time period.
    dict_difference = {}
    months = get_list_of_months(start, end)
    indexes = find_month_index(start, end, months)
    filtered_months = [months[x] for x in range(indexes[0], indexes[1] + 1)]
    dict_difference = {}

    for x in range(0, len(filtered_months) - 1):
        left_gap = month_gap[filtered_months[x]]
        right_gap = month_gap[filtered_months[x + 1]]
        numeric_change = right_gap - left_gap
        percentage_change = (numeric_change / left_gap) * 100
        dict_difference[(filtered_months[x], filtered_months[x + 1])] = (numeric_change, percentage_change)

    return dict_difference


def start_end_difference(start: str, end: str, month_gap: dict) -> tuple:
    """
    Returns a tuple containing the numeric difference and percentage difference between the monthly
    wages and the cost of housing for the beginning and end of the time period.
    """
    start_gap = month_gap[start]
    end_gap = month_gap[end]
    gap_difference = end_gap - start_gap
    gap_percentage_change = gap_difference / start_gap * 100
    return (gap_difference, gap_percentage_change)


def month_to_cost(start: str, end: str) -> dict :
    """
    Returns a dictionary of the months as the keys and the cost of housing for that month as the
    value pair.
    """
    costs = calculate_monthly_costs(start, end)
    months = get_list_of_months(start, end)
    indexes = find_month_index(start, end, months)
    filtered_months = [months[x] for x in range(indexes[0], indexes[1] + 1)]
    dict_monthly_cost = {}

    for x in range(0, len(filtered_months)):
        dict_monthly_cost[filtered_months[x]] = costs[x]

    return dict_monthly_cost


def calculate_monthly_costs(start: str, end: str) -> list:
    """
    Returns a list that contains the monthly housing costs throughout the selected time period
    indicated by the parameters called 'start' and 'end'.
    """
    monthly_costs = []
    rent = filter_rent_costs(start, end)
    electricity = filter_electricity_costs(start, end)
    water = get_monthly_water_cost(start, end)

    for x in range(0, len(rent)):
        rent_cost = rent[x]
        electricity_cost = electricity[x]
        water_cost = water[x]
        total = rent_cost + electricity_cost + water_cost
        monthly_costs.append(total)

    return monthly_costs


def filter_rent_costs(start: str, end: str) -> list:
    """
    Returns a list of the rent costs for the months between the chosen time period indicated by the
    parameters called 'start' and 'end'.
    """
    rent_data = load_data.load_rent()
    months_list = get_list_of_months(start, end)

    start_end_indexes = find_month_index(start, end, months_list)
    filtered_rent_prices = []

    for y in range(start_end_indexes[0], start_end_indexes[1] + 1):
        filtered_rent_prices.append(rent_data[y][1])

    return filtered_rent_prices


def filter_electricity_costs(start: str, end: str) -> list:
    """
    Returns a list of the electricity costs for the months between the chosen time period indicated by the
    parameters called 'start' and 'end'.
    https://www.oeb.ca/sites/default/files/uploads/Report_Defining_Typical_Elec_Customer_20160414.pdf states that
    the average Ontarian consumes 753 kWh per month
    """
    electricity_data = list(reversed(load_data.load_electricity_costs()))
    months = get_list_of_months(start, end)
    costs = []

    for x in months:
        kwh_cost = get_kwh(electricity_data, x)
        costs.append(kwh_cost * 753)

    return costs


def get_kwh(electricity_data: list, month: str) -> float:
    """
    Returns a float which holds the value of how much the consumption of a kilowatt is depending on
    the month passed by the parameter called 'month'.
    """
    kwh_cost = int
    if month in get_list_of_months('November 2019', 'February 2020'):
        kwh_cost = electricity_data[0][1]
    elif month == 'March 2021':
        kwh_cost = (23 * electricity_data[0][1]) + (7 * electricity_data[1][1])
    elif month in get_list_of_months('June 2020', 'October 2020'):
        kwh_cost = electricity_data[2][1]
    elif month in get_list_of_months('November 2020', 'December 2020'):
        kwh_cost = electricity_data[3][1]
    elif month == 'January 2021':
        kwh_cost = electricity_data[4][1]
    elif month == 'February 2021':
        kwh_cost = (22 * electricity_data[4][1]) + (8 * electricity_data[5][1])
    elif month in get_list_of_months('May 2021', 'August 2021'):
        kwh_cost = electricity_data[6][1]
    return kwh_cost / 100


def get_monthly_water_cost(start: str, end: str) -> list:
    """
    Returns a list of the water costs for the months between the chosen time period indicated by the
    parameters called 'start' and 'end'.
    """
    water_data = load_data.load_water_rates()
    months = get_list_of_months(start, end)
    water_costs = []

    for x in months:
        if '2021' in x:
            water_costs.append(water_data[0][1] * 72.3699)
        elif '2020' in x:
            water_costs.append(water_data[1][1] * 72.3699)
        elif '2021' in x:
            water_costs.append(water_data[2][1] * 72.3699)

    return water_costs


def filter_monthly_wages(occupation: str, start: str, end: str) -> list[float]:
    """
    Returns a list of the monthly wages a person with a specific occupation which is passed by
    the 'occupation' parameter throughout the specified time period indicated by the
    parameters called 'start' and 'end'.
    """
    wage_data = load_data.load_weekly_wages()
    occupation_wage_data = []

    for x in range(0, len(wage_data)):
        if occupation in wage_data[x][0]:
            row_data = wage_data[x]
            occupation_wage_data = [row_data[x] for x in range(1, len(row_data))]

    start_end_indexes = find_month_index(start, end, get_list_of_months(start, end))
    monthly_wages_filtered = []

    for y in range(start_end_indexes[0], start_end_indexes[1] + 1):
        monthly_wages_filtered.append(occupation_wage_data[y] / 7 * 30)

    return monthly_wages_filtered


def wage_cost_gap(occupation: str, start: str, end: str) -> list:
    """
    Returns a list of the gap between the monthly wages of a person with a specific occupation
    passed by the parameter 'occupation' throughout a specific time period indicated by the
    parameters called 'start' and 'end'.
    """
    wage_list = filter_monthly_wages(occupation, start, end)
    cost_list = calculate_monthly_costs(start, end)
    gap_list = []

    for x in range(0, len(wage_list)):
        gap = wage_list[x] - cost_list[x]
        gap_list.append(gap)

    return gap_list


def month_to_gap(gap: list, start: str, end: str) -> dict:
    """
    Returns a dictionary containing the months in the specific time period indicated by the
    parameters called 'start' and 'end' as the keys and the gap between the monthly wages of a
    person with a specific occupation passed by the parameter 'occupation' as the value pairs.
    """
    months = get_list_of_months(start, end)
    indexes = find_month_index(start, end, months)
    filtered_months = [months[x] for x in range(indexes[0], indexes[1] + 1)]
    dict_month_gap = {}
    for x in range(0, len(gap)):
        dict_month_gap[filtered_months[x]] = abs(gap[x])
    return dict_month_gap


def get_list_of_months(start: str, end: str) -> list[str]:
    """
    Returns a list of all the months between November 2019 to August 2021.
    """
    months_list = []
    rent_data = load_data.load_rent()

    for x in range(0, len(rent_data)):
        months_list.append(rent_data[x][0])

    return months_list


def find_month_index(start: str, end: str, months: list) -> tuple[int, int]:
    """
    Returns a tuple which holds the indexes of the start month and the end month indicated by the
    'start' and 'end' parameters in the list of months passed by the parameter 'months'.
    """
    start_index = int
    end_index = int

    for x in range(0, len(months)):
        if months[x] == start:
            start_index = x
        if months[x] == end:
            end_index = x

    return (start_index, end_index)


if __name__ == '__main__':
    import python_ta
    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()
    python_ta.check_all(config={
        'allowed-io': ['load_rent', 'load_electricity_costs', 'load_weekly_wages',
                       'load_water_rates'],
        'extra-imports': ['python_ta.contracts', 'load_data'],
        'max-line-length': 100,
        'max-args': 6,
        'max-locals': 25,
        'disable': ['R1705'],
    })

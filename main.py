"""CSC110 Fall 2020 Project, Toronto Living Cost Calculator GUI

This Python module contains the program to display the main GUI.

Copyright and Usage Information
===============================
This file is provided solely for the personal and private use of The Department of Computer Science
at the University of Toronto St. George campus. All forms of distribution of this code, whether as
given or with any changes, are expressly prohibited.

This file is Copyright (c) 2021 Derrick Ken Willis, Sebastian Noel Lie, Diler Zaza and
Humraj Bhoday.
"""
import tkinter as tk
import tabulate
import calculations
import graph


class Root(tk.Tk):
    """Create a new tkinter root that is the main frame to contain all the widgets"""
    # Private Instance Attributes:
    #   _label: the display label that is used by multiple methods
    _label: tk.Label

    def __init__(self) -> None:
        tk.Tk.__init__(self)
        self.title("Toronto Living Cost Calculator")
        containers = self.make_containers()
        self.create_display(containers[1])
        self.create_input_fields(containers[0])
        self.mainloop()

    def make_containers(self) -> tuple[tk.Frame, tk.Frame]:
        """Creates all background container widgets for the gui"""
        # Create a Canvas for all widgets to be placed in
        canvas = tk.Canvas(self, height=500, width=600)
        canvas.pack()

        # Create a Frame widget for input fields to be placed in
        frame = tk.Frame(self, bg='#33C7FF', bd=5)
        # center the inner frame 10% of root window size of 80% screen size
        frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.2, anchor='n')

        # Create a Lower Frame for Display Information Labels to be places in
        lower_frame = tk.Frame(self, bg='#33C7FF', bd=10)
        lower_frame.place(relx=0.5, rely=0.35, relwidth=0.75, relheight=0.6, anchor='n')

        return (frame, lower_frame)

    def create_display(self, display_frame: tk.Frame) -> None:
        """Creates a display to show output information based on inputs"""
        # Create a label Widget
        self._label = tk.Label(display_frame, bg="black", font=('ariel', 8))
        self._label.place(relwidth=1, relheight=1)

    def create_input_fields(self, input_frame: tk.Frame) -> None:
        """Creates all the inputs fields to gain information from the user as well as a button
        to enter the selected data"""

        # Create an input drop down menu for the start and end date
        date_options = [
            'November 2019', 'December 2019', 'January 2020', 'February 2020', 'March 2020',
            'April 2020', 'May 2020', 'June 2020', 'July 2020', 'August 2020', 'September 2020',
            'October 2020', 'November 2020', 'December 2020', 'January 2021', 'February 2021',
            'March 2021', 'April 2021', 'May 2021', 'June 2021', 'July 2021', 'August 2021'
        ]
        selected_start_date = tk.StringVar()
        selected_start_date.set("Pick A Start Date")
        menu = tk.OptionMenu(input_frame, selected_start_date, *date_options)
        menu.place(relwidth=0.34, relheight=0.45)

        selected_end_date = tk.StringVar()
        selected_end_date.set("Pick An End Date")
        menu = tk.OptionMenu(input_frame, selected_end_date, *date_options)
        menu.place(relx=0.34, relwidth=0.34, relheight=0.45)

        # Create an option menu for the user to select their occupation
        job_options = [
            'Industrial aggregate excluding unclassified businesses [11-91N] 7 8',
            'Goods producing industries [11-33N] 9',
            'Mining, quarrying, and oil and gas extraction [21]',
            'Utilities [22,221]',
            'Construction [23]',
            'Manufacturing [31-33]',
            'Service producing industries [41-91N] 11',
            'Trade [41-45N] 12',
            'Transportation and warehousing [48-49]',
            'Information and cultural industries [51]',
            'Finance and insurance [52]',
            'Real estate and rental and leasing [53]',
            'Professional, scientific and technical services [54,541]',
            'Management of companies and enterprises [55,551,5511]',
            'Administrative and support, waste management and remediation services [56]',
            'Educational services [61,611]',
            'Health care and social assistance [62]',
            'Arts, entertainment and recreation [71]',
            'Accommodation and food services [72]',
            'Other services (except public administration) [81]',
            'Public administration [91]',
        ]
        selected_job = tk.StringVar()
        selected_job.set("Pick An Occupation")
        menu = tk.OptionMenu(input_frame, selected_job, *job_options)
        menu.place(rely=0.55, relwidth=0.68, relheight=0.45)

        # Create a button to send information to test_function
        button = tk.Button(
            input_frame, text="ENTER", font=40,
            command=lambda: self.test_function(selected_start_date.get(),
                                               selected_end_date.get(), selected_job.get())
        )
        button.place(relx=0.7, relwidth=0.3, relheight=1)

    def test_function(self, start_date: str, end_date: str, occupation: str) -> None:
        """Runs functions based on output"""
        months = calculations.get_list_of_months(start_date, end_date)
        month_indexes = calculations.find_month_index(start_date, end_date, months)
        if start_date == "Pick A Date to Calculate Output on":
            self._label['text'] = 'Please Pick A Valid Start Date'

        elif end_date == "Pick A Date to Calculate Output on":
            self._label['text'] = 'Please Pick A Valid End Date'

        elif occupation == "Pick An Occupation":
            self._label['text'] = 'Please Pick A Valid Occupation'

        elif month_indexes[1] <= month_indexes[0]:
            self._label['text'] = 'Please Pick A Valid Date Range Where ' \
                                  'The End Month is After Start Month'
        else:
            a = calculations.wage_cost_gap(occupation, start_date, end_date)
            b = calculations.month_to_gap(a, start_date, end_date)
            graph.display_month_to_gap(b)
            dict_1 = calculations.get_difference(occupation, b, start_date, end_date)
            headers = ['Previous Month', 'Current Month', 'Numeric Change', 'Percentage Change']
            list_1 = []
            for x in dict_1:
                month_1 = x[0]
                month_2 = x[1]
                numeric_diff = str(round(float(dict_1[x][0])))
                percentage_change = str(round(float(dict_1[x][1])))
                list_1.append([month_1, month_2, numeric_diff, percentage_change])

            tuple_1 = calculations.start_end_difference(start_date, end_date, b)
            self._label['text'] = f"{tabulate.tabulate(list_1, headers, tablefmt='github')} " \
                                  f"\n\n\n Numeric Change: {round(tuple_1[0])} " \
                                  f"\n Percentage Change: {round(tuple_1[1])}" \
                                  f"\n Between {start_date} And {end_date}"


if __name__ == '__main__':
    import python_ta
    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()
    python_ta.check_all(config={
        'allowed-io': ['load_rent', 'load_electricity_costs', 'load_weekly_wages',
                       'load_water_rates'],
        'extra-imports': ['python_ta.contracts', 'csv', 'tkinter', 'calculations', 'graph',
                          'tabulate'],
        'max-line-length': 100,
        'max-args': 6,
        'max-locals': 25,
        'disable': ['R1705'],
    })
    Root()

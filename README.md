# COVID-19 Pandemic Impact Analysis on Housing Prices, Utilities, and Wages

This program models and visually represents the changes in housing prices, electricity costs, water expenses, and wages from 2019 to 2021 during the COVID-19 pandemic. The objective is to illustrate how the pandemic has affected these factors and particularly how it has led to a disproportionate increase in housing costs compared to the growth in wages.

## Project Overview

The program utilizes Python with Matplotlib for data visualization and Tkinter for creating a graphical user interface (GUI) to interact with the datasets. The datasets parsed and graphically represented encompass the period from 2019 to 2021, allowing users to explore and understand the significant impact of the pandemic on housing prices, utilities, and wage growth.

## Features

- **Data Analysis:** Parses and analyzes datasets representing housing prices, electricity costs, water expenses, and wages from 2019 to 2021.
- **Visualization:** Utilizes Matplotlib to create graphical representations, such as line graphs and bar charts, illustrating the trends and changes in the mentioned factors over the specified time frame.
- **GUI Interface:** Implements a Tkinter-based graphical user interface, enabling users to interact with the visualized data, zoom in/out, and explore specific data points or periods.

## How to Use

1. **Installation:**
   - Clone the repository to your local machine.
   - Ensure you have Python installed.
   - Ensure that you have Matplotlib and Tkinter packages installed

2. **Running the Program:**
   - Navigate to the project directory.
   - Run `python main.py` to start the program.

3. **Interacting with the GUI:**
   - Upon launching, the GUI will display options to select datasets and visualize specific factors.
   - Use dropdown menus or checkboxes to select specific datasets (housing prices, electricity costs, water expenses, and wages).
   - Choose visualization types (line graphs, bar charts) to represent the data changes over time.
   - Explore the interactive features to zoom in/out or navigate through the visualized data.

## Project Structure

- `main.py`: Contains the main GUI and user interaction logic.
- `load_data.py`: Loads data from various CSV files.
- `graph.py`: Generates and displays graphs.
- `calculations.py`: Performs calculations on the loaded data.

## Data Sets Used

- `average_rent.csv`
  - Contains data on average house rent for a one-bedroom apartment in Toronto. Includes monthly records from November 2019 to August 2021.
- `electricity_costs.csv`
  - Contains data on electricity rates in Toronto. Includes monthly records from November 2019 to August 2021.
- `water_rates.csv`
  - Contains data on water rates per gallon in Toronto. Includes records for different years within the period.
- `weekly_wages.csv`
  - Provides wage data across various industries in Toronto. Includes records for different industries from November 2019 to August 2021.

## License

Copyright (c) 2021 Derrick Ken Willis, Sebastian Noel Lie, Diler Zaza, and Humraj Bhoday.

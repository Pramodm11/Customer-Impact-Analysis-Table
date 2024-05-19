# Customer-Impact-Analysis-Table
## Project Description
This project is a Flask-based web application that displays a dynamic table of customer return percentages by month. The table highlights return rates with conditional formatting, helping to identify trends and alerting to high-impact return periods.

### The primary features include:

Loading customer shipment and return data from a CSV file.
Calculating monthly return percentages for each customer.
Displaying data in a tabular format with color-coded cells to indicate return rates.
Showing average return rates and impacts over recent months.
Alerting based on return rate trends.
Implementation
### Follow these steps to set up and run the application.

```Prerequisites
Python 3.x
Flask
Pandas
```
### Step-by-Step Guide
``Clone the Repository``

```
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```
### Set Up a Virtual Environment

``Set up a virtual environment to manage dependencies.``

```python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On macOS/Linux
```
### Install Dependencies

``Install the required Python packages.``

```
pip install flask pandas
```
### datasets 
##### Ensure you have a CSV file named ``dataset.csv `` in the root directory with the following 
👉click the link [datasets.csv](https://sheet.zohopublic.com/sheet/published/s3z7cc1835b27a59e42829ca3998f411c3cee?sheetid=0&range=D6)

## Run the Flask Application

``Activate your virtual environment if it's not already active and run the application:``

```
python app.py
```
### View the Application

Open your web browser and navigate to http://127.0.0.1:5000/ to see the table with conditional formatting applied.

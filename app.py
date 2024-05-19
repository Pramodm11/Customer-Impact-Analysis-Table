from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # Load and preprocess dataset
    df = pd.read_csv('dataset.csv', parse_dates=['SHIPPED DATE'], dayfirst=True)
    df['YearMonth'] = df['SHIPPED DATE'].dt.to_period('M')
    monthly_data = df.groupby(['CUSTOMER', 'YearMonth']).agg({'SHIPPED': 'sum', 'RETURN': 'sum'}).reset_index()
    monthly_data['Return_Percentage'] = (monthly_data['RETURN'] / monthly_data['SHIPPED']) * 100
    pivot_table = monthly_data.pivot(index='CUSTOMER', columns='YearMonth', values='Return_Percentage').fillna(0)
    pivot_table = pivot_table.reset_index()
    pivot_table.columns = [f'{col}' if col != 'CUSTOMER' else col for col in pivot_table.columns]
    pivot_table.columns = [str(col) for col in pivot_table.columns]
    pivot_table['Avg'] = pivot_table.iloc[:, 1:].mean(axis=1)
    pivot_table['Impact'] = pivot_table.iloc[:, -4:-1].mean(axis=1) - pivot_table.iloc[:, 1:-4].mean(axis=1)
    pivot_table['Alert'] = pivot_table['Impact'].apply(lambda x: 'High' if x > 0 else 'Low')
    data = pivot_table.to_dict(orient='records')
    months = list(pivot_table.columns[1:-3])
    
    return render_template('index.html', data=data, months=months)

if __name__ == '__main__':
    app.run(debug=True)

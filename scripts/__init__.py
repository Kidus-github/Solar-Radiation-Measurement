import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

def load_and_prepare_data(file_path):
    df = pd.read_csv(file_path)
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df.set_index('Timestamp', inplace=True)
    return df

def daily_average(df):
    daily_df = df.resample('D').mean()
    return daily_df[['GHI', 'DNI', 'DHI', 'Tamb', 'RH', 'WS', 'BP']]

def plot_ghi_trends(daily_data, region_name):
    plt.figure(figsize=(10, 6))
    plt.plot(daily_data.index, daily_data['GHI'], label=f'{region_name} (GHI)', color='blue')
    plt.title(f'Daily Average Global Horizontal Irradiance (GHI) - {region_name}')
    plt.xlabel('Date')
    plt.ylabel('GHI (W/m²)')
    plt.legend()
    plt.grid(True)
    plt.show()

def predict_solar_potential(daily_data):
    X = daily_data[['Tamb', 'RH', 'WS', 'BP']].fillna(0)  # Filling NaN values for simplicity
    y = daily_data['GHI'].fillna(0)
    
    model = LinearRegression()
    model.fit(X, y)
    
    predictions = model.predict(X)
    daily_data['Predicted_GHI'] = predictions
    
    return model, daily_data

def evaluate_region(df, region_name):
    print(f"\nAnalyzing region: {region_name}")
    daily_data = daily_average(df)
    plot_ghi_trends(daily_data, region_name)
    
    model, daily_data_with_predictions = predict_solar_potential(daily_data)
    avg_ghi = daily_data['GHI'].mean()
    print(f"Average GHI for {region_name}: {avg_ghi:.2f} W/m²")
    
    return avg_ghi, model
import pandas as pd

def analyze_results(df):
    analysis = {}

    if 'blood_pressure' in df.columns:
        bp = df['blood_pressure'].mean()
        if bp > 140:
            analysis['blood_pressure'] = "High Blood Pressure"
        elif bp < 90:
            analysis['blood_pressure'] = "Low Blood Pressure"
        else:
            analysis['blood_pressure'] = "Normal"

    if 'glucose' in df.columns:
        glucose = df['glucose'].mean()
        if glucose > 126:
            analysis['glucose'] = "Diabetic range"
        elif glucose > 100:
            analysis['glucose'] = "Pre-diabetic range"
        else:
            analysis['glucose'] = "Normal"

    # Add more medical indicators as needed
    return analysis

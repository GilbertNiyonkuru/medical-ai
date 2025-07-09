def generate_recommendations(analysis):
    recommendations = []

    if 'blood_pressure' in analysis:
        status = analysis['blood_pressure']
        if status == "High Blood Pressure":
            recommendations.append("Recommend antihypertensive medication and dietary sodium reduction.")
        elif status == "Low Blood Pressure":
            recommendations.append("Increase fluid intake and consider medications to raise blood pressure.")

    if 'glucose' in analysis:
        status = analysis['glucose']
        if status == "Diabetic range":
            recommendations.append("Start insulin therapy and lifestyle modification.")
        elif status == "Pre-diabetic range":
            recommendations.append("Encourage exercise and low-sugar diet.")

    return recommendations

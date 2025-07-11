import requests
from fpdf import FPDF

API_KEY = '13cef7bcf1963e5c9983c1b643a78d52'
CITIES = ['Pune', 'Mumbai', 'Delhi', 'Kolkata', 'Chennai']
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

# Collect data
weather_data = []

for city in CITIES:
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        entry = {
            'City': city,
            'Temperature': f"{data['main']['temp']} °C",
            'Humidity': f"{data['main']['humidity']}%",
            'Description': data['weather'][0]['description'].title()
        }
        weather_data.append(entry)
    else:
        print(f"Error fetching data for {city}")

# Create PDF Report
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 10, "Weather Report - ELiteTEch Internship Task 2", ln=True, align='C')

pdf.ln(10)
pdf.set_font("Arial", size=12)

for entry in weather_data:
    pdf.cell(0, 10, f"City: {entry['City']}", ln=True)
    pdf.cell(0, 10, f"  Temperature: {entry['Temperature']}", ln=True)
    pdf.cell(0, 10, f"  Humidity: {entry['Humidity']}", ln=True)
    pdf.cell(0, 10, f"  Description: {entry['Description']}", ln=True)
    pdf.ln(5)

# Save the file
pdf.output("weather_report.pdf")
print("✅ PDF generated as weather_report.pdf")

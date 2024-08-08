import requests
from datetime import datetime

# Get the weather data from the API
result = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat=25.606551&lon=85.163107&appid=b5b5f162c990bbda468cf71bf19b5d16&units=metric")
data = result.json()

# Get today's date in the format 'YYYY-MM-DD'
today = datetime.now().strftime('%Y-%m-%d')

# Initialize variables to store min and max temperature and descriptions
min_temp = float('inf')
max_temp = float('-inf')
descriptions = []

# Filter data for the current day and find min, max temperatures, and descriptions
for item in data['list']:
    dt_txt = item['dt_txt']
    date = dt_txt.split(' ')[0]
    
    if date == today:
        temp_min = item['main']['temp_min']
        temp_max = item['main']['temp_max']
        description = item['weather'][0]['description']
        
        if temp_min < min_temp:
            min_temp = temp_min
        
        if temp_max > max_temp:
            max_temp = temp_max
        
        descriptions.append(description)

if min_temp == float('inf') or max_temp == float('-inf'):
    print("No temperature data available for today.")
else:
    print(f"Today's minimum temperature: {min_temp}°C")
    print(f"Today's maximum temperature: {max_temp}°C")
    print(f"Weather descriptions for today: {', '.join(set(descriptions))}")

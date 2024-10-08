import pandas as pd
import folium
from folium.plugins import HeatMap

# Read the CSV file
df = pd.read_csv('anonymized-taxi-data.csv')

# Ensure the 'StartDateTime' column is in datetime format
df['StartDateTime'] = pd.to_datetime(df['StartDateTime'])

# Function to generate a heatmap for a specific time period
def generate_heatmap(start_time, end_time):
    # Filter the dataframe by the provided time period
    filtered_df = df[(df['StartDateTime'] >= pd.to_datetime(start_time)) & (df['StartDateTime'] <= pd.to_datetime(end_time))]

    # Ensure there are no missing or invalid lat/lon values
    filtered_df = filtered_df.dropna(subset=['StartLat', 'StartLon'])

    # Convert the filtered DataFrame into a list of lists for the HeatMap
    heat_data = filtered_df[['StartLat', 'StartLon']].values.tolist()

    # Initialise the map centered on Dubai
    dubai_map = folium.Map(location=[25.276987, 55.296249], zoom_start=12)

    # Add heatmap layer to the map
    HeatMap(heat_data, radius=10, max_zoom=13).add_to(dubai_map)

    # Save the map to an HTML file
    dubai_map.save('templates/taxi_heatmap.html')

# Example of user input for start and end time
# start_time = '2024-03-12T00:00:00Z'
# end_time = '2024-03-12T01:00:00Z'

print("Welcome to the Dubai Taxi Activity Heatmap!")
print("You are allowed to check the heatmap for a specific time period on March 12th, 2024.")

try:
    start_input = int(input("Enter the start time less than 24 in integer form: "))
    if start_input < 0 or start_input >= 24:
        print("Invalid input. Please enter a valid start time.")
    else:
        end_input = int(input("Enter the end time less than 24 in integer form: "))
        if end_input < 0 or end_input >= 24 or end_input <= start_input:
            print("Invalid input. Please enter a valid end time.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")

timestamp = '2024-03-12T00:00:00Z'

if start_input < 10:
    start_time = timestamp[:11] + '0' + str(start_input) + timestamp[13:]
else:
    start_time = timestamp[:11] + str(start_input) + timestamp[13:]

if end_input < 10:
    end_time = timestamp[:11] + '0' + str(end_input) + timestamp[13:]
else:
    end_time = timestamp[:11] + str(end_input) + timestamp[13:]

print(f"Generating heatmap for trips between {start_time} and {end_time}...")

# Call the function with the user input
generate_heatmap(start_time, end_time)

print(f"Heatmap generated for trips between {start_time} and {end_time}.")
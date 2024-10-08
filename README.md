# Dubai Taxi Heatmap Visualization

This project generates an interactive heatmap that visualises taxi trips in Dubai using GPS data. It allows users to filter trips by a specific time period and then visualise the density of taxi trips on a map.

#### Authors
**The Visioneers**  
Adham Sameh, Amir Hossein Kazemkhani, [Hongbo Wei](https://github.com/hongbo-wei), Pouya Abikari, Youssef Abdelsalam

## Features

- Visualise taxi trip density in Dubai on an interactive map.
- Filter trips by a custom time range.
- Outputs the heatmap as an HTML file for easy viewing.

## Dataset

The input dataset is a CSV file (`anonymized-taxi-data.csv`) containing the following columns:

- `StartDateTime`: Start time of the trip in ISO 8601 format.
- `StartLat`: Latitude of the trip's starting location.
- `StartLon`: Longitude of the trip's starting location.
- `EndDateTime`: End time of the trip in ISO 8601 format.
- `EndLat`: Latitude of the trip's end location.
- `EndLon`: Longitude of the trip's end location.
- `Distance`: Distance travelled during the trip in kilometres.
- `vehicle_id`: Anonymized ID of the taxi.

## Requirements

- Python 3.11
- Libraries:
  - `pandas`
  - `folium`
  - `folium.plugins.HeatMap`
  - `Django`

Install the required packages using pip:

1. **Install dependencies**  
   ```bash
   pipenv shell
   pipenv install
   ```

2. **Run the server**  
   ```bash
   python manage.py runserver
   ```

---

![Team Photo](static/images/the-visioneers.jpg)

😁 **Thank you for your interest in The Visioneers!**

---

© 2023-2049 [Hongbo Wei](https://github.com/hongbo-weia)

[![CC BY 4.0][cc-by-image]][cc-by]

This work is licensed under a [Creative Commons Attribution 4.0 International License][cc-by].

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

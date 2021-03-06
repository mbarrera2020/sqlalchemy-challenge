# sqlalchemy-challenge

Author: Maria Barrera
Date: 02/28/2021
Description:  Python and SQLAlchemy to do basic climate analysis and data exploration of a climate database.

### Step 1:  Climate Analysis and Exploration

Ref file:  climate_mainPy.ipynb

The following analysis are completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.
1) Using Jupyter notebook and hawaii.sqlite files to complete climate analysis and data exploration.
2) Using SQLAlchemy to create_engine to connect to the sqlite database.
3) Using SQLAlchemy automap_base() to reflect the tables into classes and save a reference to those classes called Station and Measurement.
4) Linking Python to the database by creating an SQLAlchemy session.

#### Precipitation Analysis

Find the most recent date in the data set.
Using this date, retrieve the last 12 months of precipitation data by querying the 12 preceding months of data. 
Select only the date and prcp values.
Load the query results into a Pandas DataFrame and set the index to the date column.
Sort the DataFrame values by date.
Plot the results using the DataFrame plot method.

#### Station Analysis
Design a query to calculate the total number of stations in the dataset.
Design a query to find the most active stations (i.e. which stations have the most rows?).
List the stations and observation counts in descending order.
Which station id has the highest number of observations?
Using the most active station id, calculate the lowest, highest, and average temperature.
    Functions to use in queries: func.min, func.max, func.avg, and func.count 
Design a query to retrieve the last 12 months of temperature observation data (TOBS).
Filter by the station with the highest number of observations.
Query the last 12 months of temperature observation data for this station.
Plot the results as a histogram with bins=12.


### Step 2:  Climate App

Ref file:  ClimateApp.py

Design a Flask API based on the queries that you have just developed.
Use Flask to create routes.

Routes:
/
Home page.
List all routes that are available.

/api/v1.0/precipitation
Convert the query results to a dictionary using date as the key and prcp as the value.
Return the JSON representation of your dictionary.

/api/v1.0/stations
Return a JSON list of stations from the dataset.

/api/v1.0/tobs
Query the dates and temperature observations of the most active station for the last year of data.
Return a JSON list of temperature observations (TOBS) for the previous year.

/api/v1.0/<start> and /api/v1.0/<start>/<end>
Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.

#### Bonus: Other Recommended Analyses

Temperature Analysis I
Ref file:  temp_analysis_bonus1_py.ipynb
    
Hawaii is reputed to enjoy mild weather all year. Is there a meaningful difference between the temperature in, for example, June and December?
Use pandas to perform this portion.
Convert the date column format from string to datetime.
Set the date column as the DataFrame index
Drop the date column
Identify the average temperature in June at all stations across all available years in the dataset. Do the same for December temperature.
Use the t-test to determine whether the difference in the means, if any, is statistically significant. 


Temperature Analysis II
Ref file:  temp_analysis_bonus2_py.ipynb

Looking to take a trip from August first to August seventh of this year, but are worried that the weather will be less than ideal. 
Using historical data in the dataset find out what the temperature has previously looked like.

Use a function called calc_temps that will accept a start date and end date in the format %Y-%m-%d. The function will return the minimum, average, and maximum temperatures for that range of dates.

Use the calc_temps function to calculate the min, avg, and max temperatures for your trip using the matching dates from a previous year (i.e., use "2017-08-01").

Plot the min, avg, and max temperature from your previous query as a bar chart.
Use "Trip Avg Temp" as the title.
Use the average temperature as the bar height (y value).
Use the peak-to-peak (TMAX-TMIN) value as the y error bar (YERR).

Daily Rainfall Average
Calculate the rainfall per weather station using the previous year's matching dates.
Sort this in descending order by precipitation amount and list the station, name, latitude, longitude, and elevation.
Calculate the daily normals. Normals are the averages for the min, avg, and max temperatures. 
Use a function called daily_normals that will calculate the daily normals for a specific date. This date string will be in the format %m-%d. Use all historic TOBS that match that date string.
Set the start and end date of the trip.
Use the date to create a range of dates.
Strip off the year and save a list of strings in the format %m-%d.
Use the daily_normals function to calculate the normals for each date string and append the results to a list called normals.
Load the list of daily normals into a Pandas DataFrame and set the index equal to the date.
Use Pandas to plot an area plot (stacked=False) for the daily normals.
    
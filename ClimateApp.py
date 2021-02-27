#################################################
# ClimateApp.py 
# Author: Maria Barrera
# Date: 02/27/2021
#################################################

# 1. import Flask & jsonify
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

sqlpath = "sqlite:///Resources/hawaii.sqlite"

#################################################
# Database Setup
#################################################

#engine = create_engine("sqlite:///Resources/hawaii.sqlite")
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
# 2. Create an app, being sure to pass __name__
app = Flask(__name__)

#######################################################
# Flask Routes
#######################################################
# Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return (
        f"<br/>"
        f"Welcome to the Climate App Home page! <br/>"
        f"<br/>"
        f"The following routes are available: <br/>"
        f"/api/v1.0/precipitation <br/>"
        f"/api/v1.0/stations <br/>"
        f"/api/v1.0/tobs <br/>"
        f"/api/v1.0/<start> <br>"
        f"/api/v1.0/<start>/<end> <br/>"
        )

##########################################################################################
# Define what to do when a user hits the /api/v1.0/precipitation route
# Convert the query results to a dictionary using date as the key and prcp as the value.
# Return the JSON representation of your dictionary.
##########################################################################################
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    print("Server received request for 'precipitation' page...")
    """Return measurement (precipitation) data as json"""
    # Query all measurements
    results = session.query(Measurement.date, Measurement.prcp).all()
    
    session.close()

    # Create a dictionary from the row data and append to a list of all_prcp
    all_prcp = []
    for date, prcp in results:
        prcp_dict={}
        prcp_dict["date"] = date
        prcp_dict["prcp"] = prcp
        all_prcp.append(prcp_dict)

    return jsonify(all_prcp)

##########################################################################################
# Define what to do when a user hits the /api/v1.0/stations route
# Return a JSON list of stations from the dataset.
##########################################################################################
@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    print("Server received request for 'stations' page...")
    """Return stations data as json"""
    # Query all stations
    results = session.query(Station.station, Station.name, Station.latitude, 
                Station.longitude, Station.elevation).all()
    
    session.close()

    # Create a dictionary from the row data and append to a list of all_stations
    all_stations = []
    for station, name, latitude, longitude, elevation in results:
        station_dict={}
        station_dict["station"] = station
        station_dict["name"] = name
        station_dict["latitude"] = latitude
        station_dict["longitude"] = longitude
        station_dict["elevation"] = elevation
        all_stations.append(station_dict)

    return jsonify(all_stations)

####################################################################################################
# Define what to do when a user hits the /api/v1.0/tobs route
# Query the dates and temperature observations of the most active station for the last year of data.
# Return a JSON list of temperature observations (TOBS) for the previous year.
####################################################################################################


####################################################################################################
# Define what to do when a user hits the /api/v1.0/<start> route
# Return a JSON list of the minimum temperature, the average temperature, and the max temperature 
#   for a given start or start-end range.
# When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal 
#   to the start date.
####################################################################################################


####################################################################################################
# Define what to do when a user hits the /api/v1.0/<start>/<end> route
# Return a JSON list of the minimum temperature, the average temperature, and the max temperature 
#   for a given start or start-end range.
# When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between 
# the start and end date inclusive.
####################################################################################################


if __name__ == "__main__":
    app.run(debug=True)

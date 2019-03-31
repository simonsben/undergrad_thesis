# Data formats

## Source
* `routes.dat`
    * Airline 
    * Airline ID
    * Source airport
    * Source airport ID 
    * Destination airport 
    * Destination airport ID 
    * Codeshare 
    * Stops 
    * Equipment
* `airports.dat`
    * Airport ID 
    * Name
    * City
    * Country or territory
    * IATA
    * ICAO
    * Latitude
    * Longitude
    * Altitude
    * Timezone
    * DST
    * Tz
    * Type
    * Source
* `openflights*.png`
    * These two files are visualizations of the data in `airports.dat` and `routes.dat`
    * NOTE: They are directly from the the [source](https://openflights.org/data.html)
    
## Results

* `budget_impact`, `centrality_metrics`, `max_entropy`
    * Each column is the performance of the strategy listed in the header
    * For max_entropy the betweeness centrality based heuristic was used 
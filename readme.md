# Vehicle Simulator

#Prereqs
- Python 3.*
- Install Requirments
```
pip install -r requirements.text
```


### V-simmy Anatomy
├── docs
│   ├── api_keys.txt bad idea but all api keys for google maps
│   └── rd_notes.txt general notes during rearch.
├── libs
│   ├── DataUtils.py all this class will store all Database/REST/other
│   ├── GeoUtils.py adtraction of polyline to decode/encode polylines
│   ├── GoogleUtils.py Helper Class to make calls to Places/Directions API
│   ├── PlacesUtils.py Helper Calss to get supported_place, counties and states
│   ├── RouteUtils.py Helper Class to get vvaried payloads.
│   ├── VehicleEmuDriver.py This is the Vehicle Class all logic of sim is here.
│   └── data
│       ├── countries.p a list of contries PlacesUtils uses this data
│       ├── places.p a list of supported_place  PlaceUtil uses this data
│       └── states.p a list of states PlaceUtil uses this data
├── readme.md you are currently reading this file.
├── requirements.txt s list of all requirements needed to run this tool.
└── start_sim.py the main contructor to trigger sim ```python start_sim.py N```.

### Basic  Breakdown of Simulator
I attempted to create a loop route by making two api calls
 the fist call is org=add1 dest=add2 and making a second call flipping the org, and dest I then collect all the steps into one list , the sim will take the steps and create a pause using the duration information in the steps. when the sim has completed the from -> two I print the (from) and (to) details to the screen along with a post call to a simple rest endpoint to assert a json POST call is being made to the endpoint.

 ### Pros & Cons
 #### Pros
 * You can create a realitic payload based on time, you can observe the performance of your infrastructure as you scale the workers up.

#### Cons
* It is time based so if the route takes several hours, each v-sim may take along time to run.

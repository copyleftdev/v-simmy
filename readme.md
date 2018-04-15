# Vehicle Simulator

#Prereqs
- Python 3.*
- Install Requirments
```
pip install -r requirements.text
```


### V-simmy Anatomy
```
├── docs
│   ├── api_keys.txt bad idea but all api keys for google maps
│   └── rd_notes.txt general notes during rearch.
├── libs
│   ├── DataUtils.py all this class will store all Database/REST/other
│   ├── GeoUtils.py adtraction of polyline to decode/encode polylines
│   ├── GoogleUtils.py Helper Class to make calls to Places/Directions API
│   ├── PlacesUtils.py Helper Class to get supported_place, counties and states
│   ├── PerfUtils.py Helper Nothing in it , but can be developed to start collecting performance information from the infrastructure.
│   ├── RouteUtils.py Helper Class to get vvaried payloads.
│   ├── VehicleEmuDriver.py This is the Vehicle Class all logic of sim is here.
│   └── data
│       ├── countries.p a list of contries PlacesUtils uses this data
│       ├── places.p a list of supported_place  PlaceUtil uses this data
│       └── states.p a list of states PlaceUtil uses this data
├── readme.md you are currently reading this file.
├── requirements.txt s list of all requirements needed to run this tool.
└── start_sim.py the main contructor to trigger sim ```python start_sim.py N```.
```
### Basic  Breakdown of Simulator
I attempted to create a loop route by making two api calls
 the fist call is org=add1 dest=add2 and making a second call flipping the org, and dest I then collect all the steps into one list , the sim will take the steps and create a pause using the duration information in the steps. when the sim has completed the from -> two I print the (from) and (to) details to the screen along with a post call to a simple rest endpoint to assert a json POST call is being made to the endpoint.


 #### Sample output:
 ```
 {'sim_id': 'vehicle-04afc851-b49f-4547-8986-8d0d79b12bb0', 'from_address': 'Tengoku Ramen Bar, 815, West Naomi Avenue, Arcadia, Los Angeles County, California, 91007, United States of America', 'from_cord': [34.1236612, -118.0577511], 'from_time': '2018-04-14T23:49:12.365730+00:00', 'instruction': 'Head <b>west</b> on <b>W Naomi Ave</b>'}
{'sim_id': 'vehicle-04afc851-b49f-4547-8986-8d0d79b12bb0', 'to_address': '1200, Golden West Avenue, Arcadia, Los Angeles County, California, 91007, United States of America', 'to_cord': [34.1233689, -118.0598067], 'to_time': '2018-04-14T23:49:12.365730+00:00', 'elapsed': 'a minute ago'}
{'sim_id': 'vehicle-04afc851-b49f-4547-8986-8d0d79b12bb0', 'from_address': '1200, Golden West Avenue, Arcadia, Los Angeles County, California, 91007, United States of America', 'from_cord': [34.1233689, -118.0598067], 'from_time': '2018-04-14T23:49:58.770000+00:00', 'instruction': 'Turn <b>right</b> onto <b>S Golden W Ave</b>'}
{'sim_id': 'vehicle-04afc851-b49f-4547-8986-8d0d79b12bb0', 'to_address': 'Valero, Duarte Road, Arcadia, Los Angeles County, California, 91007, United States of America', 'to_cord': [34.1253124, -118.0601631], 'to_time': '2018-04-14T23:49:58.770000+00:00', 'elapsed': 'a minute ago'}
{'sim_id': 'vehicle-04afc851-b49f-4547-8986-8d0d79b12bb0', 'from_address': 'Valero, Duarte Road, Arcadia, Los Angeles County, California, 91007, United States of America', 'from_cord': [34.1253124, -118.0601631], 'from_time': '2018-04-14T23:50:58.337982+00:00', 'instruction': 'Turn <b>right</b> onto <b>W Duarte Rd</b>'}
{'sim_id': 'vehicle-04afc851-b49f-4547-8986-8d0d79b12bb0', 'to_address': '701, Duarte Road, Arcadia, Los Angeles County, California, 91007, United States of America', 'to_cord': [34.1260823, -118.0549487], 'to_time': '2018-04-14T23:50:58.337982+00:00', 'elapsed': 'a minute ago'}
{'sim_id': 'vehicle-04afc851-b49f-4547-8986-8d0d79b12bb0', 'from_address': '701, Duarte Road, Arcadia, Los Angeles County, California, 91007, United States of America', 'from_cord': [34.1260823, -118.0549487], 'from_time': '2018-04-14T23:52:19.700777+00:00', 'instruction': 'Turn <b>right</b> onto <b>S Baldwin Ave</b><div style="font-size:0.9em">Destination will be on the right</div>'}
{'sim_id': 'vehicle-04afc851-b49f-4547-8986-8d0d79b12bb0', 'to_address': '701, West Naomi Avenue, Arcadia, Los Angeles County, California, 91007, United States of America', 'to_cord': [34.1241898, -118.055062], 'to_time': '2018-04-14T23:52:19.700777+00:00', 'elapsed': 'seconds ago'}
{'sim_id': 'vehicle-04afc851-b49f-4547-8986-8d0d79b12bb0', 'from_address': '701, West Naomi Avenue, Arcadia, Los Angeles County, California, 91007, United States of America', 'from_cord': [34.1241898, -118.055062], 'from_time': '2018-04-14T23:52:55.070966+00:00', 'instruction': 'Head <b>south</b> on <b>S Baldwin Ave</b> toward <b>W Naomi Ave</b>'}
{'sim_id': 'vehicle-04afc851-b49f-4547-8986-8d0d79b12bb0', 'to_address': '701, West Naomi Avenue, Arcadia, Los Angeles County, California, 91007, United States of America', 'to_cord': [34.1240364, -118.0550733], 'to_time': '2018-04-14T23:52:55.070966+00:00', 'elapsed': 'just now'}
{'sim_id': 'vehicle-04afc851-b49f-4547-8986-8d0d79b12bb0', 'from_address': '701, West Naomi Avenue, Arcadia, Los Angeles County, California, 91007, United States of America', 'from_cord': [34.1240364, -118.0550733], 'from_time': '2018-04-14T23:52:58.714806+00:00', 'instruction': 'Turn <b>right</b> at the 1st cross street onto <b>W Naomi Ave</b><div style="font-size:0.9em">Destination will be on the left</div>'}
{'sim_id': 'vehicle-04afc851-b49f-4547-8986-8d0d79b12bb0', 'to_address': 'Tengoku Ramen Bar, 815, West Naomi Avenue, Arcadia, Los Angeles County, California, 91007, United States of America', 'to_cord': [34.1236612, -118.0577511], 'to_time': '2018-04-14T23:52:58.714806+00:00', 'elapsed': 'a minute ago'}
 ```

 ### Pros & Cons
 #### Pros
 * You can create a realitic payload based on time, you can observe the performance of your infrastructure as you scale the workers up.

#### Cons
* It is time based so if the route takes several hour's, each v-sim may take along time to run.



### Load Test Strategy from within the sim
In this case the load testing would have to be conducted from the simulator outward.
* Generate a load of users each sim would need to connect to a given real endpoint, database, etc.
* there is a stubbed out class in libs named PerfUtils , it would have several  functions designed to capture the performance
* of the above resource types a the sim was running.

### Load Test Strategy from outside the sim
Traditionally load tests are conducted on  a body of systems [web servers, endpoint , db].
* a baseline would need to be established from production average load.
* a test plan for [Stress, Spike, Endurance, Scalability, and Volume] would need to be developed.


## Refactoring
This is a poc , it will not scale well. I would use the following tech stack to
make sure the sim could scale.
* Language : Golang ,  RabbitMQ, using Worker queues(competing consumer pattern)
* Currently this poc makes calls  to google, it stops working when  you burn you're daily call rate limit. I would rather use the calls to do a daily collection of Places, Directions and cache them, over time I would have a pretty nice set of data to run sims with.


## Things I learned in this exercise
* "geo" ain't easy.
* I have allot to learn about Geospatial Development, I bought a few book's after  doing this exercise.

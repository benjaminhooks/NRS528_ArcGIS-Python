## **Feature Impacts Python Toolbox**


This toolbox consists of 4 separate scripts that can be utilized individually or within a workflow. 
As a whole, the scripts within this toolbox are useful for quickly calculating impacts from sea level rise dataset, which is documented below.
The scripts can be utilized outside of this function, and can be used to quickly process data how the user sees fit. 

The 4 scripts and their intended uses are;

* Data Projection - To ensure accurate end results, the user should project their datasets into the relevant coordinate system for the study area.

* Buffer - Buffer the sea level rise data to a specified amount. The SLR data used within this project was documented as polylines (to show the roads being impacted by SLR.)
By buffering the SLR data out to different points, were are able to calculate the amount of features affected given different circumstances. 

* Clip - Clip the data to be analyzed by the buffered SLR data. 

* Calculate Statistics - Calculate statistics based on user input. Examples include summing the affected area, 
determining the amount of unique/total structures affected, or the average amount for a specific parameter. 
Input the desired parameter to be analyzed. Output will be a .dbf file that can be viewed within ArcGIS


## **Determining Impacts from Sea Level Rise**

The follwing instructions and images is a specific workflow utilizing this toolbox to determine the population impacts due to SLR in Rhode Island

Due to the data being buffered by a user defined amount, the data needs to be projected for the correct results. 

![Image](https://github.com/benjaminhooks/NRS528_ArcGIS-Python/blob/main/Assignments/Python%20Toolbox/images/1.png?raw=true)
![Image](https://github.com/benjaminhooks/NRS528_ArcGIS-Python/blob/main/Assignments/Python%20Toolbox/images/2.png?raw=true)

The images above show the sea level rise being projected

Next is to buffer the areas. For this example, a buffer distance of 100 feet is chose to simulate the risen water around impact zones designated by the state.
The user has an option to use meters or feet in this toolbox. The input should be based upon the earlier projection. In this example, US State Plane FIPS Feet 
was chosen, so feet was used for the buffer. 

![Image](https://github.com/benjaminhooks/NRS528_ArcGIS-Python/blob/main/Assignments/Python%20Toolbox/images/3.png?raw=true)
![Image](https://github.com/benjaminhooks/NRS528_ArcGIS-Python/blob/main/Assignments/Python%20Toolbox/images/4.png?raw=true)

Next is to clip the study area. For this example, the RI State Census data was used since we are going to calculate the population being impacted. 

![Image](https://github.com/benjaminhooks/NRS528_ArcGIS-Python/blob/main/Assignments/Python%20Toolbox/images/5.png?raw=true)
![Image](https://github.com/benjaminhooks/NRS528_ArcGIS-Python/blob/main/Assignments/Python%20Toolbox/images/6.png?raw=true)

After the study area has been clipped, we can start to perform light statistical analysis upon the shapefile. As stated previously, we are going to calculate 
population impact. The user should look into the attribute table within ArcGIS for the study area to find the appropriate field. For this file, the "POP1" field
will allow us to sum the popualation. 

![Image](https://github.com/benjaminhooks/NRS528_ArcGIS-Python/blob/main/Assignments/Python%20Toolbox/images/8.png?raw=true)
![Image](https://github.com/benjaminhooks/NRS528_ArcGIS-Python/blob/main/Assignments/Python%20Toolbox/images/7.png?raw=true)

Once the appropirate field has been established, the calculate statistics script can be performed.

![Image](https://github.com/benjaminhooks/NRS528_ArcGIS-Python/blob/main/Assignments/Python%20Toolbox/images/9.png?raw=true)
![Image](https://github.com/benjaminhooks/NRS528_ArcGIS-Python/blob/main/Assignments/Python%20Toolbox/images/10.png?raw=true)

Using the POP1 and SUM parameters, we will get a .dbf output with the output statistic. 

![Image](https://github.com/benjaminhooks/NRS528_ArcGIS-Python/blob/main/Assignments/Python%20Toolbox/images/11.png?raw=true)

Shown above, we see that a total of up to 154661 people could be affected. Due to vector data not splitting the population of specific OBJECTID's, this number represents
the "worst case" of population affected from the 100 buffer zone. 

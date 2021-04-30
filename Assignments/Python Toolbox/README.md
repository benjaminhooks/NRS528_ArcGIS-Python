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

Due to the data being buffered by a user defined amount, the data needs to be projected for the correct results. 

![Banner Image](/images/1.png?raw=true)

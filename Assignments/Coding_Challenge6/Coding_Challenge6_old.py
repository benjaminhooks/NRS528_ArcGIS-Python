
#####
# Step 3 - Python Script from Tools
#####

# NOTE THAT THIS TASK IS ALSO YOUR CODING CHALLENGE THIS WEEK, I DO NOT EXPECT US TO COMPLETE THIS IN CLASS.

# Task 1 - Use what you have learned to process the Landsat files provided, this time, you know you are
# interested in the NVDI index which will use Bands 4 (red, aka vis) and 5 (near-infrared, aka nir) from the
# Landsat 8 imagery. Data provided are monthly (a couple are missing due to cloud coverage) during the
# year 2015 for the State of RI.

# Before you start, here is a suggested workflow:

# 1) Extract the Step_3_data.zip file into a known location.
# 2) For each month provided, you want to calculate the NVDI, using the equation: nvdi = (nir - vis) / (nir + vis)
# https://en.wikipedia.org/wiki/Normalized_difference_vegetation_index. Consider using the Raster Calculator Tool
# in ArcMap and using "Copy as Python Snippet" for the first calculation.

# The only rule is, you should run your script once, and generate the NVDI for ALL MONTHS provided. As part of your
# code submission, you should also provide a visualization document (e.g. an ArcMap layout), showing the patterns for
# an area of RI that you find interesting.

import arcpy, os


listMonths = ["02", "04", "05", "07", "10", "11"]
outputDirectory = r"C:\NRS 528\Classes\06_Cheating\Step_3_Data"
if not os.path.exists(outputDirectory):
    os.mkdir(outputDirectory)

for month in listMonths:
    arcpy.env.workspace = r"C:\NRS 528\Classes\06_Cheating\Step_3_data\2015" + str(month)
    listRasters = arcpy.ListRasters("*", "TIF")
    # print(listRasters)

    # output_raster = arcpy.ia.RasterCalculator(' ("LC08_L1TP_012031_20150201_20170301_01_T1_B5.tif" - "LC08_L1TP_012031_20150201_20170301_01_T1_B4.tif") /  ("LC08_L1TP_012031_20150201_20170301_01_T1_B5.tif" + "LC08_L1TP_012031_20150201_20170301_01_T1_B4.tif")'); output_raster.save(r"C:\NRS 528\Classes\06_Cheating\Step_3_Data\nvdi_201502")
# Here is the copied Python snippet from ArcGIS that I used as the template. Tried to integrate some of the file writing code from last class into the code below, not sure if its correct
    
    listRasters = [x for x in listRasters if "BQA" not in x]
    listRasters = [x for x in listRasters if "B1" not in x]
    listRasters = [x for x in listRasters if "B2" not in x]
    listRasters = [x for x in listRasters if "B3" not in x]
    listRasters = [x for x in listRasters if "B6" not in x]
    listRasters = [x for x in listRasters if "B7" not in x]
    listRasters = [x for x in listRasters if "B8" not in x]
    listRasters = [x for x in listRasters if "B9" not in x]
    listRasters = [x for x in listRasters if "B10" not in x]
    listRasters = [x for x in listRasters if "B11" not in x]
    print(listRasters)
# Excuse this messy code, still trying to figure out how to extract B4 and B5 into the list, and this seemed to work in the meantime



arcpy.ia.RasterCalculator(' ("listRasters[1]" - "listRasters[0]") / ("listRasters[1]" + "listRasters[0]")'); os.path.join(outputDirectory, r"2015" + str(month) + "_NDVI.tif")

# Getting error TypeError: RasterCalculator() missing 2 required positional arguments: 'input_names' and 'expression' after running. Pycharm indicates
# that RasterCalculator requires 'input names' and 'expression' in the tool, but the copied code from ArcGIS does not have these parameters, and also
# seemed to get the same error when I run the tool on line 37. Correct tool, or try something else? Worked in ArcGIS, succesfully created an NDVI layer from the first month.  

# Do we need to perform the function using RasterCalculator? My googling led me to many examples using 'rasterio' and 'numpy' tools. I'm sure it is possible to do the NDVI  calculation 
# without these, but would it be ok to explore these tools? Or do you think these advanced tools would lead to further issues?

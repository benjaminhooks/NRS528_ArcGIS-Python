
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
outputDirectory = r"C:\Data\Students_2021\1_Data"
if not os.path.exists(outputDirectory):
    os.mkdir(outputDirectory)

for month in listMonths:
    arcpy.env.workspace = os.path.join(outputDirectory, "2015" + str(month))
    listRasters = arcpy.ListRasters("*", "TIF")
    # print(listRasters)

    # output_raster = arcpy.ia.RasterCalculator(' ("LC08_L1TP_012031_20150201_20170301_01_T1_B5.tif" - "LC08_L1TP_012031_20150201_20170301_01_T1_B4.tif") /  ("LC08_L1TP_012031_20150201_20170301_01_T1_B5.tif" + "LC08_L1TP_012031_20150201_20170301_01_T1_B4.tif")'); output_raster.save(r"C:\NRS 528\Classes\06_Cheating\Step_3_Data\nvdi_201502")
# Here is the copied Python snippet from ArcGIS that I used as the template. Tried to integrate some of the file writing code from last class into the code below, not sure if its correct

    #simplified by removing not.
    listRasterRed = [x for x in listRasters if "B4" in x]
    listRasterNIR = [x for x in listRasters if "B5" in x]

# Excuse this messy code, still trying to figure out how to extract B4 and B5 into the list, and this seemed to work in the meantime

    print(listRasterRed)
    print(listRasterNIR)

    #arcpy.ia.RasterCalculator(' ("listRasters[1]" - "listRasters[0]") / ("listRasters[1]" + "listRasters[0]")'); os.path.join(outputDirectory, r"2015" + str(month) + "_NDVI.tif")

# For the last decade I've had no issues with Raster Calculator, but there appears to be an error from ESRI
# the code you extract from ModelBuilder/Toolbox WILL NOT WORK in Python. Do not ask me why, I think they
# have depreciated raster calculator and not told anyone, nor did they update model builder. The below
# is the solution, which I had to find through a lot of googling:

    from arcpy.sa import * # Should be at the top of the file, btu shown here for congruency in edits.

    output_raster = (Raster(listRasterNIR) - Raster(listRasterRed)) / (Raster(listRasterNIR) + Raster(listRasterRed))
    output_raster.save(os.path.join(outputDirectory, "2015" + str(month) + "_NDVI.tif"))
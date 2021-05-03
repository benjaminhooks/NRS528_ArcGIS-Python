# Code from challenge 5, but with a function that is called upon to describe shapefile parameters and perform analysis
import arcpy
from arcpy import env
arcpy.env.overwriteOutput = True

env.workspace = r"C:\NRS_528\Assignment8"

# Function to describe shapefile

def describe_shp(inFeatures):
    desc = arcpy.Describe(inFeatures)
    print("Describing: " + str(inFeatures))
    if arcpy.Exists(inFeatures):
        if desc.dataType == "ShapeFile":
            print("Feature Type:  " + desc.shapeType)
            print("Coordinate System Type:  " + desc.spatialReference.type)
            print("Coordinate System used:  " + desc.spatialReference.GCSName)
        else:
            print("Input data not ShapeFile..")
    else:
        print("Dataset not found, please check the file path..")

# Function to create thiessen polygons

def thiessen_poly(inFeatures):
    desc = arcpy.Describe(inFeatures)
    print("Creating thiessen polygons from : " + str(inFeatures))
    if arcpy.Exists(inFeatures):
        if desc.dataType == "ShapeFile":

            inFeatures = "Emergency_Medical_Services.shp"
            outFeatureClass = "EMS_Thiessen"
            outFields = "ALL"

            arcpy.CreateThiessenPolygons_analysis(inFeatures, outFeatureClass, outFields)
        else:
            print("Input data not ShapeFile..")
    else:
        print("Dataset not found, please check the file path..")

# Function to clip to RI study area

def clip_shapefile(inFeatures):
    desc = arcpy.Describe(inFeatures)
    print("Clipping shapefile")
    if arcpy.Exists(inFeatures):
        if desc.dataType == "ShapeFile":

            inFeatures = "EMS_Thiessen.shp"
            clip_features = "Municipalities__1997_.shp"
            out_feature_class = "EMS_Thiessen_riclipped"

            arcpy.Clip_analysis(inFeatures, clip_features, out_feature_class)
        else:
            print("Input data not ShapeFile..")
    else:
        print("Dataset not found, please check the file path..")

# Calling upon functions

describe_shp(env.workspace + "/Municipalities__1997_.shp")
describe_shp(env.workspace + "/Emergency_Medical_Services.shp")
thiessen_poly(env.workspace + "/Emergency_Medical_Services.shp")
clip_shapefile(env.workspace + "/EMS_Thiessen.shp")

if arcpy.Exists("EMS_Thiessen.shp"):
    print('Complete!')

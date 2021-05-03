# Code from challenge 4, but with a function that is called upon twice to describe shapefile parameters
import arcpy
from arcpy import env
arcpy.env.overwriteOutput = True

env.workspace = r"C:\NRS_528\Assignment8"

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


# Input point features to go through thiessen polygon execution.
# In this case, I used emergency medical locations downloaded from RIGIS to visualize areas with the closest EMS location.


inFeatures = "Emergency_Medical_Services.shp"
outFeatureClass = "EMS_Thiessen"
outFields = "ALL"

describe_shp((inFeatures))
print('Creating Thiessen Polygons from:' + inFeatures)

arcpy.CreateThiessenPolygons_analysis(inFeatures, outFeatureClass, outFields)

# Clip data for desired analysis location. In this example, I clipped the thiessen data to RI, as the
# thiessen data from earlier goes beyond the extent of RI.

inFeatures = "EMS_Thiessen.shp"
clip_features = "Municipalities__1997_.shp"
out_feature_class = "EMS_Thiessen_riclipped"

describe_shp((inFeatures))
print('Clipping study area from:' + clip_features)

arcpy.Clip_analysis(inFeatures, clip_features, out_feature_class)

if arcpy.Exists(out_feature_class + ".shp"):
    print('Complete!')

## Theissen Polygon Generation - Ben Hooks

import arcpy
from arcpy import env # Not technically needed as you can just go arcpy.env.workspace


aRCPY.env.workspace = r"C:\NRS 528\Assignment4"

# Input point features to go through thiessen polygon execution.
# In this case, I used emergency medical locations downloaded from RIGIS to visualize areas with the closest EMS location.

inFeatures = "Emergency_Medical_Services.shp"
outFeatureClass = "EMS_Thiessen"
outFields = "ALL"

arcpy.CreateThiessenPolygons_analysis(inFeatures, outFeatureClass, outFields)

# Clip data for desired analysis location. In this example, I clipped the thiessen data to RI, as the
# thiessen data from earlier goes beyond the extent of RI.

in_features = "EMS_Thiessen.shp"
clip_features = "Municipalities__1997_.shp"
out_feature_class = "EMS_Thiessen_riclipped"


arcpy.Clip_analysis(in_features, clip_features, out_feature_class)

# My idea with this was to find areas that might be too far from EMS locations, possibly endangering certain locations due to 
# longer ambulance wait times and driving distances. Of course, this would require further coding and analysis. I imagine the next
# steps would be to calculate population density (because distance does not directly = time driven), road lengths within each polygon, 
# and potentially use a larger location extent, because hospitals outside of RI would not just ignore someone on the border if they were having an emergency.

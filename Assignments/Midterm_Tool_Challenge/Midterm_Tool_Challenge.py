# Turns RI soil CSV into shape file, then performs analysis upon the created shape file, extracting specific soil types for counties based on user input. 

import arcpy, csv



arcpy.env.overwriteOutput = True

# Enter folder with soil csv here

arcpy.env.workspace = r"C:\Data\Students_2021\Hooks\Assignments\Midterm_Tool_Challenge"
file_name = r"Soils_Special_Point_Features.csv"

# The code below reads the soil csv based on user input. The location inputs are restricted to RI counties, but the soil type list will populate from the csv

soils_list = []

with open(file_name) as soil:
    csv_reader = csv.reader(soil, delimiter=",")
    next(csv_reader)

    for row in csv_reader:
        if str(row[9]) not in soils_list:
            soils_list.append(str(row[9]))

for soils in soils_list:
    print(soils)

selected_soil = input("Enter Soil Type from List to be Extracted: ")

municipalities_list = ['Bristol, Kent, Providence, Washington, Newport']
for counties in municipalities_list:
    print(counties)

selected_county = input("Enter County from List: ")
selected_county = selected_county.upper()

# Code below begins processince of the csv file, converting to a shapefile and creating further files from the user input

in_Table = file_name
x_coords = "X"
y_coords = "Y"
z_coords = ""
out_Layer = "Soil_Types"
saved_Layer = r"Soil_Types.shp"

print('Creating shapefile from: ' + in_Table)


spRef = arcpy.SpatialReference(4326)

lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, z_coords)


arcpy.CopyFeatures_management(lyr, saved_Layer)


desc = arcpy.Describe(arcpy.env.workspace + '\Soil_Types.shp')



Soils = str(arcpy.env.workspace) +  "\Soil_Types.shp"
Municipalities_1997_ = str(arcpy.env.workspace) + "\Municipalities__1997_.shp"

print('Projecting soil points')

input_features = Soils
output_feature_class_soil = arcpy.env.workspace + "\Soils_projected.shp"
out_coordinate_system = arcpy.SpatialReference(4326)



arcpy.Project_management(input_features, output_feature_class_soil, out_coordinate_system)

print('Selecting soils')

input_features = output_feature_class_soil
output_feature_class_selected = arcpy.env.workspace + "\Soils_selected.shp"
where_clause = "FEAT_NAME = " + "'" + str(selected_soil) + "'"


arcpy.analysis.Select(input_features, output_feature_class_selected, where_clause)

print('Projecting study area')

input_features = Municipalities_1997_
output_feature_class_projection = arcpy.env.workspace + "\Municipalities_projected.shp"
out_coordinate_system = arcpy.SpatialReference(4326)

arcpy.Project_management(input_features, output_feature_class_projection, out_coordinate_system)

print('Selecting county')

input_features = output_feature_class_projection
output_feature_class_area = arcpy.env.workspace + "\Soils_study_area.shp"
where_clause = "COUNTY = " + "'" + str(selected_county) + "'"


arcpy.analysis.Select(input_features, output_feature_class_area, where_clause)

print('Clipping to study area')

input_features = arcpy.env.workspace + "\Soils_selected.shp"
clip_features = output_feature_class_area
soil_output_feature_class = arcpy.env.workspace + "\\" + selected_soil + '_within_' + selected_county


arcpy.analysis.Clip(input_features, clip_features, soil_output_feature_class)

# If all goes well, the script will delete any intermediate files, and you will be left with a shapefile based upon your soil and county choices.

if arcpy.Exists(selected_soil + '_within_' + selected_county + ".shp"):
    print("Succesfully Extracted soil points within county!")



if arcpy.Exists(selected_soil + '_within_' + selected_county + ".shp"):
    print('Deleting extra files')
    arcpy.Delete_management(output_feature_class_area)
    arcpy.Delete_management(output_feature_class_projection)
    arcpy.Delete_management(output_feature_class_selected)
    arcpy.Delete_management(output_feature_class_soil)
    arcpy.Delete_management(saved_Layer)

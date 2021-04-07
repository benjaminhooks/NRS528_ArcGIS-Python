import arcpy, csv

base_directory = r"C:\Data\Students_2021\Hooks\Assignments\Coding_Challenge5"

arcpy.env.workspace = base_directory
file_name = "homarus_americanus_gammarus.csv"

arcpy.env.overwriteOutput = True


species_list = []

with open(file_name, encoding="utf8") as species:
    csv_reader = csv.reader(species, delimiter="	")
    next(csv_reader)

    for row in csv_reader:
        if str(row[9]) not in species_list:
            species_list.append(str(row[9]))

for species in species_list:

    print("Extracting: " + str(species) + " from: " + file_name)
    file = open(species + ".csv", "a", encoding="utf-8")
    with open(file_name, encoding="utf8") as species_file:
        first_row = next(species_file).split("\t")
        file.write("\t".join(first_row))
        for row in csv.reader(species_file, delimiter="\t"):
            if str(row[9]) == species:
                file.write("\t".join(row))
                file.write("\n")
    file.close()


in_Table = r"Homarus americanus.csv"
x_coords = "decimalLongitude"
y_coords = "decimalLatitude"
z_coords = ""
out_Layer = "homarus_americanus"
saved_Layer = r"homarus_americanus.shp"

print('Creating shapefile from: ' + in_Table)


spRef = arcpy.SpatialReference(4326)

lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, z_coords)


arcpy.CopyFeatures_management(lyr, saved_Layer)
#
#
desc = arcpy.Describe(os.path.join(base_directory, "homarus_americanus.shp"))



arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326)


print('Creating fishnet from: ' + saved_Layer)

outFeatureClass = "homarus_americanus_fishnet.shp"
originCoordinate = str(desc.extent.XMin) + " " + str(desc.extent.YMin)
yAxisCoordinate = str(desc.extent.XMin) + " " + str(desc.extent.YMax)
cellSizeWidth = "2"
cellSizeHeight = "2"
numRows = ""
numColumns = ""
oppositeCorner = str(desc.extent.XMax) + " " + str(desc.extent.YMax)
labels = "NO_LABELS"
templateExtent = "#"
geometryType = "POLYGON"

arcpy.CreateFishnet_management(outFeatureClass, originCoordinate, yAxisCoordinate,
                               cellSizeWidth, cellSizeHeight, numRows, numColumns,
                               oppositeCorner, labels, templateExtent, geometryType)

print('Creating heatmap from: ' + outFeatureClass)

target_features="homarus_americanus_fishnet.shp"
join_features="homarus_americanus.shp"
out_feature_class="homarus_americanus_heatmap.shp"
join_operation="JOIN_ONE_TO_ONE"
join_type="KEEP_ALL"
field_mapping=""
match_option="INTERSECT"
search_radius=""
distance_field_name=""



arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class,
                           join_operation, join_type, field_mapping, match_option,
                           search_radius, distance_field_name)

print('Deleting intermediate files')

if arcpy.Exists(out_feature_class):
    arcpy.Delete_management(target_features)
    arcpy.Delete_management(join_features)


in_Table = r"Homarus gammarus.csv"
x_coords = "decimalLongitude"
y_coords = "decimalLatitude"
z_coords = ""
out_Layer = "homarus_gammarus"
saved_Layer = r"homarus_gammarus.shp"

print('Creating shapefile from: ' + in_Table)

spRef = arcpy.SpatialReference(4326)

lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, z_coords)


arcpy.CopyFeatures_management(lyr, saved_Layer)


desc = arcpy.Describe(r"C:\NRS 528\Assignment5\homarus_gammarus.shp")



arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326)


outFeatureClass = "homarus_gammarus_fishnet.shp"
originCoordinate = str(desc.extent.XMin) + " " + str(desc.extent.YMin)
yAxisCoordinate = str(desc.extent.XMin) + " " + str(desc.extent.YMax)
cellSizeWidth = "2"
cellSizeHeight = "2"
numRows = ""
numColumns = ""
oppositeCorner = str(desc.extent.XMax) + " " + str(desc.extent.YMax)
labels = "NO_LABELS"
templateExtent = "#"
geometryType = "POLYGON"

print('Creating fishnet from: ' + saved_Layer)

arcpy.CreateFishnet_management(outFeatureClass, originCoordinate, yAxisCoordinate,
                               cellSizeWidth, cellSizeHeight, numRows, numColumns,
                               oppositeCorner, labels, templateExtent, geometryType)

print('Creating heatmap from: ' + outFeatureClass)

target_features = "homarus_gammarus_fishnet.shp"
join_features = "homarus_gammarus.shp"
out_feature_class = "homarus_gammarus_heatmap.shp"
join_operation = "JOIN_ONE_TO_ONE"
join_type = "KEEP_ALL"
field_mapping = ""
match_option = "INTERSECT"
search_radius = ""
distance_field_name = ""



arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class,
                           join_operation, join_type, field_mapping, match_option,
                           search_radius, distance_field_name)

print('Deleting intermediate files')

if arcpy.Exists(out_feature_class):
    arcpy.Delete_management(target_features)
    arcpy.Delete_management(join_features)

if arcpy.Exists(out_feature_class):
     print("Created heatmaps successfully!")

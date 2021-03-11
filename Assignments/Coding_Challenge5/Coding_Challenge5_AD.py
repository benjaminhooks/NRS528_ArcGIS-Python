import arcpy, csv, os

arcpy.env.workspace = r"C:\Data\Students_2021\Hooks\Assignments\Coding_Challenge5"
file_name = "homarus_americanus_gammarus.csv" #Moved the filename out here for simplicity.

arcpy.env.overwriteOutput = True

# Create empty list to capture n species in your file.
species_list = []


# with open(file_name) as species:
#
#     csv_reader = csv.reader(species, delimiter=" ") #I also think your delimiter is likely tab not space
#     next(csv_reader)
#     line_count = 0
#
#     for row in csv_reader:
#         if species not in species_list: #issue is here, species does not exist as a row or item from the file, it is the file!
#             species_list.append(species)
#
#         species_list.append(str(row[9]))
#         line_count = line_count + 1
#
# print(species_list)

# Davies fixed code
with open(file_name, encoding="utf8") as species: #I got a character decode error, it is usually due to latin chars
    csv_reader = csv.reader(species, delimiter="	") #tab not space
    next(csv_reader)

    for row in csv_reader:
        if str(row[9]) not in species_list: #changed the variable speices to row[9]
            species_list.append(str(row[9]))

print(species_list)



# Trying to extract the information from the "species" colummn, which is the 10th variable in the list


# os.mkdir("Homarus_Americanus")
# #
# header = "gbifID	datasetKey	occurrenceID	kingdom	phylum	class	order	family	genus	species	infraspecificEpithet	taxonRank	scientificName	verbatimScientificName	verbatimScientificNameAuthorship	countryCode	locality	stateProvince	occurrenceStatus	individualCount	publishingOrgKey	decimalLatitude	decimalLongitude	coordinateUncertaintyInMeters	coordinatePrecision	elevation	elevationAccuracy	depth	depthAccuracy	eventDate	day	month	year	taxonKey	speciesKey	basisOfRecord	institutionCode	collectionCode	catalogNumber	recordNumber	identifiedBy	dateIdentified	license	rightsHolder	recordedBy	typeStatus	establishmentMeans	lastInterpreted	mediaType	issue"
# #
#
#
# for c in species_list:
#     c_count = 1
#     with open("homarus_americanus_gammarus.csv") as species_csv:
#         for row in csv.reader(species_csv):
#             if row[9] == c:
#                 if c_count == 1:
#                     file = open(r"Homarus_Americanus/" + str(c) + ".csv", "w")
#                     file.write(header)
#                     c_count = 0
#
#                 file.write(",".join(row))
#                 file.write("\n")
#     file.close()



# in_Table = r"homarus_americanus_gammarus.csv"
# x_coords = "decimalLongitude"
# y_coords = "decimalLatitude"
# z_coords = ""
# out_Layer = "homarus_americanus_gammarus"
# saved_Layer = r"homarus_americanus_gammarus.shp"
#
# spRef = arcpy.SpatialReference(4326)
#
# lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, z_coords)
#
# # print(arcpy.GetCount_management(out_Layer))
#
# arcpy.CopyFeatures_management(lyr, saved_Layer)

#
# desc = arcpy.Describe(r"C:\NRS 528\Assignment5\homarus_americanus_gammarus.shp")
#
# # print(desc.extent)
# # print("Extent:\n  XMin: {0},\n XMax: {1},\n YMin: {2},\n YMax: {3}".format(desc.extent.XMin, desc.extent.XMax, desc.extent.YMin, desc.extent.YMax))
#
#
# arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326)
#
#
#
# outFeatureClass = "homarus_americanus_gammarus_fishnet.shp"
# originCoordinate = str(desc.extent.XMin) + " " + str(desc.extent.YMin)
# yAxisCoordinate = str(desc.extent.XMin) + " " + str(desc.extent.YMax)
# cellSizeWidth = "5"
# cellSizeHeight = "5"
# numRows = ""
# numColumns = ""
# oppositeCorner = str(desc.extent.XMax) + " " + str(desc.extent.YMax)
# labels = "NO_LABELS"
# templateExtent = "#"
# geometryType = "POLYGON"
#
# arcpy.CreateFishnet_management(outFeatureClass, originCoordinate, yAxisCoordinate,
#                                cellSizeWidth, cellSizeHeight, numRows, numColumns,
#                                oppositeCorner, labels, templateExtent, geometryType)
#
#
#
# target_features="homarus_americanus_gammarus_fishnet.shp"
# join_features="homarus_americanus_gammarus.shp"
# out_feature_class="homarus_americanus_gammarus_heatmap.shp"
# join_operation="JOIN_ONE_TO_ONE"
# join_type="KEEP_ALL"
# field_mapping=""
# match_option="INTERSECT"
# search_radius=""
# distance_field_name=""
#
# arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class,
#                            join_operation, join_type, field_mapping, match_option,
#                            search_radius, distance_field_name)
#
#
#
#
# # if arcpy.Exists(out_feature_class):
# #     arcpy.Delete_management(target_features)
# #     arcpy.Delete_management(join_features)
#
# if arcpy.Exists(out_feature_class):
#      print("Created heatmap successfully!")

import arcpy

# This toolbox is intended to be used for calculating the impacts of sea level rise (SLR) from RIGIS data, but can be utilized for other forms of data analyses as well

# The 4 scripts and their intended uses are;

# Data Projection - To ensure accurate end results, the user should project their datasets into the relevant coordinate system for the study area.

# Buffer - Buffer the sea level rise data to a specified amount. The SLR data used within this project was documented as polylines 
#          (to show the roads being impacted by SLR.) By buffering the SLR data out to different points, were are able to calculate the amount 
#          of features affected given different circumstances.

# Clip - Clip the data to be analyzed by the buffered SLR data.

# Calculate Statistics - Calculate statistics based on user input. Examples include summing the affected area, determining the amount 
#                        of unique/total structures affected, or the average amount for a specific parameter. Input the desired parameter to be analyzed. Output
#                        will be a .dbf file that can be viewed within ArcGIS


class Toolbox(object):
    def __init__(self):
        self.label = "Feature Impacts Python Toolbox"
        self.alias = ""
        self.tools = [project, buffer, clip, statistics,]

class project(object):
    def __init__(self):
        self.label = "Project Areas (Step 1)"
        self.description = "Project all feature data sets to be used within the analysis" \
                           "to ensure statistical accuracy"

        self.canRunInBackground = False
        
# Parameters for projecting a shapefile. User can choose the projection they need in ArcPro based off of the data/area. 
        
    def getParameterInfo(self):
        params = []

        input_shapefile = arcpy.Parameter(name="initial_data",
                                     displayName="Input Shapefile to be Projected",
                                     datatype="DEFeatureClass",
                                     parameterType="Required",
                                     direction="Input")

        params.append(input_shapefile)


        output_projected = arcpy.Parameter(name="output_projected",
                                     displayName="Projected Shapefile Output",
                                     datatype="DEFeatureClass",
                                     parameterType="Required",
                                     direction="Output")


        params.append(output_projected)

        coordinate_system = arcpy.Parameter(name="buffer_amount",
                                     displayName="Coordinate System",
                                     datatype="GPCoordinateSystem",
                                     parameterType="Required",
                                     direction="Input")
        params.append(coordinate_system)

        return params

    def isLicensed(self):
            return True

    def updateParameters(self, parameters):
            return

    def updateMessages(self, parameters):
            return

    def execute(self, parameters, messages):

        input_shapefile = parameters[0].valueAsText
        output_projected = parameters[1].valueAsText
        coordinate_system = parameters[2].valueAsText


        arcpy.Project_management(in_dataset=input_shapefile,
                                 out_dataset=output_projected,
                                 out_coor_system=coordinate_system,
                                 transform_method="",
                                 in_coor_system="",
                                 preserve_shape="PRESERVE_SHAPE",
                                 max_deviation="",
                                 vertical=""
                                 )

        return

class buffer(object):
    def __init__(self):
        self.label = "Buffer Areas (Step 2)"
        self.description = "Buffer the input shapefile to determine the " \
                           "study area. Buffer unit should match the projected coordinate" \
                           "system used for accuracy. "

        self.canRunInBackground = False

    def getParameterInfo(self):
        
        #         Parameters for buffering the input data. User can define the buffer amount in feet or meters based off of data or previous projection
        
        params = []

        slr_data = arcpy.Parameter(name="initial_data",
                                     displayName="Input Shapefile",
                                     datatype="DEFeatureClass",
                                     parameterType="Required",
                                     direction="Input")

        params.append(slr_data)


        buffer_data = arcpy.Parameter(name="Buffer Zone",
                                     displayName="Buffer Zone Output",
                                     datatype="DEFeatureClass",
                                     parameterType="Required",
                                     direction="Output")


        params.append(buffer_data)

        buffer_amount = arcpy.Parameter(name="buffer_amount",
                                     displayName="Buffer Amount",
                                     datatype="Field",
                                     parameterType="Required",
                                     direction="Input")
        params.append(buffer_amount)

        buffer_unit = arcpy.Parameter(name="buffer_unit",
                                     displayName="Buffer Unit (same as projected coordinate system)",
                                     datatype="Field",
                                     parameterType="Required",
                                     direction="Input")

        buffer_unit.columns = [['GPString', 'Field']]
        buffer_unit.values = [['']]
        buffer_unit.filters[0].list = ['Feet', 'Meters']

        params.append(buffer_unit)

        return params

    def isLicensed(self):
            return True

    def updateParameters(self, parameters):
            return

    def updateMessages(self, parameters):
            return

    def execute(self, parameters, messages):


        slr_data = parameters[0].valueAsText
        buffer_data = parameters[1].valueAsText
        buffer_amount = parameters[2].valueAsText
        buffer_unit = parameters[3].valueAsText

        arcpy.Buffer_analysis(in_features=slr_data,
                              out_feature_class=buffer_data,
                              buffer_distance_or_field=buffer_amount + " " + buffer_unit,
                              line_side="FULL",
                              line_end_type="ROUND",
                              dissolve_option="ALL",
                              dissolve_field=[],
                              method="PLANAR")
        return

class clip(object):
    def __init__(self):
        self.label = "Clip Areas (Step 3)"
        self.description = "Clip shapefile used for analysis from " \
                           "the buffered shapefile from earlier"
        self.canRunInBackground = False

    def getParameterInfo(self):
        
#         Parameters for clipping a shapefile. Use previous buffered area to clip to the desired study area for accurate statistical analysis
        
        params = []

        buffer_data = arcpy.Parameter(name="buffer_zone",
                                     displayName="Buffered Shapefile",
                                     datatype="DEFeatureClass",
                                     parameterType="Required",
                                     direction="Input")

        params.append(buffer_data)



        building_data = arcpy.Parameter(name="building_data",
                                        displayName="Shapefile to be clipped",
                                        datatype="DEFeatureClass",
                                        parameterType="Required",
                                        direction="Input")


        params.append(building_data)

        clipped_buildings = arcpy.Parameter(name="clipped_buildings",
                                            displayName="Clipped Output",
                                            datatype="DEFeatureClass",
                                            parameterType="Required",
                                            direction="Output")

        params.append(clipped_buildings)

        return params

    def isLicensed(self):
            return True

    def updateParameters(self, parameters):
            return

    def updateMessages(self, parameters):
            return

    def execute(self, parameters, messages):

        buffer_data = parameters[0].valueAsText
        building_data = parameters[1].valueAsText
        clipped_buildings = parameters[2].valueAsText


        arcpy.Clip_analysis(in_features=building_data,
                    clip_features=buffer_data,
                    out_feature_class=clipped_buildings,
                    cluster_tolerance="")

        return


class statistics(object):
    def __init__(self):
        self.label = "Calculate Statistics (Step 4)"
        self.description = "The calculate statistics portion of this script" \
                           "allows the user to calculate a specific metric for the" \
                           "clipped dataset. Examples include summing the affected area," \
                           "determining the amount of unique structures affected, or the average" \
                           "amount for a specific parameter. Input the desired parameter to be " \
                           "analyzed. Output will be a .dbf file that can be viewed within ArcGIS"

        self.canRunInBackground = False


    def getParameterInfo(self):
        
#         Parameters for the statistical analysis. Use a parameter from the study area attribute table (such as objectid, area, population, etc. depending on data)
#         and the type of analysis you want to be done on the data
        
        params = []



        clipped_buildings = arcpy.Parameter(name="clipped_buildings",
                         displayName="Clipped Shapefile",
                         datatype="DEFeatureClass",
                         parameterType="Required",
                         direction="Input")

        params.append(clipped_buildings)



        building_output = arcpy.Parameter(name="building_output",
                         displayName="Calculation Output",
                         datatype="DEFeatureClass",
                         parameterType="Required",
                         direction="Output")

        params.append(building_output)


        stat_field = arcpy.Parameter(name="statistic_field",
                                        displayName="Field to be calculated",
                                        datatype="DEFeatureClass",
                                        parameterType="Required",
                                        direction="Input")


        stat_field.columns = [['Field', 'Field from Attribute Table'], ['GPString', 'Statistic Type']]
        stat_field.filters[1].type = 'ValueList'
        stat_field.values = [['FID', 'UNIQUE']]
        stat_field.filters[1].list = ['SUM', 'MIN', 'MAX', 'STDEV', 'MEAN', 'COUNT', 'UNIQUE', 'MEDIAN']

        params.append(stat_field)

        return params

    def isLicensed(self):

        return True

    def updateParameters(self, parameters):

        return

    def updateMessages(self, parameters):

        return

    def execute(self, parameters, messages):

        print(parameters)

        clipped_buildings = parameters[0].valueAsText
        building_output = parameters[1].valueAsText
        stat_field = parameters[2].valueAsText


        arcpy.analysis.Statistics(in_table=clipped_buildings,
                                  out_table=building_output,
                                  statistics_fields=stat_field,
                                  case_field=[])
        return


# Uncomment below if running in Python IDE

# def main():
#     tool = calculatesealevel()
#     tool.execute(tool.getParameterInfo(), None)
# if __name__ == '__main__':
#     main()

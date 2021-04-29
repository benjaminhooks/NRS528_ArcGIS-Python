import arcpy
class Toolbox(object):
    def __init__(self):
        self.label = "SLR Impacts Python Toolbox"
        self.alias = ""
        self.tools = [calculatesealevel]

class calculatesealevel(object):
    def __init__(self):
        self.label = "Determine impacts of sea level rise"
        self.description = ""


    def getParameterInfo(self):


        slr_data = arcpy.Parameter(
            displayName="Sea Level Rise Data",
            name="slr_data",
            datatype="DEFeatureClass",
            parameterType="Required",
            direction="Input")

        slr_data.filter.list = ["SLR"]

        buffer_data = arcpy.Parameter(
            displayName="Buffer Data",
            name="buffer_data",
            datatype="DEFeatureClass",
            parameterType="Required",
            direction="Output")

        buffer_data.parameterDependencies = [slr_data.name]
        buffer_data.schema.clone = True

        building_data = arcpy.Parameter(
            displayName="Building Data",
            name="building_data",
            datatype="DEFeatureClass",
            parameterType="Required",
            direction="Input")

        building_data.filter.list = ["Building"]

        clipped_building_data = arcpy.Parameter(
            displayName="Clipped Building Data",
            name="clipped_building_data",
            datatype="DEFeatureClass",
            parameterType="Required",
            direction="Output")

        clipped_building_data.parameterDependencies = [buffer_data.name]
        clipped_building_data.schema.clone = True

        parameters = [slr_data, buffer_data, building_data, clipped_building_data]


        return parameters

    def isLicensed(self):

        return True

    def updateParameters(self, parameters):


        return


    def updateMessages(self, parameters):

        return

    def execute(self, parameters, messages):

        slr_data = parameters[0].valueAsText
        buffer_data = parameters[1].valueAsText
        building_data = parameters[2].valueAsText
        clipped_building_data = parameters[3].valueAsText


        arcpy.Buffer_analysis(in_features=slr_data,
                              out_feature_class=buffer_data,
                              buffer_distance_or_field="150 Feet",
                              line_side="FULL",
                              line_end_type="ROUND",
                              dissolve_option="ALL",
                              dissolve_field=[],
                              method="PLANAR")

        arcpy.Clip_analysis(in_features=building_data,
                    clip_features=buffer_data,
                    out_feature_class=clipped_building_data,
                    cluster_tolerance="")

        return


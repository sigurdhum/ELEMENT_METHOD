# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2024 replay file
# Internal Version: 2023_09_21-14.55.25 RELr426 190762
# Run by 10992702 on Sun Feb 25 13:51:03 2024
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=378.559692382812, 
    height=153.257690429688)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
mdb.openAuxMdb(pathName='Y:/mb_rot.cae')
mdb.copyAuxMdbModel(fromName='Model-1', toName='Model-1')
mdb.closeAuxMdb()
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='simple_test')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    step='clamped_edges')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='simple_test')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    step='clamped_edges')
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=616.272, 
    farPlane=1009.63, width=554.054, height=261.021, viewOffsetX=-39.1177, 
    viewOffsetY=-11.6257)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='simple_test')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    step='clamped_edges')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='simple_test')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF, adaptiveMeshConstraints=ON)
mdb.models['Model-1'].StaticLinearPerturbationStep(name='ss_points', 
    previous='uniformed_load')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='ss_points')
del mdb.models['Model-1'].steps['ss_points']
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
mdb.models['Model-1'].StaticLinearPerturbationStep(name='ss_points', 
    previous='Initial')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='ss_points')
mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].move('simple_test', 
    'ss_points')
mdb.models['Model-1'].historyOutputRequests['H-Output-1'].move('simple_test', 
    'ss_points')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
mdb.models['Model-1'].boundaryConditions['simple_test_BC'].move('simple_test', 
    'Initial')
#* Cannot move a boundary condition created in a perturbation step.
mdb.models['Model-1'].boundaryConditions['simple_test_BC'].move('simple_test', 
    'Initial')
#* Cannot move a boundary condition created in a perturbation step.
mdb.models['Model-1'].BoundaryCondition(name='ss', 
    objectToCopy=mdb.models['Model-1'].boundaryConditions['simple_test_BC'], 
    toStepName='ss_points')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='simple_test')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    step='clamped_edges')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='ss_points')
mdb.models['Model-1'].boundaryConditions['fixed'].deactivate('ss_points')
a = mdb.models['Model-1'].rootAssembly
region = a.sets['points_assembly']
mdb.models['Model-1'].ConcentratedForce(name='points', 
    createStepName='ss_points', region=region, cf3=-2.0, 
    distributionType=UNIFORM, field='', localCsys=None)
session.viewports['Viewport: 1'].view.setValues(nearPlane=661.56, 
    farPlane=953.921, width=570.645, height=268.837, cameraPosition=(350.368, 
    579.375, 636.388), cameraUpVector=(-0.188229, 0.572299, -0.79815), 
    cameraTarget=(167.147, 106.493, 1.01038))
session.viewports['Viewport: 1'].view.setValues(nearPlane=687.412, 
    farPlane=928.048, width=592.944, height=279.342, cameraPosition=(355.313, 
    368.016, 747.15), cameraUpVector=(-0.00991979, 0.776006, -0.630648), 
    cameraTarget=(167.115, 107.857, 0.295654))
session.viewports['Viewport: 1'].view.setValues(nearPlane=729.529, 
    farPlane=880.698, width=629.273, height=296.457, cameraPosition=(181.777, 
    271.233, 796.358), cameraUpVector=(0.148692, 0.844022, -0.515285), 
    cameraTarget=(168.237, 108.483, -0.0225372))
session.viewports['Viewport: 1'].view.setValues(nearPlane=743.317, 
    farPlane=865.871, width=641.167, height=302.06, cameraPosition=(139.253, 
    95.6104, 812.115), cameraUpVector=(0.0833137, 0.94589, -0.31361), 
    cameraTarget=(168.651, 110.193, -0.175961))
session.viewports['Viewport: 1'].view.setValues(nearPlane=724.075, 
    farPlane=887.041, width=624.569, height=294.241, cameraPosition=(197.551, 
    -45.9853, 796.957), cameraUpVector=(0.00162634, 0.989527, -0.144339), 
    cameraTarget=(168.045, 111.664, -0.0184717))
session.viewports['Viewport: 1'].view.setValues(nearPlane=730.925, 
    farPlane=880.333, width=630.477, height=297.025, cameraPosition=(204.209, 
    4.5458, 805.02), cameraUpVector=(0.0326673, 0.977463, -0.208564), 
    cameraTarget=(167.984, 111.2, -0.0925007))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF, 
    bcs=OFF, predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
mdb.Job(name='ss_points', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs['ss_points'].submit(consistencyChecking=OFF)
#: The job input file "ss_points.inp" has been submitted for analysis.
#: Job ss_points: Analysis Input File Processor completed successfully.
session.viewports['Viewport: 1'].view.setValues(nearPlane=584.692, 
    farPlane=1014.74, width=504.34, height=244.61, cameraPosition=(-234.486, 
    -533.11, 277.153), cameraUpVector=(-0.254325, 0.802902, 0.539135), 
    cameraTarget=(171.973, 116.088, 4.707))
session.viewports['Viewport: 1'].view.setValues(nearPlane=601.965, 
    farPlane=1000.11, width=519.239, height=251.836, cameraPosition=(-141.099, 
    -630.319, 73.7731), cameraUpVector=(-0.31469, 0.560605, 0.765959), 
    cameraTarget=(170.427, 117.697, 8.07355))
session.viewports['Viewport: 1'].view.setValues(nearPlane=600.878, 
    farPlane=1001.19, width=518.301, height=251.381, cameraPosition=(-141.099, 
    -630.319, 73.7731), cameraUpVector=(0.1515, 0.379345, 0.912768), 
    cameraTarget=(170.427, 117.697, 8.07355))
session.viewports['Viewport: 1'].view.setValues(nearPlane=606.465, 
    farPlane=996.4, width=523.12, height=253.718, cameraPosition=(-119.684, 
    -613.853, 211.227), cameraUpVector=(0.255732, 0.501174, 0.826695), 
    cameraTarget=(170.108, 117.452, 6.02828))
session.viewports['Viewport: 1'].view.setValues(nearPlane=643.257, 
    farPlane=962.862, width=554.856, height=269.11, cameraPosition=(13.9221, 
    -526.813, 475.129), cameraUpVector=(0.364528, 0.744913, 0.558771), 
    cameraTarget=(168.187, 116.201, 2.23463))
session.viewports['Viewport: 1'].view.setValues(nearPlane=679.351, 
    farPlane=923.481, width=585.989, height=284.21, cameraPosition=(-38.9629, 
    -142.51, 742.717), cameraUpVector=(-0.0217748, 0.999337, -0.0291755), 
    cameraTarget=(168.839, 111.466, -1.06224))
session.viewports['Viewport: 1'].view.setValues(nearPlane=705.115, 
    farPlane=905.012, width=608.212, height=294.988, cameraPosition=(356.25, 
    199.207, 782.595), cameraUpVector=(-0.0452337, 0.896687, -0.440349), 
    cameraTarget=(163.15, 106.547, -1.63634))
session.viewports['Viewport: 1'].view.setValues(nearPlane=678.423, 
    farPlane=933.76, width=585.188, height=283.821, cameraPosition=(200.931, 
    -404.758, 626.043), cameraUpVector=(-0.0996963, 0.933594, 0.344183), 
    cameraTarget=(164.672, 112.466, -0.102165))
session.viewports['Viewport: 1'].view.setValues(nearPlane=656.087, 
    farPlane=959.541, width=565.921, height=274.477, cameraPosition=(168.422, 
    -666.054, 229.808), cameraUpVector=(-0.0566877, 0.582173, 0.811086), 
    cameraTarget=(164.949, 114.69, 3.2708))
session.viewports['Viewport: 1'].view.setValues(nearPlane=652.053, 
    farPlane=964.383, width=562.442, height=272.789, cameraPosition=(144.016, 
    -695.795, 61.4009), cameraUpVector=(-0.0481091, 0.399943, 0.915277), 
    cameraTarget=(165.104, 114.879, 4.34212))
session.viewports['Viewport: 1'].view.setValues(nearPlane=655.646, 
    farPlane=961.524, width=565.541, height=274.292, cameraPosition=(158.196, 
    -698.032, 5.51184), cameraUpVector=(-0.0407443, 0.334663, 0.941457), 
    cameraTarget=(165.021, 114.892, 4.66956))
session.viewports['Viewport: 1'].view.setValues(nearPlane=654.725, 
    farPlane=961.415, width=564.747, height=273.907, cameraPosition=(180.5, 
    -673.16, 203.188), cameraUpVector=(0.0312123, 0.555094, 0.831202), 
    cameraTarget=(164.9, 114.758, 3.60167))
#: Job ss_points: Abaqus/Standard completed successfully.
session.viewports['Viewport: 1'].view.setValues(nearPlane=650.449, 
    farPlane=962.844, width=561.058, height=272.118, cameraPosition=(102.201, 
    -617.214, 351.437), cameraUpVector=(0.230525, 0.681527, 0.694535), 
    cameraTarget=(165.373, 114.42, 2.7058))
session.viewports['Viewport: 1'].view.setValues(nearPlane=667.473, 
    farPlane=946.641, width=575.742, height=279.24, cameraPosition=(207.968, 
    -514.163, 516.105), cameraUpVector=(0.00895926, 0.856025, 0.516857), 
    cameraTarget=(164.546, 113.614, 1.41842))
#: Job ss_points completed successfully. 
o3 = session.openOdb(name='Y:/ss_points.odb')
#: Model: Y:/ss_points.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       4
#: Number of Node Sets:          7
#: Number of Steps:              5
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=4, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=3, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=3, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].view.setValues(nearPlane=987.153, 
    farPlane=1376.77, width=764.896, height=415.097, cameraPosition=(777.691, 
    484.983, 925.774), cameraUpVector=(-0.24177, 0.764216, -0.597931), 
    cameraTarget=(162.289, 90.0418, 21.5461))
session.viewports['Viewport: 1'].view.setValues(nearPlane=996.464, 
    farPlane=1380.37, width=772.11, height=419.012, cameraPosition=(1051.76, 
    78.8868, 773.406), cameraUpVector=(-0.124912, 0.923895, -0.361684), 
    cameraTarget=(166.71, 83.4912, 19.0883))
session.viewports['Viewport: 1'].view.setValues(nearPlane=962.541, 
    farPlane=1441.63, width=745.825, height=404.747, cameraPosition=(965.957, 
    -578.421, 553.764), cameraUpVector=(0.270508, 0.96208, 0.0350386), 
    cameraTarget=(164.867, 69.3763, 14.3718))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1004.07, 
    farPlane=1426.78, width=778.007, height=422.212, cameraPosition=(491.373, 
    -989.814, 385.35), cameraUpVector=(0.579578, 0.706435, 0.406249), 
    cameraTarget=(149.396, 55.9649, 8.88151))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1034.26, 
    farPlane=1381.89, width=801.399, height=434.906, cameraPosition=(638.403, 
    -248.129, 1040.38), cameraUpVector=(-0.441085, 0.888904, 0.123667), 
    cameraTarget=(155.75, 88.0186, 37.19))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1036.65, 
    farPlane=1398.31, width=803.25, height=435.911, cameraPosition=(168.445, 
    -1103.88, 79.0555), cameraUpVector=(-0.142569, 0.391461, 0.909083), 
    cameraTarget=(138.177, 56.0194, 1.24313))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1045.64, 
    farPlane=1393.02, width=810.218, height=439.692, cameraPosition=(248.967, 
    -809.8, 786.762), cameraUpVector=(-0.296206, 0.821993, 0.486405), 
    cameraTarget=(141.787, 69.203, 32.9695))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1114.8, 
    farPlane=1327.43, width=863.81, height=468.775, cameraPosition=(291.375, 
    165.438, 1204.67), cameraUpVector=(-0.139945, 0.922643, -0.359369), 
    cameraTarget=(143.75, 114.336, 52.3099))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1072.43, 
    farPlane=1372.06, width=830.979, height=450.958, cameraPosition=(148.677, 
    -607.082, 981.645), cameraUpVector=(-0.203266, 0.93982, 0.274629), 
    cameraTarget=(136.947, 77.5078, 41.6777))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1106.68, 
    farPlane=1334.92, width=857.517, height=465.36, cameraPosition=(312.514, 
    20.1104, 1199.66), cameraUpVector=(-0.176755, 0.954819, -0.238911), 
    cameraTarget=(144.902, 107.96, 52.2632))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=1056.02, 
    farPlane=1381.77, width=818.262, height=444.058, cameraPosition=(369.086, 
    -435.248, 1061.17), cameraUpVector=(-0.0834075, 0.986196, 0.143041), 
    cameraTarget=(147.585, 86.3639, 45.6951))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1066.21, 
    farPlane=1381.39, width=826.156, height=448.342, cameraPosition=(86.5515, 
    911.33, 915.17), cameraUpVector=(0.179468, 0.485645, -0.855535), 
    cameraTarget=(134.605, 148.227, 38.9877))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1036, 
    farPlane=1404.14, width=802.748, height=435.639, cameraPosition=(213.838, 
    1218.64, -515.68), cameraUpVector=(0.165092, -0.698046, -0.696761), 
    cameraTarget=(140.939, 163.52, -32.2186))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1062.41, 
    farPlane=1372.67, width=823.208, height=446.742, cameraPosition=(361.597, 
    630.577, -1089.65), cameraUpVector=(0.0434846, -0.994782, -0.0922912), 
    cameraTarget=(147.863, 135.963, -59.1155))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1053.69, 
    farPlane=1378.58, width=816.451, height=443.075, cameraPosition=(306.257, 
    -556.156, -1014), cameraUpVector=(-0.10361, -0.604309, 0.789984), 
    cameraTarget=(145.379, 82.7015, -55.7204))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1028.97, 
    farPlane=1401.5, width=797.296, height=432.68, cameraPosition=(75.0253, 
    -1092.52, 143.939), cameraUpVector=(-0.238561, 0.459676, 0.855445), 
    cameraTarget=(135.256, 59.2197, -5.02628))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1082.7, 
    farPlane=1339.27, width=838.929, height=455.273, cameraPosition=(173.73, 
    -375.739, 1101.17), cameraUpVector=(-0.181126, 0.980901, 0.0708997), 
    cameraTarget=(139.507, 90.0918, 36.2021))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1075.16, 
    farPlane=1346.81, width=942.836, height=511.662, viewOffsetX=6.86609, 
    viewOffsetY=-13.2013)
mdb.saveAs(pathName='Y:/mb_sss_points')
#: The model database has been saved to "Y:\mb_sss_points.cae".
session.viewports['Viewport: 1'].view.setValues(nearPlane=1030.89, 
    farPlane=1399.06, width=904.015, height=490.595, cameraPosition=(300.928, 
    -718.78, 868.291), cameraUpVector=(-0.099021, 0.905256, 0.413166), 
    cameraTarget=(146.276, 74.2323, 31.9057), viewOffsetX=6.58338, 
    viewOffsetY=-12.6577)
session.viewports['Viewport: 1'].view.setValues(nearPlane=973.724, 
    farPlane=1444.16, width=853.885, height=463.39, cameraPosition=(941.527, 
    -429.71, 735.971), cameraUpVector=(-0.393609, 0.797513, 0.457215), 
    cameraTarget=(173.874, 82.9392, 28.7041), viewOffsetX=6.21831, 
    viewOffsetY=-11.9558)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1005.5, 
    farPlane=1405.14, width=881.754, height=478.514, cameraPosition=(879.331, 
    -143.894, 922.476), cameraUpVector=(-0.553577, 0.802701, 0.221864), 
    cameraTarget=(169.048, 94.9537, 33.2196), viewOffsetX=6.42126, 
    viewOffsetY=-12.346)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1020.11, 
    farPlane=1385.49, width=894.569, height=485.468, cameraPosition=(877.197, 
    70.7703, 954.278), cameraUpVector=(-0.640231, 0.761843, 0.0984885), 
    cameraTarget=(168.075, 102.723, 33.1632), viewOffsetX=6.51458, 
    viewOffsetY=-12.5254)
session.viewports['Viewport: 1'].view.setValues(nearPlane=998.484, 
    farPlane=1425.11, width=875.605, height=475.176, cameraPosition=(585.125, 
    -690.381, 794.128), cameraUpVector=(-0.283491, 0.828693, 0.482598), 
    cameraTarget=(160.532, 76.9046, 30.3734), viewOffsetX=6.37648, 
    viewOffsetY=-12.2599)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1011.73, 
    farPlane=1419.67, width=887.224, height=481.482, cameraPosition=(358.884, 
    -965.995, 519.436), cameraUpVector=(-0.184388, 0.682271, 0.707465), 
    cameraTarget=(151.515, 63.6634, 20.3077), viewOffsetX=6.4611, 
    viewOffsetY=-12.4226)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1034.48, 
    farPlane=1396.92, width=233.495, height=327.257, viewOffsetX=-41.0315, 
    viewOffsetY=-29.478)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1057.77, 
    farPlane=1358.72, width=616.612, height=334.626, cameraPosition=(233.33, 
    -715.339, 870.872), cameraUpVector=(-0.283891, 0.871157, 0.400615), 
    cameraTarget=(140.658, 85.0324, 32.3343), viewOffsetX=-41.9554, 
    viewOffsetY=-30.1418)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U2'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U1'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U2'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U1'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=1058.06, 
    farPlane=1358.43, width=616.782, height=334.718, cameraPosition=(248.707, 
    -727.881, 857.201), cameraUpVector=(0.0988934, 0.912245, 0.397529), 
    cameraTarget=(156.035, 72.4902, 18.6636), viewOffsetX=-41.9669, 
    viewOffsetY=-30.1501)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1066.28, 
    farPlane=1392.09, width=621.574, height=337.319, cameraPosition=(125.518, 
    -1036.83, 432.056), cameraUpVector=(0.296744, 0.633501, 0.714576), 
    cameraTarget=(155.465, 43.9656, 3.9075), viewOffsetX=-42.293, 
    viewOffsetY=-30.3843)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1065.59, 
    farPlane=1418.89, width=621.173, height=337.101, cameraPosition=(39.6746, 
    -1122.38, 89.3491), cameraUpVector=(0.307163, 0.383804, 0.87083), 
    cameraTarget=(150.38, 30.7168, -12.7857), viewOffsetX=-42.2657, 
    viewOffsetY=-30.3647)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1031.64, 
    farPlane=1413.03, width=601.381, height=326.36, cameraPosition=(386.294, 
    -1060.23, 257.938), cameraUpVector=(-0.236596, 0.480905, 0.844247), 
    cameraTarget=(157.378, 54.3816, 18.0129), viewOffsetX=-40.919, 
    viewOffsetY=-29.3972)
session.viewports['Viewport: 1'].view.setValues(nearPlane=992, 
    farPlane=1413.41, width=578.273, height=313.82, cameraPosition=(656.764, 
    -854.907, 506.034), cameraUpVector=(-0.347743, 0.602082, 0.71873), 
    cameraTarget=(165.387, 81.8241, 22.9103), viewOffsetX=-39.3467, 
    viewOffsetY=-28.2676)
session.viewports['Viewport: 1'].view.setValues(nearPlane=989.659, 
    farPlane=1380.53, width=576.908, height=313.079, cameraPosition=(757.439, 
    -498.203, 812.269), cameraUpVector=(-0.456643, 0.771918, 0.44229), 
    cameraTarget=(162.451, 107.35, 17.5238), viewOffsetX=-39.2538, 
    viewOffsetY=-28.2009)
session.viewports['Viewport: 1'].view.setValues(nearPlane=988.772, 
    farPlane=1422.58, width=576.391, height=312.799, cameraPosition=(703.813, 
    -963.457, 28.0356), cameraUpVector=(-0.223174, 0.26396, 0.93836), 
    cameraTarget=(172.82, 71.1219, 23.8106), viewOffsetX=-39.2186, 
    viewOffsetY=-28.1756)
session.viewports['Viewport: 1'].view.setValues(nearPlane=993.923, 
    farPlane=1402.11, width=579.394, height=314.429, cameraPosition=(693.8, 
    -715.357, 673.942), cameraUpVector=(-0.36636, 0.710083, 0.601301), 
    cameraTarget=(166.244, 100.017, 34.2747), viewOffsetX=-39.4229, 
    viewOffsetY=-28.3224)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='simple_test')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='ss_points')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='simple_test')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='ss_points')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='simple_test')
session.viewports['Viewport: 1'].view.setValues(nearPlane=661.835, 
    farPlane=952.279, width=570.879, height=300.928, viewOffsetX=41.7007, 
    viewOffsetY=-12.3669)
session.viewports['Viewport: 1'].view.setValues(nearPlane=661.807, 
    farPlane=952.306, width=570.855, height=300.916, viewOffsetX=1.61627, 
    viewOffsetY=-16.8056)
session.viewports['Viewport: 1'].view.setValues(farPlane=952.307, 
    viewOffsetX=77.2562, viewOffsetY=-9.51258)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
odb = session.odbs['Y:/ss_points.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1005.78, 
    farPlane=1390.25, width=406.13, height=220.4, viewOffsetX=-34.2604, 
    viewOffsetY=-29.4761)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='ss_points')
session.viewports['Viewport: 1'].view.setValues(nearPlane=673.858, 
    farPlane=930.41, width=581.25, height=306.395, cameraPosition=(197.558, 
    -388.226, 634.715), cameraUpVector=(0.118744, 0.937526, 0.327024), 
    cameraTarget=(166.74, 124.513, 4.60308), viewOffsetX=78.6629, 
    viewOffsetY=-9.68579)
session.viewports['Viewport: 1'].view.setValues(nearPlane=671.175, 
    farPlane=894.257, width=578.936, height=305.175, cameraPosition=(87.1681, 
    -147.957, 743.958), cameraUpVector=(0.338372, 0.939836, 0.0470372), 
    cameraTarget=(174.953, 146.439, -8.71472), viewOffsetX=78.3498, 
    viewOffsetY=-9.64723)
session.viewports['Viewport: 1'].view.setValues(nearPlane=671.364, 
    farPlane=894.068, width=579.099, height=305.261, cameraPosition=(79.9496, 
    -167.515, 735.466), cameraUpVector=(0.114025, 0.99261, 0.0415132), 
    cameraTarget=(167.734, 126.881, -17.2064), viewOffsetX=78.3719, 
    viewOffsetY=-9.64995)
odb = session.odbs['Y:/ss_points.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1007.02, 
    farPlane=1365.5, width=406.631, height=220.673, cameraPosition=(831.979, 
    -351.732, 850.994), cameraUpVector=(-0.501247, 0.776528, 0.381779), 
    cameraTarget=(162.431, 120.878, 25.9663), viewOffsetX=-34.3027, 
    viewOffsetY=-29.5125)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1015.02, 
    farPlane=1386.61, width=409.861, height=222.426, cameraPosition=(611.403, 
    -798.719, 631.554), cameraUpVector=(-0.289612, 0.713272, 0.638254), 
    cameraTarget=(169.708, 97.6296, 36.752), viewOffsetX=-34.5752, 
    viewOffsetY=-29.7469)
session.viewports['Viewport: 1'].view.setValues(nearPlane=978.809, 
    farPlane=1393.52, width=395.239, height=214.491, cameraPosition=(981.418, 
    -481.552, 605.764), cameraUpVector=(-0.447192, 0.641114, 0.623693), 
    cameraTarget=(170.443, 119.296, 28.1596), viewOffsetX=-33.3417, 
    viewOffsetY=-28.6857)
session.viewports['Viewport: 1'].view.setValues(nearPlane=980.002, 
    farPlane=1392.33, width=395.721, height=214.752, cameraPosition=(988.631, 
    -481.865, 595.311), cameraUpVector=(-0.289472, 0.78329, 0.550147), 
    cameraTarget=(177.656, 118.983, 17.7063), viewOffsetX=-33.3823, 
    viewOffsetY=-28.7207)
session.viewports['Viewport: 1'].view.setValues(nearPlane=979.963, 
    farPlane=1392.37, width=395.705, height=214.743, cameraPosition=(990.562, 
    -482.482, 591.957), cameraUpVector=(-0.239846, 0.820393, 0.519066), 
    cameraTarget=(179.587, 118.366, 14.3526), viewOffsetX=-33.381, 
    viewOffsetY=-28.7196)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1001.8, 
    farPlane=1394.26, width=404.524, height=219.529, cameraPosition=(699.906, 
    -821.747, 513.064), cameraUpVector=(-0.166629, 0.69412, 0.700308), 
    cameraTarget=(180.556, 99.6604, 29.7333), viewOffsetX=-34.1249, 
    viewOffsetY=-29.3597)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1001.08, 
    farPlane=1394.97, width=404.234, height=219.372, cameraPosition=(697.357, 
    -821.508, 516.259), cameraUpVector=(-0.230665, 0.663848, 0.711407), 
    cameraTarget=(178.007, 99.8996, 32.928), viewOffsetX=-34.1005, 
    viewOffsetY=-29.3387)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1001.11, 
    farPlane=1394.95, width=404.245, height=219.378, cameraPosition=(700.983, 
    -821.916, 511.586), cameraUpVector=(-0.137844, 0.706903, 0.693748), 
    cameraTarget=(181.633, 99.4918, 28.2547), viewOffsetX=-34.1014, 
    viewOffsetY=-29.3395)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1001.11, 
    farPlane=1394.95, width=404.243, height=219.377, cameraPosition=(696.993, 
    -821.49, 516.685), cameraUpVector=(-0.239407, 0.659518, 0.712545), 
    cameraTarget=(177.643, 99.9176, 33.3539), viewOffsetX=-34.1013, 
    viewOffsetY=-29.3394)
session.viewports['Viewport: 1'].view.setValues(nearPlane=990.163, 
    farPlane=1403.04, width=399.823, height=216.978, cameraPosition=(773.163, 
    -839.155, 379.8), cameraUpVector=(-0.193747, 0.585585, 0.787117), 
    cameraTarget=(181.122, 98.3014, 29.1025), viewOffsetX=-33.7284, 
    viewOffsetY=-29.0186)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.rectangle(point1=(40.0, 0.0), point2=(-2.5, 15.0))
s.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=646.933, 
    farPlane=978.972, width=97.0566, height=51.1616, viewOffsetX=-16.2986, 
    viewOffsetY=110.056)
session.viewports['Viewport: 1'].view.setValues(nearPlane=646.468, 
    farPlane=979.437, width=96.9869, height=51.1249, viewOffsetX=-71.3157, 
    viewOffsetY=113.209)
session.viewports['Viewport: 1'].view.setValues(nearPlane=632.998, 
    farPlane=992.907, width=277.658, height=146.363, viewOffsetX=-108.21, 
    viewOffsetY=123.424)
session.viewports['Viewport: 1'].view.setValues(nearPlane=631.724, 
    farPlane=994.181, width=277.1, height=146.068, viewOffsetX=2.31378, 
    viewOffsetY=48.5251)
session.viewports['Viewport: 1'].view.setValues(nearPlane=627.281, 
    farPlane=998.624, width=352.419, height=185.771, viewOffsetX=-9.95242, 
    viewOffsetY=44.9402)
session.viewports['Viewport: 1'].view.setValues(nearPlane=625.622, 
    farPlane=1000.28, width=351.488, height=185.28, viewOffsetX=-11.5183, 
    viewOffsetY=28.4214)
session.viewports['Viewport: 1'].view.setValues(nearPlane=622.011, 
    farPlane=1003.89, width=420.739, height=221.785, viewOffsetX=-15.5688, 
    viewOffsetY=20.2397)
session.viewports['Viewport: 1'].view.setValues(nearPlane=620.047, 
    farPlane=1005.86, width=419.411, height=221.085, viewOffsetX=-12.4322, 
    viewOffsetY=9.45938)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    step='uniformed_load')
session.viewports['Viewport: 1'].view.setValues(nearPlane=707.514, 
    farPlane=921.866, width=610.281, height=321.698, cameraPosition=(367.29, 
    -2.2346, 786.862), cameraUpVector=(-0.278175, 0.946428, -0.163989), 
    cameraTarget=(157.676, 87.2664, 6.51501), viewOffsetX=82.5919, 
    viewOffsetY=-10.1696)
session.viewports['Viewport: 1'].view.setValues(nearPlane=704.968, 
    farPlane=924.411, width=608.085, height=320.54, cameraPosition=(367.48, 
    -4.17183, 786.589), cameraUpVector=(-0.296399, 0.941627, -0.159644), 
    cameraTarget=(157.866, 85.3292, 6.24171), viewOffsetX=82.2947, 
    viewOffsetY=-10.133)
session.viewports['Viewport: 1'].view.setValues(nearPlane=705.148, 
    farPlane=924.232, width=608.24, height=320.622, cameraPosition=(367.074, 
    0.728745, 787.26), cameraUpVector=(-0.250228, 0.953013, -0.17074), 
    cameraTarget=(157.46, 90.2298, 6.91277), viewOffsetX=82.3157, 
    viewOffsetY=-10.1356)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='ss_points')
session.viewports['Viewport: 1'].view.setValues(nearPlane=705.136, 
    farPlane=924.244, width=608.229, height=320.617, cameraPosition=(366.998, 
    2.27101, 787.457), cameraUpVector=(-0.235651, 0.956079, -0.174304), 
    cameraTarget=(157.384, 91.7721, 7.11013), viewOffsetX=82.3143, 
    viewOffsetY=-10.1354)
session.viewports['Viewport: 1'].view.setValues(nearPlane=663.606, 
    farPlane=1015.23, width=572.407, height=301.734, cameraPosition=(503.2, 
    -322.059, 638.16), cameraUpVector=(-0.18422, 0.942587, 0.278556), 
    cameraTarget=(163.328, 81.7344, 19.8339), viewOffsetX=77.4663, 
    viewOffsetY=-9.53846)
session.viewports['Viewport: 1'].view.setValues(nearPlane=680.107, 
    farPlane=946.761, width=586.64, height=309.237, cameraPosition=(283.92, 
    -299.297, 698.841), cameraUpVector=(-0.088018, 0.978544, 0.186289), 
    cameraTarget=(149.126, 98.0589, 2.54565), viewOffsetX=79.3925, 
    viewOffsetY=-9.77563)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='simple_test')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='ss_points')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='simple_test')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='ss_points')
session.viewports['Viewport: 1'].view.setValues(nearPlane=675.839, 
    farPlane=960.131, width=582.959, height=307.296, cameraPosition=(324.927, 
    -301.377, 694.141), cameraUpVector=(-0.0868158, 0.977054, 0.194495), 
    cameraTarget=(150.226, 97.1422, 7.44527), viewOffsetX=78.8942, 
    viewOffsetY=-9.71428)
session.viewports['Viewport: 1'].view.setValues(nearPlane=677.504, 
    farPlane=946.937, width=584.396, height=308.053, cameraPosition=(262.798, 
    -335.311, 678.493), cameraUpVector=(-0.11084, 0.966246, 0.232556), 
    cameraTarget=(148.179, 95.5941, -1.26618), viewOffsetX=79.0886, 
    viewOffsetY=-9.73822)
session.viewports['Viewport: 1'].view.setValues(nearPlane=677.388, 
    farPlane=947.054, width=584.296, height=308, cameraPosition=(263.881, 
    -352.514, 667.405), cameraUpVector=(-0.307997, 0.921313, 0.237317), 
    cameraTarget=(149.262, 78.3913, -12.3538), viewOffsetX=79.075, 
    viewOffsetY=-9.73655)
session.viewports['Viewport: 1'].view.setValues(nearPlane=677.396, 
    farPlane=947.046, width=584.302, height=308.003, cameraPosition=(263.313, 
    -330.165, 681.668), cameraUpVector=(-0.0515847, 0.97262, 0.226605), 
    cameraTarget=(148.694, 100.74, 1.90914), viewOffsetX=79.0759, 
    viewOffsetY=-9.73666)
session.viewports['Viewport: 1'].view.setValues(nearPlane=672.837, 
    farPlane=956.47, width=580.369, height=305.93, cameraPosition=(272.754, 
    -374.503, 652.021), cameraUpVector=(-0.0897896, 0.952865, 0.289804), 
    cameraTarget=(148.508, 96.1938, 0.947983), viewOffsetX=78.5437, 
    viewOffsetY=-9.67113)
session.viewports['Viewport: 1'].view.setValues(nearPlane=673.135, 
    farPlane=956.171, width=580.626, height=306.066, viewOffsetX=30.9053, 
    viewOffsetY=1.29009)
session.viewports['Viewport: 1'].view.setValues(nearPlane=673.137, 
    farPlane=956.17, width=580.627, height=306.067, viewOffsetX=32.8781, 
    viewOffsetY=-9.35291)
session.viewports['Viewport: 1'].view.setValues(nearPlane=659.779, 
    farPlane=986.018, width=569.105, height=299.993, cameraPosition=(254.795, 
    -576.464, 450.229), cameraUpVector=(-0.112015, 0.792042, 0.600102), 
    cameraTarget=(148.066, 91.8363, -0.184475), viewOffsetX=32.2257, 
    viewOffsetY=-9.16731)
session.viewports['Viewport: 1'].view.setValues(nearPlane=642.788, 
    farPlane=1028.78, width=554.449, height=292.267, cameraPosition=(364.663, 
    -679.286, 185.733), cameraUpVector=(-0.177458, 0.514774, 0.838759), 
    cameraTarget=(150.282, 81.6921, -3.58522), viewOffsetX=31.3958, 
    viewOffsetY=-8.93122)
session.viewports['Viewport: 1'].view.setValues(nearPlane=646.482, 
    farPlane=1033.16, width=557.635, height=293.947, cameraPosition=(364.269, 
    -701.947, 56.1757), cameraUpVector=(-0.171678, 0.374948, 0.911011), 
    cameraTarget=(150.31, 79.68, -8.38889), viewOffsetX=31.5762, 
    viewOffsetY=-8.98254)
session.viewports['Viewport: 1'].view.setValues(nearPlane=652.066, 
    farPlane=1032.45, width=562.452, height=296.486, cameraPosition=(341.829, 
    -709.635, -44.8356), cameraUpVector=(-0.161266, 0.265417, 0.950551), 
    cameraTarget=(149.333, 79.5454, -12.7725), viewOffsetX=31.849, 
    viewOffsetY=-9.06013)
session.viewports['Viewport: 1'].view.setValues(nearPlane=651.441, 
    farPlane=1007.45, width=561.913, height=296.202, cameraPosition=(309.114, 
    -631.079, 346.716), cameraUpVector=(-0.180477, 0.677687, 0.712859), 
    cameraTarget=(147.617, 87.5958, 2.7484), viewOffsetX=31.8185, 
    viewOffsetY=-9.05145)
odb = session.odbs['Y:/ss_points.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='ss_points', frame=0)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='ss_points', frame=1)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='ss_points', frame=0)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='ss_points', frame=1)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='simple_test', frame=0)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='simple_test', frame=1)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='clamped_edges', frame=0)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='clamped_edges', frame=1)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='points_load', frame=0)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='points_load', frame=1)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='uniformed_load', frame=0)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='uniformed_load', frame=1)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='uniformed_load', frame=0)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='ss_points', frame=0)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=3, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=3, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=4, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=4, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=4, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=4, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=4, frame=1 )
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF, adaptiveMeshConstraints=ON)
mdb.models['Model-1'].StaticStep(name='turbo', previous='Initial', 
    maxNumInc=200, initialInc=0.01, minInc=1e-05, maxInc=0.01)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='turbo')
mdb.models['Model-1'].steps['ss_points'].suppress()
mdb.models['Model-1'].steps['simple_test'].suppress()
mdb.models['Model-1'].steps['clamped_edges'].suppress()
mdb.models['Model-1'].steps['points_load'].suppress()
mdb.models['Model-1'].steps['uniformed_load'].suppress()
mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].resume()
#* Cannot resume while the step is still suppressed.  Resume the step first.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
mdb.models['Model-1'].BoundaryCondition(name='ss-Copy', 
    objectToCopy=mdb.models['Model-1'].boundaryConditions['ss'], 
    toStepName='turbo')
#* Suppressed boundary condition can only be copied to the step in which it was 
#* created.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='turbo')
mdb.models['Model-1'].boundaryConditions['fixed'].suppress()
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Part-1-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#f ]', ), )
region = a.Set(edges=edges1, name='Set-5')
mdb.models['Model-1'].DisplacementBC(name='ss_static', createStepName='turbo', 
    region=region, u1=0.0, u2=0.0, u3=0.0, ur1=UNSET, ur2=UNSET, ur3=UNSET, 
    amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', 
    localCsys=None)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Part-1-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
region = a.Surface(side1Faces=side1Faces1, name='Surf-3')
mdb.models['Model-1'].Pressure(name='s_ss_uniformed', createStepName='turbo', 
    region=region, distributionType=UNIFORM, field='', magnitude=2.0, 
    amplitude=UNSET)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF, 
    bcs=OFF, predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
mdb.Job(name='turbo_job', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=4, numDomains=4, numGPUs=0)
mdb.jobs['turbo_job'].submit(consistencyChecking=OFF)
#: The job input file "turbo_job.inp" has been submitted for analysis.
#: Job turbo_job: Analysis Input File Processor completed successfully.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
#: Job turbo_job: Abaqus/Standard completed successfully.
#: Job turbo_job completed successfully. 
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['Part-1']
p.deleteMesh()
p = mdb.models['Model-1'].parts['Part-1']
p.seedPart(size=10.0, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Part-1']
p.generateMesh()
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
mdb.Job(name='turbo_job_10', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=4, numDomains=4, numGPUs=0)
o3 = session.openOdb(name='Y:/turbo_job.odb')
#: Model: Y:/turbo_job.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       5
#: Number of Node Sets:          8
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=100 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=99 )
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='turbo', frame=78)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='turbo', frame=66)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='turbo', frame=55)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='turbo', frame=38)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='turbo', frame=6)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='turbo', frame=5)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='turbo', frame=0)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='turbo', frame=3)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='turbo', frame=100)
session.viewports['Viewport: 1'].view.setValues(nearPlane=990.375, 
    farPlane=1408.18, width=767.393, height=416.452, cameraPosition=(-421.483, 
    -533.069, 823.047), cameraUpVector=(0.158404, 0.92665, 0.340922), 
    cameraTarget=(153.055, 82.203, 20.7551))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1019.82, 
    farPlane=1395.36, width=790.209, height=428.834, cameraPosition=(57.4082, 
    -1050.79, 308.215), cameraUpVector=(-0.377169, 0.579996, 0.722045), 
    cameraTarget=(167.583, 66.497, 5.1368))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1023.7, 
    farPlane=1396, width=793.213, height=430.464, cameraPosition=(258.389, 
    -1094.99, -17.832), cameraUpVector=(-0.400138, 0.297299, 0.866893), 
    cameraTarget=(175.022, 64.8611, -6.93073))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1012.68, 
    farPlane=1401.39, width=784.673, height=425.83, cameraPosition=(25.4248, 
    -1084.6, 99.5292), cameraUpVector=(-0.196796, 0.438866, 0.876737), 
    cameraTarget=(165.98, 65.2644, -2.3758))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1032.24, 
    farPlane=1384.78, width=799.83, height=434.055, cameraPosition=(165.935, 
    -1093.58, -110.748), cameraUpVector=(-0.205828, 0.253368, 0.945219), 
    cameraTarget=(171.118, 64.9359, -10.0652))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1017.19, 
    farPlane=1397.91, width=788.169, height=427.726, cameraPosition=(63.3692, 
    -1088.21, 104.444), cameraUpVector=(0.0642168, 0.414062, 0.907981), 
    cameraTarget=(167.247, 65.1386, -1.94267))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1017.71, 
    farPlane=1396.83, width=788.568, height=427.943, cameraPosition=(54.4293, 
    -1092.46, -9.04724), cameraUpVector=(-0.00440032, 0.332964, 0.942929), 
    cameraTarget=(166.916, 64.9816, -6.1397))
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='turbo', frame=96)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='turbo', frame=0)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='turbo', frame=1)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='turbo', frame=2)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='turbo', frame=3)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='turbo', frame=4)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='turbo', frame=13)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='turbo', frame=14)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='turbo', frame=15)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='turbo', frame=16)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='turbo', frame=17)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='turbo', frame=44)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='turbo', frame=71)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='turbo', frame=90)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='turbo', frame=0)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='turbo', frame=1)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='turbo', frame=2)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='turbo', frame=3)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='turbo', frame=0)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='turbo', frame=1)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='turbo', frame=2)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='turbo', frame=3)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='turbo', frame=4)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='turbo', frame=5)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='turbo', frame=6)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    deformationScaling=UNIFORM, uniformScaleFactor=1)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='turbo', frame=33)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='turbo', frame=56)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1059.24, 
    farPlane=1355.38, width=297.743, height=161.581, viewOffsetX=-49.2082, 
    viewOffsetY=-1.37928)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='turbo', frame=73)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='turbo', frame=88)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    uniformScaleFactor=100)
session.viewports['Viewport: 1'].view.setValues(nearPlane=998.13, 
    farPlane=1416.17, width=1086.3, height=589.516, viewOffsetX=-265.371, 
    viewOffsetY=19.2406)
session.viewports['Viewport: 1'].view.setValues(nearPlane=993.139, 
    farPlane=1421.16, width=1080.86, height=586.568, cameraPosition=(54.5963, 
    -1092.5, -0.960694), cameraUpVector=(-0.027956, 0.335256, 0.941712), 
    cameraTarget=(167.083, 64.9451, 1.94685), viewOffsetX=-264.044, 
    viewOffsetY=19.1443)
session.viewports['Viewport: 1'].view.setValues(nearPlane=993.586, 
    farPlane=1420.72, width=1081.35, height=586.832, cameraPosition=(51.524, 
    -1092.1, -42.868), cameraUpVector=(0.0945875, 0.323347, 0.941541), 
    cameraTarget=(164.011, 65.3489, -39.9605), viewOffsetX=-264.163, 
    viewOffsetY=19.1529)
session.viewports['Viewport: 1'].view.setValues(nearPlane=968.827, 
    farPlane=1373.85, width=1054.4, height=572.209, cameraPosition=(190.995, 
    -1060.38, -59.1101), cameraUpVector=(0.0642964, 0.321394, 0.94476), 
    cameraTarget=(170.155, 102.229, -42.894), viewOffsetX=-257.58, 
    viewOffsetY=18.6756)
session.viewports['Viewport: 1'].view.setValues(nearPlane=970.833, 
    farPlane=1371.85, width=1056.59, height=573.394, viewOffsetX=-21.1887, 
    viewOffsetY=-0.0662956)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='turbo', frame=87)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='turbo', frame=80)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='turbo', frame=0)
mdb.save()
#: The model database has been saved to "Y:\mb_sss_points.cae".
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    uniformScaleFactor=10)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='turbo', frame=23)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='turbo', frame=38)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='turbo', frame=100)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    uniformScaleFactor=100)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='turbo', frame=100)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1013.87, 
    farPlane=1328.57, width=558.666, height=303.179, viewOffsetX=-25.6583, 
    viewOffsetY=15.5145)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1011.24, 
    farPlane=1331.2, width=557.217, height=302.393, viewOffsetX=-23.0675, 
    viewOffsetY=5.87934)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1011.36, 
    farPlane=1331.08, width=557.284, height=302.429, viewOffsetX=-12.9723, 
    viewOffsetY=-15.7884)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1005.66, 
    farPlane=1338.26, width=554.14, height=300.723, cameraPosition=(181.653, 
    -1047.98, 111.852), cameraUpVector=(0.0347256, 0.454888, 0.889871), 
    cameraTarget=(169.502, 104.735, -41.3145), viewOffsetX=-12.8991, 
    viewOffsetY=-15.6993)
session.viewports['Viewport: 1'].view.setValues(nearPlane=996.509, 
    farPlane=1350.14, width=549.098, height=297.987, cameraPosition=(178.385, 
    -953.905, 428.831), cameraUpVector=(0.0774541, 0.684889, 0.724519), 
    cameraTarget=(170.237, 109.891, -40.8816), viewOffsetX=-12.7817, 
    viewOffsetY=-15.5564)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='turbo', frame=100)
session.viewports['Viewport: 1'].view.setValues(nearPlane=967.997, 
    farPlane=1374.93, width=533.388, height=289.461, cameraPosition=(490.766, 
    -995.349, 130.098), cameraUpVector=(0.0348958, 0.497283, 0.866886), 
    cameraTarget=(173.246, 109.759, -43.8997), viewOffsetX=-12.416, 
    viewOffsetY=-15.1113)
session.viewports['Viewport: 1'].view.setValues(nearPlane=966.957, 
    farPlane=1376.81, width=532.815, height=289.15, cameraPosition=(-235.439, 
    -993.484, -103.727), cameraUpVector=(0.194511, 0.231888, 0.953097), 
    cameraTarget=(166.773, 96.0287, -44.1776), viewOffsetX=-12.4027, 
    viewOffsetY=-15.0951)
session.viewports['Viewport: 1'].view.setValues(nearPlane=988.684, 
    farPlane=1356.13, width=544.787, height=295.647, cameraPosition=(283.601, 
    -1008.46, 261.845), cameraUpVector=(0.0443942, 0.573896, 0.817724), 
    cameraTarget=(171.553, 108.469, -41.9148), viewOffsetX=-12.6814, 
    viewOffsetY=-15.4343)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1002.4, 
    farPlane=1342.2, width=552.343, height=299.748, cameraPosition=(189.36, 
    -1032.59, 193.98), cameraUpVector=(0.0754706, 0.518193, 0.851927), 
    cameraTarget=(170.933, 105.99, -41.93), viewOffsetX=-12.8573, 
    viewOffsetY=-15.6484)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1003, 
    farPlane=1339.95, width=552.672, height=299.927, cameraPosition=(84.8251, 
    -1058.96, -69.2941), cameraUpVector=(0.166966, 0.302064, 0.938552), 
    cameraTarget=(171.124, 100.484, -44.7884), viewOffsetX=-12.865, 
    viewOffsetY=-15.6577)
session.viewports['Viewport: 1'].view.setValues(nearPlane=993.379, 
    farPlane=1351.72, width=547.371, height=297.05, cameraPosition=(93.589, 
    -1025.15, 220.997), cameraUpVector=(0.0660986, 0.533918, 0.842949), 
    cameraTarget=(169.467, 105.296, -41.1112), viewOffsetX=-12.7416, 
    viewOffsetY=-15.5075)
session.viewports['Viewport: 1'].view.setValues(nearPlane=991.635, 
    farPlane=1354.47, width=546.41, height=296.528, cameraPosition=(108.072, 
    -982.844, 358.012), cameraUpVector=(0.015819, 0.635812, 0.771682), 
    cameraTarget=(168.73, 108.207, -39.8529), viewOffsetX=-12.7192, 
    viewOffsetY=-15.4803)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.jobs['turbo_job_10'].submit(consistencyChecking=OFF)
#: The job input file "turbo_job_10.inp" has been submitted for analysis.
#: Job turbo_job_10: Analysis Input File Processor completed successfully.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
#: Job turbo_job_10: Abaqus/Standard completed successfully.
#: Job turbo_job_10 completed successfully. 
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
o3 = session.openOdb(name='Y:/turbo_job_10.odb')
#: Model: Y:/turbo_job_10.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       5
#: Number of Node Sets:          6
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
odb = session.odbs['Y:/turbo_job.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
odb = session.odbs['Y:/turbo_job_10.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['Y:/turbo_job_10.odb'])
odb = session.odbs['Y:/turbo_job_10.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U2'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='turbo', frame=72)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='turbo', frame=35)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='turbo', frame=0)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF, adaptiveMeshConstraints=ON)
regionDef=mdb.models['Model-1'].rootAssembly.sets['Set-5']
mdb.models['Model-1'].HistoryOutputRequest(name='history', 
    createStepName='turbo', variables=('RF3', ), region=regionDef, 
    sectionPoints=DEFAULT, rebar=EXCLUDE)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
mdb.jobs['turbo_job_10'].submit(consistencyChecking=OFF)
#: The job input file "turbo_job_10.inp" has been submitted for analysis.
#: Job turbo_job_10: Analysis Input File Processor completed successfully.
mdb.save()
#: The model database has been saved to "Y:\mb_sss_points.cae".
#: Job turbo_job_10: Abaqus/Standard completed successfully.
#: Job turbo_job_10 completed successfully. 
session.viewports['Viewport: 1'].view.setValues(nearPlane=653.823, 
    farPlane=1005.07, width=503.435, height=246.92, viewOffsetX=-5.51149, 
    viewOffsetY=-31.5862)
mdb.save()
#: The model database has been saved to "Y:\mb_sss_points.cae".
o3 = session.openOdb(name='Y:/turbo_job_10.odb')
#: Model: Y:/turbo_job_10.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       5
#: Number of Node Sets:          6
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
odb = session.odbs['Y:/turbo_job_10.odb']
xy1 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 1 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c1 = session.Curve(xyData=xy1)
xy2 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 2 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c2 = session.Curve(xyData=xy2)
xy3 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 3 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c3 = session.Curve(xyData=xy3)
xy4 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 4 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c4 = session.Curve(xyData=xy4)
xy5 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 5 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c5 = session.Curve(xyData=xy5)
xy6 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 6 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c6 = session.Curve(xyData=xy6)
xy7 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 7 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c7 = session.Curve(xyData=xy7)
xy8 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 8 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c8 = session.Curve(xyData=xy8)
xy9 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 9 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c9 = session.Curve(xyData=xy9)
xy10 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 10 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c10 = session.Curve(xyData=xy10)
xy11 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 11 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c11 = session.Curve(xyData=xy11)
xy12 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 12 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c12 = session.Curve(xyData=xy12)
xy13 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 13 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c13 = session.Curve(xyData=xy13)
xy14 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 14 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c14 = session.Curve(xyData=xy14)
xy15 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 15 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c15 = session.Curve(xyData=xy15)
xy16 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 16 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c16 = session.Curve(xyData=xy16)
xy17 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 17 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c17 = session.Curve(xyData=xy17)
xy18 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 18 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c18 = session.Curve(xyData=xy18)
xy19 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 19 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c19 = session.Curve(xyData=xy19)
xy20 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 20 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c20 = session.Curve(xyData=xy20)
xy21 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 21 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c21 = session.Curve(xyData=xy21)
xy22 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 22 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c22 = session.Curve(xyData=xy22)
xy23 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 23 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c23 = session.Curve(xyData=xy23)
xy24 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 24 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c24 = session.Curve(xyData=xy24)
xy25 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 46 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c25 = session.Curve(xyData=xy25)
xy26 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 47 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c26 = session.Curve(xyData=xy26)
xy27 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 69 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c27 = session.Curve(xyData=xy27)
xy28 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 70 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c28 = session.Curve(xyData=xy28)
xy29 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 92 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c29 = session.Curve(xyData=xy29)
xy30 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 93 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c30 = session.Curve(xyData=xy30)
xy31 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 115 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c31 = session.Curve(xyData=xy31)
xy32 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 116 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c32 = session.Curve(xyData=xy32)
xy33 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 138 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c33 = session.Curve(xyData=xy33)
xy34 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 139 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c34 = session.Curve(xyData=xy34)
xy35 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 161 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c35 = session.Curve(xyData=xy35)
xy36 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 162 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c36 = session.Curve(xyData=xy36)
xy37 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 184 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c37 = session.Curve(xyData=xy37)
xy38 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 185 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c38 = session.Curve(xyData=xy38)
xy39 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 207 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c39 = session.Curve(xyData=xy39)
xy40 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 208 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c40 = session.Curve(xyData=xy40)
xy41 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 230 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c41 = session.Curve(xyData=xy41)
xy42 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 231 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c42 = session.Curve(xyData=xy42)
xy43 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 253 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c43 = session.Curve(xyData=xy43)
xy44 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 254 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c44 = session.Curve(xyData=xy44)
xy45 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 276 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c45 = session.Curve(xyData=xy45)
xy46 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 277 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c46 = session.Curve(xyData=xy46)
xy47 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 299 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c47 = session.Curve(xyData=xy47)
xy48 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 300 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c48 = session.Curve(xyData=xy48)
xy49 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 322 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c49 = session.Curve(xyData=xy49)
xy50 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 323 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c50 = session.Curve(xyData=xy50)
xy51 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 345 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c51 = session.Curve(xyData=xy51)
xy52 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 346 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c52 = session.Curve(xyData=xy52)
xy53 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 368 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c53 = session.Curve(xyData=xy53)
xy54 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 369 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c54 = session.Curve(xyData=xy54)
xy55 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 391 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c55 = session.Curve(xyData=xy55)
xy56 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 392 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c56 = session.Curve(xyData=xy56)
xy57 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 414 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c57 = session.Curve(xyData=xy57)
xy58 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 415 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c58 = session.Curve(xyData=xy58)
xy59 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 437 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c59 = session.Curve(xyData=xy59)
xy60 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 438 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c60 = session.Curve(xyData=xy60)
xy61 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 460 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c61 = session.Curve(xyData=xy61)
xy62 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 461 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c62 = session.Curve(xyData=xy62)
xy63 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 483 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c63 = session.Curve(xyData=xy63)
xy64 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 484 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c64 = session.Curve(xyData=xy64)
xy65 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 506 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c65 = session.Curve(xyData=xy65)
xy66 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 507 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c66 = session.Curve(xyData=xy66)
xy67 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 529 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c67 = session.Curve(xyData=xy67)
xy68 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 530 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c68 = session.Curve(xyData=xy68)
xy69 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 552 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c69 = session.Curve(xyData=xy69)
xy70 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 553 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c70 = session.Curve(xyData=xy70)
xy71 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 575 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c71 = session.Curve(xyData=xy71)
xy72 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 576 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c72 = session.Curve(xyData=xy72)
xy73 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 598 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c73 = session.Curve(xyData=xy73)
xy74 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 599 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c74 = session.Curve(xyData=xy74)
xy75 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 621 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c75 = session.Curve(xyData=xy75)
xy76 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 622 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c76 = session.Curve(xyData=xy76)
xy77 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 644 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c77 = session.Curve(xyData=xy77)
xy78 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 645 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c78 = session.Curve(xyData=xy78)
xy79 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 667 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c79 = session.Curve(xyData=xy79)
xy80 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 668 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c80 = session.Curve(xyData=xy80)
xy81 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 690 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c81 = session.Curve(xyData=xy81)
xy82 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 691 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c82 = session.Curve(xyData=xy82)
xy83 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 713 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c83 = session.Curve(xyData=xy83)
xy84 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 714 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c84 = session.Curve(xyData=xy84)
xy85 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 715 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c85 = session.Curve(xyData=xy85)
xy86 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 716 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c86 = session.Curve(xyData=xy86)
xy87 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 717 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c87 = session.Curve(xyData=xy87)
xy88 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 718 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c88 = session.Curve(xyData=xy88)
xy89 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 719 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c89 = session.Curve(xyData=xy89)
xy90 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 720 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c90 = session.Curve(xyData=xy90)
xy91 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 721 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c91 = session.Curve(xyData=xy91)
xy92 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 722 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c92 = session.Curve(xyData=xy92)
xy93 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 723 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c93 = session.Curve(xyData=xy93)
xy94 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 724 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c94 = session.Curve(xyData=xy94)
xy95 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 725 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c95 = session.Curve(xyData=xy95)
xy96 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 726 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c96 = session.Curve(xyData=xy96)
xy97 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 727 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c97 = session.Curve(xyData=xy97)
xy98 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 728 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c98 = session.Curve(xyData=xy98)
xy99 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 729 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c99 = session.Curve(xyData=xy99)
xy100 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 730 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c100 = session.Curve(xyData=xy100)
xy101 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 731 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c101 = session.Curve(xyData=xy101)
xy102 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 732 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c102 = session.Curve(xyData=xy102)
xy103 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 733 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c103 = session.Curve(xyData=xy103)
xy104 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 734 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c104 = session.Curve(xyData=xy104)
xy105 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 735 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c105 = session.Curve(xyData=xy105)
xy106 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 736 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
c106 = session.Curve(xyData=xy106)
xyp = session.XYPlot('XYPlot-1')
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
chart.setValues(curvesToPlot=(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, 
    c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25, c26, 
    c27, c28, c29, c30, c31, c32, c33, c34, c35, c36, c37, c38, c39, c40, c41, 
    c42, c43, c44, c45, c46, c47, c48, c49, c50, c51, c52, c53, c54, c55, c56, 
    c57, c58, c59, c60, c61, c62, c63, c64, c65, c66, c67, c68, c69, c70, c71, 
    c72, c73, c74, c75, c76, c77, c78, c79, c80, c81, c82, c83, c84, c85, c86, 
    c87, c88, c89, c90, c91, c92, c93, c94, c95, c96, c97, c98, c99, c100, 
    c101, c102, c103, c104, c105, c106, ), )
session.charts[chartName].autoColor(lines=True, symbols=True)
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
odb = session.odbs['Y:/turbo_job_10.odb']
xy0 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 1 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy1 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 2 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy2 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 3 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy3 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 4 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy4 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 5 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy5 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 6 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy6 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 7 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy7 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 8 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy8 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 9 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy9 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 10 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy10 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 11 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy11 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 12 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy12 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 13 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy13 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 14 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy14 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 15 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy15 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 16 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy16 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 17 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy17 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 18 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy18 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 19 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy19 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 20 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy20 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 21 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy21 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 22 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy22 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 23 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy23 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 24 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy24 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 46 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy25 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 47 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy26 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 69 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy27 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 70 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy28 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 92 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy29 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 93 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy30 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 115 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy31 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 116 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy32 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 138 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy33 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 139 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy34 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 161 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy35 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 162 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy36 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 184 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy37 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 185 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy38 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 207 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy39 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 208 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy40 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 230 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy41 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 231 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy42 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 253 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy43 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 254 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy44 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 276 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy45 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 277 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy46 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 299 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy47 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 300 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy48 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 322 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy49 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 323 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy50 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 345 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy51 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 346 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy52 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 368 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy53 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 369 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy54 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 391 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy55 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 392 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy56 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 414 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy57 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 415 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy58 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 437 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy59 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 438 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy60 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 460 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy61 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 461 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy62 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 483 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy63 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 484 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy64 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 506 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy65 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 507 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy66 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 529 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy67 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 530 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy68 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 552 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy69 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 553 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy70 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 575 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy71 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 576 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy72 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 598 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy73 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 599 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy74 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 621 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy75 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 622 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy76 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 644 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy77 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 645 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy78 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 667 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy79 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 668 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy80 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 690 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy81 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 691 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy82 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 713 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy83 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 714 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy84 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 715 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy85 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 716 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy86 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 717 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy87 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 718 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy88 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 719 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy89 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 720 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy90 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 721 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy91 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 722 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy92 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 723 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy93 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 724 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy94 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 725 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy95 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 726 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy96 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 727 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy97 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 728 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy98 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 729 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy99 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 730 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy100 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 731 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy101 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 732 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy102 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 733 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy103 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 734 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy104 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 735 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy105 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 736 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy106 = sum((xy0, xy1, xy2, xy3, xy4, xy5, xy6, xy7, xy8, xy9, xy10, xy11, 
    xy12, xy13, xy14, xy15, xy16, xy17, xy18, xy19, xy20, xy21, xy22, xy23, 
    xy24, xy25, xy26, xy27, xy28, xy29, xy30, xy31, xy32, xy33, xy34, xy35, 
    xy36, xy37, xy38, xy39, xy40, xy41, xy42, xy43, xy44, xy45, xy46, xy47, 
    xy48, xy49, xy50, xy51, xy52, xy53, xy54, xy55, xy56, xy57, xy58, xy59, 
    xy60, xy61, xy62, xy63, xy64, xy65, xy66, xy67, xy68, xy69, xy70, xy71, 
    xy72, xy73, xy74, xy75, xy76, xy77, xy78, xy79, xy80, xy81, xy82, xy83, 
    xy84, xy85, xy86, xy87, xy88, xy89, xy90, xy91, xy92, xy93, xy94, xy95, 
    xy96, xy97, xy98, xy99, xy100, xy101, xy102, xy103, xy104, xy105, ), )
session.XYData(name='XYData-1', objectToCopy=xy106, 
    sourceDescription='sum((XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, XYData-1, ),)')
del session.xyDataObjects[xy0.name]
del session.xyDataObjects[xy1.name]
del session.xyDataObjects[xy2.name]
del session.xyDataObjects[xy3.name]
del session.xyDataObjects[xy4.name]
del session.xyDataObjects[xy5.name]
del session.xyDataObjects[xy6.name]
del session.xyDataObjects[xy7.name]
del session.xyDataObjects[xy8.name]
del session.xyDataObjects[xy9.name]
del session.xyDataObjects[xy10.name]
del session.xyDataObjects[xy11.name]
del session.xyDataObjects[xy12.name]
del session.xyDataObjects[xy13.name]
del session.xyDataObjects[xy14.name]
del session.xyDataObjects[xy15.name]
del session.xyDataObjects[xy16.name]
del session.xyDataObjects[xy17.name]
del session.xyDataObjects[xy18.name]
del session.xyDataObjects[xy19.name]
del session.xyDataObjects[xy20.name]
del session.xyDataObjects[xy21.name]
del session.xyDataObjects[xy22.name]
del session.xyDataObjects[xy23.name]
del session.xyDataObjects[xy24.name]
del session.xyDataObjects[xy25.name]
del session.xyDataObjects[xy26.name]
del session.xyDataObjects[xy27.name]
del session.xyDataObjects[xy28.name]
del session.xyDataObjects[xy29.name]
del session.xyDataObjects[xy30.name]
del session.xyDataObjects[xy31.name]
del session.xyDataObjects[xy32.name]
del session.xyDataObjects[xy33.name]
del session.xyDataObjects[xy34.name]
del session.xyDataObjects[xy35.name]
del session.xyDataObjects[xy36.name]
del session.xyDataObjects[xy37.name]
del session.xyDataObjects[xy38.name]
del session.xyDataObjects[xy39.name]
del session.xyDataObjects[xy40.name]
del session.xyDataObjects[xy41.name]
del session.xyDataObjects[xy42.name]
del session.xyDataObjects[xy43.name]
del session.xyDataObjects[xy44.name]
del session.xyDataObjects[xy45.name]
del session.xyDataObjects[xy46.name]
del session.xyDataObjects[xy47.name]
del session.xyDataObjects[xy48.name]
del session.xyDataObjects[xy49.name]
del session.xyDataObjects[xy50.name]
del session.xyDataObjects[xy51.name]
del session.xyDataObjects[xy52.name]
del session.xyDataObjects[xy53.name]
del session.xyDataObjects[xy54.name]
del session.xyDataObjects[xy55.name]
del session.xyDataObjects[xy56.name]
del session.xyDataObjects[xy57.name]
del session.xyDataObjects[xy58.name]
del session.xyDataObjects[xy59.name]
del session.xyDataObjects[xy60.name]
del session.xyDataObjects[xy61.name]
del session.xyDataObjects[xy62.name]
del session.xyDataObjects[xy63.name]
del session.xyDataObjects[xy64.name]
del session.xyDataObjects[xy65.name]
del session.xyDataObjects[xy66.name]
del session.xyDataObjects[xy67.name]
del session.xyDataObjects[xy68.name]
del session.xyDataObjects[xy69.name]
del session.xyDataObjects[xy70.name]
del session.xyDataObjects[xy71.name]
del session.xyDataObjects[xy72.name]
del session.xyDataObjects[xy73.name]
del session.xyDataObjects[xy74.name]
del session.xyDataObjects[xy75.name]
del session.xyDataObjects[xy76.name]
del session.xyDataObjects[xy77.name]
del session.xyDataObjects[xy78.name]
del session.xyDataObjects[xy79.name]
del session.xyDataObjects[xy80.name]
del session.xyDataObjects[xy81.name]
del session.xyDataObjects[xy82.name]
del session.xyDataObjects[xy83.name]
del session.xyDataObjects[xy84.name]
del session.xyDataObjects[xy85.name]
del session.xyDataObjects[xy86.name]
del session.xyDataObjects[xy87.name]
del session.xyDataObjects[xy88.name]
del session.xyDataObjects[xy89.name]
del session.xyDataObjects[xy90.name]
del session.xyDataObjects[xy91.name]
del session.xyDataObjects[xy92.name]
del session.xyDataObjects[xy93.name]
del session.xyDataObjects[xy94.name]
del session.xyDataObjects[xy95.name]
del session.xyDataObjects[xy96.name]
del session.xyDataObjects[xy97.name]
del session.xyDataObjects[xy98.name]
del session.xyDataObjects[xy99.name]
del session.xyDataObjects[xy100.name]
del session.xyDataObjects[xy101.name]
del session.xyDataObjects[xy102.name]
del session.xyDataObjects[xy103.name]
del session.xyDataObjects[xy104.name]
del session.xyDataObjects[xy105.name]
del session.xyDataObjects[xy106.name]
odb = session.odbs['Y:/turbo_job_10.odb']
xy0 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 1 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy1 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 2 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy2 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 3 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy3 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 4 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy4 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 5 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy5 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 6 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy6 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 7 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy7 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 8 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy8 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 9 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy9 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 10 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy10 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 11 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy11 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 12 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy12 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 13 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy13 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 14 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy14 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 15 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy15 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 16 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy16 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 17 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy17 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 18 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy18 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 19 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy19 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 20 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy20 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 21 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy21 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 22 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy22 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 23 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy23 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 24 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy24 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 46 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy25 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 47 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy26 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 69 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy27 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 70 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy28 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 92 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy29 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 93 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy30 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 115 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy31 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 116 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy32 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 138 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy33 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 139 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy34 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 161 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy35 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 162 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy36 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 184 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy37 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 185 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy38 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 207 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy39 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 208 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy40 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 230 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy41 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 231 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy42 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 253 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy43 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 254 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy44 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 276 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy45 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 277 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy46 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 299 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy47 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 300 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy48 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 322 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy49 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 323 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy50 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 345 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy51 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 346 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy52 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 368 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy53 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 369 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy54 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 391 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy55 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 392 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy56 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 414 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy57 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 415 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy58 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 437 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy59 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 438 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy60 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 460 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy61 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 461 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy62 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 483 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy63 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 484 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy64 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 506 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy65 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 507 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy66 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 529 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy67 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 530 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy68 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 552 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy69 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 553 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy70 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 575 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy71 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 576 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy72 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 598 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy73 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 599 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy74 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 621 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy75 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 622 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy76 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 644 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy77 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 645 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy78 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 667 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy79 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 668 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy80 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 690 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy81 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 691 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy82 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 713 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy83 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 714 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy84 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 715 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy85 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 716 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy86 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 717 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy87 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 718 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy88 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 719 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy89 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 720 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy90 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 721 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy91 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 722 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy92 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 723 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy93 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 724 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy94 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 725 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy95 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 726 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy96 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 727 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy97 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 728 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy98 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 729 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy99 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 730 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy100 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 731 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy101 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 732 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy102 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 733 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy103 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 734 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy104 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 735 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy105 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Reaction force: RF3 at Node 736 in NSET SET-5', steps=(
    'turbo', ), suppressQuery=True, __linkedVpName__='Viewport: 1')
xy106 = sum((xy0, xy1, xy2, xy3, xy4, xy5, xy6, xy7, xy8, xy9, xy10, xy11, 
    xy12, xy13, xy14, xy15, xy16, xy17, xy18, xy19, xy20, xy21, xy22, xy23, 
    xy24, xy25, xy26, xy27, xy28, xy29, xy30, xy31, xy32, xy33, xy34, xy35, 
    xy36, xy37, xy38, xy39, xy40, xy41, xy42, xy43, xy44, xy45, xy46, xy47, 
    xy48, xy49, xy50, xy51, xy52, xy53, xy54, xy55, xy56, xy57, xy58, xy59, 
    xy60, xy61, xy62, xy63, xy64, xy65, xy66, xy67, xy68, xy69, xy70, xy71, 
    xy72, xy73, xy74, xy75, xy76, xy77, xy78, xy79, xy80, xy81, xy82, xy83, 
    xy84, xy85, xy86, xy87, xy88, xy89, xy90, xy91, xy92, xy93, xy94, xy95, 
    xy96, xy97, xy98, xy99, xy100, xy101, xy102, xy103, xy104, xy105, ), )
session.XYData(name='rf3', objectToCopy=xy106, 
    sourceDescription='sum((rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, rf3, ),)')
del session.xyDataObjects[xy0.name]
del session.xyDataObjects[xy1.name]
del session.xyDataObjects[xy2.name]
del session.xyDataObjects[xy3.name]
del session.xyDataObjects[xy4.name]
del session.xyDataObjects[xy5.name]
del session.xyDataObjects[xy6.name]
del session.xyDataObjects[xy7.name]
del session.xyDataObjects[xy8.name]
del session.xyDataObjects[xy9.name]
del session.xyDataObjects[xy10.name]
del session.xyDataObjects[xy11.name]
del session.xyDataObjects[xy12.name]
del session.xyDataObjects[xy13.name]
del session.xyDataObjects[xy14.name]
del session.xyDataObjects[xy15.name]
del session.xyDataObjects[xy16.name]
del session.xyDataObjects[xy17.name]
del session.xyDataObjects[xy18.name]
del session.xyDataObjects[xy19.name]
del session.xyDataObjects[xy20.name]
del session.xyDataObjects[xy21.name]
del session.xyDataObjects[xy22.name]
del session.xyDataObjects[xy23.name]
del session.xyDataObjects[xy24.name]
del session.xyDataObjects[xy25.name]
del session.xyDataObjects[xy26.name]
del session.xyDataObjects[xy27.name]
del session.xyDataObjects[xy28.name]
del session.xyDataObjects[xy29.name]
del session.xyDataObjects[xy30.name]
del session.xyDataObjects[xy31.name]
del session.xyDataObjects[xy32.name]
del session.xyDataObjects[xy33.name]
del session.xyDataObjects[xy34.name]
del session.xyDataObjects[xy35.name]
del session.xyDataObjects[xy36.name]
del session.xyDataObjects[xy37.name]
del session.xyDataObjects[xy38.name]
del session.xyDataObjects[xy39.name]
del session.xyDataObjects[xy40.name]
del session.xyDataObjects[xy41.name]
del session.xyDataObjects[xy42.name]
del session.xyDataObjects[xy43.name]
del session.xyDataObjects[xy44.name]
del session.xyDataObjects[xy45.name]
del session.xyDataObjects[xy46.name]
del session.xyDataObjects[xy47.name]
del session.xyDataObjects[xy48.name]
del session.xyDataObjects[xy49.name]
del session.xyDataObjects[xy50.name]
del session.xyDataObjects[xy51.name]
del session.xyDataObjects[xy52.name]
del session.xyDataObjects[xy53.name]
del session.xyDataObjects[xy54.name]
del session.xyDataObjects[xy55.name]
del session.xyDataObjects[xy56.name]
del session.xyDataObjects[xy57.name]
del session.xyDataObjects[xy58.name]
del session.xyDataObjects[xy59.name]
del session.xyDataObjects[xy60.name]
del session.xyDataObjects[xy61.name]
del session.xyDataObjects[xy62.name]
del session.xyDataObjects[xy63.name]
del session.xyDataObjects[xy64.name]
del session.xyDataObjects[xy65.name]
del session.xyDataObjects[xy66.name]
del session.xyDataObjects[xy67.name]
del session.xyDataObjects[xy68.name]
del session.xyDataObjects[xy69.name]
del session.xyDataObjects[xy70.name]
del session.xyDataObjects[xy71.name]
del session.xyDataObjects[xy72.name]
del session.xyDataObjects[xy73.name]
del session.xyDataObjects[xy74.name]
del session.xyDataObjects[xy75.name]
del session.xyDataObjects[xy76.name]
del session.xyDataObjects[xy77.name]
del session.xyDataObjects[xy78.name]
del session.xyDataObjects[xy79.name]
del session.xyDataObjects[xy80.name]
del session.xyDataObjects[xy81.name]
del session.xyDataObjects[xy82.name]
del session.xyDataObjects[xy83.name]
del session.xyDataObjects[xy84.name]
del session.xyDataObjects[xy85.name]
del session.xyDataObjects[xy86.name]
del session.xyDataObjects[xy87.name]
del session.xyDataObjects[xy88.name]
del session.xyDataObjects[xy89.name]
del session.xyDataObjects[xy90.name]
del session.xyDataObjects[xy91.name]
del session.xyDataObjects[xy92.name]
del session.xyDataObjects[xy93.name]
del session.xyDataObjects[xy94.name]
del session.xyDataObjects[xy95.name]
del session.xyDataObjects[xy96.name]
del session.xyDataObjects[xy97.name]
del session.xyDataObjects[xy98.name]
del session.xyDataObjects[xy99.name]
del session.xyDataObjects[xy100.name]
del session.xyDataObjects[xy101.name]
del session.xyDataObjects[xy102.name]
del session.xyDataObjects[xy103.name]
del session.xyDataObjects[xy104.name]
del session.xyDataObjects[xy105.name]
del session.xyDataObjects[xy106.name]
xy1 = session.xyDataObjects['rf3']
xy2 = xy1*1
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
c1 = session.Curve(xyData=xy2)
chart.setValues(curvesToPlot=(c1, ), )
session.charts[chartName].autoColor(lines=True, symbols=True)
del session.xyDataObjects['_temp_319']
xy1 = session.xyDataObjects['rf3']
xy2 = xy1/(312.6*221.2)
xy2.setValues(sourceDescription='"rf3"/(312.6*221.2)')
tmpName = xy2.name
session.xyDataObjects.changeKey(tmpName, 'stressData')
xy1 = session.xyDataObjects['rf3']
xy2 = xy1/(312.6*221.2)
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
c1 = session.Curve(xyData=xy2)
chart.setValues(curvesToPlot=(c1, ), )
session.charts[chartName].autoColor(lines=True, symbols=True)
session.xyPlots[session.viewports['Viewport: 1'].displayedObject.name].setValues(
    transform=(1.19102, 0, 0, 0.084903, 0, 1.19102, 0, 0.0876041, 0, 0, 
    1.19102, 0, 0, 0, 0, 1))
odb = session.odbs['Y:/turbo_job_10.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=933.927, 
    farPlane=1475.45, width=868.562, height=392.716, cameraPosition=(834.122, 
    763.585, 691.138), cameraUpVector=(-0.0302477, 0.378148, -0.925251), 
    cameraTarget=(162.723, 92.187, 19.7394))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1061.6, 
    farPlane=1445.2, width=987.301, height=446.403, cameraPosition=(435.586, 
    206.699, 1154.86), cameraUpVector=(0.246345, 0.82525, -0.508209), 
    cameraTarget=(148.897, 72.868, 35.8263))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1069.84, 
    farPlane=1444.79, width=994.966, height=449.868, cameraPosition=(346.785, 
    166.33, 1178.27), cameraUpVector=(0.206845, 0.868621, -0.450237), 
    cameraTarget=(142.485, 69.953, 37.5165))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1123.41, 
    farPlane=1391.23, width=303.098, height=137.044, viewOffsetX=17.5849, 
    viewOffsetY=37.4152)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, 
    adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=653.801, 
    farPlane=1005.09, width=498.583, height=218.171, viewOffsetX=-3.89038, 
    viewOffsetY=-25.954)
session.viewports['Viewport: 1'].view.setValues(nearPlane=711.534, 
    farPlane=860.96, width=542.61, height=237.437, cameraPosition=(277.735, 
    112.458, 784.635), cameraUpVector=(-0.145357, 0.941378, -0.304431), 
    cameraTarget=(147.799, 120.747, -17.8212), viewOffsetX=-4.23391, 
    viewOffsetY=-28.2458)
session.viewports['Viewport: 1'].view.setValues(nearPlane=639.512, 
    farPlane=920.523, width=487.687, height=213.404, cameraPosition=(487.761, 
    278.805, 693.593), cameraUpVector=(-0.248779, 0.855472, -0.454176), 
    cameraTarget=(139.772, 114.223, -22.4407), viewOffsetX=-3.80535, 
    viewOffsetY=-25.3867)
session.viewports['Viewport: 1'].view.setValues(nearPlane=644.004, 
    farPlane=916.03, width=491.113, height=214.903, cameraPosition=(496.705, 
    276.047, 689.88), cameraUpVector=(0.0250512, 0.815589, -0.578089), 
    cameraTarget=(148.716, 111.465, -26.1534), viewOffsetX=-3.83208, 
    viewOffsetY=-25.565)
session.viewports['Viewport: 1'].view.setValues(nearPlane=697.939, 
    farPlane=871.06, width=532.243, height=232.901, cameraPosition=(20.4898, 
    201.751, 775.081), cameraUpVector=(0.0435342, 0.902896, -0.427648), 
    cameraTarget=(163.046, 118.005, -20.8788), viewOffsetX=-4.15301, 
    viewOffsetY=-27.706)
p1 = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=627.34, 
    farPlane=998.565, width=311.602, height=136.352, viewOffsetX=-14.0203, 
    viewOffsetY=11.3517)
session.viewports['Viewport: 1'].view.setValues(nearPlane=713.036, 
    farPlane=914.716, width=354.168, height=154.978, cameraPosition=(339.024, 
    364.304, 759.279), cameraUpVector=(-0.189625, 0.78622, -0.588133), 
    cameraTarget=(167.768, 105.571, 7.86662), viewOffsetX=-15.9355, 
    viewOffsetY=12.9024)
session.viewports['Viewport: 1'].view.setValues(nearPlane=709.617, 
    farPlane=918.134, width=352.47, height=154.235, cameraPosition=(333.816, 
    358.966, 762.304), cameraUpVector=(0.127013, 0.750867, -0.648126), 
    cameraTarget=(162.56, 100.233, 10.8916), viewOffsetX=-15.8591, 
    viewOffsetY=12.8405)
session.viewports['Viewport: 1'].view.setValues(nearPlane=707.913, 
    farPlane=919.839, width=397.945, height=174.134, viewOffsetX=-14.8722, 
    viewOffsetY=9.78713)
odb = session.odbs['Y:/turbo_job_10.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1111.63, 
    farPlane=1403, width=494.034, height=223.375, viewOffsetX=47.943, 
    viewOffsetY=28.0765)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p1 = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF, 
    optimizationTasks=ON, geometricRestrictions=ON, stopConditions=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, 
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=686.796, 
    farPlane=882.203, width=592.742, height=259.374, viewOffsetX=-3.09008, 
    viewOffsetY=-30.2275)
session.viewports['Viewport: 1'].view.setValues(nearPlane=667.418, 
    farPlane=895.918, width=576.018, height=252.055, cameraPosition=(339.911, 
    275.637, 749.484), cameraUpVector=(-0.0973409, 0.85777, -0.504732), 
    cameraTarget=(151.226, 114.595, -24.6936), viewOffsetX=-3.00289, 
    viewOffsetY=-29.3746)
session.viewports['Viewport: 1'].view.setValues(nearPlane=710.681, 
    farPlane=857.657, width=613.357, height=268.394, cameraPosition=(195.238, 
    202.738, 785.591), cameraUpVector=(-0.0116501, 0.902948, -0.429593), 
    cameraTarget=(158.008, 118.101, -22.0837), viewOffsetX=-3.19754, 
    viewOffsetY=-31.2787)
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].view.setValues(nearPlane=637.182, 
    farPlane=905.913, width=445.099, height=194.768, cameraPosition=(170.459, 
    703.038, 501.818), cameraUpVector=(-0.0396745, 0.349244, -0.936192), 
    cameraTarget=(156.499, 112.043, 7.5896))
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].view.setValues(session.views['Back'])
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(session.views['Back'])
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
p1 = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedRegions = f.getSequenceFromMask(mask=('[#1 ]', ), )
p.deleteMesh(regions=pickedRegions)
p = mdb.models['Model-1'].parts['Part-1']
f, e, d1 = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f[0], sketchUpEdge=e[2], 
    sketchPlaneSide=SIDE1, origin=(156.3, 110.6, 7.75))
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=766.05, gridSpacing=19.15, transform=t)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['Part-1']
p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
s1.rectangle(point1=(-19.15, 19.15), point2=(19.15, -19.15))
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedFaces = f.getSequenceFromMask(mask=('[#1 ]', ), )
e1, d2 = p.edges, p.datums
p.PartitionFaceBySketch(sketchUpEdge=e1[2], faces=pickedFaces, sketch=s1)
s1.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p = mdb.models['Model-1'].parts['Part-1']
p.generateMesh()
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedRegions = f.getSequenceFromMask(mask=('[#3 ]', ), )
p.deleteMesh(regions=pickedRegions)
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
pickedRegions = f.getSequenceFromMask(mask=('[#3 ]', ), )
p.setMeshControls(regions=pickedRegions, elemShape=QUAD)
p = mdb.models['Model-1'].parts['Part-1']
p.generateMesh()
p = mdb.models['Model-1'].parts['Part-1']
p.deleteMesh()
p = mdb.models['Model-1'].parts['Part-1']
p.seedPart(size=16.0, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Part-1']
p.generateMesh()
p = mdb.models['Model-1'].parts['Part-1']
p.deleteMesh()
p = mdb.models['Model-1'].parts['Part-1']
p.seedPart(size=10.0, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Part-1']
p.generateMesh()
session.viewports['Viewport: 1'].view.setValues(nearPlane=723.903, 
    farPlane=809.139, width=401.872, height=175.852, viewOffsetX=-2.65485, 
    viewOffsetY=0.574307)
p = mdb.models['Model-1'].parts['Part-1']
n = p.nodes
nodes = n.getSequenceFromMask(mask=('[#0:3 #40000000 ]', ), )
p.Set(nodes=nodes, name='Set-3')
#: The set 'Set-3' has been created (1 node).
mdb.models['Model-1'].parts['Part-1'].sets.changeKey(fromName='Set-3', 
    toName='displaycmentNode')
a1 = mdb.models['Model-1'].rootAssembly
a1.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF, 
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
regionDef=mdb.models['Model-1'].rootAssembly.allInstances['Part-1-1'].sets['displaycmentNode']
mdb.models['Model-1'].HistoryOutputRequest(name='displacement', 
    createStepName='turbo', variables=('U3', ), region=regionDef, 
    sectionPoints=DEFAULT, rebar=EXCLUDE)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
mdb.Job(name='displaycment_history', model='Model-1', description='', 
    type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, 
    memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=4, numDomains=4, numGPUs=0)
mdb.save()
#: The model database has been saved to "Y:\mb_sss_points.cae".
mdb.jobs['displaycment_history'].submit(consistencyChecking=OFF)
#: The job input file "displaycment_history.inp" has been submitted for analysis.
#: Error in job displaycment_history: SURFACE DEFINITION ASSEMBLY_SURF-3 NOT FOUND.
#: Error in job displaycment_history: THE SURFACE ASSEMBLY_SURF-3 HAS NOT BEEN LOCATED
#: Job displaycment_history: Analysis Input File Processor aborted due to errors.
#: Error in job displaycment_history: Analysis Input File Processor exited with an error - Please see the  displaycment_history.dat file for possible error messages if the file exists.
#: Job displaycment_history aborted due to errors.
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p1 = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
del mdb.models['Model-1'].parts['Part-1'].sets['points_load']
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.jobs['displaycment_history'].submit(consistencyChecking=OFF)
#: The job input file "displaycment_history.inp" has been submitted for analysis.
#: Error in job displaycment_history: SURFACE DEFINITION ASSEMBLY_SURF-3 NOT FOUND.
#: Error in job displaycment_history: THE SURFACE ASSEMBLY_SURF-3 HAS NOT BEEN LOCATED
#: Job displaycment_history: Analysis Input File Processor aborted due to errors.
#: Error in job displaycment_history: Analysis Input File Processor exited with an error - Please see the  displaycment_history.dat file for possible error messages if the file exists.
#: Job displaycment_history aborted due to errors.
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['Part-1']
del p.features['Partition face-1']
#: 
#: The distance used for offset is: 7.750000
#: Warning: Failed to attach mesh to part geometry.
del mdb.models['Model-1'].parts['Part-1'].sets['displaycmentNode']
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=700.564, 
    farPlane=832.477, width=672.176, height=286.274, viewOffsetX=163.48, 
    viewOffsetY=-17.8858)
a1 = mdb.models['Model-1'].rootAssembly
a1.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
del mdb.models['Model-1'].historyOutputRequests['displacement']
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF, 
    bcs=OFF, predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['Part-1']
p.generateMesh()
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
p = mdb.models['Model-1'].parts['Part-1']
n = p.nodes
nodes = n.getSequenceFromMask(mask=(
    '[#0:7 #7fc000 #f0003fe0 #ff8001f #7fc00 #ff0003fe #ff8001', 
    ' #e0007fc0 #1ff0003f #ff800 #7fc ]', ), )
p.Set(nodes=nodes, name='displays')
#: The set 'displays' has been created (117 nodes).
a1 = mdb.models['Model-1'].rootAssembly
a1.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF, 
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
regionDef=mdb.models['Model-1'].rootAssembly.allInstances['Part-1-1'].sets['displays']
mdb.models['Model-1'].HistoryOutputRequest(name='displays_his', 
    createStepName='turbo', variables=('U3', ), region=regionDef, 
    sectionPoints=DEFAULT, rebar=EXCLUDE)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
mdb.jobs['displaycment_history'].submit(consistencyChecking=OFF)
#: The job input file "displaycment_history.inp" has been submitted for analysis.
#: Job displaycment_history: Analysis Input File Processor completed successfully.
#: Job displaycment_history: Abaqus/Standard completed successfully.
#: Job displaycment_history completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['Y:/turbo_job_10.odb'])
o3 = session.openOdb(name='Y:/displaycment_history.odb')
#: Model: Y:/displaycment_history.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       5
#: Number of Node Sets:          7
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=1011.29, 
    farPlane=1472.62, width=965.417, height=425.247, cameraPosition=(704.167, 
    259.259, 1041.96), cameraUpVector=(-0.620429, 0.761502, -0.187571), 
    cameraTarget=(158.215, 74.691, 31.91))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1006.01, 
    farPlane=1522.25, width=960.378, height=423.028, cameraPosition=(761.707, 
    -428.344, 907.434), cameraUpVector=(-0.466865, 0.82867, 0.308778), 
    cameraTarget=(161.878, 30.921, 23.3466))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1076.25, 
    farPlane=1538.51, width=1027.43, height=452.565, cameraPosition=(-85.5325, 
    -839.708, 801.203), cameraUpVector=(-0.232705, 0.887011, 0.398824), 
    cameraTarget=(94.0301, -2.02152, 14.8395))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1066.29, 
    farPlane=1537, width=1017.92, height=448.378, cameraPosition=(298.386, 
    -1065.51, 476.505), cameraUpVector=(-0.292492, 0.659428, 0.692534), 
    cameraTarget=(136.458, -26.9757, -21.044))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1065.75, 
    farPlane=1529.3, width=1017.41, height=448.151, cameraPosition=(269.159, 
    -898.352, 744.561), cameraUpVector=(-0.262778, 0.818827, 0.510363), 
    cameraTarget=(133.343, -9.15759, 7.52932))
odb = session.odbs['Y:/displaycment_history.odb']
session.XYDataFromHistory(name='maxU3displaycment', odb=odb, 
    outputVariableName='Spatial displacement: U3 at Node 357 in NSET DISPLAYS', 
    steps=('turbo', ), __linkedVpName__='Viewport: 1')
xy1 = session.xyDataObjects['maxU3displaycment']
xy2 = session.xyDataObjects['stressData']
xy3 = combine(xy1, xy2)
xy3.setValues(
    sourceDescription='combine ( "maxU3displaycment", "stressData" )')
tmpName = xy3.name
session.xyDataObjects.changeKey(tmpName, 'displaycment_plot_max')
xy1 = session.xyDataObjects['maxU3displaycment']
xy2 = session.xyDataObjects['stressData']
xy3 = combine(xy1, xy2)
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
c1 = session.Curve(xyData=xy3)
chart.setValues(curvesToPlot=(c1, ), )
session.charts[chartName].autoColor(lines=True, symbols=True)
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
xy1 = session.xyDataObjects['displaycment_plot_max']
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
session.charts[chartName].autoColor(lines=True, symbols=True)
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
xy1 = session.xyDataObjects['displaycment_plot_max']
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
session.charts[chartName].autoColor(lines=True, symbols=True)
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
xy1 = session.xyDataObjects['displaycment_plot_max']
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
session.charts[chartName].autoColor(lines=True, symbols=True)
xy1 = session.xyDataObjects['displaycment_plot_max']
xy2 = session.xyDataObjects['stressData']
xy3 = combine(xy1*(-1), xy2)
xy3.setValues(
    sourceDescription='combine ( "displaycment_plot_max"*(-1),"stressData" )')
tmpName = xy3.name
session.xyDataObjects.changeKey(tmpName, 'max_abs_display')
#* XypError: X values are not monotonic in the same direction and interpolation 
#* is undefined.
xy1 = session.xyDataObjects['displaycment_plot_max']
xy2 = session.xyDataObjects['stressData']
xy3 = combine(xy1*(-1), xy2)
xy3.setValues(
    sourceDescription='combine ( "displaycment_plot_max"*(-1),"stressData" )')
tmpName = xy3.name
session.xyDataObjects.changeKey(tmpName, 'max_abs_display')
#* XypError: X values are not monotonic in the same direction and interpolation 
#* is undefined.
xy1 = session.xyDataObjects['displaycment_plot_max']
xy2 = session.xyDataObjects['stressData']
xy3 = combine(xy1*(-1), xy2*(1))
xy3.setValues(
    sourceDescription='combine ( "displaycment_plot_max"*(-1),"stressData"*(1) )')
tmpName = xy3.name
session.xyDataObjects.changeKey(tmpName, 'asfAFSDasdf')
#* XypError: X values are not monotonic in the same direction and interpolation 
#* is undefined.
xy1 = session.xyDataObjects['maxU3displaycment']
xy2 = session.xyDataObjects['stressData']
xy3 = combine(-xy1, xy2)
xy3.setValues(sourceDescription='combine ( -"maxU3displaycment","stressData")')
tmpName = xy3.name
session.xyDataObjects.changeKey(tmpName, 'abs_display_right')
xy1 = session.xyDataObjects['maxU3displaycment']
xy2 = session.xyDataObjects['stressData']
xy3 = combine(-xy1, xy2)
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
c1 = session.Curve(xyData=xy3)
chart.setValues(curvesToPlot=(c1, ), )
session.charts[chartName].autoColor(lines=True, symbols=True)
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
xy1 = session.xyDataObjects['displaycment_plot_max']
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
session.charts[chartName].autoColor(lines=True, symbols=True)
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
xy1 = session.xyDataObjects['displaycment_plot_max']
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
session.charts[chartName].autoColor(lines=True, symbols=True)
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
xy1 = session.xyDataObjects['displaycment_plot_max']
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
session.charts[chartName].autoColor(lines=True, symbols=True)
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
xy1 = session.xyDataObjects['displaycment_plot_max']
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
session.charts[chartName].autoColor(lines=True, symbols=True)
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
xy1 = session.xyDataObjects['abs_display_right']
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
session.charts[chartName].autoColor(lines=True, symbols=True)
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
xy1 = session.xyDataObjects['displaycment_plot_max']
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), appendMode=True)
session.charts[chartName].autoColor(lines=True, symbols=True)
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
chart.removeCurve(curve=('abs_display_right', ), )
mdb.save()
#: The model database has been saved to "Y:\mb_sss_points.cae".

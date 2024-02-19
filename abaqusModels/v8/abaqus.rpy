# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2024 replay file
# Internal Version: 2023_09_21-14.55.25 RELr426 190762
# Run by 10992702 on Mon Feb 19 14:33:04 2024
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=190.885437011719, 
    height=193.773132324219)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
mdb.openAuxMdb(pathName='Y:/mp16_v3.cae')
mdb.copyAuxMdbModel(fromName='Model-1', toName='Model-1')
mdb.closeAuxMdb()
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON, 
    adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    step='uniformed_load')
session.viewports['Viewport: 1'].view.setValues(nearPlane=664.961, 
    farPlane=940.444, width=629.09, height=270.219, cameraPosition=(-83.656, 
    217.093, 766.358), cameraUpVector=(0.1174, 0.88832, -0.443965), 
    cameraTarget=(167.147, 106.493, 1.01039))
session.viewports['Viewport: 1'].view.setValues(nearPlane=603.99, 
    farPlane=1013.37, width=571.408, height=245.442, cameraPosition=(397.596, 
    -508.667, 468.501), cameraUpVector=(-0.140296, 0.806898, 0.573789), 
    cameraTarget=(161.002, 115.76, 4.81377))
session.viewports['Viewport: 1'].view.setValues(nearPlane=561.083, 
    farPlane=1063.83, width=530.816, height=228.006, cameraPosition=(825.306, 
    -311.677, 192.741), cameraUpVector=(-0.396489, 0.380979, 0.835255), 
    cameraTarget=(158.742, 114.719, 6.27069))
session.viewports['Viewport: 1'].view.setValues(nearPlane=611.951, 
    farPlane=1020.6, width=578.94, height=248.677, cameraPosition=(382.36, 
    848.36, 274.063), cameraUpVector=(-0.233323, -0.582137, 0.778895), 
    cameraTarget=(159.013, 114.01, 6.22101))
session.viewports['Viewport: 1'].view.setValues(nearPlane=562.844, 
    farPlane=1072.87, width=532.482, height=228.721, cameraPosition=(863.359, 
    518.272, 60.3753), cameraUpVector=(-0.42188, -0.0602487, 0.904648), 
    cameraTarget=(160.971, 112.667, 5.35131))
session.viewports['Viewport: 1'].view.setValues(nearPlane=670.083, 
    farPlane=962.041, width=633.936, height=272.299, cameraPosition=(118.742, 
    -435.901, 612.636), cameraUpVector=(-0.212028, 0.910092, 0.356058), 
    cameraTarget=(156.506, 106.945, 8.66301))
session.viewports['Viewport: 1'].view.setValues(nearPlane=658.821, 
    farPlane=973.302, width=623.281, height=267.722, cameraPosition=(118.742, 
    -435.901, 612.636), cameraUpVector=(-0.00696887, 0.924286, 0.381637), 
    cameraTarget=(156.506, 106.945, 8.66301))
session.viewports['Viewport: 1'].view.setValues(nearPlane=654.244, 
    farPlane=978.677, width=618.951, height=265.862, cameraPosition=(160.312, 
    -537.312, 504.546), cameraUpVector=(-0.0886569, 0.836806, 0.540274), 
    cameraTarget=(156.664, 106.559, 8.25117))
session.viewports['Viewport: 1'].view.setValues(nearPlane=616.542, 
    farPlane=1016.39, width=583.283, height=250.541, cameraPosition=(396.832, 
    -484.4, 512.464), cameraUpVector=(-0.284717, 0.797203, 0.532357), 
    cameraTarget=(157.68, 106.786, 8.28519))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='points_load')
session.viewports['Viewport: 1'].view.setValues(nearPlane=620.085, 
    farPlane=1012.84, width=586.635, height=251.983, cameraPosition=(396.832, 
    -484.4, 512.464), cameraUpVector=(-0.40192, 0.74719, 0.529308), 
    cameraTarget=(157.68, 106.786, 8.28519))
session.viewports['Viewport: 1'].view.setValues(nearPlane=620.124, 
    farPlane=1012.8, width=586.672, height=251.999, cameraPosition=(396.832, 
    -484.4, 512.464), cameraUpVector=(-0.195068, 0.827912, 0.525842), 
    cameraTarget=(157.68, 106.786, 8.28519))
session.viewports['Viewport: 1'].view.setValues(nearPlane=573.717, 
    farPlane=1059.75, width=542.768, height=233.141, cameraPosition=(754.858, 
    -335.125, 339.586), cameraUpVector=(-0.312425, 0.685352, 0.657787), 
    cameraTarget=(159.219, 107.428, 7.54196))
session.viewports['Viewport: 1'].view.setValues(nearPlane=605.754, 
    farPlane=1027.05, width=573.077, height=246.16, cameraPosition=(567.535, 
    -384.901, 509.628), cameraUpVector=(-0.270804, 0.827142, 0.492444), 
    cameraTarget=(158.352, 107.198, 8.3291))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF, 
    bcs=OFF, predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF, mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF, 
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, 
    adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=600.11, 
    farPlane=1025.8, width=487.446, height=210.015, viewOffsetX=-5.08241, 
    viewOffsetY=0.204623)
session.viewports['Viewport: 1'].view.setValues(nearPlane=600.11, 
    width=487.446, height=210.015, cameraPosition=(637.103, 572.662, 472.96), 
    cameraUpVector=(-0.124306, 0.437527, -0.890572), cameraTarget=(167.745, 
    103.303, 3.6021), viewOffsetX=-5.08242, viewOffsetY=0.204623)
session.viewports['Viewport: 1'].view.setValues(nearPlane=668.22, 
    farPlane=948.637, width=542.769, height=233.851, cameraPosition=(48.4165, 
    518.617, 697.387), cameraUpVector=(0.381804, 0.611133, -0.693356), 
    cameraTarget=(168.429, 104.872, 7.96428), viewOffsetX=-5.65925, 
    viewOffsetY=0.227847)
session.viewports['Viewport: 1'].view.setValues(nearPlane=608.36, 
    farPlane=1017.11, width=494.147, height=212.902, cameraPosition=(711.707, 
    351.565, 550.058), cameraUpVector=(-0.352886, 0.793414, -0.495949), 
    cameraTarget=(163.488, 106.686, 1.98639), viewOffsetX=-5.15229, 
    viewOffsetY=0.207436)
session.viewports['Viewport: 1'].view.setValues(nearPlane=704.12, 
    farPlane=920.039, width=571.929, height=246.414, cameraPosition=(357.879, 
    168.742, 792.325), cameraUpVector=(-0.0457586, 0.913381, -0.404526), 
    cameraTarget=(165.223, 107.05, 4.94316), viewOffsetX=-5.9633, 
    viewOffsetY=0.240088)
session.viewports['Viewport: 1'].view.setValues(nearPlane=725.895, 
    farPlane=898.082, width=589.616, height=254.034, cameraPosition=(211.927, 
    65.4023, 816.628), cameraUpVector=(-0.0608269, 0.957873, -0.280675), 
    cameraTarget=(165.585, 107.863, 6.10833), viewOffsetX=-6.14772, 
    viewOffsetY=0.247513)
p = mdb.models['Model-1'].parts['Part-1']
n = p.nodes
nodes = n.getSequenceFromMask(mask=(
    '[#0:21 #200000 #0:7 #20000000 #0:14 #1000010 #0:14', 
    ' #2000 #0:6 #80000 ]', ), )
p.Set(nodes=nodes, name='points_load')
#: The set 'points_load' has been created (6 nodes).
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].view.setValues(nearPlane=681.263, 
    farPlane=949.562, width=644.513, height=277.686, cameraPosition=(314.753, 
    -135.801, 768.723), cameraUpVector=(-0.0474907, 0.998531, -0.0260912), 
    cameraTarget=(157.284, 108.25, 9.42377))
session.viewports['Viewport: 1'].view.setValues(nearPlane=672.935, 
    farPlane=957.89, width=636.634, height=274.291, cameraPosition=(314.753, 
    -135.801, 768.723), cameraUpVector=(-0.0631188, 0.997739, -0.0231048), 
    cameraTarget=(157.284, 108.25, 9.42377))
session.viewports['Viewport: 1'].view.setValues(nearPlane=673.812, 
    farPlane=957.013, width=637.464, height=274.648, cameraUpVector=(
    -0.0445177, 0.998653, -0.0266686), cameraTarget=(157.284, 108.25, 9.42377))
session.viewports['Viewport: 1'].view.setValues(nearPlane=618.377, 
    farPlane=1015.91, width=585.019, height=252.052, cameraPosition=(357.659, 
    -515.353, -477.387), cameraUpVector=(0.538449, 0.804103, -0.251974), 
    cameraTarget=(157.413, 107.105, 5.66536))
session.viewports['Viewport: 1'].view.setValues(nearPlane=624.216, 
    farPlane=1010.07, width=590.543, height=254.432, cameraPosition=(357.659, 
    -515.353, -477.387), cameraUpVector=(-0.596801, -0.325723, 0.733302), 
    cameraTarget=(157.413, 107.105, 5.66546))
session.viewports['Viewport: 1'].view.setValues(nearPlane=644.64, 
    farPlane=989.869, width=609.865, height=262.757, cameraPosition=(165.134, 
    -645.004, -303.521), cameraUpVector=(-0.0403768, -0.0516092, 0.997851), 
    cameraTarget=(156.426, 106.44, 6.55705))
session.viewports['Viewport: 1'].view.setValues(nearPlane=693.118, 
    farPlane=942.19, width=655.728, height=282.517, cameraPosition=(-100.299, 
    111.78, 784.097), cameraUpVector=(0.243765, 0.930884, -0.272093), 
    cameraTarget=(155.029, 110.423, 12.2818))
session.viewports['Viewport: 1'].view.setValues(nearPlane=705.566, 
    farPlane=929.908, width=667.504, height=287.592, cameraPosition=(276.412, 
    177.973, 813.807), cameraUpVector=(-0.00476478, 0.910376, -0.413754), 
    cameraTarget=(157.195, 110.804, 12.4526))
a = mdb.models['Model-1'].rootAssembly
n1 = a.instances['Part-1-1'].nodes
nodes1 = n1.getSequenceFromMask(mask=(
    '[#0:26 #80 #0 #80000 #0:13 #20000000 #0:18', ' #4000 #0:7 #100 ]', ), )
a.Set(nodes=nodes1, name='points_assembly')
#: The set 'points_assembly' has been created (5 nodes).
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF, loads=ON, 
    bcs=ON, predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
a = mdb.models['Model-1'].rootAssembly
region = a.sets['points_assembly']
mdb.models['Model-1'].ConcentratedForce(name='points_loads', 
    createStepName='points_load', region=region, cf3=-0.0005, 
    distributionType=UNIFORM, field='', localCsys=None)
session.viewports['Viewport: 1'].view.setValues(nearPlane=590.159, 
    farPlane=1045.11, width=560.022, height=240.551, cameraPosition=(441.042, 
    821.907, 293.214), cameraUpVector=(-0.595964, 0.170121, -0.784784), 
    cameraTarget=(158.158, 114.571, 9.4072))
session.viewports['Viewport: 1'].view.setValues(nearPlane=592.901, 
    farPlane=1042.39, width=562.624, height=241.669, cameraPosition=(490.243, 
    825.863, 220.879), cameraUpVector=(-0.5859, 0.130591, -0.799792), 
    cameraTarget=(158.44, 114.594, 8.9931))
session.viewports['Viewport: 1'].view.setValues(nearPlane=695.643, 
    farPlane=939.725, width=660.119, height=283.547, cameraPosition=(310.16, 
    278.867, 793.002), cameraUpVector=(0.0108185, 0.84736, -0.530909), 
    cameraTarget=(157.406, 111.455, 12.2766))
session.viewports['Viewport: 1'].view.setValues(nearPlane=584.124, 
    farPlane=1051.67, width=554.295, height=238.091, cameraPosition=(972.298, 
    140.924, -38.977), cameraUpVector=(-0.387953, 0.830927, -0.398815), 
    cameraTarget=(161.237, 110.657, 7.46303))
session.viewports['Viewport: 1'].view.setValues(nearPlane=611.305, 
    farPlane=1024.54, width=580.088, height=249.17, cameraPosition=(805.146, 
    -11.6977, -474.992), cameraUpVector=(-0.416217, 0.882728, -0.218072), 
    cameraTarget=(160.227, 109.734, 4.82746))
session.viewports['Viewport: 1'].view.setValues(nearPlane=678.495, 
    farPlane=957.364, width=643.847, height=276.557, cameraPosition=(410.16, 
    -32.1495, -756.571), cameraUpVector=(-0.174398, 0.977781, 0.116319), 
    cameraTarget=(157.827, 109.61, 3.11669))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.Job(name='mp16_up', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON, 
    adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, 
    interactions=OFF, constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF, 
    optimizationTasks=ON, geometricRestrictions=ON, stopConditions=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON, mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].move('uniformed_load', 
    'points_load')
mdb.models['Model-1'].historyOutputRequests['H-Output-1'].move(
    'uniformed_load', 'points_load')
mdb.saveAs(pathName='Y:/m+16_v4')
#: The model database has been saved to "Y:\m+16_v4.cae".
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
mdb.jobs['mp16_up'].submit(consistencyChecking=OFF)
#: The job input file "mp16_up.inp" has been submitted for analysis.
#: Job mp16_up: Analysis Input File Processor completed successfully.
#: Job mp16_up: Abaqus/Standard completed successfully.
#: Job mp16_up completed successfully. 
o3 = session.openOdb(name='Y:/mp16_up.odb')
#: Model: Y:/mp16_up.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       2
#: Number of Node Sets:          5
#: Number of Steps:              2
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )

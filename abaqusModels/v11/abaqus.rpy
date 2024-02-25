# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2024 replay file
# Internal Version: 2023_09_21-14.55.25 RELr426 190762
# Run by 10992702 on Sat Feb 24 11:51:06 2024
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
mdb.openAuxMdb(pathName='Y:/mb_ce.cae')
mdb.copyAuxMdbModel(fromName='Model-1', toName='Model-1')
mdb.closeAuxMdb()
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
mdb.Job(name='check', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs['check'].submit(consistencyChecking=OFF)
#: The job input file "check.inp" has been submitted for analysis.
#: Job check: Analysis Input File Processor completed successfully.
#: Job check: Abaqus/Standard completed successfully.
#: Job check completed successfully. 
o3 = session.openOdb(name='Y:/check.odb')
#: Model: Y:/check.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       3
#: Number of Node Sets:          6
#: Number of Steps:              3
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].view.setValues(nearPlane=1018.58, 
    farPlane=1326.64, width=883.096, height=428.311, cameraPosition=(198.726, 
    875.959, 880.096), cameraUpVector=(-0.0652825, 0.472509, -0.878905), 
    cameraTarget=(157.831, 93.0523, 21.1944))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1020.98, 
    farPlane=1339.8, width=885.177, height=429.32, cameraPosition=(378.957, 
    637.868, 1024.95), cameraUpVector=(0.0149199, 0.660872, -0.750351), 
    cameraTarget=(159.324, 91.08, 22.3943))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1106.66, 
    farPlane=1287.77, width=959.457, height=465.347, cameraPosition=(184.394, 
    11.9975, 1185.23), cameraUpVector=(0.0833492, 0.956817, -0.278484), 
    cameraTarget=(156.441, 81.8058, 24.7694))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1036.12, 
    farPlane=1403.04, width=898.297, height=435.684, cameraPosition=(230.764, 
    -954.915, 580.954), cameraUpVector=(0.0871453, 0.757935, 0.646483), 
    cameraTarget=(157.77, 54.0872, 7.44653))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1063.52, 
    farPlane=1353.4, width=922.05, height=447.204, cameraPosition=(499.753, 
    -121.992, 1127.2), cameraUpVector=(-0.0824732, 0.987326, -0.135595), 
    cameraTarget=(170.272, 92.8009, 32.8357))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1085.18, 
    farPlane=1327.57, width=940.827, height=456.311, cameraPosition=(436.156, 
    130.515, 1165.45), cameraUpVector=(-0.0941967, 0.934369, -0.34363), 
    cameraTarget=(167.874, 102.321, 34.278))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1088.9, 
    farPlane=1323.96, width=944.051, height=457.875, cameraPosition=(405.498, 
    117.906, 1172.55), cameraUpVector=(-0.0811641, 0.938065, -0.336817), 
    cameraTarget=(166.769, 101.867, 34.5338))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1109.92, 
    farPlane=1303.18, width=962.271, height=466.712, cameraPosition=(232.46, 
    73.853, 1195.74), cameraUpVector=(-0.0120738, 0.950112, -0.311676), 
    cameraTarget=(160.525, 100.277, 35.3706))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1089.18, 
    farPlane=1327.37, width=944.286, height=457.989, cameraPosition=(242.307, 
    -146.479, 1169.63), cameraUpVector=(0.00237422, 0.991091, -0.133166), 
    cameraTarget=(160.881, 92.3054, 34.4258))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1027.4, 
    farPlane=1399.99, width=890.723, height=432.011, cameraPosition=(365.128, 
    -774.145, 796.317), cameraUpVector=(0.00136606, 0.886383, 0.46295), 
    cameraTarget=(165.493, 68.7344, 20.4066))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1041.2, 
    farPlane=1384.29, width=902.689, height=437.814, cameraPosition=(346.472, 
    -666.274, 903.77), cameraUpVector=(0.00390741, 0.937775, 0.347222), 
    cameraTarget=(164.712, 73.249, 24.9037))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1083.29, 
    farPlane=1337.48, width=939.178, height=455.512, cameraPosition=(195.139, 
    -354.2, 1109.05), cameraUpVector=(-0.120091, 0.991525, 0.049559), 
    cameraTarget=(158.492, 86.0755, 33.3409))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1089.66, 
    farPlane=1330.24, width=944.704, height=458.191, cameraPosition=(167.876, 
    -287.305, 1134.73), cameraUpVector=(-0.110509, 0.993807, -0.0116351), 
    cameraTarget=(157.422, 88.6999, 34.3485))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1010.77, 
    farPlane=1413.98, width=876.31, height=425.019, cameraPosition=(604.168, 
    -591.398, 873.317), cameraUpVector=(-0.181223, 0.916537, 0.356537), 
    cameraTarget=(174.387, 76.875, 24.1833))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1000.04, 
    farPlane=1428.81, width=867.009, height=420.508, cameraPosition=(586.558, 
    -849.442, 598.801), cameraUpVector=(-0.0117548, 0.800929, 0.598643), 
    cameraTarget=(173.668, 66.3439, 12.98))
session.viewports['Viewport: 1'].view.setValues(nearPlane=999.778, 
    farPlane=1433.18, width=866.782, height=420.398, cameraPosition=(-227.366, 
    -985.264, 355.082), cameraUpVector=(0.256935, 0.548702, 0.795556), 
    cameraTarget=(139.133, 60.5809, 2.63891))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1017.65, 
    farPlane=1417.57, width=882.279, height=427.914, cameraPosition=(-51.7135, 
    -1080.4, 136.583), cameraUpVector=(-0.0756425, 0.465569, 0.881773), 
    cameraTarget=(146.87, 56.3907, -6.98529))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1042.07, 
    farPlane=1384.3, width=903.446, height=438.18, cameraPosition=(432.891, 
    -533.816, 982.097), cameraUpVector=(-0.153189, 0.955386, 0.25253), 
    cameraTarget=(168.644, 80.9492, 31.0044))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1076.48, 
    farPlane=1347.98, width=933.283, height=452.651, cameraPosition=(295.888, 
    -302.588, 1123.19), cameraUpVector=(-0.252973, 0.967172, 0.0241214), 
    cameraTarget=(162.966, 90.533, 36.8523))
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    step='clamped_edges')
mdb.models['Model-1'].loads['uniformed_load-Copy'].setValues(
    magnitude=0.00452079566)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.Job(name='magnitude', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs['magnitude'].submit(consistencyChecking=OFF)
#: The job input file "magnitude.inp" has been submitted for analysis.
#: Job magnitude: Analysis Input File Processor completed successfully.
#: Job magnitude: Abaqus/Standard completed successfully.
#: Job magnitude completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['Y:/check.odb'])
o3 = session.openOdb(name='Y:/magnitude.odb')
#: Model: Y:/magnitude.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       3
#: Number of Node Sets:          6
#: Number of Steps:              3
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
mdb.models['Model-1'].loads['uniformed_load-Copy'].setValues(
    distributionType=TOTAL_FORCE, magnitude=1.0)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.Job(name='total_force', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs['total_force'].submit(consistencyChecking=OFF)
#: The job input file "total_force.inp" has been submitted for analysis.
#: Job total_force: Analysis Input File Processor completed successfully.
#: Job total_force: Abaqus/Standard completed successfully.
#: Job total_force completed successfully. 
o3 = session.openOdb(name='Y:/total_force.odb')
#: Model: Y:/total_force.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       3
#: Number of Node Sets:          6
#: Number of Steps:              3
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
odb = session.odbs['Y:/magnitude.odb']
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
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
odb = session.odbs['Y:/total_force.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
mdb.models['Model-1'].loads['uniformed_load-Copy'].setValues(
    distributionType=UNIFORM)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.jobs['total_force'].submit(consistencyChecking=OFF)
#: The job input file "total_force.inp" has been submitted for analysis.
#: Job total_force: Analysis Input File Processor completed successfully.
#: Job total_force: Abaqus/Standard completed successfully.
#: Job total_force completed successfully. 
o3 = session.openOdb(name='Y:/total_force.odb')
#: Model: Y:/total_force.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       3
#: Number of Node Sets:          6
#: Number of Steps:              3
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
mdb.models['Model-1'].boundaryConditions['clamped_edges'].setValues(ur1=UNSET, 
    ur2=UNSET, ur3=UNSET)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.Job(name='simply_supported', model='Model-1', description='', 
    type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, 
    memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs['simply_supported'].submit(consistencyChecking=OFF)
#: The job input file "simply_supported.inp" has been submitted for analysis.
#: Job simply_supported: Analysis Input File Processor completed successfully.
#: Job simply_supported: Abaqus/Standard completed successfully.
#: Job simply_supported completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['Y:/total_force.odb'])
o3 = session.openOdb(name='Y:/simply_supported.odb')
#: Model: Y:/simply_supported.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       3
#: Number of Node Sets:          6
#: Number of Steps:              3
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
o7 = session.odbs['Y:/simply_supported.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=o7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=956.079, 
    farPlane=1387.76, width=228.392, height=315.753, viewOffsetX=10.1329, 
    viewOffsetY=18.7448)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF, adaptiveMeshConstraints=ON)
o7 = session.odbs['Y:/simply_supported.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=o7)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1050.6, 
    farPlane=1303.35, width=250.97, height=346.968, cameraPosition=(456.3, 
    -125.348, 1105.89), cameraUpVector=(0.0360564, 0.983647, -0.176463), 
    cameraTarget=(144.428, 82.6778, 5.07972), viewOffsetX=11.1347, 
    viewOffsetY=20.5979)
session.viewports['Viewport: 1'].view.setValues(nearPlane=960.278, 
    farPlane=1397.05, width=229.394, height=317.138, cameraPosition=(805.692, 
    -634.269, 635.227), cameraUpVector=(-0.313716, 0.768268, 0.557984), 
    cameraTarget=(156.399, 77.859, -15.6297), viewOffsetX=10.1774, 
    viewOffsetY=18.8271)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1087.3, 
    farPlane=1272.18, width=259.737, height=359.088, cameraPosition=(293.345, 
    194.8, -1176.88), cameraUpVector=(0.178607, -0.934893, 0.306716), 
    cameraTarget=(139.295, 128.268, -26.1595), viewOffsetX=11.5236, 
    viewOffsetY=21.3175)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1019.98, 
    farPlane=1335.17, width=243.655, height=336.854, cameraPosition=(147.394, 
    1094.11, -655.927), cameraUpVector=(0.0690947, -0.806138, -0.58768), 
    cameraTarget=(140.453, 134.183, 0.426716), viewOffsetX=10.8101, 
    viewOffsetY=19.9976)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1007.38, 
    farPlane=1345.79, width=240.646, height=332.694, cameraPosition=(179.028, 
    1284.69, -85.3315), cameraUpVector=(-0.077494, -0.409606, -0.908965), 
    cameraTarget=(144.201, 126.502, 13.1026), viewOffsetX=10.6766, 
    viewOffsetY=19.7507)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1006.05, 
    farPlane=1346.14, width=240.329, height=332.255, cameraPosition=(192.278, 
    1257.1, 253.052), cameraUpVector=(-0.130029, -0.131691, -0.982726), 
    cameraTarget=(145.611, 119.331, 17.255), viewOffsetX=10.6625, 
    viewOffsetY=19.7246)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1029.35, 
    farPlane=1319.71, width=245.895, height=339.949, cameraPosition=(396.98, 
    575.033, 1044.05), cameraUpVector=(-0.214212, 0.71964, -0.660478), 
    cameraTarget=(148.875, 94.8313, 14.4151), viewOffsetX=10.9094, 
    viewOffsetY=20.1814)
session.viewports['Viewport: 1'].view.setValues(nearPlane=977.083, 
    farPlane=1369.43, width=233.409, height=322.688, cameraPosition=(867.661, 
    -287.828, 836.168), cameraUpVector=(-0.237779, 0.957333, 0.164239), 
    cameraTarget=(153.06, 83.5055, -2.73356), viewOffsetX=10.3555, 
    viewOffsetY=19.1567)
session.viewports['Viewport: 1'].view.setValues(nearPlane=973.148, 
    farPlane=1373.37, width=279.886, height=386.944, viewOffsetX=14.6114, 
    viewOffsetY=13.845)
session.viewports['Viewport: 1'].view.setValues(nearPlane=949.934, 
    farPlane=1399.75, width=273.21, height=377.714, cameraPosition=(813.49, 
    -609.111, 648.644), cameraUpVector=(-0.0466424, 0.908678, 0.414883), 
    cameraTarget=(149.16, 83.3021, -8.26382), viewOffsetX=14.2629, 
    viewOffsetY=13.5148)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1001.69, 
    farPlane=1351.14, width=288.097, height=398.295, cameraPosition=(165.282, 
    -1046.59, 205.275), cameraUpVector=(0.290372, 0.508072, 0.810892), 
    cameraTarget=(137.373, 93.6958, -21.1611), viewOffsetX=15.04, 
    viewOffsetY=14.2512)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1000.47, 
    farPlane=1345.51, width=287.747, height=397.811, cameraPosition=(4.30851, 
    -765.275, 757.799), cameraUpVector=(0.358159, 0.811, 0.462603), 
    cameraTarget=(135.388, 94.8857, -13.7225), viewOffsetX=15.0217, 
    viewOffsetY=14.2339)
session.viewports['Viewport: 1'].view.setValues(nearPlane=986.661, 
    farPlane=1363, width=283.775, height=392.32, cameraPosition=(299.988, 
    -932.047, 514.77), cameraUpVector=(0.00490612, 0.735405, 0.67761), 
    cameraTarget=(141.707, 88.5501, -19.6762), viewOffsetX=14.8144, 
    viewOffsetY=14.0374)
session.viewports['Viewport: 1'].view.setValues(nearPlane=943.119, 
    farPlane=1405.18, width=271.252, height=375.007, cameraPosition=(-403.131, 
    -865.091, 330.34), cameraUpVector=(0.18037, 0.591098, 0.786174), 
    cameraTarget=(136.807, 100.941, -26.8058), viewOffsetX=14.1606, 
    viewOffsetY=13.4179)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1007.73, 
    farPlane=1336.69, width=289.836, height=400.699, cameraPosition=(-41.5167, 
    -638.627, 872.068), cameraUpVector=(0.107297, 0.930715, 0.349653), 
    cameraTarget=(137.982, 90.6937, -15.7246), viewOffsetX=15.1307, 
    viewOffsetY=14.3372)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1008.41, 
    farPlane=1335.11, width=290.033, height=400.971, cameraPosition=(-57.0163, 
    -553.978, 933.698), cameraUpVector=(0.0909858, 0.960656, 0.262415), 
    cameraTarget=(138.244, 90.0864, -14.6478), viewOffsetX=15.141, 
    viewOffsetY=14.3469)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1008.37, 
    farPlane=1335.15, width=290.023, height=400.958, viewOffsetX=14.2643, 
    viewOffsetY=13.4869)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1008.37, 
    farPlane=1335.15, width=290.024, height=400.96, viewOffsetX=10.3214, 
    viewOffsetY=19.9333)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1008.37, 
    farPlane=1335.15, width=290.025, height=400.961, viewOffsetX=60.2653, 
    viewOffsetY=4.46217)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1008.37, 
    farPlane=1335.15, width=290.026, height=400.962, viewOffsetX=-6.76469, 
    viewOffsetY=-8.4305)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
mdb.models['Model-1'].loads['uniformed_load-Copy'].setValues(
    magnitude=0.00319898)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.Job(name='excel', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs['excel'].submit(consistencyChecking=OFF)
#: The job input file "excel.inp" has been submitted for analysis.
#: Job excel: Analysis Input File Processor completed successfully.
#: Job excel: Abaqus/Standard completed successfully.
#: Job excel completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['Y:/simply_supported.odb'])
o3 = session.openOdb(name='Y:/excel.odb')
#: Model: Y:/excel.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       3
#: Number of Node Sets:          6
#: Number of Steps:              3
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
odb = session.odbs['Y:/total_force.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
odb = session.odbs['Y:/magnitude.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['Y:/magnitude.odb'])
odb = session.odbs['Y:/magnitude.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['Y:/magnitude.odb'])
odb = session.odbs['Y:/magnitude.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
odb = session.odbs['Y:/simply_supported.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=996.099, 
    farPlane=1347.42, width=324.238, height=448.261, viewOffsetX=-10.3311, 
    viewOffsetY=11.8329)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.models['Model-1'].boundaryConditions['clamped_edges'].setValues(ur1=0.0, 
    ur2=0.0, ur3=0.0)
mdb.models['Model-1'].boundaryConditions['clamped_edges'].setValues(ur1=UNSET, 
    ur2=UNSET, ur3=UNSET)
mdb.models['Model-1'].boundaryConditions['clamped_edges'].setValues(ur1=0.0, 
    ur2=0.0, ur3=0.0)
mdb.models['Model-1'].loads['uniformed_load-Copy'].setValues(
    magnitude=1.446191829826e-05)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.jobs['excel'].submit(consistencyChecking=OFF)
#: The job input file "excel.inp" has been submitted for analysis.
#: Job excel: Analysis Input File Processor completed successfully.
#: Job excel: Abaqus/Standard completed successfully.
#: Job excel completed successfully. 
mdb.saveAs(pathName='Y:/mb_rot')
#: The model database has been saved to "Y:\mb_rot.cae".
o3 = session.openOdb(name='Y:/excel.odb')
#: Model: Y:/excel.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       3
#: Number of Node Sets:          6
#: Number of Steps:              3
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
mdb.models['Model-1'].StaticLinearPerturbationStep(name='simple_test', 
    previous='Initial')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='simple_test')
mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].move('clamped_edges', 
    'simple_test')
mdb.models['Model-1'].historyOutputRequests['H-Output-1'].move('clamped_edges', 
    'simple_test')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
mdb.models['Model-1'].boundaryConditions['fixed'].deactivate('simple_test')
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Part-1-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#f ]', ), )
region = a.Set(edges=edges1, name='Set-4')
mdb.models['Model-1'].DisplacementBC(name='simple_test_BC', 
    createStepName='simple_test', region=region, u1=0.0, u2=0.0, u3=0.0, 
    ur1=UNSET, ur2=UNSET, ur3=UNSET, amplitude=UNSET, fixed=OFF, 
    distributionType=UNIFORM, fieldName='', localCsys=None)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Part-1-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
region = a.Surface(side1Faces=side1Faces1, name='Surf-2')
mdb.models['Model-1'].Pressure(name='q', createStepName='simple_test', 
    region=region, distributionType=UNIFORM, field='', magnitude=1.0)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.Job(name='simple_test', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.jobs['simple_test'].submit(consistencyChecking=OFF)
#: The job input file "simple_test.inp" has been submitted for analysis.
#: Job simple_test: Analysis Input File Processor completed successfully.
#: Job simple_test: Abaqus/Standard completed successfully.
#: Job simple_test completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['Y:/excel.odb'])
o3 = session.openOdb(name='Y:/simple_test.odb')
#: Model: Y:/simple_test.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       4
#: Number of Node Sets:          7
#: Number of Steps:              4
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=3, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
odb = session.odbs['Y:/simply_supported.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
odb = session.odbs['Y:/simple_test.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=3, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
mdb.models['Model-1'].loads['q'].setValues(magnitude=2.0)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.Job(name='simple_test2', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs['simple_test2'].submit(consistencyChecking=OFF)
#: The job input file "simple_test2.inp" has been submitted for analysis.
#: Job simple_test2: Analysis Input File Processor completed successfully.
#: Job simple_test2: Abaqus/Standard completed successfully.
#: Job simple_test2 completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['Y:/simple_test.odb'])
o3 = session.openOdb(name='Y:/simple_test2.odb')
#: Model: Y:/simple_test2.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       4
#: Number of Node Sets:          7
#: Number of Steps:              4
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=3, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].view.setValues(nearPlane=922.88, 
    farPlane=1462.22, width=433.662, height=599.541, cameraPosition=(1084.87, 
    -350.693, 581.848), cameraUpVector=(0.0549597, 0.998456, -0.00813115), 
    cameraTarget=(164.654, 83.6072, 18.8979))
session.viewports['Viewport: 1'].view.setValues(nearPlane=959.996, 
    farPlane=1472.75, width=451.103, height=623.653, cameraPosition=(-335.963, 
    -919.982, 410.693), cameraUpVector=(0.50998, 0.446297, 0.73535), 
    cameraTarget=(129.323, 69.4512, 14.6419))
session.viewports['Viewport: 1'].view.setValues(nearPlane=988.904, 
    farPlane=1435.01, width=464.687, height=642.433, cameraPosition=(45.1359, 
    -1084.62, -175.15), cameraUpVector=(0.26417, 0.1792, 0.947682), 
    cameraTarget=(146.078, 62.2129, -11.1146))
session.viewports['Viewport: 1'].view.setValues(nearPlane=939.022, 
    farPlane=1488.94, width=441.247, height=610.027, cameraPosition=(-620.764, 
    843.227, -585.14), cameraUpVector=(0.285854, -0.7366, -0.61295), 
    cameraTarget=(119.121, 140.257, -27.7119))
session.viewports['Viewport: 1'].view.setValues(nearPlane=981.871, 
    farPlane=1450.19, width=461.382, height=637.863, cameraPosition=(-121.731, 
    1162.9, 534.471), cameraUpVector=(-0.429981, -0.0352308, -0.90215), 
    cameraTarget=(140.121, 153.709, 19.4037))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1005.35, 
    farPlane=1434.87, width=472.415, height=653.117, cameraPosition=(328.378, 
    -786.289, 801.238), cameraUpVector=(-0.393773, 0.793641, 0.463764), 
    cameraTarget=(159.789, 68.5392, 31.0601))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1047.21, 
    farPlane=1391.83, width=492.086, height=680.312, cameraPosition=(551.902, 
    148.237, 1145.09), cameraUpVector=(-0.679504, 0.720113, -0.1404), 
    cameraTarget=(170.271, 112.361, 47.1842))
session.viewports['Viewport: 1'].view.setValues(nearPlane=955.947, 
    farPlane=1479.73, width=449.202, height=621.024, cameraPosition=(530.967, 
    -1034.49, -185.464), cameraUpVector=(-0.11096, 0.164881, 0.980052), 
    cameraTarget=(169.299, 57.4449, -14.5957))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1049.34, 
    farPlane=1391.11, width=493.09, height=681.7, cameraPosition=(-43.6802, 
    -246.135, 1141.78), cameraUpVector=(-0.366761, 0.921015, -0.131214), 
    cameraTarget=(143.374, 93.0106, 45.2813))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1062.89, 
    farPlane=1376.46, width=499.457, height=690.503, cameraPosition=(139.247, 
    -262.291, 1153.28), cameraUpVector=(-0.521615, 0.849016, -0.0842055), 
    cameraTarget=(151.969, 92.2515, 45.8215))
session.viewports['Viewport: 1'].view.setValues(nearPlane=972.237, 
    farPlane=1470.43, width=456.859, height=631.611, cameraPosition=(-178.527, 
    -881.459, 620.912), cameraUpVector=(-0.00087988, 0.795354, 0.606145), 
    cameraTarget=(137.176, 63.4275, 21.0383))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1020.2, 
    farPlane=1419.75, width=479.398, height=662.771, cameraPosition=(252.082, 
    -732.837, 868.355), cameraUpVector=(0.0924538, 0.911097, 0.40169), 
    cameraTarget=(157.779, 70.5387, 32.8778))
session.viewports['Viewport: 1'].view.setValues(nearPlane=990.68, 
    farPlane=1448.99, width=465.527, height=643.594, cameraPosition=(353.283, 
    -888.771, 663.287), cameraUpVector=(0.0546491, 0.810331, 0.583418), 
    cameraTarget=(162.514, 63.243, 23.2833))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1006.32, 
    farPlane=1432.99, width=472.879, height=653.758, cameraPosition=(365.221, 
    -700.244, 878.948), cameraUpVector=(0.0406252, 0.925329, 0.376983), 
    cameraTarget=(163.071, 72.0429, 33.3497))
session.viewports['Viewport: 1'].view.setValues(nearPlane=969.165, 
    farPlane=1469.1, width=455.42, height=629.62, cameraPosition=(598.421, 
    -783.214, 693.49), cameraUpVector=(-0.0701321, 0.841322, 0.535966), 
    cameraTarget=(173.923, 68.1817, 24.7191))
session.viewports['Viewport: 1'].view.setValues(nearPlane=972.636, 
    farPlane=1466.59, width=457.051, height=631.875, cameraPosition=(467.55, 
    -1039.23, 253.797), cameraUpVector=(-0.0216442, 0.539464, 0.841731), 
    cameraTarget=(167.886, 56.3721, 4.43692))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1012.32, 
    farPlane=1427.21, width=475.7, height=657.657, cameraPosition=(344.333, 
    -682.229, 899.814), cameraUpVector=(-0.00353861, 0.930912, 0.365227), 
    cameraTarget=(162.156, 72.9746, 34.4803))
session.viewports['Viewport: 1'].view.setValues(nearPlane=998.364, 
    farPlane=1441.64, width=469.142, height=648.59, cameraPosition=(296.227, 
    -894.521, 669.294), cameraUpVector=(0.0281381, 0.806722, 0.590261), 
    cameraTarget=(159.913, 63.0767, 23.7324))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1017.66, 
    farPlane=1422.07, width=478.211, height=661.128, cameraPosition=(302.755, 
    -649.081, 935.261), cameraUpVector=(0.0138497, 0.944866, 0.327163), 
    cameraTarget=(160.219, 74.5655, 36.1821))
session.viewports['Viewport: 1'].view.setValues(nearPlane=953.307, 
    farPlane=1483.21, width=447.971, height=619.322, cameraPosition=(910.537, 
    -490.857, 736.123), cameraUpVector=(-0.186607, 0.907496, 0.376335), 
    cameraTarget=(188.604, 81.9549, 26.882))
session.viewports['Viewport: 1'].view.setValues(nearPlane=938.983, 
    farPlane=1493.77, width=441.24, height=610.016, cameraPosition=(914.285, 
    954.373, 431.524), cameraUpVector=(-0.671155, -0.240636, 0.701174), 
    cameraTarget=(188.774, 147.634, 13.0394))
session.viewports['Viewport: 1'].view.setValues(nearPlane=955.702, 
    farPlane=1477.05, width=350.632, height=484.75, viewOffsetX=-38.3381, 
    viewOffsetY=-17.6272)
session.viewports['Viewport: 1'].view.setValues(nearPlane=990.811, 
    farPlane=1378.44, width=363.513, height=502.558, cameraPosition=(-189.418, 
    710.799, 955.143), cameraUpVector=(0.308047, -0.897466, 0.315692), 
    cameraTarget=(140.527, 70.8973, 41.9151), viewOffsetX=-39.7465, 
    viewOffsetY=-18.2747)
session.viewports['Viewport: 1'].view.setValues(nearPlane=18517.1, 
    farPlane=18968.9, width=529.566, height=732.128, cameraPosition=(-5171.2, 
    10372.6, 14743.8), viewOffsetX=-65.0914, viewOffsetY=-132.385)
session.viewports['Viewport: 1'].view.setValues(nearPlane=18381.5, 
    farPlane=18956.5, width=525.69, height=726.769, cameraPosition=(-12748.2, 
    -9373.9, 9586.96), cameraUpVector=(0.888298, -0.444537, 0.115388), 
    cameraTarget=(244.101, 48.073, -52.0937), viewOffsetX=-64.615, 
    viewOffsetY=-131.416)
session.viewports['Viewport: 1'].view.setValues(nearPlane=18445.9, 
    farPlane=18881.9, width=527.531, height=729.314, cameraPosition=(-6404.13, 
    -5732, 16459.5), cameraUpVector=(0.974652, -0.215373, -0.0605697), 
    cameraTarget=(251.979, 58.6072, -52.5804), viewOffsetX=-64.8413, 
    viewOffsetY=-131.876)
session.viewports['Viewport: 1'].view.setValues(nearPlane=18470.3, 
    farPlane=18908.6, width=528.228, height=730.278, cameraPosition=(795.421, 
    15146.5, 11074.8), cameraUpVector=(0.323801, -0.797208, 0.509522), 
    cameraTarget=(109.16, 11.3177, 77.6468), viewOffsetX=-64.927, 
    viewOffsetY=-132.05)
session.viewports['Viewport: 1'].view.setValues(nearPlane=18462.6, 
    farPlane=18941.6, width=528.008, height=729.975, cameraPosition=(-1460.41, 
    18409, 3504.95), cameraUpVector=(0.476941, -0.439391, 0.761224), 
    cameraTarget=(132.8, 66.1058, 116.703), viewOffsetX=-64.9, 
    viewOffsetY=-131.995)
session.viewports['Viewport: 1'].view.setValues(nearPlane=18469.9, 
    farPlane=18883.7, width=528.217, height=730.264, cameraPosition=(5257.08, 
    5783.7, 17040.5), cameraUpVector=(-0.213881, -0.97637, 0.0309403), 
    cameraTarget=(40.0883, -4.29712, 18.096), viewOffsetX=-64.9257, 
    viewOffsetY=-132.047)
session.viewports['Viewport: 1'].view.setValues(nearPlane=18444.3, 
    farPlane=18919.8, width=527.486, height=729.253, cameraPosition=(3196.04, 
    14815.7, 11108.1), cameraUpVector=(0.0454681, -0.836903, 0.545459), 
    cameraTarget=(74.6283, 7.18889, 87.908), viewOffsetX=-64.8358, 
    viewOffsetY=-131.864)
mdb.save()
#: The model database has been saved to "Y:\mb_rot.cae".

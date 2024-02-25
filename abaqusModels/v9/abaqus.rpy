# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2024 replay file
# Internal Version: 2023_09_21-14.55.25 RELr426 190762
# Run by 10992702 on Thu Feb 22 12:46:47 2024
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
mdb.openAuxMdb(pathName='Y:/m+16_v4.cae')
mdb.copyAuxMdbModel(fromName='Model-1', toName='Model-1')
mdb.closeAuxMdb()
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, optimizationTasks=OFF, 
    geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=656.368, 
    farPlane=959.66, width=526.262, height=266.727, cameraPosition=(363.297, 
    400.911, 732.949), cameraUpVector=(0.0165727, 0.740048, -0.672349), 
    cameraTarget=(167.147, 106.493, 1.01038))
session.viewports['Viewport: 1'].view.setValues(nearPlane=714.32, 
    farPlane=895.332, width=572.726, height=290.277, cameraPosition=(112.053, 
    129.911, 811.217), cameraUpVector=(0.110196, 0.929671, -0.351524), 
    cameraTarget=(168.682, 108.149, 0.532066))
session.viewports['Viewport: 1'].view.setValues(nearPlane=718.104, 
    farPlane=893.756, width=575.76, height=291.815, cameraPosition=(178.98, 
    86.8689, 813.101), cameraUpVector=(-0.0111552, 0.95135, -0.307909), 
    cameraTarget=(168.006, 108.584, 0.513049))
session.viewports['Viewport: 1'].view.setValues(nearPlane=689.417, 
    farPlane=925.049, width=552.759, height=280.157, cameraPosition=(244.431, 
    -37.4401, 796.473), cameraUpVector=(-0.0455987, 0.987075, -0.153638), 
    cameraTarget=(167.436, 109.667, 0.657925))
session.viewports['Viewport: 1'].view.setValues(nearPlane=688.633, 
    farPlane=926.162, width=552.13, height=279.838, cameraPosition=(252.199, 
    -55.6786, 792.089), cameraUpVector=(-0.0341961, 0.990713, -0.131596), 
    cameraTarget=(167.381, 109.796, 0.688981))
session.viewports['Viewport: 1'].view.setValues(nearPlane=621.889, 
    farPlane=997.454, width=498.616, height=252.715, cameraPosition=(286.009, 
    -534.207, 480.09), cameraUpVector=(-0.00912848, 0.829118, 0.558999), 
    cameraTarget=(167.148, 113.088, 2.83516))
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    step='uniformed_load')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.Job(name='mb_faanes', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs['mb_faanes'].submit(consistencyChecking=OFF)
#: The job input file "mb_faanes.inp" has been submitted for analysis.
#: Job mb_faanes: Analysis Input File Processor completed successfully.
#: Job mb_faanes: Abaqus/Standard completed successfully.
#: Job mb_faanes completed successfully. 
o3 = session.openOdb(name='Y:/mb_faanes.odb')
#: Model: Y:/mb_faanes.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       2
#: Number of Node Sets:          5
#: Number of Steps:              2
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U2'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U1'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='SF', outputPosition=INTEGRATION_POINT, refinement=(
    COMPONENT, 'SF1'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Mises'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S11'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S33'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S11'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=928.799, 
    farPlane=1415.04, width=610.801, height=286.584, viewOffsetX=-11.0108, 
    viewOffsetY=1.55187)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S12'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S33'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S22'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S33'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S22'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S11'), )
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p1 = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
odb = session.odbs['Y:/mb_faanes.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=959.965, 
    farPlane=1383.87, width=557.814, height=286.997, viewOffsetX=-18.5216, 
    viewOffsetY=12.3713)
session.viewports['Viewport: 1'].view.setValues(nearPlane=977.41, 
    farPlane=1371.96, width=567.951, height=292.213, cameraPosition=(664.835, 
    877.295, 723.299), cameraUpVector=(-0.548644, 0.472582, -0.689678), 
    cameraTarget=(163.679, 95.0022, 23.8802), viewOffsetX=-18.8582, 
    viewOffsetY=12.5961)
session.viewports['Viewport: 1'].view.setValues(nearPlane=938.351, 
    farPlane=1390.7, width=545.255, height=280.536, cameraPosition=(953.127, 
    785.918, 508.379), cameraUpVector=(-0.518935, 0.511192, -0.68512), 
    cameraTarget=(161.873, 87.1592, 20.5468), viewOffsetX=-18.1046, 
    viewOffsetY=12.0927)
session.viewports['Viewport: 1'].view.setValues(nearPlane=969.077, 
    farPlane=1376.21, width=563.11, height=289.722, cameraPosition=(756.384, 
    829.114, 699.04), cameraUpVector=(-0.593712, 0.518698, -0.615189), 
    cameraTarget=(165.272, 93.6633, 19.3159), viewOffsetX=-18.6974, 
    viewOffsetY=12.4887)
session.viewports['Viewport: 1'].view.setValues(nearPlane=967.761, 
    farPlane=1377.52, width=562.346, height=289.329, viewOffsetX=-1.56404, 
    viewOffsetY=-24.7011)
session.viewports['Viewport: 1'].view.setValues(nearPlane=967.758, 
    farPlane=1377.52, width=562.344, height=289.328, viewOffsetX=26.9492, 
    viewOffsetY=27.0311)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=33.9191, 
    viewOffsetY=38.1829)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=18.0784, 
    viewOffsetY=2.55897)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=68.7686, 
    viewOffsetY=18.0476)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=13.643, 
    viewOffsetY=69.47)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=10.4748, 
    viewOffsetY=54.6009)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=-5.6827, 
    viewOffsetY=21.4552)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=-2.51458, 
    viewOffsetY=41.5905)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=8.57389, 
    viewOffsetY=44.0687)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=14.2765, 
    viewOffsetY=21.4552)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=89.3613, 
    viewOffsetY=17.7379)
mdb.saveAs(pathName='Y:/faanes')
#: The model database has been saved to "Y:\faanes.cae".

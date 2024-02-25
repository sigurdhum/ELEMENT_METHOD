# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2024 replay file
# Internal Version: 2023_09_21-14.55.25 RELr426 190762
# Run by 10992702 on Fri Feb 23 14:37:49 2024
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
mdb.openAuxMdb(pathName='Y:/faanes.cae')
mdb.copyAuxMdbModel(fromName='Model-1', toName='Model-1')
mdb.closeAuxMdb()
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
mdb.Job(name='mb_16_job', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs['mb_16_job'].submit(consistencyChecking=OFF)
#: The job input file "mb_16_job.inp" has been submitted for analysis.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='points_load')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    step='uniformed_load')
#: Job mb_16_job: Analysis Input File Processor completed successfully.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
#: Job mb_16_job: Abaqus/Standard completed successfully.
#: Job mb_16_job completed successfully. 
mdb.models['Model-1'].StaticLinearPerturbationStep(name='clamped_edges', 
    previous='Initial')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    step='clamped_edges')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='points_load')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    step='uniformed_load')
mdb.models['Model-1'].boundaryConditions['fixed'].deactivate('uniformed_load')
mdb.models['Model-1'].boundaryConditions['fixed'].reset('uniformed_load')
mdb.models['Model-1'].boundaryConditions['fixed'].deactivate('clamped_edges')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    step='clamped_edges')
mdb.models['Model-1'].Load(name='uniformed_load-Copy', 
    objectToCopy=mdb.models['Model-1'].loads['uniformed_load'], 
    toStepName='clamped_edges')
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['Part-1-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#f ]', ), )
region = a.Set(edges=edges1, name='Set-3')
mdb.models['Model-1'].DisplacementBC(name='clamped_edges', 
    createStepName='clamped_edges', region=region, u1=0.0, u2=0.0, u3=0.0, 
    ur1=0.0, ur2=0.0, ur3=0.0, amplitude=UNSET, fixed=OFF, 
    distributionType=UNIFORM, fieldName='', localCsys=None)
session.viewports['Viewport: 1'].view.setValues(nearPlane=621.785, 
    farPlane=1004.12, width=419.225, height=223.262, viewOffsetX=-12.3852, 
    viewOffsetY=4.1006)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].move('points_load', 
    'clamped_edges')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
mdb.models['Model-1'].historyOutputRequests['H-Output-1'].move('points_load', 
    'clamped_edges')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
mdb.jobs['mb_16_job'].submit(consistencyChecking=OFF)
#: The job input file "mb_16_job.inp" has been submitted for analysis.
#: Job mb_16_job: Analysis Input File Processor completed successfully.
#: Job mb_16_job: Abaqus/Standard completed successfully.
#: Job mb_16_job completed successfully. 
o3 = session.openOdb(name='Y:/mb_16_job.odb')
#: Model: Y:/mb_16_job.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       3
#: Number of Node Sets:          6
#: Number of Steps:              3
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U1'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U2'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].view.setValues(nearPlane=1018.49, 
    farPlane=1340.56, width=781.131, height=428.273, cameraPosition=(389.749, 
    663.912, 1007.81), cameraUpVector=(-0.169097, 0.656542, -0.735091), 
    cameraTarget=(159.302, 91.4195, 22.1778))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1050.5, 
    farPlane=1328.99, width=805.683, height=441.734, cameraPosition=(460.507, 
    292.768, 1128.2), cameraUpVector=(-0.0847025, 0.867451, -0.490259), 
    cameraTarget=(160.3, 86.1867, 23.8751))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1032.17, 
    farPlane=1402.75, width=791.625, height=434.026, cameraPosition=(281.311, 
    -929.623, 612.32), cameraUpVector=(0.153236, 0.78004, 0.606677), 
    cameraTarget=(156.257, 58.6037, 12.2344))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1079.01, 
    farPlane=1345.57, width=827.546, height=453.721, cameraPosition=(206.232, 
    -408.985, 1086.32), cameraUpVector=(0.328525, 0.942902, 0.0548347), 
    cameraTarget=(152.892, 81.9364, 33.4771))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1061.09, 
    farPlane=1351.95, width=813.803, height=446.186, cameraPosition=(557.927, 
    212.771, 1125.27), cameraUpVector=(-0.0527386, 0.904056, -0.424149), 
    cameraTarget=(167.222, 107.269, 35.064))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1088.4, 
    farPlane=1328.34, width=834.748, height=457.669, cameraPosition=(378.757, 
    13.1758, 1175.86), cameraUpVector=(-0.0333602, 0.964938, -0.260351), 
    cameraTarget=(160.744, 100.052, 36.8932))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1104.95, 
    farPlane=1314.39, width=847.44, height=464.628, cameraPosition=(101.803, 
    -48.2011, 1190.11), cameraUpVector=(-0.0190681, 0.976774, -0.213421), 
    cameraTarget=(150.321, 97.7421, 37.4294))
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
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
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
odb = session.odbs['Y:/mb_16_job.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['Y:/mb_16_job.odb'])
odb = session.odbs['Y:/mb_16_job.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].view.setValues(nearPlane=1103.97, 
    farPlane=1315.37, width=846.689, height=464.216, viewOffsetX=19.375, 
    viewOffsetY=-58.9179)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1103.97, 
    farPlane=1315.37, width=846.686, height=464.214, viewOffsetX=21.3125, 
    viewOffsetY=-11.8786)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1042.16, 
    farPlane=1406.48, width=799.279, height=438.223, cameraPosition=(407.835, 
    -640.21, 925.959), cameraUpVector=(-0.158459, 0.925169, 0.344897), 
    cameraTarget=(161.999, 68.0682, 37.0083), viewOffsetX=20.1192, 
    viewOffsetY=-11.2135)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=1 )
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    step='uniformed_load')
mdb.models['Model-1'].loads['uniformed_load'].setValues(magnitude=0.70761)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.Job(name='mb_uf_70', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
o3 = session.openOdb(name='Y:/mb_16_job.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=1 )
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.jobs['mb_uf_70'].submit(consistencyChecking=OFF)
#: The job input file "mb_uf_70.inp" has been submitted for analysis.
#: Job mb_uf_70: Analysis Input File Processor completed successfully.
#: Job mb_uf_70: Abaqus/Standard completed successfully.
#: Job mb_uf_70 completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['Y:/mb_16_job.odb'])
o3 = session.openOdb(name='Y:/mb_uf_70.odb')
#: Model: Y:/mb_uf_70.odb
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
    variableLabel='UR', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=1 )
session.viewports['Viewport: 1'].view.setValues(nearPlane=1019.21, 
    farPlane=1346.57, width=781.686, height=428.577, cameraPosition=(496.947, 
    535.5, 1042.64), cameraUpVector=(-0.327568, 0.735735, -0.592784), 
    cameraTarget=(160.127, 90.4308, 22.4459))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1089.96, 
    farPlane=1290.96, width=835.945, height=458.326, cameraPosition=(160.379, 
    295.378, 1168.52), cameraUpVector=(-0.169001, 0.852981, -0.493824), 
    cameraTarget=(154.438, 86.3724, 24.5735))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1034.33, 
    farPlane=1398.31, width=793.276, height=434.932, cameraPosition=(284.361, 
    -848.339, 729.464), cameraUpVector=(-0.222119, 0.815951, 0.533748), 
    cameraTarget=(157.308, 59.8929, 14.4084))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1033.43, 
    farPlane=1407.31, width=792.585, height=434.553, cameraPosition=(255.129, 
    -1025.53, 426.781), cameraUpVector=(-0.216158, 0.633338, 0.743074), 
    cameraTarget=(156.024, 52.1103, 1.11429))
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
mdb.models['Model-1'].loads['uniformed_load'].setValues(magnitude=144619183.0)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.Job(name='mb_uf_00001', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs['mb_uf_00001'].submit(consistencyChecking=OFF)
#: The job input file "mb_uf_00001.inp" has been submitted for analysis.
#: Job mb_uf_00001: Analysis Input File Processor completed successfully.
#: Job mb_uf_00001: Abaqus/Standard completed successfully.
#: Job mb_uf_00001 completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['Y:/mb_uf_70.odb'])
o3 = session.openOdb(name='Y:/mb_uf_00001.odb')
#: Model: Y:/mb_uf_00001.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       3
#: Number of Node Sets:          6
#: Number of Steps:              3
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=1 )
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
mdb.models['Model-1'].loads['uniformed_load'].setValues(magnitude=1.44619e-05)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.jobs['mb_uf_00001'].submit(consistencyChecking=OFF)
#: The job input file "mb_uf_00001.inp" has been submitted for analysis.
#: Job mb_uf_00001: Analysis Input File Processor completed successfully.
#: Job mb_uf_00001: Abaqus/Standard completed successfully.
#: Job mb_uf_00001 completed successfully. 
o3 = session.openOdb(name='Y:/mb_uf_00001.odb')
#: Model: Y:/mb_uf_00001.odb
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
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=1 )
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
mdb.models['Model-1'].loads['uniformed_load'].setValues(
    magnitude=1.44619183e-05)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.jobs['mb_uf_00001'].submit(consistencyChecking=OFF)
#: The job input file "mb_uf_00001.inp" has been submitted for analysis.
#: Job mb_uf_00001: Analysis Input File Processor completed successfully.
#: Job mb_uf_00001: Abaqus/Standard completed successfully.
#: Job mb_uf_00001 completed successfully. 
o3 = session.openOdb(name='Y:/mb_uf_00001.odb')
#: Model: Y:/mb_uf_00001.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       3
#: Number of Node Sets:          6
#: Number of Steps:              3
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
del mdb.models['Model-1'].loads['uniformed_load-Copy']
mdb.models['Model-1'].Load(name='uniformed_load-Copy', 
    objectToCopy=mdb.models['Model-1'].loads['uniformed_load'], 
    toStepName='clamped_edges')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.Job(name='mb_uf_ce', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs['mb_uf_ce'].submit(consistencyChecking=OFF)
#: The job input file "mb_uf_ce.inp" has been submitted for analysis.
#: Job mb_uf_ce: Analysis Input File Processor completed successfully.
#: Job mb_uf_ce: Abaqus/Standard completed successfully.
#: Job mb_uf_ce completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['Y:/mb_uf_00001.odb'])
o3 = session.openOdb(name='Y:/mb_uf_ce.odb')
#: Model: Y:/mb_uf_ce.odb
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
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].view.setValues(nearPlane=1017.18, 
    farPlane=1368.97, width=477.976, height=688.902, cameraPosition=(610.483, 
    86.0606, 1095.37), cameraUpVector=(-0.253251, 0.933325, -0.254496), 
    cameraTarget=(161.001, 86.9702, 22.852))
session.viewports['Viewport: 1'].view.setValues(nearPlane=902.869, 
    farPlane=1500.44, width=424.261, height=611.483, cameraPosition=(1094.49, 
    -593.559, 253.783), cameraUpVector=(-0.0516124, 0.759324, 0.648662), 
    cameraTarget=(173.244, 69.7798, 1.56474))
session.viewports['Viewport: 1'].view.setValues(nearPlane=958.505, 
    farPlane=1420.33, width=450.405, height=649.164, cameraPosition=(1040.21, 
    173.605, -801.502), cameraUpVector=(0.216548, 0.551744, 0.80541), 
    cameraTarget=(171.493, 94.5243, -32.4729))
session.viewports['Viewport: 1'].view.setValues(nearPlane=973.896, 
    farPlane=1406.16, width=457.637, height=659.588, cameraPosition=(789.707, 
    276.583, -1001.76), cameraUpVector=(0.397169, 0.520888, 0.755601), 
    cameraTarget=(165.907, 96.8204, -36.9382))
session.viewports['Viewport: 1'].view.setValues(nearPlane=900.794, 
    farPlane=1489.45, width=423.286, height=610.079, cameraPosition=(1187.07, 
    -469.657, -179.616), cameraUpVector=(0.0388569, 0.52777, 0.848498), 
    cameraTarget=(174.967, 79.8051, -18.1921))
session.viewports['Viewport: 1'].view.setValues(nearPlane=983.102, 
    farPlane=1434.35, width=461.963, height=665.824, cameraPosition=(289.993, 
    -1084.4, 115.858), cameraUpVector=(0.34884, 0.469214, 0.811264), 
    cameraTarget=(150.775, 63.227, -10.2239))
session.viewports['Viewport: 1'].view.setValues(nearPlane=974.282, 
    farPlane=1458.47, width=457.818, height=659.85, cameraPosition=(-124.714, 
    -931.731, -568.482), cameraUpVector=(0.415885, -0.193288, 0.888639), 
    cameraTarget=(135.051, 69.0157, -36.1715))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1000.94, 
    farPlane=1430.41, width=470.344, height=677.904, cameraPosition=(54.4762, 
    -873.841, -713.921), cameraUpVector=(0.269379, -0.271353, 0.924015), 
    cameraTarget=(142.929, 71.561, -42.566))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1012.7, 
    farPlane=1421.17, width=475.87, height=685.868, cameraPosition=(53.0371, 
    -697.127, -912.296), cameraUpVector=(0.153258, -0.477843, 0.864973), 
    cameraTarget=(142.867, 79.2332, -51.1785))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1008.41, 
    farPlane=1417.97, width=473.854, height=682.962, cameraPosition=(-48.1398, 
    -530.521, 1001.62), cameraUpVector=(0.365125, 0.898705, 0.242926), 
    cameraTarget=(138.374, 86.6315, 33.8102))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1037.42, 
    farPlane=1385.16, width=487.487, height=702.612, cameraPosition=(240.994, 
    -320.974, 1120.79), cameraUpVector=(0.218073, 0.975932, -0.00103813), 
    cameraTarget=(150.361, 95.319, 38.7507))
mdb.saveAs(pathName='Y:/mb_ce')
#: The model database has been saved to "Y:\mb_ce.cae".

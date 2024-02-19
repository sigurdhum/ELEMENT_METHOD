# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2024 replay file
# Internal Version: 2023_09_21-14.55.25 RELr426 190762
# Run by 10992702 on Sat Feb 17 13:25:48 2024
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=193.77392578125, 
    height=197.34196472168)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
Mdb()
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(250.0, 0.0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=416.953, 
    farPlane=742.612, width=813.495, height=1001.14, cameraPosition=(-201.318, 
    137.54, 579.783), cameraTarget=(-201.318, 137.54, 0))
p = mdb.models['Model-1'].Part(name='excersize', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['excersize']
p.BaseShellExtrude(sketch=s, depth=500.0)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['excersize']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].view.setValues(nearPlane=1254.8, 
    farPlane=2403.74, width=711.098, height=824.124, viewOffsetX=22.2353, 
    viewOffsetY=26.9161)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1317.45, 
    farPlane=2393.35, width=746.597, height=865.266, cameraPosition=(1198.82, 
    1345.25, -194.357), cameraUpVector=(-0.941732, 0.331643, -0.0561602), 
    cameraTarget=(49.2651, -3.74754, 258.363), viewOffsetX=23.3453, 
    viewOffsetY=28.2598)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1386.83, 
    farPlane=2363.3, width=785.917, height=910.836, cameraPosition=(-412.643, 
    330.099, -1550.19), cameraUpVector=(-0.144467, 0.817163, 0.558009), 
    cameraTarget=(34.5565, -30.5766, 186.513), viewOffsetX=24.5748, 
    viewOffsetY=29.7481)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1298.43, 
    farPlane=2440.8, width=735.822, height=852.778, cameraPosition=(-814.867, 
    917.416, -1162.05), cameraUpVector=(0.330804, 0.635683, 0.697478), 
    cameraTarget=(5.61955, -20.0303, 177.434), viewOffsetX=23.0084, 
    viewOffsetY=27.8519)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
mdb.saveAs(pathName='Y:/excersize')
#: The model database has been saved to "Y:\excersize.cae".
mdb.models['Model-1'].Material(name='alu')
mdb.models['Model-1'].materials['alu'].Elastic(table=((72000.0, 0.35), ))
mdb.models['Model-1'].materials['alu'].Plastic(scaleStress=None, table=((160.0, 
    0.0), (340.0, 0.3)))
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
a = mdb.models['Model-1'].rootAssembly
a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-1'].parts['excersize']
a.Instance(name='excersize-1', part=p, dependent=ON)
a = mdb.models['Model-1'].rootAssembly
a.ReferencePoint(point=(0.0, 0.0, 0.0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1383.68, 
    farPlane=2291.56, width=609.717, height=706.629, cameraPosition=(431.793, 
    333.806, 2004.87), cameraUpVector=(-0.399891, 0.815291, -0.418793), 
    cameraTarget=(10.4896, -20.979, 260.49))
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['excersize-1'].edges
a.ReferencePoint(point=a.instances['excersize-1'].InterestingPoint(edge=e1[0], 
    rule=CENTER))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
p = mdb.models['Model-1'].parts['excersize']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
mdb.models['Model-1'].HomogeneousShellSection(name='Section-1', 
    preIntegrate=OFF, material='alu', thicknessType=UNIFORM, thickness=2.0, 
    thicknessField='', nodalThicknessField='', idealization=NO_IDEALIZATION, 
    poissonDefinition=DEFAULT, thicknessModulus=None, temperature=GRADIENT, 
    useDensity=OFF, integrationRule=SIMPSON, numIntPts=5)
p = mdb.models['Model-1'].parts['excersize']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region = p.Set(faces=faces, name='Set-1')
p = mdb.models['Model-1'].parts['excersize']
p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
a1 = mdb.models['Model-1'].rootAssembly
a1.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, interactions=ON, constraints=ON, 
    engineeringFeatures=ON)
mdb.save()
#: The model database has been saved to "Y:\excersize.cae".
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[4], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-1')
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['excersize-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#2 ]', ), )
region2=a.Set(edges=edges1, name='s_Set-1')
mdb.models['Model-1'].Coupling(name='rp1', controlPoint=region1, 
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC, 
    alpha=0.0, localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[5], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-3')
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['excersize-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#1 ]', ), )
region2=a.Set(edges=edges1, name='s_Set-3')
mdb.models['Model-1'].Coupling(name='rp2', controlPoint=region1, 
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC, 
    alpha=0.0, localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1378.87, 
    farPlane=2296.37, width=607.599, height=704.174, viewOffsetX=33.3148, 
    viewOffsetY=-3.11237)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1378.84, 
    farPlane=2296.4, width=607.586, height=704.159, viewOffsetX=-38.0733, 
    viewOffsetY=6.22463)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1275.66, 
    farPlane=2315.4, width=562.119, height=651.465, cameraPosition=(1479.21, 
    837.201, 829.522), cameraUpVector=(-0.674481, 0.669174, -0.3119), 
    cameraTarget=(-10.2151, -35.1409, 223.823), viewOffsetX=-35.2242, 
    viewOffsetY=5.75882)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1239.48, 
    farPlane=2296.88, width=546.175, height=632.987, cameraPosition=(1067.58, 
    669.936, -990.74), cameraUpVector=(-0.757668, 0.629025, 0.173973), 
    cameraTarget=(-47.8352, -51.9825, 266.602), viewOffsetX=-34.2251, 
    viewOffsetY=5.59547)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1374.92, 
    farPlane=2140.17, width=605.857, height=702.155, cameraPosition=(-223.124, 
    -13.0715, -1493.81), cameraUpVector=(-0.527787, 0.746469, 0.405246), 
    cameraTarget=(-16.3155, -36.6287, 323.576), viewOffsetX=-37.965, 
    viewOffsetY=6.2069)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[4], )
region = a.Set(referencePoints=refPoints1, name='Set-5')
mdb.models['Model-1'].DisplacementBC(name='encaster', createStepName='Initial', 
    region=region, u1=SET, u2=SET, u3=SET, ur1=SET, ur2=SET, ur3=SET, 
    amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=None)
mdb.save()
#: The model database has been saved to "Y:\excersize.cae".
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF, adaptiveMeshConstraints=ON)
mdb.models['Model-1'].BuckleStep(name='lin_pert', previous='Initial', 
    numEigen=3, vectors=6, maxIterations=6500)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='lin_pert')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, 
    adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['Model-1'].parts['excersize']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF, mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['Model-1'].parts['excersize']
p.seedPart(size=10.0, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['excersize']
p.generateMesh()
mdb.save()
#: The model database has been saved to "Y:\excersize.cae".
a1 = mdb.models['Model-1'].rootAssembly
a1.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
mdb.Job(name='lp_coarse', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['Model-1'].parts['excersize']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['excersize']
p.deleteMesh()
p = mdb.models['Model-1'].parts['excersize']
p.seedPart(size=5.0, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['excersize']
p.generateMesh()
mdb.save()
#: The model database has been saved to "Y:\excersize.cae".
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
mdb.Job(name='lp_fine', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1218.44, 
    farPlane=2289.94, width=536.906, height=660.749, cameraPosition=(-770.309, 
    -930.155, -1023.27), cameraUpVector=(-0.693715, 0.400828, 0.598412), 
    cameraTarget=(48.8147, -5.8882, 326.172), viewOffsetX=-33.6443, 
    viewOffsetY=5.50051)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1227.9, 
    farPlane=2277.93, width=541.076, height=665.881, cameraPosition=(-902.852, 
    -1303.36, -499.349), cameraUpVector=(-0.574352, 0.474616, 0.666978), 
    cameraTarget=(67.9184, 19.2763, 309.633), viewOffsetX=-33.9056, 
    viewOffsetY=5.54323)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1245.65, 
    farPlane=2265.42, width=548.896, height=675.505, cameraPosition=(-484.058, 
    -1084.55, -1043.82), cameraUpVector=(-0.803873, 0.298844, 0.514277), 
    cameraTarget=(40.7431, 3.23143, 330.049), viewOffsetX=-34.3956, 
    viewOffsetY=5.62334)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1222.21, 
    farPlane=2285.01, width=538.57, height=662.796, cameraPosition=(-856.525, 
    -950.236, -950.586), cameraUpVector=(-0.593382, 0.171848, 0.786363), 
    cameraTarget=(66.2323, -4.51032, 314.453), viewOffsetX=-33.7485, 
    viewOffsetY=5.51754)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1214.03, 
    farPlane=2293.19, width=1444.06, height=700.383, viewOffsetX=-59.9944, 
    viewOffsetY=7.31432)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1354.19, 
    farPlane=2219.86, width=1610.77, height=781.243, cameraPosition=(-444.143, 
    1709.83, -35.4505), cameraUpVector=(-0.214059, -0.259667, 0.941675), 
    cameraTarget=(-68.9744, -63.8874, 208.25), viewOffsetX=-66.9208, 
    viewOffsetY=8.15876)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1274.32, 
    farPlane=2285.27, width=1515.77, height=735.167, cameraPosition=(1346.85, 
    -212.529, 1397.74), cameraUpVector=(-0.726322, 0.544777, 0.419137), 
    cameraTarget=(16.4685, 73.5563, 175.268), viewOffsetX=-62.974, 
    viewOffsetY=7.67757)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1252.96, 
    farPlane=2301.84, width=1490.37, height=722.846, cameraPosition=(680.097, 
    -972.868, 1576.26), cameraUpVector=(-0.563621, 0.738755, 0.369558), 
    cameraTarget=(66.7546, 70.6657, 204.744), viewOffsetX=-61.9186, 
    viewOffsetY=7.5489)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1297.43, 
    farPlane=2255.15, width=1543.27, height=748.504, cameraPosition=(213.128, 
    -1260.48, 1486.8), cameraUpVector=(-0.516026, 0.768748, 0.377814), 
    cameraTarget=(84.3519, 63.4214, 231.045), viewOffsetX=-64.1164, 
    viewOffsetY=7.81685)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1245.7, 
    farPlane=2300.15, width=1481.74, height=718.661, cameraPosition=(-483.713, 
    -1154.52, 1508.9), cameraUpVector=(-0.407453, 0.895358, 0.179766), 
    cameraTarget=(98.696, 43.2886, 255), viewOffsetX=-61.5601, 
    viewOffsetY=7.50519)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1259.72, 
    farPlane=2286.57, width=1498.42, height=726.752, cameraPosition=(1121.28, 
    525.287, 1522.3), cameraUpVector=(-0.886518, 0.447769, 0.11657), 
    cameraTarget=(8.71313, 40.6657, 153.522), viewOffsetX=-62.2532, 
    viewOffsetY=7.58969)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1270.13, 
    farPlane=2272.22, width=1510.8, height=732.756, cameraPosition=(1009.09, 
    1433.39, 518.149), cameraUpVector=(-0.912179, 0.145236, 0.383193), 
    cameraTarget=(-42.8735, -18.5357, 155.533), viewOffsetX=-62.7675, 
    viewOffsetY=7.65239)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1230.16, 
    farPlane=2311.21, width=1463.26, height=709.696, cameraPosition=(947.359, 
    1005.49, 1361.18), cameraUpVector=(-0.974029, 0.204775, 0.0966157), 
    cameraTarget=(-5.44471, 24.177, 146.521), viewOffsetX=-60.7922, 
    viewOffsetY=7.41157)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1267.91, 
    farPlane=2280.73, width=1508.17, height=731.476, cameraPosition=(1024.9, 
    -379.171, 1650.7), cameraUpVector=(-0.852475, 0.425692, 0.303436), 
    cameraTarget=(22.3062, 84.7369, 192.692), viewOffsetX=-62.6579, 
    viewOffsetY=7.63903)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
mdb.jobs['lp_fine'].submit(consistencyChecking=OFF)
#: The job input file "lp_fine.inp" has been submitted for analysis.
#: Job lp_fine: Analysis Input File Processor completed successfully.
#: Error in job lp_fine: DIFFERENTIAL STIFFNESS MATRIX IS COMPLETELY NULL.  THE EIGENPROBLEM CANNOT BE SOLVED.  IN A *BUCKLE ANALYSIS THE MOST LIKELY CAUSE IS THAT A NONZERO LOADING PATTERN WAS NOT SPECIFIED VIA *BOUNDARY, *CLOAD, *DLOAD, ETC,.  SEE Eigenvalue Buckling Prediction IN THE Abaqus/Standard USERS MANUAL.
#: Job lp_fine: Abaqus/Standard aborted due to errors.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
#: Error in job lp_fine: Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.
#: Job lp_fine aborted due to errors.
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[5], )
region = a.Set(referencePoints=refPoints1, name='Set-6')
mdb.models['Model-1'].ConcentratedForce(name='lp', createStepName='lin_pert', 
    region=region, cf3=-1.0, distributionType=UNIFORM, field='', 
    localCsys=None)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1247.52, 
    farPlane=2317.47, width=2098.09, height=719.711, cameraPosition=(1577.39, 
    -753.561, -109.375), cameraUpVector=(-0.089181, 0.150695, 0.984549), 
    cameraTarget=(-3.58644, 99.2505, 236.213), viewOffsetX=-61.6501, 
    viewOffsetY=7.51617)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1249.62, 
    farPlane=2315.37, width=2101.62, height=720.923, cameraPosition=(1570.03, 
    -758.549, -130.721), cameraUpVector=(0.0152913, 0.36633, 0.930359), 
    cameraTarget=(-10.9431, 94.2625, 214.867), viewOffsetX=-61.7539, 
    viewOffsetY=7.52883)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1236.07, 
    farPlane=2321.59, width=2078.84, height=713.108, cameraPosition=(954.465, 
    -345.15, 1713.55), cameraUpVector=(-0.633797, 0.752806, 0.177722), 
    cameraTarget=(43.5631, 60.0083, 179.833), viewOffsetX=-61.0845, 
    viewOffsetY=7.44722)
mdb.save()
#: The model database has been saved to "Y:\excersize.cae".
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF, adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
mdb.jobs['lp_fine'].submit(consistencyChecking=OFF)
#: The job input file "lp_fine.inp" has been submitted for analysis.
#: Job lp_fine: Analysis Input File Processor completed successfully.
session.viewports['Viewport: 1'].view.setValues(nearPlane=1211.61, 
    farPlane=2345.01, width=2037.7, height=886.312, cameraPosition=(-1462.11, 
    -677.46, 1007.19), cameraUpVector=(-0.218613, 0.870531, -0.44089), 
    cameraTarget=(63.088, 52.5514, 309.313), viewOffsetX=-59.8757, 
    viewOffsetY=7.29985)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1221.7, 
    farPlane=2332.55, width=2054.68, height=893.696, cameraPosition=(444.961, 
    1027.03, 1633.18), cameraUpVector=(-0.875923, 0.300383, -0.37753), 
    cameraTarget=(40.1352, 23.14, 158.559), viewOffsetX=-60.3745, 
    viewOffsetY=7.36066)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1197.01, 
    farPlane=2357.01, width=2013.16, height=875.637, cameraPosition=(986.736, 
    573.21, -1115.08), cameraUpVector=(-0.93596, 0.339937, -0.0917664), 
    cameraTarget=(-40.457, -94.5669, 243.277), viewOffsetX=-59.1545, 
    viewOffsetY=7.21192)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1252.93, 
    farPlane=2300.8, width=2107.21, height=916.545, cameraPosition=(-1367.07, 
    -1138.52, 247.508), cameraUpVector=(-0.330127, 0.926767, -0.179219), 
    cameraTarget=(32.2586, 35.9368, 340.904), viewOffsetX=-61.9181, 
    viewOffsetY=7.54884)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1251.53, 
    farPlane=2301.85, width=2104.85, height=915.521, cameraPosition=(-779.607, 
    198.869, 1836.54), cameraUpVector=(-0.397928, 0.641162, -0.656174), 
    cameraTarget=(89.1945, 48.8011, 233.779), viewOffsetX=-61.8489, 
    viewOffsetY=7.5404)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1251.71, 
    farPlane=2301.66, width=2105.16, height=915.655, cameraPosition=(-768.59, 
    173.623, 1844.88), cameraUpVector=(-0.170862, 0.817753, -0.549624), 
    cameraTarget=(100.212, 23.5555, 242.115), viewOffsetX=-61.8579, 
    viewOffsetY=7.5415)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1205.44, 
    farPlane=2348.18, width=2027.35, height=881.811, cameraPosition=(-1054.82, 
    -433.583, 1615.4), cameraUpVector=(-0.195732, 0.934861, -0.296183), 
    cameraTarget=(95.1351, 33.7242, 271.743), viewOffsetX=-59.5715, 
    viewOffsetY=7.26275)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1200.55, 
    farPlane=2353.2, width=2019.12, height=878.231, cameraPosition=(-1024.57, 
    -575.421, 1585.8), cameraUpVector=(-0.243637, 0.941473, -0.232957), 
    cameraTarget=(93.4155, 36.9109, 273.791), viewOffsetX=-59.3296, 
    viewOffsetY=7.23326)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1201.2, 
    farPlane=2352.56, width=2020.22, height=878.71, cameraPosition=(-1031.32, 
    -562.076, 1586.28), cameraUpVector=(-0.337894, 0.876161, -0.343757), 
    cameraTarget=(86.6685, 50.256, 274.27), viewOffsetX=-59.3619, 
    viewOffsetY=7.2372)
o3 = session.openOdb(name='Y:/lp_fine.odb')
#: Model: Y:/lp_fine.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          10
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
#: Job lp_fine: Abaqus/Standard completed successfully.
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
#: Job lp_fine completed successfully. 
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(name='Y:/lp_fine.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=3 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=3 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=3 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=3 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=3 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=3 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U1'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U2'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=1340.54, 
    farPlane=2360.85, width=594.213, height=629.058, cameraPosition=(455.308, 
    -897.414, 1803.26), cameraUpVector=(-0.136053, 0.971177, 0.195715), 
    cameraTarget=(10.4901, -20.9795, 260.49))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1374.72, 
    farPlane=2341.21, width=609.364, height=645.098, cameraPosition=(259.686, 
    -1680.38, 999.055), cameraUpVector=(0.0815501, 0.702356, 0.707139), 
    cameraTarget=(8.22285, -30.054, 251.169))
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='UR', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='UR', outputPosition=NODAL, refinement=(COMPONENT, 'UR1'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='UR', outputPosition=NODAL, refinement=(COMPONENT, 'UR2'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='UR', outputPosition=NODAL, refinement=(COMPONENT, 'UR3'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=SYMBOLS_ON_DEF)
session.viewports['Viewport: 1'].odbDisplay.setSymbolVariable(
    variableLabel='U', outputPosition=NODAL, vectorQuantity=RESULTANT, )
session.viewports['Viewport: 1'].odbDisplay.setSymbolVariable(
    variableLabel='UR', outputPosition=NODAL, vectorQuantity=RESULTANT, )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U1'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U2'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=1375.2, 
    farPlane=2325.2, width=1483.65, height=645.321, cameraPosition=(-1687.86, 
    -175.041, 987.448), cameraUpVector=(0.529835, 0.667544, 0.523125), 
    cameraTarget=(-21.8845, -6.78273, 250.99))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1328.34, 
    farPlane=2367.29, width=1433.09, height=623.331, cameraPosition=(-486.597, 
    -1043.18, 1695.5), cameraUpVector=(0.596018, 0.742851, 0.304853), 
    cameraTarget=(-8.28246, -16.6128, 259.007))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1412.78, 
    farPlane=2275.96, width=1524.18, height=662.953, cameraPosition=(-49.8725, 
    -543.704, 2011.72), cameraUpVector=(0.642384, 0.759756, -0.100564), 
    cameraTarget=(-3.89354, -11.5932, 262.185))
mdb.save()
#: The model database has been saved to "Y:\excersize.cae".
Mdb()
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=300.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=STANDALONE)
s1.rectangle(point1=(0.0, 0.0), point2=(312.6, 221.2))
p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Part-1']
p.BaseSolidExtrude(sketch=s1, depth=15.5)
s1.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].view.setValues(nearPlane=607.615, 
    farPlane=1018.29, width=625.621, height=262.676, viewOffsetX=13.972, 
    viewOffsetY=-4.3648)
p = mdb.models['Model-1'].parts['Part-1']
c1 = p.cells
p.AssignMidsurfaceRegion(cellList = c1[0:1])
#: 
#: The selected cells have been added as reference representation.
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
f1 = p.faces
p.OffsetFaces(faceList = f[1:2], targetFaces = f1[3:4], 
    targetFacesMethod=HALF_OF_AVERAGE, trimToReferenceRep=False)
#: 
#: The distance used for offset is: 7.750000
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
mdb.models['Model-1'].Material(name='apple_alu')
mdb.models['Model-1'].materials['apple_alu'].Elastic(table=((72000.0, 0.333), 
    ))
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a1 = mdb.models['Model-1'].rootAssembly
a1.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-1'].parts['Part-1']
a1.Instance(name='Part-1-1', part=p, dependent=ON)
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
mdb.models['Model-1'].StaticLinearPerturbationStep(name='uniformed_load', 
    previous='Initial')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    step='uniformed_load')
mdb.models['Model-1'].StaticLinearPerturbationStep(name='points_loads', 
    previous='uniformed_load')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='points_loads')
del mdb.models['Model-1'].steps['points_loads']
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
mdb.models['Model-1'].StaticLinearPerturbationStep(name='points_load', 
    previous='Initial')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='points_load')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
mdb.models['Model-1'].HomogeneousShellSection(name='mb_section', 
    preIntegrate=OFF, material='apple_alu', thicknessType=UNIFORM, 
    thickness=15.5, thicknessField='', nodalThicknessField='', 
    idealization=NO_IDEALIZATION, poissonDefinition=DEFAULT, 
    thicknessModulus=None, temperature=GRADIENT, useDensity=OFF, 
    integrationRule=SIMPSON, numIntPts=5)
p = mdb.models['Model-1'].parts['Part-1']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region = p.Set(faces=faces, name='Set-1')
p = mdb.models['Model-1'].parts['Part-1']
p.SectionAssignment(region=region, sectionName='mb_section', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].view.setValues(nearPlane=613.693, 
    farPlane=998.582, width=631.879, height=265.304, cameraPosition=(464.064, 
    701.434, 461.86), cameraUpVector=(-0.570902, 0.39236, -0.721197), 
    cameraTarget=(165.034, 104.473, -1.93944), viewOffsetX=14.1117, 
    viewOffsetY=-4.40847)
session.viewports['Viewport: 1'].view.setValues(nearPlane=612.972, 
    farPlane=999.304, width=631.136, height=264.992, cameraPosition=(463.975, 
    701.722, 461.547), cameraUpVector=(-0.553912, 0.393554, -0.733688), 
    cameraTarget=(164.945, 104.761, -2.25282), viewOffsetX=14.0951, 
    viewOffsetY=-4.40329)
session.viewports['Viewport: 1'].view.setValues(nearPlane=605.485, 
    farPlane=1019.2, width=623.427, height=261.755, cameraPosition=(629.472, 
    572.172, 480.093), cameraUpVector=(-0.525099, 0.583035, -0.619953), 
    cameraTarget=(165.439, 108.473, -0.0614958), viewOffsetX=13.9229, 
    viewOffsetY=-4.34951)
a1 = mdb.models['Model-1'].rootAssembly
a1.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1397.42, 
    farPlane=1822.96, width=726.476, height=305.022, viewOffsetX=-72.9153, 
    viewOffsetY=53.4903)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(variables=(
    'CF', 'LE', 'RF', 'S', 'U', 'SF'))
mdb.saveAs(pathName='Y:/mp16_v2')
#: The model database has been saved to "Y:\mp16_v2.cae".
mdb.save()
#: The model database has been saved to "Y:\mp16_v2.cae".

# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2024 replay file
# Internal Version: 2023_09_21-14.55.25 RELr426 190762
# Run by 10992702 on Fri Feb 16 12:09:52 2024
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
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.rectangle(point1=(0.0, 0.0), point2=(45.0, 25.0))
s.ObliqueDimension(vertex1=v[0], vertex2=v[1], textPoint=(-16.5716514587402, 
    14.2221069335938), value=221.2)
s.ObliqueDimension(vertex1=v[1], vertex2=v[2], textPoint=(20.9518432617188, 
    30.7727699279785), value=312.6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1825.7, 
    farPlane=2045.17, width=1600.59, height=776.304, cameraPosition=(204.308, 
    -154.649, 1935.43), cameraTarget=(204.308, -154.649, 0))
p = mdb.models['Model-1'].Part(name='mb_16', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['mb_16']
p.BaseSolidExtrude(sketch=s, depth=15.5)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['mb_16']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
p = mdb.models['Model-1'].parts['mb_16']
c1 = p.cells
p.AssignMidsurfaceRegion(cellList = c1[0:1])
#: 
#: The selected cells have been added as reference representation.
session.viewports['Viewport: 1'].view.setValues(nearPlane=606.934, 
    farPlane=1025.69, width=523.527, height=246.639, cameraPosition=(792.909, 
    238.653, 402.871), cameraUpVector=(-0.498531, 0.718449, -0.485074), 
    cameraTarget=(167.147, -89.7071, 1.01027))
mdb.saveAs(pathName='Y:/mb_16_v2')
#: The model database has been saved to "Y:\mb_16_v2.cae".
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
p = mdb.models['Model-1'].parts['mb_16']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['mb_16']
f = p.faces
f1 = p.faces
p.OffsetFaces(faceList = f[1:2], targetFaces = f1[3:4], 
    targetFacesMethod=HALF_OF_AVERAGE, trimToReferenceRep=False)
#: 
#: The distance used for offset is: 7.750000
mdb.save()
#: The model database has been saved to "Y:\mb_16_v2.cae".
session.viewports['Viewport: 1'].view.setValues(nearPlane=635.141, 
    farPlane=993.782, width=547.857, height=258.101, cameraPosition=(708.096, 
    141.971, 562.047), cameraUpVector=(-0.540841, 0.790145, -0.288378), 
    cameraTarget=(166.798, -90.1049, 1.66522))
session.viewports['Viewport: 1'].view.setValues(nearPlane=588.352, 
    farPlane=1015.56, width=507.498, height=239.088, cameraPosition=(-384.896, 
    384.231, 367.621), cameraUpVector=(0.202076, 0.365055, -0.908791), 
    cameraTarget=(164.772, -89.6558, 1.30476))
session.viewports['Viewport: 1'].view.setValues(nearPlane=653.054, 
    farPlane=950.188, width=563.308, height=265.381, cameraPosition=(-96.3812, 
    321.937, 650.144), cameraUpVector=(-0.190232, 0.532154, -0.825), 
    cameraTarget=(160.816, -88.8017, -2.56913))
session.viewports['Viewport: 1'].view.setValues(nearPlane=648.983, 
    farPlane=954.258, width=559.796, height=263.727, cameraPosition=(-96.3812, 
    321.937, 650.144), cameraUpVector=(0.101207, 0.628783, -0.770967), 
    cameraTarget=(160.816, -88.8017, -2.56913))
session.viewports['Viewport: 1'].view.setValues(nearPlane=649.239, 
    farPlane=954.002, width=560.017, height=263.831, cameraPosition=(-96.3812, 
    321.937, 650.144), cameraUpVector=(0.304017, 0.644903, -0.701195), 
    cameraTarget=(160.816, -88.8017, -2.56913))
session.viewports['Viewport: 1'].view.setValues(nearPlane=693.136, 
    farPlane=907.303, width=597.881, height=281.669, cameraPosition=(-129.318, 
    -60.3761, 754.84), cameraUpVector=(0.235431, 0.926032, -0.295019), 
    cameraTarget=(161.282, -83.3974, -4.0491))
session.viewports['Viewport: 1'].view.setValues(nearPlane=664.946, 
    farPlane=934.404, width=573.565, height=270.213, cameraPosition=(-176.607, 
    -221.203, 722.083), cameraUpVector=(0.0680373, 0.9862, -0.150931), 
    cameraTarget=(162.034, -80.8384, -3.52789))
session.viewports['Viewport: 1'].view.setValues(nearPlane=718.237, 
    farPlane=881.591, width=619.533, height=291.869, cameraPosition=(241.988, 
    -195.244, 795.471), cameraUpVector=(0.00132548, 0.979956, -0.199209), 
    cameraTarget=(155.084, -81.2694, -4.74636))
session.viewports['Viewport: 1'].view.setValues(nearPlane=640.907, 
    farPlane=962.245, width=604.378, height=260.445, cameraPosition=(273.65, 
    350.643, 669.904), cameraUpVector=(0.0647782, 0.592709, -0.802807), 
    cameraTarget=(154.568, -90.1668, -2.69975))
session.viewports['Viewport: 1'].view.setValues(nearPlane=675.89, 
    farPlane=927.261, width=529.387, height=249.4, viewOffsetX=16.8722, 
    viewOffsetY=4.51699)
session.viewports['Viewport: 1'].view.setValues(nearPlane=673.812, 
    farPlane=929.34, width=527.759, height=248.633, cameraPosition=(274.855, 
    346.652, 672.306), cameraUpVector=(-0.151852, 0.611339, -0.776663), 
    cameraTarget=(155.773, -94.1578, -0.297377), viewOffsetX=16.8203, 
    viewOffsetY=4.5031)
session.viewports['Viewport: 1'].view.setValues(nearPlane=736.814, 
    farPlane=858.642, width=577.105, height=271.88, cameraPosition=(201.673, 
    -45.5312, 803.182), cameraUpVector=(0.000718996, 0.923505, -0.383585), 
    cameraTarget=(155.8, -88.715, -7.32452), viewOffsetX=18.393, 
    viewOffsetY=4.92414)
session.viewports['Viewport: 1'].view.setValues(nearPlane=696.571, 
    farPlane=911.329, width=545.585, height=257.03, cameraPosition=(449.435, 
    -93.2113, 756.316), cameraUpVector=(-0.0401913, 0.941735, -0.333945), 
    cameraTarget=(152.164, -86.4502, -0.304634), viewOffsetX=17.3884, 
    viewOffsetY=4.65519)
session.viewports['Viewport: 1'].view.setValues(nearPlane=700.197, 
    farPlane=901.642, width=548.425, height=258.368, cameraPosition=(341.279, 
    -212.837, 776.563), cameraUpVector=(-0.0164753, 0.982812, -0.183872), 
    cameraTarget=(152.605, -86.3097, -4.00334), viewOffsetX=17.4789, 
    viewOffsetY=4.67942)
session.viewports['Viewport: 1'].view.setValues(nearPlane=700.001, 
    farPlane=901.838, width=548.272, height=258.297, cameraPosition=(341.01, 
    -211.045, 776.919), cameraUpVector=(0.064849, 0.976712, -0.204518), 
    cameraTarget=(152.336, -84.5176, -3.64774), viewOffsetX=17.474, 
    viewOffsetY=4.67811)
session.viewports['Viewport: 1'].view.setValues(nearPlane=702.612, 
    farPlane=902.493, width=550.317, height=259.26, cameraPosition=(399.603, 
    -124.616, 771.543), cameraUpVector=(-0.0639013, 0.956615, -0.284262), 
    cameraTarget=(152.245, -87.721, -1.9845), viewOffsetX=17.5392, 
    viewOffsetY=4.69556)
session.viewports['Viewport: 1'].view.setValues(nearPlane=644.083, 
    farPlane=977.232, width=504.474, height=237.663, cameraPosition=(682.825, 
    51.2199, 608.772), cameraUpVector=(-0.191561, 0.856749, -0.478838), 
    cameraTarget=(152.584, -86.7139, 8.17965), viewOffsetX=16.0781, 
    viewOffsetY=4.30441)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
mdb.models['Model-1'].Material(name='mb_alu')
mdb.models['Model-1'].materials['mb_alu'].Elastic(table=((72000.0, 0.333), ))
mdb.models['Model-1'].HomogeneousShellSection(name='mb_sec', preIntegrate=OFF, 
    material='mb_alu', thicknessType=UNIFORM, thickness=15.5, 
    thicknessField='', nodalThicknessField='', idealization=NO_IDEALIZATION, 
    poissonDefinition=DEFAULT, thicknessModulus=None, temperature=GRADIENT, 
    useDensity=OFF, integrationRule=SIMPSON, numIntPts=5)
p = mdb.models['Model-1'].parts['mb_16']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
region = p.Set(faces=faces, name='Set-1')
p = mdb.models['Model-1'].parts['mb_16']
p.SectionAssignment(region=region, sectionName='mb_sec', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].view.setValues(nearPlane=625.657, 
    farPlane=996.606, width=490.042, height=230.864, cameraPosition=(642.922, 
    274, 547.967), cameraUpVector=(-0.390271, 0.688413, -0.611373), 
    cameraTarget=(153.628, -88.2278, 9.19535), viewOffsetX=15.6181, 
    viewOffsetY=4.18127)
session.viewports['Viewport: 1'].view.setValues(nearPlane=613.971, 
    farPlane=1008.75, width=480.89, height=226.552, cameraPosition=(593.031, 
    -631.153, 420.349), cameraUpVector=(-0.265367, 0.75997, 0.593318), 
    cameraTarget=(151.869, -96.7595, -4.7308), viewOffsetX=15.3264, 
    viewOffsetY=4.10318)
session.viewports['Viewport: 1'].view.setValues(nearPlane=620.213, 
    farPlane=1000.18, width=485.779, height=228.855, cameraPosition=(539.289, 
    -655.299, 438.441), cameraUpVector=(-0.270584, 0.763178, 0.586808), 
    cameraTarget=(151.406, -95.9657, -6.06633), viewOffsetX=15.4822, 
    viewOffsetY=4.1449)
session.viewports['Viewport: 1'].view.setValues(nearPlane=619.857, 
    farPlane=1000.54, width=485.5, height=228.723, cameraPosition=(540.781, 
    -656.675, 435.409), cameraUpVector=(-0.411426, 0.68078, 0.606026), 
    cameraTarget=(152.898, -97.3412, -9.09875), viewOffsetX=15.4733, 
    viewOffsetY=4.14252)
session.viewports['Viewport: 1'].view.setValues(nearPlane=600.384, 
    farPlane=1029.32, width=470.248, height=221.538, cameraPosition=(683.67, 
    -646.437, 275.626), cameraUpVector=(-0.37152, 0.530142, 0.762183), 
    cameraTarget=(153.805, -98.9519, -7.92139), viewOffsetX=14.9872, 
    viewOffsetY=4.01238)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
mdb.models['Model-1'].StaticLinearPerturbationStep(name='uniform_load', 
    previous='Initial')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='uniform_load')
mdb.models['Model-1'].StaticLinearPerturbationStep(name='seveal_load', 
    previous='uniform_load')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='seveal_load')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON, 
    adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
p = mdb.models['Model-1'].parts['mb_16']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
p = mdb.models['Model-1'].parts['mb_16']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
a = mdb.models['Model-1'].rootAssembly
a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-1'].parts['mb_16']
a.Instance(name='mb_16-1', part=p, dependent=ON)
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].view.setValues(nearPlane=651.797, 
    farPlane=974.107, width=33.3376, height=15.7057, viewOffsetX=89.5483, 
    viewOffsetY=27.3229)
session.viewports['Viewport: 1'].view.setValues(nearPlane=705.197, 
    farPlane=1090.38, width=36.0689, height=16.9924, cameraPosition=(835.859, 
    494.897, -80.4162), cameraUpVector=(-0.817541, 0.351349, -0.456268), 
    cameraTarget=(222.941, -29.6449, 19.9727), viewOffsetX=96.8848, 
    viewOffsetY=29.5614)
session.viewports['Viewport: 1'].view.setValues(nearPlane=668.154, 
    farPlane=975.554, width=34.1743, height=16.0998, cameraPosition=(567.32, 
    361.393, 564.529), cameraUpVector=(-0.58445, 0.572923, -0.574611), 
    cameraTarget=(139.915, -109.527, 58.1197), viewOffsetX=91.7956, 
    viewOffsetY=28.0086)
session.viewports['Viewport: 1'].view.setValues(nearPlane=622.226, 
    farPlane=1021.48, width=628.709, height=296.192, viewOffsetX=1.67818, 
    viewOffsetY=-18.2401)
session.viewports['Viewport: 1'].view.setValues(nearPlane=623.733, 
    farPlane=1019.79, width=630.232, height=296.909, cameraPosition=(576.537, 
    357.382, 560.677), cameraUpVector=(-0.576729, 0.579024, -0.576294), 
    cameraTarget=(140.303, -109.425, 58.0016), viewOffsetX=1.68224, 
    viewOffsetY=-18.2842)
session.viewports['Viewport: 1'].view.setValues(nearPlane=623.63, 
    farPlane=1019.89, width=630.128, height=296.86, viewOffsetX=48.24, 
    viewOffsetY=18.6308)
p = mdb.models['Model-1'].parts['mb_16']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='uniform_load')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='seveal_load')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON, 
    adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
a = mdb.models['Model-1'].rootAssembly
v1 = a.instances['mb_16-1'].vertices
verts1 = v1.getSequenceFromMask(mask=('[#f ]', ), )
region = a.Set(vertices=verts1, name='Set-1')
mdb.models['Model-1'].DisplacementBC(name='feets', 
    createStepName='seveal_load', region=region, u1=0.0, u2=0.0, u3=0.0, 
    ur1=0.0, ur2=0.0, ur3=0.0, amplitude=UNSET, fixed=OFF, 
    distributionType=UNIFORM, fieldName='', localCsys=None)
session.viewports['Viewport: 1'].view.setValues(nearPlane=623.629, 
    farPlane=1019.89, width=630.127, height=296.86, cameraPosition=(586.012, 
    347.893, 561.267), cameraUpVector=(-0.704062, 0.554791, -0.443288), 
    cameraTarget=(149.778, -118.914, 58.5911), viewOffsetX=48.2399, 
    viewOffsetY=18.6308)
session.viewports['Viewport: 1'].view.setValues(nearPlane=688.61, 
    farPlane=956.948, width=695.785, height=327.792, cameraPosition=(553.18, 
    -146.899, 728.53), cameraUpVector=(-0.489728, 0.867727, -0.0849529), 
    cameraTarget=(134.398, -139.171, 31.7852), viewOffsetX=53.2664, 
    viewOffsetY=20.5721)
session.viewports['Viewport: 1'].view.setValues(nearPlane=608.956, 
    farPlane=1054.26, width=615.302, height=289.875, cameraPosition=(642.202, 
    -667.878, 355.338), cameraUpVector=(-0.383083, 0.624002, 0.681079), 
    cameraTarget=(133.656, -148.493, -8.68314), viewOffsetX=47.1049, 
    viewOffsetY=18.1925)
session.viewports['Viewport: 1'].view.setValues(nearPlane=608.406, 
    farPlane=1071.74, width=614.747, height=289.613, cameraPosition=(959.357, 
    168.062, 50.6633), cameraUpVector=(-0.494338, 0.173911, 0.851695), 
    cameraTarget=(209.622, -141.614, -3.08977), viewOffsetX=47.0624, 
    viewOffsetY=18.1761)
session.viewports['Viewport: 1'].view.setValues(nearPlane=703.132, 
    farPlane=952.379, width=710.46, height=334.704, cameraPosition=(277.514, 
    380.99, 684.836), cameraUpVector=(0.719846, -0.687173, -0.0980563), 
    cameraTarget=(178.723, -16.6532, -17.3116), viewOffsetX=54.3898, 
    viewOffsetY=21.006)
session.viewports['Viewport: 1'].view.setValues(nearPlane=692.283, 
    farPlane=958.696, width=699.498, height=329.54, cameraPosition=(-2.18661, 
    242.017, 752.473), cameraUpVector=(0.543337, -0.835862, 0.0782269), 
    cameraTarget=(197.65, -21.7743, 9.9302), viewOffsetX=53.5506, 
    viewOffsetY=20.6819)
session.viewports['Viewport: 1'].view.setValues(nearPlane=627.852, 
    farPlane=1027.44, width=634.395, height=298.87, cameraPosition=(-129.123, 
    544.985, 467.536), cameraUpVector=(0.142388, -0.820456, 0.553695), 
    cameraTarget=(212.007, -34.4528, 10.6201), viewOffsetX=48.5666, 
    viewOffsetY=18.757)
session.viewports['Viewport: 1'].view.setValues(nearPlane=599.486, 
    farPlane=1055.86, width=605.733, height=285.367, cameraPosition=(-314.352, 
    571.388, 201.304), cameraUpVector=(0.215663, -0.544852, 0.810325), 
    cameraTarget=(200.263, -24.2832, -1.76553), viewOffsetX=46.3724, 
    viewOffsetY=17.9096)
session.viewports['Viewport: 1'].view.setValues(nearPlane=627.577, 
    farPlane=1026.96, width=634.116, height=298.739, cameraPosition=(-188.949, 
    520.973, 458.05), cameraUpVector=(0.202274, -0.801929, 0.562134), 
    cameraTarget=(207.739, -30.1812, 11.1071), viewOffsetX=48.5453, 
    viewOffsetY=18.7488)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['mb_16']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['mb_16']
p.checkGeometry()
#: Part 'mb_16' contains valid geometry and topology.
#: Part 'mb_16' is a mixed dimensional part(1 cell, 6 solid faces, 1 shell face, 16 edges, 12 vertices).
p = mdb.models['Model-1'].parts['mb_16']
f, e, d1 = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f[0], sketchUpEdge=e[2], 
    sketchPlaneSide=SIDE1, origin=(156.3, -85.6, 7.75))
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=766.05, gridSpacing=19.15, transform=t)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['mb_16']
p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
#: Warning: Coincident point selected
s1.rectangle(point1=(-38.3, -38.3), point2=(38.3, 38.3))
p = mdb.models['Model-1'].parts['mb_16']
f = p.faces
pickedFaces = f.getSequenceFromMask(mask=('[#1 ]', ), )
e1, d2 = p.edges, p.datums
p.PartitionFaceBySketch(sketchUpEdge=e1[2], faces=pickedFaces, sketch=s1)
s1.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
a1 = mdb.models['Model-1'].rootAssembly
a1.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON, 
    adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
mdb.models['Model-1'].boundaryConditions['feets'].move('seveal_load', 
    'Initial')
#* Cannot move a boundary condition created in a perturbation step.
del mdb.models['Model-1'].boundaryConditions['feets']
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
a = mdb.models['Model-1'].rootAssembly
v1 = a.instances['mb_16-1'].vertices
verts1 = v1.getSequenceFromMask(mask=('[#f ]', ), )
region = a.Set(vertices=verts1, name='Set-2')
mdb.models['Model-1'].DisplacementBC(name='fixed_BC', createStepName='Initial', 
    region=region, u1=SET, u2=SET, u3=SET, ur1=SET, ur2=SET, ur3=SET, 
    amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=None)
session.viewports['Viewport: 1'].view.setValues(nearPlane=671.087, 
    farPlane=985.378, width=678.08, height=319.451, cameraPosition=(74.9255, 
    530.648, 560.094), cameraUpVector=(0.116136, -0.883691, 0.453434), 
    cameraTarget=(218.803, -43.1946, 2.51518), viewOffsetX=51.9109, 
    viewOffsetY=20.0487)
mdb.save()
#: The model database has been saved to "Y:\mb_16_v2.cae".
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
p = mdb.models['Model-1'].parts['mb_16']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=598.597, 
    farPlane=1057.87, width=1544.33, height=727.548, viewOffsetX=103.976, 
    viewOffsetY=85.4685)
session.viewports['Viewport: 1'].view.setValues(nearPlane=603.427, 
    farPlane=1053.04, width=1556.79, height=733.418, cameraPosition=(123.585, 
    439.183, 666.783), cameraUpVector=(-0.58017, -0.794021, 0.181474), 
    cameraTarget=(267.463, -134.66, 109.204), viewOffsetX=104.815, 
    viewOffsetY=86.1581)
session.viewports['Viewport: 1'].view.setValues(nearPlane=667.383, 
    farPlane=1098.79, width=1721.79, height=811.152, cameraPosition=(378.218, 
    -643.631, 700.159), cameraUpVector=(-0.822366, 0.540274, 0.178377), 
    cameraTarget=(100.233, -334.535, 1.5356), viewOffsetX=115.924, 
    viewOffsetY=95.2898)
session.viewports['Viewport: 1'].view.setValues(nearPlane=656.097, 
    farPlane=1121.38, width=1692.67, height=797.434, cameraPosition=(339.557, 
    -713.95, 658.15), cameraUpVector=(-0.780112, 0.584596, 0.222873), 
    cameraTarget=(84.8479, -334.075, -13.943), viewOffsetX=113.964, 
    viewOffsetY=93.6783)
session.viewports['Viewport: 1'].view.setValues(nearPlane=515.467, 
    farPlane=1101.16, width=1329.86, height=626.509, cameraPosition=(896.439, 
    57.9677, 348.307), cameraUpVector=(-0.72768, -0.166098, 0.665502), 
    cameraTarget=(241.176, -234.289, -33.9331), viewOffsetX=89.5365, 
    viewOffsetY=73.5989)
session.viewports['Viewport: 1'].view.setValues(nearPlane=550.202, 
    farPlane=1064.65, width=1419.47, height=668.727, cameraPosition=(-27.071, 
    683.343, 230.562), cameraUpVector=(-0.0676661, -0.66307, 0.745493), 
    cameraTarget=(293.252, -25.0804, -6.96706), viewOffsetX=95.57, 
    viewOffsetY=78.5584)
session.viewports['Viewport: 1'].view.setValues(nearPlane=683.967, 
    farPlane=994.985, width=1764.57, height=831.308, cameraPosition=(244.13, 
    314.122, 755.293), cameraUpVector=(0.129218, -0.990943, 0.0365419), 
    cameraTarget=(265.766, 15.6108, -0.560043), viewOffsetX=118.805, 
    viewOffsetY=97.6575)
session.viewports['Viewport: 1'].view.setValues(nearPlane=704.84, 
    farPlane=1005.86, width=1818.42, height=856.677, cameraPosition=(185.441, 
    21.9896, 868.795), cameraUpVector=(0.191415, -0.929457, -0.315388), 
    cameraTarget=(257.337, 20.0197, 59.0311), viewOffsetX=122.431, 
    viewOffsetY=100.638)
session.viewports['Viewport: 1'].view.setValues(nearPlane=779.279, 
    farPlane=931.425, width=702.216, height=330.821, viewOffsetX=105.883, 
    viewOffsetY=61.6096)
session.viewports['Viewport: 1'].view.setValues(nearPlane=690.539, 
    farPlane=1047.61, width=622.251, height=293.149, cameraPosition=(47.1414, 
    651.074, 479.072), cameraUpVector=(0.20492, -0.812443, 0.545843), 
    cameraTarget=(250.852, 37.6514, -13.9859), viewOffsetX=93.826, 
    viewOffsetY=54.5938)
session.viewports['Viewport: 1'].view.setValues(nearPlane=720.912, 
    farPlane=1022.45, width=649.621, height=306.043, cameraPosition=(243.056, 
    719.898, 360.993), cameraUpVector=(0.0874476, -0.749595, 0.656094), 
    cameraTarget=(270.638, 12.2299, -38.1773), viewOffsetX=97.9529, 
    viewOffsetY=56.9951)
session.viewports['Viewport: 1'].view.setValues(nearPlane=702.349, 
    farPlane=1035.27, width=632.894, height=298.163, cameraPosition=(73.1478, 
    623.216, 524.228), cameraUpVector=(0.214143, -0.844593, 0.490719), 
    cameraTarget=(251.226, 37.0351, -10.1615), viewOffsetX=95.4307, 
    viewOffsetY=55.5275)
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['mb_16-1'].edges
a.ReferencePoint(point=a.instances['mb_16-1'].InterestingPoint(edge=e1[5], 
    rule=MIDDLE))
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
a.ReferencePoint(point=r1[6])
mdb.save()
#: The model database has been saved to "Y:\mb_16_v2.cae".
a = mdb.models['Model-1'].rootAssembly
a.deleteFeatures(('RP-1', 'RP-2', ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=715.421, 
    farPlane=1022.2, width=444.74, height=236.445, viewOffsetX=98.2231, 
    viewOffsetY=58.1402)
mdb.save()
#: The model database has been saved to "Y:\mb_16_v2.cae".
session.viewports['Viewport: 1'].view.setValues(nearPlane=734.886, 
    farPlane=1002.74, width=169.75, height=90.2473, viewOffsetX=106.06, 
    viewOffsetY=57.5952)
p = mdb.models['Model-1'].parts['mb_16']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['mb_16']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#40 ]', ), )
p.PartitionEdgeByParam(edges=pickedEdges, parameter=0.535287762435236)
p = mdb.models['Model-1'].parts['mb_16']
f1, e2, d1 = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f1[0], sketchUpEdge=e2[2], 
    sketchPlaneSide=SIDE1, origin=(156.3, -85.6, 7.75))
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=765.89, gridSpacing=19.14, transform=t)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['mb_16']
p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
s.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
p = mdb.models['Model-1'].parts['mb_16']
p.deleteFeatures(('Partition face-1', 'Partition edge-1', ))
#: 
#: The distance used for offset is: 7.750000
p = mdb.models['Model-1'].parts['mb_16']
f, e1, d2 = p.faces, p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=f[0], sketchUpEdge=e1[2], 
    sketchPlaneSide=SIDE1, origin=(156.3, -85.6, 7.75))
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=766.05, gridSpacing=19.15, transform=t)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['mb_16']
p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
#: Warning: Coincident point selected
s1.rectangle(point1=(-38.3, -38.3), point2=(0.0, 0.0))
s1.rectangle(point1=(0.0, 0.0), point2=(38.3, -38.3))
s1.rectangle(point1=(38.3, 0.0), point2=(0.0, 38.3))
s1.rectangle(point1=(0.0, 38.3), point2=(-38.3, 0.0))
s1.rectangle(point1=(-19.15, 19.15), point2=(0.0, 0.0))
s1.rectangle(point1=(0.0, 0.0), point2=(19.15, 19.15))
s1.rectangle(point1=(0.0, 0.0), point2=(19.15, -19.15))
s1.rectangle(point1=(0.0, -19.15), point2=(-19.15, 0.0))
s1.rectangle(point1=(-28.725, 28.725), point2=(28.725, -28.725))
p = mdb.models['Model-1'].parts['mb_16']
f = p.faces
pickedFaces = f.getSequenceFromMask(mask=('[#1 ]', ), )
e2, d1 = p.edges, p.datums
p.PartitionFaceBySketch(sketchUpEdge=e2[2], faces=pickedFaces, sketch=s1)
s1.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].view.setValues(nearPlane=611.81, 
    farPlane=1017.9, width=310.749, height=165.209, viewOffsetX=15.358, 
    viewOffsetY=12.0913)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
a1 = mdb.models['Model-1'].rootAssembly
a1.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=726.924, 
    farPlane=1010.7, width=294.24, height=156.432, viewOffsetX=98.021, 
    viewOffsetY=52.194)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
a = mdb.models['Model-1'].rootAssembly
e11 = a.instances['mb_16-1'].edges
a.ReferencePoint(point=a.instances['mb_16-1'].InterestingPoint(edge=e11[29], 
    rule=MIDDLE))
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['mb_16-1'].edges
a.ReferencePoint(point=a.instances['mb_16-1'].InterestingPoint(edge=e1[34], 
    rule=MIDDLE))
a = mdb.models['Model-1'].rootAssembly
e11 = a.instances['mb_16-1'].edges
a.ReferencePoint(point=a.instances['mb_16-1'].InterestingPoint(edge=e11[32], 
    rule=MIDDLE))
session.viewports['Viewport: 1'].view.setValues(nearPlane=717.092, 
    farPlane=1020.53, width=420.747, height=223.689, viewOffsetX=88.2013, 
    viewOffsetY=45.659)
session.viewports['Viewport: 1'].view.setValues(nearPlane=677.019, 
    farPlane=1055.02, width=397.235, height=211.189, cameraPosition=(-165.489, 
    591.29, 465.111), cameraUpVector=(0.215075, -0.806532, 0.55068), 
    cameraTarget=(231.437, 48.8967, 7.78068), viewOffsetX=83.2724, 
    viewOffsetY=43.1075)
session.viewports['Viewport: 1'].view.setValues(nearPlane=679.195, 
    farPlane=1065.14, width=398.512, height=211.868, cameraPosition=(-108.19, 
    701.833, 310.147), cameraUpVector=(0.103906, -0.699645, 0.706895), 
    cameraTarget=(243.015, 42.5601, -10.6441), viewOffsetX=83.5401, 
    viewOffsetY=43.2461)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='uniform_load')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='uniform_load')
session.viewports['Viewport: 1'].view.setValues(nearPlane=748.142, 
    farPlane=960.996, width=438.967, height=233.375, cameraPosition=(6.88597, 
    130.537, 832.303), cameraUpVector=(0.0567825, -0.985204, -0.161705), 
    cameraTarget=(256.096, -5.11132, 70.4722), viewOffsetX=92.0205, 
    viewOffsetY=47.6361)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['mb_16-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#1ffb ]', ), )
region = a.Surface(side1Faces=side1Faces1, name='Surf-1')
mdb.models['Model-1'].Pressure(name='uniformed_load', 
    createStepName='uniform_load', region=region, distributionType=UNIFORM, 
    field='', magnitude=0.0001)
session.viewports['Viewport: 1'].view.setValues(nearPlane=744.968, 
    farPlane=964.169, width=437.105, height=232.385, cameraPosition=(-6.92802, 
    153.298, 823.731), cameraUpVector=(0.268373, -0.958392, -0.0972636), 
    cameraTarget=(242.282, 17.6498, 61.9006), viewOffsetX=91.6301, 
    viewOffsetY=47.434)
session.viewports['Viewport: 1'].view.setValues(nearPlane=671.199, 
    farPlane=1051.76, width=393.821, height=209.373, cameraPosition=(-191.284, 
    551.254, 492.614), cameraUpVector=(0.279357, -0.799952, 0.531072), 
    cameraTarget=(227.908, 42.8222, 16.5188), viewOffsetX=82.5566, 
    viewOffsetY=42.7369)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='seveal_load')
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[8], r1[9], r1[10], )
region = a.Set(referencePoints=refPoints1, name='Set-3')
mdb.models['Model-1'].ConcentratedForce(name='P', createStepName='seveal_load', 
    region=region, cf3=-0.005, distributionType=UNIFORM, field='', 
    localCsys=None)
session.viewports['Viewport: 1'].view.setValues(nearPlane=674.589, 
    farPlane=1048.37, width=395.81, height=210.431, viewOffsetX=104.222, 
    viewOffsetY=23.2179)
session.viewports['Viewport: 1'].view.setValues(nearPlane=674.598, 
    farPlane=1048.36, width=395.815, height=210.434, viewOffsetX=94.7292, 
    viewOffsetY=51.6012)
session.viewports['Viewport: 1'].view.setValues(nearPlane=643.844, 
    farPlane=1077.77, width=377.771, height=200.841, cameraPosition=(-483.14, 
    460.479, 238.322), cameraUpVector=(0.380554, -0.516606, 0.767005), 
    cameraTarget=(179.279, 58.5551, -7.74857), viewOffsetX=90.4107, 
    viewOffsetY=49.2488)
session.viewports['Viewport: 1'].view.setValues(nearPlane=713.691, 
    farPlane=1010.16, width=418.753, height=222.629, cameraPosition=(324.804, 
    770.577, 32.4643), cameraUpVector=(-0.22736, -0.388567, 0.89293), 
    cameraTarget=(291.719, -39.6631, -25.0647), viewOffsetX=100.219, 
    viewOffsetY=54.5915)
session.viewports['Viewport: 1'].view.setValues(nearPlane=662.167, 
    farPlane=1062.05, width=388.522, height=206.557, cameraPosition=(413.829, 
    -872.94, -267.491), cameraUpVector=(-0.00133234, 0.0944657, 0.995527), 
    cameraTarget=(60.7756, -169.938, -62.4686), viewOffsetX=92.9838, 
    viewOffsetY=50.6503)
session.viewports['Viewport: 1'].view.setValues(nearPlane=657.123, 
    farPlane=1067.93, width=385.563, height=204.984, cameraPosition=(942.83, 
    -382.604, -228.827), cameraUpVector=(-0.0967988, 0.132262, 0.986477), 
    cameraTarget=(166.469, -218.256, -52.3425), viewOffsetX=92.2755, 
    viewOffsetY=50.2645)
session.viewports['Viewport: 1'].view.setValues(nearPlane=676.514, 
    farPlane=1049.22, width=396.941, height=211.033, cameraPosition=(543.922, 
    696.909, -22.4226), cameraUpVector=(-0.0973405, -0.36199, 0.927086), 
    cameraTarget=(286.567, -73.4167, -57.9269), viewOffsetX=94.9985, 
    viewOffsetY=51.7478)
session.viewports['Viewport: 1'].view.setValues(nearPlane=646.56, 
    farPlane=1079.7, width=379.366, height=201.689, cameraPosition=(994.209, 
    150.711, 84.7612), cameraUpVector=(-0.355489, -0.478464, 0.802932), 
    cameraTarget=(255.612, -145.581, -81.3089), viewOffsetX=90.7922, 
    viewOffsetY=49.4566)
session.viewports['Viewport: 1'].view.setValues(nearPlane=651.291, 
    farPlane=1075.52, width=382.142, height=203.165, cameraPosition=(611.198, 
    -800.833, 222.285), cameraUpVector=(-0.211775, 0.587867, 0.780746), 
    cameraTarget=(94.4693, -217.734, -9.83877), viewOffsetX=91.4566, 
    viewOffsetY=49.8185)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF, 
    bcs=OFF, predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['Model-1'].parts['mb_16']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF, mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['Model-1'].parts['mb_16']
p.seedPart(size=4.0, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['mb_16']
p.generateMesh()
session.viewports['Viewport: 1'].view.setValues(nearPlane=610.229, 
    farPlane=1019.48, width=309.946, height=165.159, cameraPosition=(677.673, 
    -645.919, 287.834), cameraUpVector=(0.00192147, 0.804462, 0.594001), 
    cameraTarget=(147.808, -98.4335, 4.28673), viewOffsetX=15.3183, 
    viewOffsetY=12.06)
session.viewports['Viewport: 1'].view.setValues(nearPlane=662.737, 
    farPlane=948.982, width=336.616, height=179.37, cameraPosition=(-43.6958, 
    -647.266, 550.242), cameraUpVector=(0.244938, 0.854515, 0.45805), 
    cameraTarget=(142.191, -84.9215, -6.63385), viewOffsetX=16.6364, 
    viewOffsetY=13.0977)
session.viewports['Viewport: 1'].view.setValues(nearPlane=648.655, 
    farPlane=967.592, width=329.463, height=175.559, cameraPosition=(319.716, 
    -783.602, 381.308), cameraUpVector=(-0.193352, 0.717831, 0.66883), 
    cameraTarget=(143.71, -91.5183, -7.19893), viewOffsetX=16.2829, 
    viewOffsetY=12.8194)
session.viewports['Viewport: 1'].view.setValues(nearPlane=638.325, 
    farPlane=978.573, width=324.216, height=172.763, cameraPosition=(376.11, 
    -789.126, 340.491), cameraUpVector=(-0.192023, 0.677721, 0.709804), 
    cameraTarget=(143.263, -91.8056, -6.52783), viewOffsetX=16.0236, 
    viewOffsetY=12.6152)
session.viewports['Viewport: 1'].view.setValues(nearPlane=638.758, 
    farPlane=978.14, width=324.436, height=172.88, cameraPosition=(374.476, 
    -788.704, 342.435), cameraUpVector=(-0.102155, 0.704168, 0.702647), 
    cameraTarget=(141.629, -91.3839, -4.5842), viewOffsetX=16.0345, 
    viewOffsetY=12.6238)
a1 = mdb.models['Model-1'].rootAssembly
a1.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF, loads=ON, 
    bcs=ON, predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.save()
#: The model database has been saved to "Y:\mb_16_v2.cae".
mdb.Job(name='mb_us_randomM', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs['mb_us_randomM'].submit(consistencyChecking=OFF)
#: The job input file "mb_us_randomM.inp" has been submitted for analysis.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF, 
    optimizationTasks=ON, geometricRestrictions=ON, stopConditions=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
#: Error in job mb_us_randomM: NODE SET ASSEMBLY_SET-3 HAS NOT BEEN DEFINED
#: Error in job mb_us_randomM: A CONCENTRATED LOAD HAS BEEN SPECIFIED ON NODE SET ASSEMBLY_SET-3.  THIS NODE SET IS NOT ACTIVE IN THE MODEL
#: Job mb_us_randomM: Analysis Input File Processor aborted due to errors.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
#: Error in job mb_us_randomM: Analysis Input File Processor exited with an error - Please see the  mb_us_randomM.dat file for possible error messages if the file exists.
#: Job mb_us_randomM aborted due to errors.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='uniform_load')
mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(variables=(
    'S', 'LE', 'U', 'RF', 'CF', 'SF'))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
mdb.jobs['mb_us_randomM'].submit(consistencyChecking=OFF)
#: The job input file "mb_us_randomM.inp" has been submitted for analysis.
#: Error in job mb_us_randomM: NODE SET ASSEMBLY_SET-3 HAS NOT BEEN DEFINED
#: Error in job mb_us_randomM: A CONCENTRATED LOAD HAS BEEN SPECIFIED ON NODE SET ASSEMBLY_SET-3.  THIS NODE SET IS NOT ACTIVE IN THE MODEL
#: Job mb_us_randomM: Analysis Input File Processor aborted due to errors.
#: Error in job mb_us_randomM: Analysis Input File Processor exited with an error - Please see the  mb_us_randomM.dat file for possible error messages if the file exists.
#: Job mb_us_randomM aborted due to errors.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='seveal_load')
del mdb.models['Model-1'].loads['P']
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.jobs['mb_us_randomM'].submit(consistencyChecking=OFF)
#: The job input file "mb_us_randomM.inp" has been submitted for analysis.
#: Job mb_us_randomM: Analysis Input File Processor completed successfully.
#: Job mb_us_randomM: Abaqus/Standard completed successfully.
#: Job mb_us_randomM completed successfully. 
o3 = session.openOdb(name='Y:/mb_us_randomM.odb')
#: Model: Y:/mb_us_randomM.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       2
#: Number of Node Sets:          4
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
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].view.setValues(nearPlane=946.43, 
    farPlane=1397.41, width=727.114, height=397.973, viewOffsetX=22.8391, 
    viewOffsetY=10.9982)
session.viewports['Viewport: 1'].view.setValues(nearPlane=983.032, 
    farPlane=1369.89, width=755.234, height=413.365, cameraPosition=(881.579, 
    146.301, 889.569), cameraUpVector=(-0.461726, 0.831178, -0.30976), 
    cameraTarget=(160.406, -113.82, 15.1713), viewOffsetX=23.7224, 
    viewOffsetY=11.4235)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1051.83, 
    farPlane=1296.74, width=808.086, height=442.293, cameraPosition=(380.451, 
    -269.902, 1130.57), cameraUpVector=(-0.334749, 0.929763, -0.153241), 
    cameraTarget=(149.169, -122.518, 0.480804), viewOffsetX=25.3825, 
    viewOffsetY=12.2229)
session.viewports['Viewport: 1'].view.setValues(nearPlane=957.095, 
    farPlane=1382.57, width=735.304, height=402.457, cameraPosition=(-499.378, 
    -627.541, 795.956), cameraUpVector=(0.0126224, 0.987727, 0.155677), 
    cameraTarget=(142.723, -113.714, -26.2372), viewOffsetX=23.0964, 
    viewOffsetY=11.122)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1033.84, 
    farPlane=1317.14, width=794.263, height=434.727, cameraPosition=(392.856, 
    -467.92, 1078.84), cameraUpVector=(-0.180111, 0.983645, -0.00141073), 
    cameraTarget=(142.733, -121.195, -2.60576), viewOffsetX=24.9483, 
    viewOffsetY=12.0138)
session.viewports['Viewport: 1'].view.setValues(nearPlane=965.408, 
    farPlane=1400.32, width=741.689, height=405.952, cameraPosition=(844.143, 
    -640.622, 779.2), cameraUpVector=(-0.335611, 0.867177, 0.367926), 
    cameraTarget=(153.009, -128.957, -3.63935), viewOffsetX=23.2969, 
    viewOffsetY=11.2186)
mdb.save()
#: The model database has been saved to "Y:\mb_16_v2.cae".
session.viewports['Viewport: 1'].view.setValues(nearPlane=999.795, 
    farPlane=1365.93, width=401.293, height=200.082, viewOffsetX=36.781, 
    viewOffsetY=16.5304)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U1'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U2'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
mdb.save()
#: The model database has been saved to "Y:\mb_16_v2.cae".
mdb.save()
#: The model database has been saved to "Y:\mb_16_v2.cae".
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[8], r1[9], r1[10], )
region = a.Set(referencePoints=refPoints1, name='Set-4')
mdb.models['Model-1'].ConcentratedForce(name='concentrated_force', 
    createStepName='seveal_load', region=region, cf3=-0.005, 
    distributionType=UNIFORM, field='', localCsys=None)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, interactions=ON, constraints=ON, 
    engineeringFeatures=ON)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[8], r1[9], r1[10], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-5')
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['mb_16-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#1fff ]', ), )
s1 = a.instances['mb_16-1'].edges
side1Edges1 = s1.getSequenceFromMask(mask=('[#0 #20 ]', ), )
region2=a.Surface(side1Edges=side1Edges1, side1Faces=side1Faces1, 
    name='s_Surf-2')
mdb.models['Model-1'].Coupling(name='coupling', controlPoint=region1, 
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC, 
    alpha=0.0, localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
#* Surface containing both 3D shell faces and 3D shell edges is not yet 
#* supported.
session.viewports['Viewport: 1'].view.setValues(nearPlane=667.611, 
    farPlane=1059.2, width=170.471, height=82.3218, viewOffsetX=83.1617, 
    viewOffsetY=44.167)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[10], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-6')
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['mb_16-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#0 #1 ]', ), )
region2=a.Set(edges=edges1, name='s_Set-6')
mdb.models['Model-1'].Coupling(name='Constraint-1', controlPoint=region1, 
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC, 
    alpha=0.0, localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=673.89, 
    farPlane=1052.92, width=98.5978, height=47.6137, viewOffsetX=90.5402, 
    viewOffsetY=48.9615)
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[8], r1[9], r1[10], )
region1=a.Set(referencePoints=refPoints1, name='m_Set-8')
a = mdb.models['Model-1'].rootAssembly
e1 = a.instances['mb_16-1'].edges
edges1 = e1.getSequenceFromMask(mask=('[#20000000 #5 ]', ), )
region2=a.Set(edges=edges1, name='s_Set-8')
mdb.models['Model-1'].Coupling(name='coupling', controlPoint=region1, 
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC, 
    alpha=0.0, localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
del mdb.models['Model-1'].constraints['Constraint-1']
del mdb.models['Model-1'].constraints['coupling']
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['mb_16-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#200 ]', ), )
region2=a.Set(faces=faces1, name='b_Set-10')
a = mdb.models['Model-1'].rootAssembly
r1 = a.referencePoints
refPoints1=(r1[9], )
region1=regionToolset.Region(referencePoints=refPoints1)
mdb.models['Model-1'].RigidBody(name='rb', refPointRegion=region1, 
    bodyRegion=region2)
del mdb.models['Model-1'].constraints['rb']
mdb.save()
#: The model database has been saved to "Y:\mb_16_v2.cae".
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
del mdb.models['Model-1'].loads['concentrated_force']
session.viewports['Viewport: 1'].view.setValues(nearPlane=703.563, 
    farPlane=1028.11, width=102.939, height=49.7102, cameraPosition=(305.113, 
    -942.646, 116.893), cameraUpVector=(0.0903735, 0.531809, 0.842028), 
    cameraTarget=(47.5545, -182.694, -13.6108), viewOffsetX=94.5268, 
    viewOffsetY=51.1173)
session.viewports['Viewport: 1'].view.setValues(nearPlane=702.108, 
    farPlane=1029.57, width=132.112, height=63.7981, viewOffsetX=93.7187, 
    viewOffsetY=52.4767)
a = mdb.models['Model-1'].rootAssembly
v1 = a.instances['mb_16-1'].vertices
verts1 = v1.getSequenceFromMask(mask=('[#8800020 ]', ), )
region = a.Set(vertices=verts1, name='Set-11')
mdb.models['Model-1'].ConcentratedForce(name='concentrated_force', 
    createStepName='seveal_load', region=region, cf3=-0.0005, 
    distributionType=UNIFORM, field='', localCsys=None)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.jobs['mb_us_randomM'].submit(consistencyChecking=OFF)
#: The job input file "mb_us_randomM.inp" has been submitted for analysis.
#: Job mb_us_randomM: Analysis Input File Processor completed successfully.
#: Job mb_us_randomM: Abaqus/Standard completed successfully.
#: Job mb_us_randomM completed successfully. 
o3 = session.openOdb(name='Y:/mb_us_randomM.odb')
#: Model: Y:/mb_us_randomM.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       5
#: Number of Node Sets:          8
#: Number of Steps:              2
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
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
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
mdb.save()
#: The model database has been saved to "Y:\mb_16_v2.cae".

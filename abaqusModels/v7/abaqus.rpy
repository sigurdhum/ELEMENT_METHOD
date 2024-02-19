# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2024 replay file
# Internal Version: 2023_09_21-14.55.25 RELr426 190762
# Run by 10992702 on Sun Feb 18 14:30:02 2024
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
mdb.openAuxMdb(pathName='Y:/mp16_v2.cae')
mdb.copyAuxMdbModel(fromName='Model-1', toName='Model-1')
mdb.closeAuxMdb()
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='points_load')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    step='uniformed_load')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
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
session.viewports['Viewport: 1'].view.setValues(nearPlane=726.086, 
    farPlane=882.71, width=626.304, height=295.058, cameraPosition=(18.3222, 
    95.3336, 800.146), cameraUpVector=(0.191578, 0.937555, -0.290326), 
    cameraTarget=(167.147, 106.493, 1.01038))
session.viewports['Viewport: 1'].view.setValues(nearPlane=720.773, 
    farPlane=893.003, width=621.721, height=292.899, cameraPosition=(276.26, 
    188.513, 801.921), cameraUpVector=(-0.071341, 0.903765, -0.422042), 
    cameraTarget=(164.404, 105.502, 0.991501))
session.viewports['Viewport: 1'].view.setValues(nearPlane=610.411, 
    farPlane=1008.74, width=526.526, height=248.052, cameraPosition=(652.069, 
    504.937, 511.951), cameraUpVector=(-0.492732, 0.65396, -0.574065), 
    cameraTarget=(161.58, 103.124, 3.17065))
session.viewports['Viewport: 1'].view.setValues(nearPlane=622.377, 
    farPlane=998.439, width=536.848, height=252.915, cameraPosition=(686.933, 
    423.414, 534.465), cameraUpVector=(-0.425263, 0.733083, -0.530793), 
    cameraTarget=(161.435, 103.464, 3.07676))
session.viewports['Viewport: 1'].view.setValues(nearPlane=637.015, 
    farPlane=983.677, width=549.475, height=258.863, cameraPosition=(649.989, 
    358.091, 600.854), cameraUpVector=(-0.38236, 0.791111, -0.477434), 
    cameraTarget=(161.551, 103.669, 2.86838))
session.viewports['Viewport: 1'].view.setValues(nearPlane=636.046, 
    farPlane=984.645, width=548.639, height=258.469, cameraPosition=(649.989, 
    358.091, 600.854), cameraUpVector=(-0.153947, 0.74796, -0.645644), 
    cameraTarget=(161.551, 103.669, 2.86838))
session.viewports['Viewport: 1'].view.setValues(nearPlane=723.147, 
    farPlane=892.032, width=623.77, height=293.864, cameraPosition=(277.849, 
    212.146, 799.709), cameraUpVector=(-0.025023, 0.889304, -0.456631), 
    cameraTarget=(162.747, 104.138, 2.22905))
session.viewports['Viewport: 1'].view.setValues(nearPlane=650.449, 
    farPlane=968.56, width=561.062, height=264.322, cameraPosition=(570.189, 
    315.228, 672.733), cameraUpVector=(-0.249924, 0.821946, -0.511803), 
    cameraTarget=(160.806, 103.454, 3.07205))
session.viewports['Viewport: 1'].view.setValues(nearPlane=667.21, 
    farPlane=951.72, width=575.52, height=271.133, cameraPosition=(532.215, 
    272.59, 706.15), cameraUpVector=(-0.163226, 0.848687, -0.503078), 
    cameraTarget=(160.968, 103.636, 2.9298))
session.viewports['Viewport: 1'].view.setValues(nearPlane=665.169, 
    farPlane=953.745, width=573.76, height=270.304, cameraPosition=(535.278, 
    277.57, 703.306), cameraUpVector=(-0.171726, 0.845744, -0.505199), 
    cameraTarget=(160.955, 103.615, 2.94204))
session.viewports['Viewport: 1'].view.setValues(nearPlane=717.115, 
    farPlane=894.258, width=618.567, height=291.414, cameraPosition=(106.538, 
    312.412, 786.206), cameraUpVector=(0.0269895, 0.825369, -0.563949), 
    cameraTarget=(162.805, 103.465, 2.58424))
session.viewports['Viewport: 1'].view.setValues(nearPlane=716.206, 
    farPlane=897.04, width=617.784, height=291.045, cameraPosition=(220.462, 
    300.005, 789.234), cameraUpVector=(-0.0380124, 0.834328, -0.549956), 
    cameraTarget=(161.778, 103.577, 2.55695))
session.viewports['Viewport: 1'].view.setValues(nearPlane=658.02, 
    farPlane=954.84, width=567.594, height=267.4, cameraPosition=(388.779, 
    491.708, 679.394), cameraUpVector=(-0.233113, 0.667691, -0.706999), 
    cameraTarget=(160.458, 102.073, 3.41859))
session.viewports['Viewport: 1'].view.setValues(nearPlane=660.696, 
    farPlane=954.339, width=569.904, height=268.488, cameraPosition=(456.713, 
    407.98, 695.839), cameraUpVector=(-0.17852, 0.74476, -0.643011), 
    cameraTarget=(159.909, 102.75, 3.28561))
session.viewports['Viewport: 1'].view.setValues(nearPlane=645.752, 
    farPlane=975.845, width=557.014, height=262.415, cameraPosition=(708.994, 
    191.983, 595.419), cameraUpVector=(-0.0881231, 0.859406, -0.503643), 
    cameraTarget=(158.212, 104.203, 3.96124))
session.viewports['Viewport: 1'].view.setValues(nearPlane=711.681, 
    farPlane=901.325, width=613.884, height=289.207, cameraPosition=(95.7014, 
    357.545, 773.145), cameraUpVector=(0.168536, 0.784545, -0.596728), 
    cameraTarget=(159.84, 103.764, 3.48949))
session.viewports['Viewport: 1'].view.setValues(nearPlane=580.598, 
    farPlane=1034.73, width=500.814, height=235.939, cameraPosition=(851.214, 
    440.127, 254.45), cameraUpVector=(-0.413331, 0.570827, -0.709446), 
    cameraTarget=(153.8, 103.104, 7.63597))
session.viewports['Viewport: 1'].view.setValues(nearPlane=693.765, 
    farPlane=920.517, width=598.43, height=281.927, cameraPosition=(-53.3561, 
    314.713, 760.009), cameraUpVector=(0.222586, 0.821495, -0.524978), 
    cameraTarget=(159.72, 103.925, 4.32715))
session.viewports['Viewport: 1'].view.setValues(nearPlane=653.691, 
    farPlane=959.038, width=563.863, height=265.642, cameraPosition=(374.882, 
    550.181, 647.475), cameraUpVector=(0.024808, 0.565291, -0.824519), 
    cameraTarget=(156.638, 102.23, 5.13708))
session.viewports['Viewport: 1'].view.setValues(nearPlane=751.419, 
    farPlane=865.803, width=648.161, height=305.356, cameraPosition=(155.097, 
    161.948, 814.746), cameraUpVector=(-0.139442, 0.906751, -0.397944), 
    cameraTarget=(158.433, 105.401, 3.7709))
session.viewports['Viewport: 1'].view.setValues(nearPlane=662.695, 
    farPlane=955.964, width=571.63, height=269.301, cameraPosition=(563.358, 
    211.387, 699.985), cameraUpVector=(-0.0865764, 0.876884, -0.472841), 
    cameraTarget=(156.242, 105.136, 4.38686))
session.viewports['Viewport: 1'].view.setValues(nearPlane=707.748, 
    farPlane=910.881, width=610.492, height=287.609, cameraPosition=(-37.3102, 
    -1.91754, 785.486), cameraUpVector=(-0.017725, 0.976168, -0.216292), 
    cameraTarget=(158.93, 106.09, 4.00424))
session.viewports['Viewport: 1'].view.setValues(nearPlane=704.914, 
    farPlane=913.716, width=608.047, height=286.457, cameraPosition=(-37.3102, 
    -1.91754, 785.486), cameraUpVector=(-0.189606, 0.9458, -0.263651), 
    cameraTarget=(158.93, 106.09, 4.00424))
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
a = mdb.models['Model-1'].rootAssembly
v1 = a.instances['Part-1-1'].vertices
verts1 = v1.getSequenceFromMask(mask=('[#f ]', ), )
region = a.Set(vertices=verts1, name='Set-1')
mdb.models['Model-1'].DisplacementBC(name='fixed', createStepName='Initial', 
    region=region, u1=SET, u2=SET, u3=SET, ur1=SET, ur2=SET, ur3=SET, 
    amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=None)
session.viewports['Viewport: 1'].view.setValues(nearPlane=661.807, 
    farPlane=959.181, width=570.858, height=268.937, cameraPosition=(510.119, 
    368.282, 690.016), cameraUpVector=(-0.304946, 0.784716, -0.539657), 
    cameraTarget=(167.147, 106.493, 1.01039))
mdb.saveAs(pathName='Y:/mp16_v3')
#: The model database has been saved to "Y:\mp16_v3.cae".
mdb.save()
#: The model database has been saved to "Y:\mp16_v3.cae".
session.viewports['Viewport: 1'].view.setValues(nearPlane=658.154, 
    farPlane=962.835, width=642.493, height=302.685, viewOffsetX=9.61319, 
    viewOffsetY=1.94911)
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
p = mdb.models['Model-1'].parts['Part-1']
p.seedPart(size=5.0, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Part-1']
p.generateMesh()
a1 = mdb.models['Model-1'].rootAssembly
a1.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF, loads=ON, 
    bcs=ON, predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    step='uniformed_load')
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Part-1-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
region = a.Surface(side1Faces=side1Faces1, name='Surf-1')
mdb.models['Model-1'].Pressure(name='uniformed_load', 
    createStepName='uniformed_load', region=region, distributionType=UNIFORM, 
    field='', magnitude=0.001)
mdb.save()
#: The model database has been saved to "Y:\mp16_v3.cae".
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF, 
    bcs=OFF, predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=696.966, 
    farPlane=908.109, width=680.382, height=321.185, cameraPosition=(253.035, 
    362.624, 763.609), cameraUpVector=(-0.11439, 0.788592, -0.604183), 
    cameraTarget=(166.509, 106.345, -3.02437), viewOffsetX=10.1801, 
    viewOffsetY=2.06405)
session.viewports['Viewport: 1'].view.setValues(nearPlane=689.985, 
    farPlane=915.09, width=694.397, height=327.801, viewOffsetX=11.3634, 
    viewOffsetY=2.47519)
mdb.save()
#: The model database has been saved to "Y:\mp16_v3.cae".
session.viewports['Viewport: 1'].view.setValues(nearPlane=638.75, 
    farPlane=980.781, width=642.834, height=303.46, cameraPosition=(457.544, 
    531.595, 630.515), cameraUpVector=(-0.152277, 0.613968, -0.774503), 
    cameraTarget=(164.495, 107.391, 1.97217), viewOffsetX=10.5196, 
    viewOffsetY=2.2914)
session.viewports['Viewport: 1'].view.setValues(nearPlane=712.59, 
    farPlane=886.026, width=717.146, height=338.54, cameraPosition=(101.643, 
    -41.3467, 790.686), cameraUpVector=(-0.236093, 0.953822, -0.185698), 
    cameraTarget=(166.274, 103.526, -6.63933), viewOffsetX=11.7357, 
    viewOffsetY=2.55629)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF, loads=ON, 
    bcs=ON, predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF, 
    bcs=OFF, predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF, 
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON, mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=653.597, 
    farPlane=972.35, width=659.109, height=310.513, cameraPosition=(667.029, 
    128.603, 640.073), cameraUpVector=(-0.315199, 0.924825, -0.21295), 
    cameraTarget=(158.618, 102.397, 6.25542), viewOffsetX=10.7641, 
    viewOffsetY=2.34466)
session.viewports['Viewport: 1'].view.setValues(nearPlane=636.142, 
    farPlane=986.005, width=641.507, height=302.22, cameraPosition=(268.77, 
    912.852, -40.7799), cameraUpVector=(-0.288883, -0.259374, 0.92156), 
    cameraTarget=(182.215, 105.494, -1.09218), viewOffsetX=10.4766, 
    viewOffsetY=2.28204)
session.viewports['Viewport: 1'].view.setValues(nearPlane=649.092, 
    farPlane=968.739, width=654.566, height=308.372, cameraPosition=(170.307, 
    919.888, 8.7227), cameraUpVector=(-0.124497, -0.348828, 0.928881), 
    cameraTarget=(182.503, 107.113, -3.13503), viewOffsetX=10.6899, 
    viewOffsetY=2.3285)
session.viewports['Viewport: 1'].view.setValues(nearPlane=627.604, 
    farPlane=992.979, width=632.897, height=298.164, cameraPosition=(314.98, 
    902.402, 80.1132), cameraUpVector=(-0.196821, -0.400675, 0.89483), 
    cameraTarget=(181.612, 104.836, -3.51027), viewOffsetX=10.336, 
    viewOffsetY=2.25142)
session.viewports['Viewport: 1'].view.setValues(nearPlane=629.185, 
    farPlane=991.399, width=634.491, height=298.915, cameraPosition=(288.547, 
    906.308, 85.0196), cameraUpVector=(-0.10604, -0.220369, -0.969635), 
    cameraTarget=(155.179, 108.742, 1.39614), viewOffsetX=10.362, 
    viewOffsetY=2.25709)
session.viewports['Viewport: 1'].view.setValues(nearPlane=605.221, 
    farPlane=1017.84, width=610.325, height=287.53, cameraPosition=(652.771, 
    552.946, 472.976), cameraUpVector=(-0.278481, 0.539961, -0.794286), 
    cameraTarget=(156.69, 110.503, 4.95989), viewOffsetX=9.96734, 
    viewOffsetY=2.17112)
session.viewports['Viewport: 1'].view.setValues(nearPlane=654.347, 
    farPlane=943.203, width=659.865, height=310.869, cameraPosition=(-56.2321, 
    492.919, 676.132), cameraUpVector=(0.170002, 0.668263, -0.72424), 
    cameraTarget=(155.121, 105.027, -6.33501), viewOffsetX=10.7764, 
    viewOffsetY=2.34735)
session.viewports['Viewport: 1'].view.setValues(nearPlane=650.734, 
    farPlane=946.817, width=656.222, height=309.153, cameraPosition=(-55.5138, 
    490.366, 677.805), cameraUpVector=(-0.0419592, 0.635284, -0.771138), 
    cameraTarget=(155.839, 102.474, -4.66171), viewOffsetX=10.7169, 
    viewOffsetY=2.33439)
session.viewports['Viewport: 1'].view.setValues(nearPlane=682.962, 
    farPlane=919.878, width=688.722, height=324.464, cameraPosition=(202.175, 
    500.934, 706.199), cameraUpVector=(-0.192459, 0.650877, -0.734383), 
    cameraTarget=(151.058, 103.851, -1.33391), viewOffsetX=11.2477, 
    viewOffsetY=2.45)
mdb.save()
#: The model database has been saved to "Y:\mp16_v3.cae".
mdb.save()
#: The model database has been saved to "Y:\mp16_v3.cae".

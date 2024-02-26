# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2024 replay file
# Internal Version: 2023_09_21-14.55.25 RELr426 190762
# Run by 10992702 on Mon Feb 26 14:27:18 2024
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
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, optimizationTasks=OFF, 
    geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='simple_test')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    step='clamped_edges')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='simple_test')
mdb.openAuxMdb(pathName='Y:/mb_sss_points.cae')
mdb.copyAuxMdbModel(fromName='Model-1', toName='feet')
mdb.closeAuxMdb()
a = mdb.models['feet'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a.regenerate()
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='turbo')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.saveAs(pathName='Y:/mb_both_feet_ss')
#: The model database has been saved to "Y:\mb_both_feet_ss.cae".
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='simple_test')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='simple_test')
a = mdb.models['feet'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='turbo')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='turbo')
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['feet'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
a = mdb.models['feet'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['feet'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
a = mdb.models['feet'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON, 
    adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, interactions=ON, constraints=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF, 
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF, 
    bcs=OFF, predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['feet'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF, mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
a = mdb.models['feet'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
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
p = mdb.models['feet'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
Mdb()
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].setValues(displayedObject=None)
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.rectangle(point1=(0.0, 0.0), point2=(28.75, 20.0))
p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Part-1']
p.BaseShellExtrude(sketch=s, depth=20.0)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
del mdb.models['Model-1'].parts['Part-1']
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=STANDALONE)
s1.rectangle(point1=(0.0, 0.0), point2=(17.5, 12.5))
p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Part-1']
p.BaseShell(sketch=s1)
s1.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
del mdb.models['Model-1'].parts['Part-1']
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.rectangle(point1=(0.0, 0.0), point2=(30.0, 21.25))
p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Part-1']
p.BaseShellExtrude(sketch=s, depth=20.0)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
del mdb.models['Model-1'].parts['Part-1']
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=STANDALONE)
s1.rectangle(point1=(0.0, 0.0), point2=(10.0, 12.5))
p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Part-1']
p.BaseShell(sketch=s1)
s1.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
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
p = mdb.models['Model-1'].parts['Part-1']
f, e = p.faces, p.edges
t = p.MakeSketchTransform(sketchPlane=f[0], sketchUpEdge=e[1], 
    sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(5.0, 6.25, 0.0))
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=32.01, gridSpacing=0.8, transform=t)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['Part-1']
p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
s.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
p = mdb.models['Model-1'].parts['Part-1']
f1, e1 = p.faces, p.edges
t = p.MakeSketchTransform(sketchPlane=f1[0], sketchUpEdge=e1[1], 
    sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(5.0, 6.25, 0.0))
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=32.01, gridSpacing=0.8, transform=t)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['Part-1']
p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
s1.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
del mdb.models['Model-1'].parts['Part-1']
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.rectangle(point1=(0.0, 0.0), point2=(20.0, 15.0))
s.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=STANDALONE)
s1.rectangle(point1=(0.0, 0.0), point2=(10.0, 10.0))
p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Part-1']
p.BaseShell(sketch=s1)
s1.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
openMdb(pathName='Y:/mb_both_feet_ss.cae')
#: The model database "Y:\mb_both_feet_ss.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
p1 = mdb.models['feet'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p1 = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p1 = mdb.models['feet'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p1 = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.rectangle(point1=(0.0, 0.0), point2=(23.75, 13.75))
p = mdb.models['Model-1'].Part(name='Part-2', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Part-2']
p.BaseShell(sketch=s)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Part-2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].view.setValues(nearPlane=51.4368, 
    farPlane=58.3357, width=47.0275, height=23.613, viewOffsetX=4.20249, 
    viewOffsetY=1.42903)
del mdb.models['Model-1'].parts['Part-2']
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=STANDALONE)
s1.rectangle(point1=(0.0, 0.0), point2=(20.0, 20.0))
p = mdb.models['Model-1'].Part(name='Part-2', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Part-2']
p.BaseShellExtrude(sketch=s1, depth=12.0)
s1.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Part-2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
del mdb.models['Model-1'].parts['Part-2']
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.rectangle(point1=(0.0, 0.0), point2=(27.5, 15.0))
p = mdb.models['Model-1'].Part(name='Part-2', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Part-2']
p.BaseSolidExtrude(sketch=s, depth=20.0)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Part-2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].view.setValues(nearPlane=59.8554, 
    farPlane=98.0459, width=49.7046, height=24.9572, cameraPosition=(36.865, 
    69.4904, -33.102), cameraUpVector=(-0.162491, 0.284848, 0.9447), 
    cameraTarget=(14.6729, 6.24541, 10.3317))
del mdb.models['Model-1'].parts['Part-2']
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=STANDALONE)
s1.rectangle(point1=(0.0, 0.0), point2=(51.25, 22.5))
p = mdb.models['Model-1'].Part(name='Part-2', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Part-2']
p.BaseSolidExtrude(sketch=s1, depth=12.0)
s1.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Part-2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
p = mdb.models['Model-1'].parts['Part-2']
c1 = p.cells
p.AssignMidsurfaceRegion(cellList = c1[0:1])
#: 
#: The selected cells have been added as reference representation.
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['Part-2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
mdb.models['Model-1'].HomogeneousShellSection(name='Section-2', 
    preIntegrate=OFF, material='apple_alu', thicknessType=UNIFORM, 
    thickness=1.0, thicknessField='', nodalThicknessField='', 
    idealization=NO_IDEALIZATION, poissonDefinition=DEFAULT, 
    thicknessModulus=None, temperature=GRADIENT, useDensity=OFF, 
    integrationRule=SIMPSON, numIntPts=5)
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['Part-2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sections['Section-2']
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
a = mdb.models['feet'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON, 
    adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF, 
    bcs=OFF, predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=613.262, 
    farPlane=1011.35, width=495.254, height=249.21, cameraPosition=(451.662, 
    864.411, 75.1951), cameraUpVector=(-0.708114, -0.0226414, -0.705735), 
    cameraTarget=(167.147, 106.493, 1.01035))
session.viewports['Viewport: 1'].view.setValues(nearPlane=642.031, 
    farPlane=979.17, width=518.487, height=260.901, cameraPosition=(534.036, 
    500.984, 609.552), cameraUpVector=(-0.452115, 0.660117, -0.599865), 
    cameraTarget=(167.081, 106.782, 0.585045))
session.viewports['Viewport: 1'].view.setValues(nearPlane=737.411, 
    farPlane=872.981, width=595.513, height=299.66, cameraPosition=(189.956, 
    221.641, 804.635), cameraUpVector=(-0.352316, 0.823863, -0.443985), 
    cameraTarget=(168.079, 107.593, 0.0189667))
session.viewports['Viewport: 1'].view.setValues(nearPlane=681.301, 
    farPlane=932.674, width=550.2, height=276.859, cameraPosition=(338.105, 
    397.41, 739.911), cameraUpVector=(-0.330612, 0.742443, -0.582644), 
    cameraTarget=(166.652, 105.9, 0.642456))
session.viewports['Viewport: 1'].view.setValues(nearPlane=614.592, 
    farPlane=1003.41, width=496.328, height=249.751, cameraPosition=(501.9, 
    712.559, 423.482), cameraUpVector=(-0.289943, 0.334394, -0.896724), 
    cameraTarget=(165.441, 103.57, 2.98149))
session.viewports['Viewport: 1'].view.setValues(nearPlane=730.249, 
    farPlane=882.879, width=589.73, height=296.751, cameraPosition=(233.128, 
    232.772, 801.382), cameraUpVector=(-0.365393, 0.821108, -0.438485), 
    cameraTarget=(166.754, 105.914, 1.1353))
session.viewports['Viewport: 1'].view.setValues(nearPlane=615.645, 
    farPlane=1010.5, width=497.178, height=250.179, cameraPosition=(745.236, 
    359.625, 510.061), cameraUpVector=(-0.43596, 0.790128, -0.430856), 
    cameraTarget=(162.697, 104.909, 3.44308))
session.viewports['Viewport: 1'].view.setValues(nearPlane=657.521, 
    farPlane=971.247, width=530.996, height=267.196, cameraPosition=(659.422, 
    -17.1885, 635.325), cameraUpVector=(-0.45717, 0.883603, 0.101201), 
    cameraTarget=(162.684, 104.854, 3.46139))
session.viewports['Viewport: 1'].view.setValues(nearPlane=699.293, 
    farPlane=914.16, width=564.73, height=284.171, cameraPosition=(58.6261, 
    392.825, 757.182), cameraUpVector=(0.132158, 0.763194, -0.632511), 
    cameraTarget=(161.629, 105.574, 3.67526))
session.viewports['Viewport: 1'].view.setValues(nearPlane=627.109, 
    farPlane=981.766, width=506.436, height=254.838, cameraPosition=(-276.201, 
    420.537, 611.098), cameraUpVector=(0.315734, 0.735221, -0.599801), 
    cameraTarget=(164.214, 105.36, 4.80307))
session.viewports['Viewport: 1'].view.setValues(nearPlane=645.572, 
    farPlane=964.162, width=521.346, height=262.341, cameraPosition=(-123.993, 
    536.122, 630.811), cameraUpVector=(0.339882, 0.621455, -0.705885), 
    cameraTarget=(162.602, 104.136, 4.59436))
session.viewports['Viewport: 1'].view.setValues(nearPlane=698.516, 
    farPlane=915.601, width=564.102, height=283.856, cameraPosition=(234.898, 
    445.623, 737.782), cameraUpVector=(0.0469493, 0.709592, -0.703047), 
    cameraTarget=(158.996, 105.045, 3.51944))
session.viewports['Viewport: 1'].view.setValues(nearPlane=610.495, 
    farPlane=1003.54, width=493.018, height=248.087, cameraPosition=(529.347, 
    666.808, 458.048), cameraUpVector=(-0.148992, 0.357872, -0.921807), 
    cameraTarget=(156.845, 103.429, 5.56324))
session.viewports['Viewport: 1'].view.setValues(nearPlane=687.929, 
    farPlane=928.644, width=555.552, height=279.554, cameraPosition=(405.137, 
    306.429, 751.442), cameraUpVector=(-0.135279, 0.830712, -0.540017), 
    cameraTarget=(157.759, 106.081, 3.40455))
session.viewports['Viewport: 1'].view.setValues(nearPlane=704.321, 
    farPlane=914.548, width=568.79, height=286.215, cameraPosition=(357.256, 
    -10.4492, 782.454), cameraUpVector=(-0.0992415, 0.97981, -0.173562), 
    cameraTarget=(158.036, 107.911, 3.22545))
mdb.save()
#: The model database has been saved to "Y:\mb_both_feet_ss.cae".
session.viewports['Viewport: 1'].view.setValues(nearPlane=659.493, 
    farPlane=958.686, width=532.591, height=267.998, cameraPosition=(555.549, 
    269.746, 693.255), cameraUpVector=(-0.247745, 0.856722, -0.452383), 
    cameraTarget=(157.174, 106.693, 3.61335))
session.viewports['Viewport: 1'].view.setValues(nearPlane=706.801, 
    farPlane=911.902, width=570.796, height=287.223, cameraPosition=(370.985, 
    14.5992, 782.193), cameraUpVector=(-0.0143953, 0.97372, -0.227291), 
    cameraTarget=(158.056, 107.912, 3.18852))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
mdb.Job(name='feet', model='feet', description='', type=ANALYSIS, atTime=None, 
    waitMinutes=0, waitHours=0, queue=None, memory=90, memoryUnits=PERCENTAGE, 
    getMemoryFromAnalysis=True, explicitPrecision=SINGLE, 
    nodalOutputPrecision=SINGLE, echoPrint=OFF, modelPrint=OFF, 
    contactPrint=OFF, historyPrint=OFF, userSubroutine='', scratch='', 
    resultsFormat=ODB, numThreadsPerMpiProcess=1, multiprocessingMode=DEFAULT, 
    numCpus=4, numDomains=4, numGPUs=0)
mdb.jobs['feet'].submit(consistencyChecking=OFF)
#: The job input file "feet.inp" has been submitted for analysis.
#: Job feet: Analysis Input File Processor completed successfully.
mdb.Job(name='ss', model='Model-1', description='', type=ANALYSIS, atTime=None, 
    waitMinutes=0, waitHours=0, queue=None, memory=90, memoryUnits=PERCENTAGE, 
    getMemoryFromAnalysis=True, explicitPrecision=SINGLE, 
    nodalOutputPrecision=SINGLE, echoPrint=OFF, modelPrint=OFF, 
    contactPrint=OFF, historyPrint=OFF, userSubroutine='', scratch='', 
    resultsFormat=ODB, numThreadsPerMpiProcess=1, multiprocessingMode=DEFAULT, 
    numCpus=4, numDomains=4, numGPUs=0)
#: Job feet: Abaqus/Standard completed successfully.
#: Job feet completed successfully. 
mdb.jobs['ss'].submit(consistencyChecking=OFF)
#: The job input file "ss.inp" has been submitted for analysis.
#: Job ss: Analysis Input File Processor completed successfully.
o3 = session.openOdb(name='Y:/feet.odb')
#: Model: Y:/feet.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       6
#: Number of Node Sets:          8
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
#: Job ss: Abaqus/Standard completed successfully.
#: Job ss completed successfully. 
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S11'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
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
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S22'), )
a = mdb.models['feet'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(name='Y:/ss.odb')
#: Model: Y:/ss.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       4
#: Number of Node Sets:          7
#: Number of Steps:              4
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['feet'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['Y:/ss.odb'])
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S11'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S22'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S33'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S12'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Mises'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S11'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=958.316, 
    farPlane=1385.52, width=688.813, height=356.065, viewOffsetX=-10.4155, 
    viewOffsetY=15.0929)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=1070.36, 
    farPlane=1322.46, width=769.347, height=397.695, cameraPosition=(191.998, 
    -483.837, 1029.92), cameraUpVector=(0.0673572, 0.984331, 0.162958), 
    cameraTarget=(152.424, 80.8445, 14.0986), viewOffsetX=-11.6332, 
    viewOffsetY=16.8575)
session.viewports['Viewport: 1'].view.setValues(nearPlane=991.04, 
    farPlane=1412.3, width=712.334, height=368.224, cameraPosition=(-319.136, 
    -773.477, 652.891), cameraUpVector=(0.16556, 0.805455, 0.569062), 
    cameraTarget=(137.988, 74.2536, 1.18951), viewOffsetX=-10.7711, 
    viewOffsetY=15.6083)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1014.18, 
    farPlane=1389.16, width=444.356, height=229.699, viewOffsetX=-6.26374, 
    viewOffsetY=16.9516)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1020.12, 
    farPlane=1379.76, width=446.96, height=231.045, cameraPosition=(-198.543, 
    -893.671, 544.95), cameraUpVector=(0.0658556, 0.750808, 0.657229), 
    cameraTarget=(143.516, 72.9055, -3.72967), viewOffsetX=-6.30044, 
    viewOffsetY=17.0509)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1084.33, 
    farPlane=1313.82, width=475.092, height=245.587, cameraPosition=(178.343, 
    -598.626, 958.804), cameraUpVector=(-0.0985629, 0.955849, 0.276837), 
    cameraTarget=(156.679, 78.4362, 13.5835), viewOffsetX=-6.69699, 
    viewOffsetY=18.1241)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1072.17, 
    farPlane=1325.98, width=640.091, height=330.88, viewOffsetX=-9.97152, 
    viewOffsetY=41.9287)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Mises'), )
odb = session.mdbData['Model-1']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
a = mdb.models['feet'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='simple_test')
o3 = session.openOdb(name='Y:/ss.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['Y:/ss.odb'])
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
odb = session.mdbData['Model-1']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
odb = session.odbs['Y:/ss.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S33'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(
    plotState=CONTOURS_ON_DEF)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=3, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=2, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0 )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1 )
session.viewports['Viewport: 1'].view.setValues(nearPlane=1006.6, 
    farPlane=1363.82, width=600.942, height=310.642, cameraPosition=(388.979, 
    -864.288, 624.901), cameraUpVector=(-0.183731, 0.771595, 0.609002), 
    cameraTarget=(164.094, 84.5871, -8.65008), viewOffsetX=-9.36164, 
    viewOffsetY=39.3643)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S22'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=1056.4, 
    farPlane=1330.17, width=630.674, height=326.012, cameraPosition=(159.218, 
    -750.683, 818.206), cameraUpVector=(-0.0484966, 0.898682, 0.435912), 
    cameraTarget=(156.597, 76.8207, 1.16578), viewOffsetX=-9.82481, 
    viewOffsetY=41.3119)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S11'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=1079.17, 
    farPlane=1321.53, width=644.271, height=333.04, cameraPosition=(170.196, 
    -520.632, 1013.18), cameraUpVector=(0.00696312, 0.980456, 0.196614), 
    cameraTarget=(154.026, 75.0917, 14.5943), viewOffsetX=-10.0366, 
    viewOffsetY=42.2025)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1027.62, 
    farPlane=1349.42, width=613.498, height=317.133, cameraPosition=(259.371, 
    -855.177, 677.409), cameraUpVector=(-0.185627, 0.807005, 0.560613), 
    cameraTarget=(164.826, 79.5206, -7.95395), viewOffsetX=-9.55721, 
    viewOffsetY=40.1867)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1012.27, 
    farPlane=1372.12, width=604.335, height=312.396, cameraPosition=(1089.21, 
    81.5078, 734.182), cameraUpVector=(-0.55152, 0.818287, 0.161961), 
    cameraTarget=(184.451, 90.0093, 3.65907), viewOffsetX=-9.41447, 
    viewOffsetY=39.5865)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=957.622, 
    farPlane=1407.09, width=571.709, height=295.531, cameraPosition=(1007.41, 
    -519.224, 519.167), cameraUpVector=(-0.0190207, 0.936235, 0.35086), 
    cameraTarget=(158.548, 75.2747, -8.40223), viewOffsetX=-8.90622, 
    viewOffsetY=37.4494)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1082.61, 
    farPlane=1317.02, width=646.329, height=334.104, cameraPosition=(324.159, 
    -315.867, 1101.34), cameraUpVector=(-0.114647, 0.993309, 0.0138989), 
    cameraTarget=(165.208, 71.2129, 16.3346), viewOffsetX=-10.0687, 
    viewOffsetY=42.3373)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1038.67, 
    farPlane=1361.27, width=620.095, height=320.543, cameraPosition=(879.229, 
    143.8, 949.746), cameraUpVector=(-0.390721, 0.902227, -0.182548), 
    cameraTarget=(185.932, 84.6756, 17.9858), viewOffsetX=-9.66001, 
    viewOffsetY=40.6188)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1030.36, 
    farPlane=1355.62, width=615.136, height=317.98, cameraPosition=(397.516, 
    -678.297, 854.49), cameraUpVector=(0.0193429, 0.934963, 0.354218), 
    cameraTarget=(159.708, 67.1472, -5.79729), viewOffsetX=-9.58276, 
    viewOffsetY=40.294)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1021.54, 
    farPlane=1351.25, width=609.872, height=315.259, cameraPosition=(212.672, 
    -1015.07, 364.005), cameraUpVector=(0.0895718, 0.636406, 0.766136), 
    cameraTarget=(154.333, 77.2756, -30.5952), viewOffsetX=-9.50075, 
    viewOffsetY=39.9492)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1050.19, 
    farPlane=1338.47, width=626.974, height=324.1, cameraPosition=(369.48, 
    -516.085, 986.889), cameraUpVector=(0.022955, 0.983413, 0.179921), 
    cameraTarget=(158.4, 63.388, 0.994987), viewOffsetX=-9.76717, 
    viewOffsetY=41.0695)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1031.26, 
    farPlane=1351.89, width=615.677, height=318.259, cameraPosition=(325.206, 
    -772.925, 774.339), cameraUpVector=(-0.196727, 0.86187, 0.467417), 
    cameraTarget=(168.566, 68.2086, -13.2449), viewOffsetX=-9.59116, 
    viewOffsetY=40.3294)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1020.8, 
    farPlane=1356.39, width=609.435, height=315.032, cameraPosition=(265.395, 
    -971.685, 472.486), cameraUpVector=(-0.0755692, 0.702853, 0.707309), 
    cameraTarget=(162.207, 72.749, -28.3538), viewOffsetX=-9.49392, 
    viewOffsetY=39.9205)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1007.02, 
    farPlane=1361.32, width=601.208, height=310.779, cameraPosition=(302.691, 
    -1064.12, 38.6615), cameraUpVector=(-0.0227761, 0.398448, 0.916908), 
    cameraTarget=(159.891, 87.1273, -42.4051), viewOffsetX=-9.36576, 
    viewOffsetY=39.3816)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1035.74, 
    farPlane=1342.86, width=618.357, height=319.643, cameraPosition=(174.165, 
    -958.01, 515.139), cameraUpVector=(-0.0611945, 0.733592, 0.67683), 
    cameraTarget=(161.295, 70.2709, -27.8219), viewOffsetX=-9.63291, 
    viewOffsetY=40.5049)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1034.47, 
    farPlane=1344.14, width=617.6, height=319.254, cameraPosition=(158.186, 
    -959.106, 513.442), cameraUpVector=(0.254563, 0.720662, 0.644859), 
    cameraTarget=(145.316, 69.1749, -29.5187), viewOffsetX=-9.62112, 
    viewOffsetY=40.4553)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1035.93, 
    farPlane=1346.82, width=618.47, height=319.704, cameraPosition=(343.545, 
    -671.345, 872.187), cameraUpVector=(0.171272, 0.937775, 0.302065), 
    cameraTarget=(150.907, 61.3696, -10.0557), viewOffsetX=-9.63468, 
    viewOffsetY=40.5123)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1057.85, 
    farPlane=1328.9, width=631.555, height=326.468, cameraPosition=(358.755, 
    -423.569, 1040.67), cameraUpVector=(0.0958074, 0.992824, 0.0715584), 
    cameraTarget=(154.911, 61.29, 3.5137), viewOffsetX=-9.83852, 
    viewOffsetY=41.3694)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1033.37, 
    farPlane=1349.17, width=616.942, height=318.914, cameraPosition=(363.584, 
    -680.957, 858.713), cameraUpVector=(-0.201198, 0.90458, 0.375839), 
    cameraTarget=(169.528, 65.8782, -11.294), viewOffsetX=-9.61088, 
    viewOffsetY=40.4122)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1034.6, 
    farPlane=1348.72, width=617.678, height=319.294, cameraPosition=(510.254, 
    -455.846, 979.775), cameraUpVector=(-0.0639547, 0.986762, 0.149034), 
    cameraTarget=(164.083, 62.8028, -1.80602), viewOffsetX=-9.62232, 
    viewOffsetY=40.4603)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1001.05, 
    farPlane=1389.61, width=597.65, height=308.941, cameraPosition=(-285.957, 
    -753.251, 690.939), cameraUpVector=(-0.0680875, 0.894148, 0.442565), 
    cameraTarget=(155.391, 61.6044, -11.5953), viewOffsetX=-9.31033, 
    viewOffsetY=39.1484)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1059.99, 
    farPlane=1332.4, width=632.838, height=327.131, cameraPosition=(-9.27028, 
    -498.249, 1009.05), cameraUpVector=(-0.0806878, 0.985295, 0.150609), 
    cameraTarget=(160.594, 62.6169, 4.60155), viewOffsetX=-9.8585, 
    viewOffsetY=41.4533)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='SF', outputPosition=INTEGRATION_POINT, refinement=(
    COMPONENT, 'SF1'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='SM', outputPosition=INTEGRATION_POINT, refinement=(
    COMPONENT, 'SM2'), )
session.viewports['Viewport: 1'].odbDisplay.basicOptions.setValues(
    averageElementOutput=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1079.82, 
    farPlane=1311.51, width=644.676, height=333.25, cameraPosition=(136.566, 
    -449.099, 1049.15), cameraUpVector=(-0.143476, 0.983685, 0.108528), 
    cameraTarget=(165.813, 64.3042, 6.12727), viewOffsetX=-10.0429, 
    viewOffsetY=42.2286)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1084.19, 
    farPlane=1308.48, width=647.286, height=334.599, cameraPosition=(332.989, 
    -191.233, 1136.81), cameraUpVector=(-0.0998928, 0.989665, -0.102878), 
    cameraTarget=(166.402, 67.046, 15.2589), viewOffsetX=-10.0836, 
    viewOffsetY=42.3996)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1051.24, 
    farPlane=1338.96, width=627.614, height=324.43, cameraPosition=(24.8156, 
    -600.414, 944.413), cameraUpVector=(-0.0151692, 0.964779, 0.262623), 
    cameraTarget=(157.885, 61.2489, -2.59805), viewOffsetX=-9.77714, 
    viewOffsetY=41.111)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U2'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U1'), )
session.viewports['Viewport: 1'].odbDisplay.basicOptions.setValues(
    averageElementOutput=True)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U2'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=1052.7, 
    farPlane=1337.5, width=628.484, height=324.88, cameraPosition=(11.5625, 
    -601.188, 942.01), cameraUpVector=(0.246938, 0.929292, 0.274659), 
    cameraTarget=(144.632, 60.4754, -5.00074), viewOffsetX=-9.79069, 
    viewOffsetY=41.168)
session.viewports['Viewport: 1'].view.setValues(nearPlane=984.964, 
    farPlane=1393.74, width=588.044, height=303.976, cameraPosition=(1002.57, 
    -281.47, 731.353), cameraUpVector=(0.0871798, 0.981668, -0.169492), 
    cameraTarget=(161.548, 62.8124, 5.76044), viewOffsetX=-9.16071, 
    viewOffsetY=38.519)
session.viewports['Viewport: 1'].view.setValues(nearPlane=972.129, 
    farPlane=1399.89, width=580.381, height=300.015, cameraPosition=(722.803, 
    -826.833, 448.761), cameraUpVector=(0.256178, 0.8452, 0.469052), 
    cameraTarget=(152.571, 68.35, -26.4401), viewOffsetX=-9.04134, 
    viewOffsetY=38.0171)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1000.76, 
    farPlane=1384.22, width=597.477, height=308.852, cameraPosition=(-517.513, 
    -439.456, 808.867), cameraUpVector=(0.504312, 0.765511, 0.399578), 
    cameraTarget=(133.401, 66.2734, -11.4271), viewOffsetX=-9.30766, 
    viewOffsetY=39.1369)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1034.29, 
    farPlane=1347.31, width=617.495, height=319.199, cameraPosition=(36.3161, 
    -808.164, 741.222), cameraUpVector=(0.0705896, 0.866284, 0.494539), 
    cameraTarget=(163.379, 62.8104, -18.7727), viewOffsetX=-9.61948, 
    viewOffsetY=40.448)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1020.82, 
    farPlane=1352.18, width=609.453, height=315.042, cameraPosition=(121.112, 
    -1074.77, 49.0413), cameraUpVector=(0.000562509, 0.409762, 0.912192), 
    cameraTarget=(167.693, 83.2832, -46.244), viewOffsetX=-9.4942, 
    viewOffsetY=39.9212)
mdb.save()
#: The model database has been saved to "Y:\mb_both_feet_ss.cae".
mdb.save()
#: The model database has been saved to "Y:\mb_both_feet_ss.cae".
mdb.save()
#: The model database has been saved to "Y:\mb_both_feet_ss.cae".

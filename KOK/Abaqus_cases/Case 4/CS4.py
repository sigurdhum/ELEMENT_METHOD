########### IMPORTING THE MODULES ########### 
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
########### PART MODULE ###########
mdb.models.changeKey(fromName='Model-1', toName='BEAM')
mdb.models['BEAM'].ConstrainedSketch(name='__profile__', sheetSize=3000.0)
mdb.models['BEAM'].sketches['__profile__'].rectangle(point1=(-1000.0, -75.0), 
    point2=(1000.0, 75.0))
mdb.models['BEAM'].Part(dimensionality=THREE_D, name='Beam', type=
    DEFORMABLE_BODY)
mdb.models['BEAM'].parts['Beam'].BaseSolidExtrude(depth=100.0, sketch=
    mdb.models['BEAM'].sketches['__profile__'])
mdb.models['BEAM'].parts['Beam'].Set(faces=
    mdb.models['BEAM'].parts['Beam'].faces.getSequenceFromMask(('[#4 ]', ), ), 
    name='Fixed')
########### PROPERTY MODULE ###########
#### ASSIGN MATERIAL PROPERTIES ####
mdb.models['BEAM'].Material(name='Wood')
mdb.models['BEAM'].materials['Wood'].Elastic(table=((10000.0, 0.3), ))
#### DEFINE SECTION ####
mdb.models['BEAM'].Material(name='Wood')
mdb.models['BEAM'].materials['Wood'].Elastic(table=((10000.0, 0.3), ))
mdb.models['BEAM'].HomogeneousSolidSection(material='Wood', name='BeamSection', 
    thickness=None)
#### ASSIGN SECTION ####
mdb.models['BEAM'].Material(name='Wood')
mdb.models['BEAM'].materials['Wood'].Elastic(table=((10000.0, 0.3), ))
mdb.models['BEAM'].HomogeneousSolidSection(material='Wood', name='BeamSection', 
    thickness=None)
mdb.models['BEAM'].parts['Beam'].Set(cells=
    mdb.models['BEAM'].parts['Beam'].cells.getSequenceFromMask(('[#1 ]', ), ), 
    name='Whole')
mdb.models['BEAM'].parts['Beam'].SectionAssignment(offset=0.0, offsetField='', 
    offsetType=MIDDLE_SURFACE, region=
    mdb.models['BEAM'].parts['Beam'].sets['Whole'], sectionName='BeamSection', 
    thicknessAssignment=FROM_SECTION)
########### ASSEMBLY MODULE ###########
mdb.models['BEAM'].rootAssembly.DatumCsysByDefault(CARTESIAN)
mdb.models['BEAM'].rootAssembly.Instance(dependent=ON, name='Beam-1', part=
    mdb.models['BEAM'].parts['Beam'])
########### STEP MODULE ###########
mdb.models['BEAM'].StaticStep(initialInc=0.1, name='BeamLoad', previous=
    'Initial')
########### LOAD MODULE ###########
mdb.models['BEAM'].rootAssembly.Surface(name='BeamLoad', side1Faces=
    mdb.models['BEAM'].rootAssembly.instances['Beam-1'].faces.getSequenceFromMask(
    ('[#2 ]', ), ))
mdb.models['BEAM'].Pressure(amplitude=UNSET, createStepName='BeamLoad', 
    distributionType=UNIFORM, field='', magnitude=0.025, name='Pressure', 
    region=mdb.models['BEAM'].rootAssembly.surfaces['BeamLoad'])
########### MESH MODULE ###########
mdb.models['BEAM'].parts['Beam'].setElementType(elemTypes=(ElemType(
    elemCode=C3D8R, elemLibrary=STANDARD, secondOrderAccuracy=OFF, 
    distortionControl=DEFAULT), ElemType(elemCode=C3D6, elemLibrary=STANDARD), 
    ElemType(elemCode=C3D4, elemLibrary=STANDARD)), regions=(
    mdb.models['BEAM'].parts['Beam'].cells.getSequenceFromMask(('[#1 ]', ), ), 
    ))
mdb.models['BEAM'].parts['Beam'].seedPart(deviationFactor=0.1, minSizeFactor=
    0.1, size=50.0)
mdb.models['BEAM'].parts['Beam'].generateMesh()
########### JOB MODULE ###########
mdb.models['BEAM'].rootAssembly.regenerate()
mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
    explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
    memory=90, memoryUnits=PERCENTAGE, model='BEAM', modelPrint=OFF, 
    multiprocessingMode=DEFAULT, name='Deform', nodalOutputPrecision=SINGLE, 
    numCpus=2, numDomains=2, numGPUs=0, numThreadsPerMpiProcess=1, queue=None, 
    resultsFormat=ODB, scratch='', type=ANALYSIS, userSubroutine='', waitHours=
    0, waitMinutes=0)
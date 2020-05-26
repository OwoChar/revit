import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import FilePath
import os
from os import path, remove

uiapp = __revit__
app = uiapp.Application

filelocation = ""
localfilelocation = ""

modelfilelocation = modelpath(filelocation)
modellocalfilelocation = modelpath(localfilelocation)

if filecheckcentral == True:   
    if filechecklocal == True:
        os.remove(localfilelocation)
        CreateNewLocal(modelfilelocation,modellocalfilelocation)
    else:
        CreateNewLocal(modelfilelocation,modellocalfilelocation)
else:
    print('Central File Does Not Exist')

uiapp.OpenAndActivateDocument(localfilelocation)
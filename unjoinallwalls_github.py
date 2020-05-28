import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import FilteredElementCollector

walllist = FilteredElementCollector(doc,ActiveView.Id).OfCategory(OST_Walls).WhereElementIsNotElementType().ToElements()

t.Start()
for wall in walllist:
    joinelementlist = GetJoinedElements(doc, wall)
    for joinelementid in joinelementlist:
        joinelement = GetElement(joinelementid)
        UnjoinGeometry(doc, wall, joinelement)
t.Commit()
import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import BuiltInParameter
from Autodesk.Revit.DB import Level

currentbaseconstraint = 'T.O.S.'
newbaseconstraint = 'FLOOR'

selectedelements = [doc.GetElement(id) for id in ActiveUIDocument.Selection.GetElementIds()]
for sel in selectedelements:
    orig = sel.get_Parameter(WALL_BASE_CONSTRAINT).AsValueString()
    new = orig.replace(currentbaseconstraint, newbaseconstraint)
    t.Start()
    for l in FilteredElementCollector(doc).OfClass(Level):
        if new == l.Name:
            sel.get_Parameter(WALL_BASE_CONSTRAINT).Set(l.Id)
    t.Commit()
    print sel.get_Parameter(WALL_BASE_CONSTRAINT).AsValueString()
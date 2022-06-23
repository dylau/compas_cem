# This script is to be set and run in Rhino.

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg

import compas.geometry as cg
import compas.datastructures.network as nw

from compas.datastructures import Network
from compas_rhino.artists import NetworkArtist



print("hello rhino!")

# ask Rhino users to input list of lines
LineIds = rs.GetObjects( message="pick some lines",
                                    filter=4)

#TODO - rebase the network
rhinoLines = []
vector = rg.Vector3d(50,0,0)
xform = rg.Transform.Translation(vector)

# move the lines
for id in LineIds:
    print("Object id:", id)
    rhinoLine = rg.LineCurve(rs.coerceline(id)).Duplicate()
    rhinoLine.Transform(xform)
    rhinoLines.append(rhinoLine)

# build this diagram into a compas network
compasLines = []
for rline in rhinoLines:
    cLine = cg.Line(rline.PointAtStart  , rline.PointAtEnd)
    compasLines.append(cLine)

network = Network.from_lines(compasLines)

networkartist = NetworkArtist(network)
networkartist.draw()
networkartist.draw_edgelabels()
networkartist.draw_nodelabels()

network.to_json("C:\\Users\\uk083720\\Documents\\dliu\\04_Code\\CompasCEM\\compas_cem\\src\\compas_cem\\ghpython\\WIP_braced-frame\\network.json",pretty=True)
# network.to_obj("C:\\Users\\uk083720\\Documents\\dliu\\04_Code\\CompasCEM\\compas_cem\\src\\compas_cem\\ghpython\\WIP\\network.obj")
print(network.to_data())


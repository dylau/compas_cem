"""
Export a COMPAS CEM diagram and save it as a JSON file.
"""
import os

from ghpythonlib.componentbase import executingcomponent as component


class DiagramToJSON(component):
    def RunScript(self, diagram, filepath):
        if diagram and filepath:
            filepath = os.path.abspath(filepath)
            diagram.to_json(filepath, pretty=True)
            return diagram.data
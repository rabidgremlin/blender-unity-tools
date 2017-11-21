#    Addon info
bl_info = {
    'name': 'Unity Tools',
    'author': 'Jonathan Ackerman',
    'location': 'View3D > Tools panel > Misc > Unity Tools',
    'category': '3D View'
    }
 
# To support reload properly, try to access a package var, 
# if it's there, reload everything
if "bpy" in locals():
    import imp
    imp.reload(addrig)
    #imp.reload(mysphere)
    #imp.reload(mycylinder)
    print("Reloaded unity tools")
else:
    #from . import mycube, mysphere, mycylinder
    from . import addrig
    print("Imported unity tools")
 
import bpy
from bpy.props import *
 
#
#   class AddMeshPanel(bpy.types.Panel):
#
class AddMeshPanel(bpy.types.Panel):
    bl_label = "Unity Tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_idname = "multifile.addmesh.panel"
 
    def draw(self, context):
        self.layout.operator("multifile.add", 
            text="Add Rig").mesh = "cube"
        #self.layout.operator("multifile.add", 
        #    text="Add cylinder").mesh = "cylinder"
        #self.layout.operator("multifile.add", 
        #    text="Add sphere").mesh = "sphere"
 
#
#   class OBJECT_OT_AddButton(bpy.types.Operator):
#
class OBJECT_OT_AddButton(bpy.types.Operator):
    bl_idname = "multifile.add"
    bl_label = "Add"
    mesh = bpy.props.StringProperty()
 
    def execute(self, context):
        if self.mesh == "cube":
            addrig.makeMesh(-8)
        #elif self.mesh == "cylinder":
        #    mycylinder.makeMesh(-5)
        #elif self.mesh == "sphere":
        #    mysphere.makeMesh(-2)
        return{'FINISHED'}    
 
#
#    Registration
#
 
def register():
    bpy.utils.register_module(__name__)
 
def unregister():
    bpy.utils.unregister_module(__name__)
 
if __name__ == "__main__":
    register()
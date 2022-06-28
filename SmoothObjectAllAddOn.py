import bpy

bl_info = {
    "name": "Smooth Object",
    "autor": "wangxiaowen",
    "version": (1, 0),
    "blender": (3, 20, 0),
    "location": "view3d>Tool",
    "warning": "",
    "wiki_url": "",
    "category": "Mesh",
}


class AutoSmoothOperator(bpy.types.Operator):
    bl_idname = "wm.smooth_angle_all"
    bl_label = "AutoSmooth Operator"

    def execute(self, context):
        all_objects = bpy.data.objects
        all_mesh=[];
        for mesh_object in all_objects:
            if(mesh_object.type == "MESH"):
                # find mesh objects:
               all_mesh.append(mesh_object)
        
        for sigle_mesh in all_mesh:
            print(sigle_mesh.data)
            
            sigle_mesh.data.use_auto_smooth=True
            
        return {'FINISHED'}


# Only needed if you want to add into a dynamic menu.
def menu_func(self, context):
    self.layout.operator(AutoSmoothOperator.bl_idname, text="Hello World Operator")


# Register and add to the view menu (required to also use F3 search "Hello World Operator" for quick access).
bpy.utils.register_class(AutoSmoothOperator)
bpy.types.VIEW3D_MT_view.append(menu_func)

# Test call to the newly defined operator.
#result = bpy.ops.wm.smooth_angle_all()
#print(result)

class SmoothPanel(bpy.types.Panel):
    bl_label = "Smooth object"
    bl_idname = "PT_Smooth"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Tool"
    bl_category = "Smooth Object"

    def draw(self, context):
        print(self)
        layout = self.layout
        layout.scale_y = 1.4
        row = layout.row()
        row.label(text="Smooth All")
        row = layout.row()
        row.operator("object.shade_smooth")
        row = layout.row()
        row.operator("object.shade_flat")
        row = layout.row()
        row.operator("wm.smooth_angle_all")
        
        
def register():
    bpy.utils.register_class(SmoothPanel)

def unregister():
    bpy.utils.unregister_class(SmoothPanel)
   

if __name__ == "__main__":
    register()

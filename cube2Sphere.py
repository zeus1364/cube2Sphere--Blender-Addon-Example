bl_info = {
    "name": "cube2Sphere",
    "author": "Aaron Prater",
    "version": (1, 1),
    "blender": (5, 0, 0),
    "location": "View3D > N-Panel > Cube2Sphere",
    "description": "Convert selected cube into a smooth sphere, or reverse sphere back into cube.",
    "category": "Object",
}

import bpy

# ---------------------------------------------------------
# Core Conversion: Cube → Sphere (Production-Grade)
# ---------------------------------------------------------

def convert_cube_to_sphere(context):
    before_objects = set(bpy.data.objects)

    shape_A = context.active_object
    if shape_A is None or shape_A.type != 'MESH':
        raise RuntimeError("Active object must be a mesh (Cube).")

    shape_A_name = shape_A.name
    shape_A_location = shape_A.location.copy()

    bpy.ops.mesh.primitive_uv_sphere_add(radius=1.0, location=shape_A_location)

    after_objects = set(bpy.data.objects)
    new_objects = after_objects - before_objects

    shape_B = None
    for obj in new_objects:
        shape_B = obj
        break

    if shape_B is None:
        raise RuntimeError("Failed to detect newly created sphere.")

    shape_B.name = "Shape_B_Sphere"

    bpy.ops.object.shade_smooth()

    subdiv = shape_B.modifiers.new(name="Smooth_Subdiv", type='SUBSURF')
    subdiv.levels = 3
    subdiv.render_levels = 3
    bpy.ops.object.modifier_apply(modifier=subdiv.name)

    bpy.ops.object.select_all(action='DESELECT')
    shape_A_ref = bpy.data.objects.get(shape_A_name)
    if shape_A_ref:
        shape_A_ref.select_set(True)
        bpy.ops.object.delete()

    return {'FINISHED'}


# ---------------------------------------------------------
# Reverse Conversion: Sphere → Cube (Production-Grade)
# ---------------------------------------------------------

def convert_sphere_to_cube(context):
    before_objects = set(bpy.data.objects)

    shape_A = context.active_object
    if shape_A is None or shape_A.type != 'MESH':
        raise RuntimeError("Active object must be a mesh (Sphere).")

    shape_A_name = shape_A.name
    shape_A_location = shape_A.location.copy()

    bpy.ops.mesh.primitive_cube_add(size=2.0, location=shape_A_location)

    after_objects = set(bpy.data.objects)
    new_objects = after_objects - before_objects

    shape_B = None
    for obj in new_objects:
        shape_B = obj
        break

    if shape_B is None:
        raise RuntimeError("Failed to detect newly created cube.")

    shape_B.name = "Shape_B_Cube"

    bpy.ops.object.select_all(action='DESELECT')
    shape_A_ref = bpy.data.objects.get(shape_A_name)
    if shape_A_ref:
        shape_A_ref.select_set(True)
        bpy.ops.object.delete()

    return {'FINISHED'}


# ---------------------------------------------------------
# Operators
# ---------------------------------------------------------

class C2S_OT_Convert(bpy.types.Operator):
    bl_idname = "object.c2s_convert"
    bl_label = "Cube → Sphere"
    bl_description = "Convert the selected cube into a smooth sphere"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        try:
            convert_cube_to_sphere(context)
        except Exception as e:
            self.report({'ERROR'}, str(e))
            return {'CANCELLED'}
        return {'FINISHED'}


class C2S_OT_Reverse(bpy.types.Operator):
    bl_idname = "object.c2s_reverse"
    bl_label = "Sphere → Cube"
    bl_description = "Convert the selected sphere back into a cube"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        try:
            convert_sphere_to_cube(context)
        except Exception as e:
            self.report({'ERROR'}, str(e))
            return {'CANCELLED'}
        return {'FINISHED'}


# ---------------------------------------------------------
# N-Panel UI
# ---------------------------------------------------------

class C2S_PT_Panel(bpy.types.Panel):
    bl_label = "Cube2Sphere"
    bl_idname = "C2S_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Cube2Sphere"

    def draw(self, context):
        layout = self.layout
        layout.operator("object.c2s_convert", icon='MESH_UVSPHERE')
        layout.operator("object.c2s_reverse", icon='MESH_CUBE')


# ---------------------------------------------------------
# Registration
# ---------------------------------------------------------

classes = (
    C2S_OT_Convert,
    C2S_OT_Reverse,
    C2S_PT_Panel,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()

import bpy

class EZQUADREMESHES_OT_remesh(bpy.types.Operator):
    bl_idname = "ezquadremeshes.remesh"
    bl_label = "EZ Quad Remesh"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = context.active_object
        ez_props = context.scene.ez_quadremeshes_props
        
        if obj and obj.type == 'MESH':
            bpy.ops.object.quadriflow_remesh(
                target_faces=ez_props.target_faces,
                use_preserve_sharp=True,
                use_preserve_boundary=True,
                smooth_normals=True
            )
            for _ in range(ez_props.smooth_iterations):
                bpy.ops.object.modifier_add(type='SMOOTH')
                context.object.modifiers["Smooth"].factor = 0.5
                context.object.modifiers["Smooth"].iterations = 1
                bpy.ops.object.modifier_apply(modifier="Smooth")
            return {'FINISHED'}
        return {'CANCELLED'}

def register():
    bpy.utils.register_class(EZQUADREMESHES_OT_remesh)

def unregister():
    bpy.utils.unregister_class(EZQUADREMESHES_OT_remesh)
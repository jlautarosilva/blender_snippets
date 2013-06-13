#----------------------------------------------------------
# File PasoPeaton.py
# Creates an array modifier whit offset and applies it
# Update to API rev. 37702
# Created by Laboratorio de Experimentacion Tridimensional
# Universidad del Bio-Bio, Concepcion, Chile
#----------------------------------------------------------
import bpy
 
def run(origin):
    # Add single plane to the scene
    bpy.ops.mesh.primitive_plane_add(
        location=(0,0,0), 
        rotation=(0,0,0))
    
    # Scale the plane along the x and y axis
    ob = bpy.context.object
    ob.scale = (width, long, 0)
    bpy.ops.object.transform_apply(scale=True)

    #bpy.ops.object.editmode_toggle()
    #bpy.ops.mesh.duplicate_move(MESH_OT_duplicate={"mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "texture_space":False, "release_confirm":False})
    #bpy.ops.object.editmode_toogle()
 

 
#Do not modificate 
    # Create an empty
    separation=width*4
    bpy.ops.object.add(
        type='EMPTY',
        location=(separation,0,0), 
        rotation=(0, 0, 0))
    empty = bpy.context.object
 
    # Make chain link active again
    scn = bpy.context.scene
    scn.objects.active = ob
 
    # Add modifier
    mod = ob.modifiers.new('Repeat', 'ARRAY')
    mod.fit_type = 'FIXED_COUNT'
    mod.count = lines
    mod.use_relative_offset = width
    mod.use_object_offset = True
    mod.offset_object = empty
 
    # Apply the modifier
    bpy.ops.object.visual_transform_apply()
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier='Repeat')
 
    # Move chain into place
    bpy.ops.transform.translate(value=origin)
 
    # Don't need empty anymore
    scn.objects.unlink(empty)
    del(empty)
 
    return
 
if __name__ == "__main__":
    lines = 8 #quantity of lines
    width = 0.5 #width for each line
    width = width/2
    long = 5 #long of each line
    long = long/2
    run((0,0,0))
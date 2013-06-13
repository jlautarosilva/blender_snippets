import bpy


class DialogOperator(bpy.types.Operator):
    bl_idname = "object.dialog_operator"
    bl_label = "POPUP de Lautaro :D"

    my_float = bpy.props.FloatProperty(name="Aqui se pone un float")
    my_bool = bpy.props.BoolProperty(name="Opcion xD")
    my_string = bpy.props.StringProperty(name="Aqui se escribe un string")

    def execute(self, context):
        message = "Popup Values: %f, %d, '%s'" % \
            (self.my_float, self.my_bool, self.my_string)
        self.report({'INFO'}, message)
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


#bpy.utils.register_class(DialogOperator)



if __name__ == "__main__":
    bpy.utils.register_class(DialogOperator)
# test call
    bpy.ops.object.dialog_operator('INVOKE_DEFAULT')
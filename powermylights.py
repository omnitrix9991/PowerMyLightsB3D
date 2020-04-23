import bpy


class ChangeLightPower_OT_operator(bpy.types.Operator):
    bl_idname = "view3d.clp"
    bl_label = "Changes the power of your lights "

    @classmethod
    def poll(cls, context):

        if len(bpy.context.scene.objects) == 0:
            return False
        else:
            return True

    def execute(self, context):

        for i in bpy.context.scene.objects:

            listoflights = []
            
            if i.type == 'LIGHT':
                if i.data.type != 'SUN':
                    listoflights.append(i)
                else:
                    pass
            else:
                pass
            for i in listoflights:
                oldenergy = i.data.energy

                i.data.energy = (bpy.context.scene.powerpercent * oldenergy)

        bpy.context.scene.powerpercent = 1
        
        return {'FINISHED'}


class ChangePower_PT_Panel(bpy.types.Panel):
    bl_idname = "CP_PT_Panel"
    bl_label = "PowerMyLights"
    bl_category = "PowerMyLights"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        col = self.layout.column()
        col.label(text="Change Power :")
        col.prop(bpy.context.scene, "powerpercent",
                 text='(All Current Powers) *')
        if bpy.context.scene.powerpercent != 1:
            col.operator('view3d.clp', text='Apply')
        col = self.layout.column()


class MYLIGHTS_PT_Panel(bpy.types.Panel):
    bl_parent_id = "CP_PT_Panel"
    bl_label = "All Scene Lights :"
    bl_category = "PowerMyLights"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        col = self.layout.column()

        for i in bpy.context.scene.objects:
            if i.type == 'LIGHT':
                if i.data.type != 'SUN':

                    col.prop(i.data, 'energy', text=i.name)
                else:
                    pass
            else:
                pass

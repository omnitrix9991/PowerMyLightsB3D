import bpy

bl_info = {
    "name": "PowerMyLights",
    "author": "omnitrix9991",
    "location": "View3D",
    "description": "A addon to manage power of all lights in the Scene.",
    "blender": (2, 80, 0),
    "version": (0, 0, 1),
    "wiki_url": "https://github.com/omnitrix9991/MeshVolumeModellerB3D",
    "warning": "",
    "category": "Object",
}


class ChangeLightPower_OT_operator(bpy.types.Operator):
    bl_idname = "view3d.clp"
    bl_label = "Changes the power of your lights "

    @classmethod
    def poll(cls, context):

        if len(bpy.context.scene.objects) == 0:

            return False
        else:
            if bpy.context.scene.light_tool.checkto_applya == True:
                return True
            elif bpy.context.scene.light_tool.collectioninfo is None:
                return False
            else:
                return True

    def execute(self, context):
        light_tool = bpy.context.scene.light_tool

        if light_tool.checkto_applya == True:

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
                    i.data.energy = (light_tool.powerpercent * oldenergy)/100

            light_tool.powerpercent = 100

        else:
            for i in light_tool.collectioninfo.objects:
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
                    i.data.energy = (light_tool.powerpercent * oldenergy)/100

            light_tool.powerpercent = 100

        return {'FINISHED'}


class ChangePower_PT_Panel(bpy.types.Panel):
    bl_idname = "CP_PT_Panel"
    bl_label = "PowerMyLights"
    bl_category = "PowerMyLights"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):

        light_tool = bpy.context.scene.light_tool
        col = self.layout.column()
        col.prop(light_tool, "checkto_applya", text='Apply to all Collections')

        if light_tool.checkto_applya == True:

            col = self.layout.column()
            col.label(text="Power = x% of current Power's :")
            col.prop(light_tool, "powerpercent",
                     text='(x) ')
            if light_tool.powerpercent != 100:
                col.operator('view3d.clp', text='Apply')
            col = self.layout.column()
        else:
            col = self.layout.column()

            col.label(text="Applying to selected collection:")
            col.prop(light_tool, "collectioninfo", text="")
            col.label(text="Power = x% of current Power's :")
            col.prop(light_tool, "powerpercent",
                     text='(x) ')
            if light_tool.powerpercent != 100:
                col.operator('view3d.clp', text='Apply')
            col = self.layout.column()


class MYLIGHTS_PT_Panel(bpy.types.Panel):
    bl_parent_id = "CP_PT_Panel"
    bl_label = "All Scene Lights :"
    bl_category = "PowerMyLights"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        light_tool = bpy.context.scene.light_tool

        col = self.layout.column()
        col.label(text='Master Collection')

        for i in bpy.context.scene.collection.objects:
            if i.type == 'LIGHT':
                if i.data.type != 'SUN':
                    col.prop(i.data, 'energy', text=i.name)
                else:
                    pass
            else:
                pass

        for x in bpy.context.scene.collection.children:

            col = self.layout.column()
            col.label(text=x.name)

            for i in x.objects:
                if i.type == 'LIGHT':
                    if i.data.type != 'SUN':
                        col.prop(i.data, 'energy', text=i.name)
                    else:
                        pass
                else:
                    pass

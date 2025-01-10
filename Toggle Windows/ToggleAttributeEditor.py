import maya.cmds as cmds

def toggle_attribute_editor():
    if cmds.workspaceControl("AttributeEditor", exists=True):
        if cmds.workspaceControl("AttributeEditor", q=True, vis=True):
            # Attribute Editor is open, so close it
            cmds.workspaceControl("AttributeEditor", edit=True, vis=False)
        else:
            # Attribute Editor is closed, so restore it
            cmds.workspaceControl("AttributeEditor", edit=True, vis=True)
    else:
        # Initialize the Attribute Editor and restore the workspace control
        cmds.AttributeEditor()
        cmds.workspaceControl("AttributeEditor", edit=True, restore=True)

toggle_attribute_editor()
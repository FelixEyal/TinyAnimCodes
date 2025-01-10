import maya.cmds as cmds

def toggle_script_editor():
    if cmds.workspaceControl("ScriptEditor", exists=True):
        if cmds.workspaceControl("ScriptEditor", q=True, vis=True):
            # Script Editor is open, so close it
            cmds.workspaceControl("ScriptEditor", edit=True, vis=False)
        else:
            # Script Editor is closed, so restore it
            cmds.workspaceControl("ScriptEditor", edit=True, vis=True)
    else:
        # Initialize the Script Editor and restore the workspace control
        cmds.ScriptEditor()
        cmds.workspaceControl("ScriptEditor", edit=True, restore=True)

toggle_script_editor()
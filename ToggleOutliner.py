import maya.cmds as cmds

def toggle_outliner():
    if cmds.workspaceControl("Outliner", exists=True):
        if cmds.workspaceControl("Outliner", q=True, vis=True):
            # Outliner is open, so close it
            cmds.workspaceControl("Outliner", edit=True, vis=False)
        else:
            # Outliner is closed, so restore it
            cmds.workspaceControl("Outliner", edit=True, vis=True)
    else:
        # Initialize the Outliner panel and restore the workspace control
        cmds.optionVar(iv=("gOutlinerPanelNeedsInit", 1))
        cmds.OutlinerPanel()
        cmds.workspaceControl("Outliner", edit=True, restore=True)

toggle_outliner()
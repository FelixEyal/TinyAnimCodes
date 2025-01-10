import maya.cmds as cmds

def toggle_channel_box():
    if cmds.workspaceControl("ChannelBoxLayerEditor", exists=True):
        if cmds.workspaceControl("ChannelBoxLayerEditor", q=True, vis=True):
            # Channel Box is open, so close it
            cmds.workspaceControl("ChannelBoxLayerEditor", edit=True, vis=False)
        else:
            # Channel Box is closed, so restore it
            cmds.workspaceControl("ChannelBoxLayerEditor", edit=True, vis=True)
    else:
        # Initialize the Channel Box and restore the workspace control
        cmds.ChannelBox("channelBox", mlc=True)
        cmds.workspaceControl("ChannelBoxLayerEditor", edit=True, restore=True)

toggle_channel_box()
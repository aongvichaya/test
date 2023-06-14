import maya.cmds as cmds

MyLabel = 'My Panel'
cmds.window()
cmds.frameLayout( lv=0 )
cmds.modelPanel( l=MyLabel )
cmds.showWindow()

panels = cmds.getPanel( all=True )

for panel in panels:
	if MyLabel == cmds.panel( panel, q=True, label=True ):
		myPanel = panel
		print( 'Found: '+MyLabel )


#setenv PYTHONPATH RMANTREE/bin  
#Win: Go to Control Panel>>Systems>>Advanced>>Environment Vars, 
# edit/add PYTHONPATH variable...use %RMANTREE%/bin   So annoying... 


#  # this is where prman.py lives
#python
import prman
ri = prman.Ri() # create an instance of the RenderMan interface
rendertarget = "SeriousStruff.rib"
ri.Begin(rendertarget)  # set rendertarget to ri.RENDER to render pixels
ri.Display("SeriousStruff.exr", "it", "rgba")

ri.Format(512,512,1)
ri.Projection(ri.PERSPECTIVE, {ri.FOV: 45}) # standard Ri tokens are available
ri.Translate(0,0,8)
ri.Rotate(-90,0,0,1)
ri.Rotate(60,0,1,0)
#ri.Rotate(-90,1,0,0)

ri.WorldBegin()

#Lens Frame
ri.TransformBegin()
ri.AttributeBegin()

ri.Bxdf("PxrDisney","forFrame",
{"color baseColor": [0.0,0.3,1.0]}

)
ri.Cylinder(1.0,0.6,0.8,360)

ri.AttributeEnd()
ri.TransformEnd()

#lens 1
ri.TransformBegin()
ri.AttributeBegin()

ri.Translate(0.0,0.0,0.7)
ri.Scale(1.95,1.95,0.3)
ri.Sphere(0.5,-1.0,0.0,360)

ri.AttributeEnd()
ri.TransformEnd()

#lens 2
ri.TransformBegin()
ri.AttributeBegin()

ri.Translate(0.0,0.0,0.8)
ri.Scale(1.95,1.95,0.3)
ri.Sphere(0.5,1.0,0.0,360)

ri.AttributeEnd()
ri.TransformEnd()

#Handle

ri.AttributeBegin()
ri.TransformBegin()
ri.Rotate(45,0,0,1)
ri.Rotate(90,0,1,0)
ri.Translate(-0.69,0,-1.78)
ri.Scale(0.6,0.6,8.0)

ri.Cylinder(0.15,0.35,0.6,360)
ri.TransformEnd()

ri.TransformBegin()

ri.TransformEnd()

ri.AttributeEnd()

ri.WorldEnd()
ri.End()
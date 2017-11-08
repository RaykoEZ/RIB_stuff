
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

#domelight
ri.AttributeBegin()
ri.TransformBegin()

ri.Light("PxrDomeLight","myLight",{"float exposure":[0]},
{"string lightColorMap": ["sky_env.tx"]})

ri.TransformEnd()
ri.AttributeEnd()


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
ri.Scale(2.0,2.0,0.3)
ri.Sphere(0.5,-1.0,0.0,360)

ri.AttributeEnd()
ri.TransformEnd()

#lens 2
ri.TransformBegin()
ri.AttributeBegin()

ri.Translate(0.0,0.0,0.8)
ri.Scale(2.0,2.0,0.3)
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

#Handle to frame
ri.AttributeBegin()
ri.TransformBegin()
ri.Bxdf("PxrDisney","frameToHandle",{"color baseColor":[0.1,0.5,0.5]})

ri.Scale(0.7,0.3,0.5)
#ri.Rotate(0,0,0,1)

ri.Translate(0,2.0,1.4)

ri.Torus(1,0.25,90,-90, 45 )

ri.TransformEnd()
ri.AttributeEnd()

#cone at the end of handle
ri.AttributeBegin()
ri.TransformBegin()

ri.Translate(0,0.0,-1)
ri.Rotate(90, 0,1,0)
ri.Cone(0.5,0.15,360)

ri.TransformEnd()
ri.AttributeEnd()

ri.AttributeEnd()

ri.WorldEnd()
ri.End()
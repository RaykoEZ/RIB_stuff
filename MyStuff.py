import prman

ri = prman.Ri() # create an instance of the RenderMan interface

rendertarget = "MyStuff.rib"
ri.Begin(rendertarget)  # set rendertarget to ri.RENDER to render pixels
ri.Display("MyStuff.exr", "it", "rgba")
ri.Format(512,512,1)

#ri.Declare("Light1","string")


ri.Projection(ri.PERSPECTIVE, {ri.FOV: 60}) # standard Ri tokens are available
ri.Translate(0,0,10)
ri.Rotate(-45,1,0,0)
ri.WorldBegin()

#ri.LightSource("pointight", {ri.HANDLEID:"Light1", "point from":[-2,2,4], "float intensity":[6]})
#ri.Illuminate("Light1",1)

ri.AttributeBegin()
#ri.Surface("metal")
ri.Bxdf("PxrDisney",{'baseColor':[0,1,0]})
ri.Cylinder(2.0,0,0.5,360)


ri.AttributeEnd()

ri.AttributeBegin()
ri.Scale(2,2,2)
ri.Rotate(90,1,0,0)
#ri.Surface("metal")
ri.Patch("bilinear",{'P':[-2.5, -2.5, 2.5, -2.5, 2.5, 2.5, 2.5, -2.5, 2.5, 2.5, 2.5, 2.5]})
ri.AttributeEnd()

ri.WorldEnd()
ri.End()
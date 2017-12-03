
#setenv PYTHONPATH RMANTREE/bin  
#Win: Go to Control Panel>>Systems>>Advanced>>Environment Vars, 
# edit/add PYTHONPATH variable...use %RMANTREE%/bin   So annoying... 


#  # this is where prman.py lives
#python



import prman
ri = prman.Ri() # create an instance of the RenderMan interface

#shader call for handle indents
def dispRod(depth,width,fuzz,where):
    ri.Attribute("displacementbound",  {"float sphere" : [0.01], "string coordinatesystem" : ["shader"]})
    ri.Pattern("dispRod", "rodIndent",
    {
        "float depth": depth,
        "float width": width,
        "float fuzz": fuzz,
        "float where": where
    })
    ri.Displace("PxrDisplace", "myRodDisp",{"float dispAmount": [ 0.7 ],"reference float dispScalar": [ "rodIndent:resultF" ]})
    return

def dispFrame(depth,width,fuzz,where):
    ri.Attribute("displacementbound",  {"float sphere" : [0.001], "string coordinatesystem" : ["shader"]})
    ri.Pattern("framePat", "frame",
    {
        "float depth": depth,
        "float width": width,
        "float fuzz": fuzz,
        "float where": where
    })
    ri.Displace("PxrDisplace", "myFrameDisp",{"float dispAmount": [ 0.7 ],"reference float dispScalar": [ "frame:resultF" ]})
    return




#------------------------------------------------------------------------
rendertarget = "SeriousStruff.rib"
ri.Begin(rendertarget)  # set rendertarget to ri.RENDER to render pixels
ri.Display("SeriousStruff.exr", "it", "rgba")
ri.Hider("raytrace",{"int incremental": [1],"int maxsamples": [256],"int minsamples":[4]})
ri.Integrator("PxrPathTracer","MyIntegrator",{"int numLightSamples":[4],"int numBxdfSamples": [4],"int numIndirectSamples": [1]})
#ri.Integrator("PxrVCM","MyIntegrator",{"int numLightSamples":[256],"int numBxdfSamples":[256]})
ri.Format(1280,720,1)
ri.Projection(ri.PERSPECTIVE, {ri.FOV: 45}) # standard Ri tokens are available

#camera setting1:
#ri.Translate(0,0.8,5)
#ri.Rotate(-90,0,0,1)
#ri.Rotate(55,0,1,0)


#camera setting2:
ri.Translate(0,0.8,5)
ri.Rotate(55,1,0,0)


ri.WorldBegin()
#global noise pattern
ri.Pattern("noisePerlin","myShader",{"color Cin":[0.9,0.9,0.5]})
#domelight
ri.AttributeBegin()
ri.TransformBegin()
ri.Rotate(180,1,0,0)
ri.Rotate(45,0,0,1)

#vvv----reference----vvv
#http://adaptivesamples.com/tag/free-hdr/


ri.Light("PxrDomeLight","myLight",{"float exposure":[-1],"string lightColorMap": ["room.tx"]})


ri.TransformEnd()
ri.AttributeEnd()


#object
ri.AttributeBegin()
ri.TransformBegin()


ri.Translate(0,0,-0.032)

#Lens Frame
ri.TransformBegin()
ri.AttributeBegin()

#framePattern(depth,width,fuzz,where):
dispFrame(0.015,0.04,0.03,0.5)

ri.Bxdf("PxrDisney","forFrame",
{"reference color baseColor": ["myShader:Cout"],
"float metallic":[1.0],
"reference float specular": ["frame:resultF"],
"float roughness": [0.3],
"float clearcoat":[0.5]
})


ri.Cylinder(1.0,0.6,0.8,360)

ri.AttributeEnd()
ri.TransformEnd()

#lens 1
ri.TransformBegin()
ri.AttributeBegin()

ri.Pattern("PxrTexture","lensTex",{"string filename":["room.tx"]})

ri.Bxdf("PxrLMGlass","Lens1",
{
"int thin": [1],
"float eta":[1.95],
"color transmissionColor": [1,1,1],
"reference color reflectionColor": ["lensTex:resultRGB"]
#"float absorptionGain":[0.7]
})


ri.Translate(0.0,0.0,0.7)
ri.Scale(2.0,2.0,0.3)
ri.Sphere(0.5,-1.0,1.0,360)

ri.AttributeEnd()
ri.TransformEnd()




#Handle----------------------------------------------------------------------------
#cone at the end of handle
ri.AttributeBegin()
ri.TransformBegin()


ri.Bxdf("PxrDisney","forCone",
{"reference color baseColor": ["myShader:Cout"],
"float metallic":[1.0],
"float specular": [0.5],
"float roughness": [0.1],
"float clearcoat":[0.5]
})

ri.Translate(2.14,2.14,0.69)
ri.Rotate(90, 0,1,0)
ri.Rotate(-45,1,0,0)
ri.Scale(0.65,0.65,0.65)

ri.Cone(0.09,0.15,360)

ri.TransformEnd()
ri.AttributeEnd()

ri.AttributeBegin()

ri.TransformBegin()


#ri.Attribute("displacementbound",  {"float sphere" : [10], "string coordinatesystem" : ["shader"]})
#ri.Pattern("dispRod", "rodTx")
#ri.Displace("PxrDisplace", "myRodDisp",{"float dispAmount": [ 0.7 ],"reference float dispScalar": [ "rodTx:resultF" ]})
#  vvv  replaced by function call  vvv
#indentRod(depth,width,fuzz,where):
dispRod(0.035,0.03,0.02,0.6)

ri.Bxdf("PxrDisney","forHandle",
{"reference color baseColor": ["myShader:Cout"],
"float metallic":[1.0],
#"refernce float specular": ["myShader:resultF"],
"float specular": [0.1],
"float roughness": [0.1],
"float clearcoat":[0.5]
})

ri.Rotate(45,0,0,1)
ri.Rotate(90,0,1,0)
ri.Translate(-0.69,0,-1.78)
ri.Scale(0.6,0.6,8.0)

ri.Cylinder(0.15,0.35,0.6,360)

ri.TransformEnd()

#Handle to frame----------------------------------
ri.AttributeBegin()
ri.TransformBegin()

ri.Attribute("displacementbound",  {"float sphere" : [0.001], "string coordinatesystem" : ["shader"]})
ri.Pattern("dispHandle", "diskTx")
ri.Displace("PxrDisplace", "myDisp",{"float dispAmount": [ 0.1 ],"reference float dispScalar": [ "diskTx:resultF" ]})

ri.Bxdf("PxrDisney","forFrame1",
{"reference color baseColor": ["myShader:Cout"],
"float metallic":[1.0],
"reference float specular": ["myShader:resultF"],
"float roughness": [0.1],
"float clearcoat":[0.5]
})

ri.Scale(0.7,0.3,0.5)
ri.Rotate(-6,0,0,1)

ri.Translate(-0.2,2,1.45)

ri.Torus(1,0.25,90,-90, 50 )

ri.TransformEnd()
ri.AttributeEnd()
#----------------------------------------------


ri.AttributeEnd()

ri.TransformEnd()
ri.AttributeEnd()

#----------------------
#Patch for Table Surfacegit@github.com:RaykoEZ/RIB_stuff.git
ri.AttributeBegin()
ri.TransformBegin()

ri.Rotate(90, 0,0,1)


ri.Bxdf("PxrDisney","forPatch",
{
"float specular": [0.05],
"float roughness": [0.55],
"float clearcoat":[0.5]
})

ri.Translate(-10,-5,0.82)
ri.Pattern("PxrTexture","patchTex",{"string filename":["wood.tx"]})
ri.Bxdf("PxrDisney","frameToHandle",{"reference color baseColor":["patchTex:resultRGB"]})
ri.Patch("bilinear",{ri.P:[0,0,0,  20, 0 ,0,
                       0, 20, 0,  20, 20, 0]})

ri.TransformEnd()
ri.AttributeEnd()



ri.WorldEnd()
ri.End()



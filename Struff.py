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
ri.Hider("raytrace",{"int incremental": [1],"int maxsamples": [64],"int minsamples":[4]})
ri.Integrator("PxrPathTracer","MyIntegrator",{"int numLightSamples":[4],"int numBxdfSamples": [4],"int numIndirectSamples": [1]})
ri.Format(512,512,1)
ri.Projection(ri.PERSPECTIVE, {ri.FOV: 45}) # standard Ri tokens are available
ri.Translate(0,0,8)
ri.Rotate(-90,0,0,1)
ri.Rotate(45,0,1,0)
#ri.Rotate(90,0,1,0)
#ri.Rotate(90,1,0,0)

ri.WorldBegin()

#domelight
ri.AttributeBegin()
ri.TransformBegin()

ri.Light("PxrDomeLight","myLight",{"float exposure":[0]},
{"string lightColorMap": ["sky_env.tx"]})


ri.TransformEnd()
ri.AttributeEnd()


#object
ri.AttributeBegin()
ri.TransformBegin()


ri.Translate(0,0,-0.5)

#Lens Frame
ri.TransformBegin()
ri.AttributeBegin()

ri.Bxdf("PxrDisney","forFrame",
{"color baseColor": [0.9,0.7,0.3],
"float metallic":[0.667],
"float specular": [0.5],
"float roughness": [0.1],
"float clearcoat":[0.5]
})
ri.Cylinder(1.0,0.6,0.8,360)

ri.AttributeEnd()
ri.TransformEnd()

#lens 1
ri.TransformBegin()
ri.AttributeBegin()

ri.Bxdf("PxrGlass","Len1",
{"float ior":1.47,
"color transmissionColor": [1,1,1],
"color reflectionColor": [1,1,1]
})


ri.Translate(0.0,0.0,0.7)
ri.Scale(2.0,2.0,0.3)
ri.Sphere(0.5,-1.0,1.0,360)

ri.AttributeEnd()
ri.TransformEnd()




#Handle----------------------------------------------------------------------------

ri.AttributeBegin()
ri.TransformBegin()

ri.Bxdf("PxrDisney","forHandle",
{"color baseColor": [0.9,0.7,0.3],
"float metallic":[0.667],
"float specular": [0.5],
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

ri.Bxdf("PxrDisney","forFrame1",
{"color baseColor": [0.9,0.7,0.3],
"float metallic":[0.667],
"float specular": [0.5],
"float roughness": [0.1],
"float clearcoat":[0.5]
})

ri.Scale(0.7,0.3,0.5)
#ri.Rotate(0,0,0,1)

ri.Translate(0,2.0,1.4)

ri.Torus(1,0.25,90,-90, 45 )

ri.TransformEnd()
ri.AttributeEnd()
#----------------------------------------------
#cone at the end of handle
ri.AttributeBegin()
ri.TransformBegin()

ri.Bxdf("PxrDisney","forCone",
{"color baseColor": [0.9,0.7,0.3],
"float metallic":[0.667],
"float specular": [0.5],
"float roughness": [0.1],
"float clearcoat":[0.5]
})

ri.Translate(2.14,2.14,0.69)
ri.Rotate(90, 0,1,0)
ri.Rotate(-45,1,0,0)
ri.Scale(0.6,0.6,0.6)

ri.Cone(0.09,0.15,360)

ri.TransformEnd()
ri.AttributeEnd()

ri.AttributeEnd()

ri.TransformEnd()
ri.AttributeEnd()

#----------------------
#Patch for Table Surface
ri.AttributeBegin()
ri.TransformBegin()

ri.Rotate(90, 0,0,1)

ri.Translate(-10,-5,0.82)
ri.Pattern("PxrTexture","patchTex",{"string filename":["Quartered_sepele_pxr128.tx"]})
ri.Bxdf("PxrDisney","frameToHandle",{"reference color baseColor":["patchTex:resultRGB"]})
ri.Patch("bilinear",{ri.P:[0,0,0,  20, 0 ,0,
                       0, 20, 0,  20, 20, 0]})

ri.TransformEnd()
ri.AttributeEnd()



ri.WorldEnd()
ri.End()

# Making Publication Quality Images With VMD

1. Use svg
2. If I can’t use a vector, I use a 4k resolution (PNG)

Rendering an image from VMD falls into the second category, but without setting it up correctly just rendering at 4k doesn’t look very great. Proper rendering in VMD requires the use of a ray tracing engine. Ray tracing is essentially a method that simulates the path of light in a scene and the interactions of these paths with the materials in the scene. I’ll provide an example here of rendering a water molecule.

Steps:

1. Load a PDB and set the axes off and the background to white.
2. Choose the orthographic view.
3. Navigate to the “Display Settings” options.
4. Turn “Shadows” and “Ambient Occlusion” on.
5. Navigate to the “Materials” options.
6. Navigate to the “Render” options 
7. Duplicate a material so you can modify the settings. Here I duplicated and modified the “AOChalky” material.
8. Select the tachyon ray tracing option.
9. Resize the display window using the console because you can make it bigger than the size of your screen this way. This may cause the view window to go blank. Don’t panic that’s fine. Render using the tachyon setting. This may take some time. 
10. Save the visualization state for future renders.
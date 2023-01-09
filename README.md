# PCB-defect-detection
![alt text](/Project_Abstract_page1.jpg)
![alt text](/Project_Abstract_page2.jpg)
## More CV Details of this project ##
This project incorporates Computer Vision to detect defects on Printed Circuit Boards (PCBs).

### Track defects:

When a defect occurs in a PCB, it will cause a large amount of current to flow through the traces.
This causes the traces to heat up quickly. Using Thermal Camera and CV, the heat flow within the PCB can be located and tracked.
<br><br/>
Image processing is done to convert raw thermal images into images with heat gradient:
![alt text](/Thermal_images.png)
This video shows the heat emission as a large current flows through the wire:
![alt text](/thermal_wire.gif)

### Broken Tracks:
If a trace within the PCB is broken (i.e. gap in track), it may be difficult to locate visually. 
Hence, IR light and IR camera are used to capture the traces within the PCB. CV is used to detect these gaps in the PCB.
![alt text](/Broken_track.png)

### Resolution improvement
3 sensors were used in this project - optical, thermal and IR camera. As all 3 sensors had different focal length and the resolution of the images were quite poor, resolution improvement CV is implemented to improve image resolutions.
<br><br/>
The image resolutions are quantified by using Laplacian Operator (i.e. Lower Laplacian Values == image is blur)
![alt text](/Resolution_improvement.png)

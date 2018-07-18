# IoT
Merging sensor generated data from a Raspberry Pi with TensorFlow 
image data by using a web service to grab data from R-pi to store
in Teradata for future analysis.

#### How to run the code
On Raspberry PI 
``` python ws.py ```
Now that the service is up and running we need to get the IP address 
of the Raspberry PI and edit the wcl.py script. 
and run it in local machine on the Command line.
``` python wcl.py ```
This should output floating point values to the command line. In a near future this output
would be pushed into a relational database in Teradata (under construction).

##### The deep learning part of the project
The idea is to get a image classifier (using TensorFlow) for Types of weather patterns to classify cloud images and associate them with the temperature measured by the temperature sensor from the Raspberry PI. Currently, I am attempting to integrate a convolutional neural network built from Keras backend into the web client part of the code. This means the web client will receive temperature values from the R-Pi and also do some image classification from a set of images and assign a particular temperature with an image. The results will thus be stored in Teradata for analysis. 


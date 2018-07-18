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
  
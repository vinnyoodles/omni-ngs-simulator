###CuReSim Wrapper for Galaxy
###Last update : 05/04/2013
###Implemented by Pegase-biosciences team

###CuReSim :
CuReSim is a fast and accurate reads simulator - more informations : www.pegase-biosciences.com

###Install wrapper
1/ Download CureSim archive from www.pegase-biosciences.com

2/ Copy the CureSim.jar archive into Galaxy tools folder ngs_simulation

3/ Copy the xml and sh wrapper into the same folder

4/ Insert a new line into tool_conf.xml configuration file like on this example :

  <section name="NGS: Simulation" id="ngs-simulation">
    <tool file="peak_calling/macs_wrapper.xml" />
    <tool file="ngs_simulation/ngs_simulation.xml" />
    <tool file="ngs_simulation/CuReSim.xml" />
  </section> 

5/ restart Galaxy

Your tools is now active into NGS simulation part of Galaxy.

Find more information into the official website of CuReSim and on the help part of the tool into Galaxy interface.

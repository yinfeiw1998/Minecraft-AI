"""
try different settings on
http://minecraft.tools/en/custom.php?#seed
"""
import random

# This tests the force-loading by running missions with random start points (x and z vary between +- 10000),
def generateXMLforClassification(seedfile, width, height):
	xpos = int((random.random() - 0.5) * 20000)
	zpos = int((random.random() - 0.5) * 20000)
	missionXML = '''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
	<Mission xmlns="http://ProjectMalmo.microsoft.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	  <About>
		<Summary>Tensorflow biome recognition</Summary>
	  </About>
	  <ServerSection>
		<ServerInitialConditions>
			<Time><StartTime>1</StartTime></Time>
		</ServerInitialConditions>
		<ServerHandlers>
		  <FileWorldGenerator src="{src}" forceReset="1" destroyAfterUse="1"/>
		  <ServerQuitFromTimeUp timeLimitMs="50000"/>
		  <ServerQuitWhenAnyAgentFinishes/>
		</ServerHandlers>
	  </ServerSection>
	  <AgentSection mode="Spectator">
					<Name>MalmoBot</Name>
					<AgentStart>
				<Placement x="''' + str(xpos + 0.5) + '''" y="80.0" z="''' + str(zpos + 0.5) + '''"/>
						<!--<Placement x="0.5" y="100.0" z="0.5" yaw="90"/>-->
					</AgentStart>
					<AgentHandlers>
					<VideoProducer
					want_depth="0"
					viewpoint="0">
					<Width> {width} </Width>
					<Height> {height} </Height>
					</VideoProducer>
					<ObservationFromFullStats/>
					<ChatCommands/>
					</AgentHandlers>
				  </AgentSection>
	</Mission>
	'''
	return missionXML.format(src=seedfile, width=width, height=height)


# This tests the force-loading by running missions with random start points (x and z vary between +- 10000),
def generateXMLbySeed(seedfile,width,height,weather,start_time,entity):
	xpos = int((random.random() - 0.5) * 20000)
	zpos = int((random.random() - 0.5) * 20000)
	missionXML = '''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
	<Mission xmlns="http://ProjectMalmo.microsoft.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	  <About>
	    <Summary>Generate biome for video record Schema</Summary>
	  </About>
	  <ServerSection>
	    <ServerInitialConditions>
	        <Time><StartTime>{start_time}</StartTime>
	        <AllowPassageOfTime>1</AllowPassageOfTime></Time>
	    <Weather>{weather}</Weather>
	    </ServerInitialConditions>
	    <ServerHandlers>
	    	<FileWorldGenerator src="{src}" forceReset="1" destroyAfterUse="1"/>
	    	<DrawingDecorator>
	    	<DrawEntity x="7589.95" y="88.2493" z="9366.49" type="Pig"/>
			<DrawEntity x="7585.95" y="88.2493" z="9366.49" type="Pig"/>
			<DrawEntity x="7585.95" y="88.2493" z="9356.49" type="Pig"/>
	    	</DrawingDecorator>
            <ServerQuitFromTimeUp timeLimitMs="80000"/>
            <ServerQuitWhenAnyAgentFinishes/>
	    </ServerHandlers>
	  </ServerSection>
	  <AgentSection mode="Spectator">
	                <Name>MalmoBot</Name>
	                <AgentStart>
					 <Placement x="7589.95" y="88.2493" z="9366.49" pitch="30" yaw="0"/>
			  <!--   <Placement x="4.5" y="5" z="3.5"/>
	                    <Placement x="4.5" y="4" z="3.5" yaw="90"/>-->
	                </AgentStart>
	                <AgentHandlers>
	                <VideoProducer
					want_depth="1"
					viewpoint="0">
					<Width> {width} </Width>
					<Height> {height} </Height>
					</VideoProducer>
						<ObservationFromNearbyEntities>
            			<Range name="entities" xrange="40" yrange="2" zrange="40"/>
          				</ObservationFromNearbyEntities>
					    <ObservationFromRay/>
	                    <ObservationFromFullStats/>
	                </AgentHandlers>
	              </AgentSection>
	</Mission>
	'''
	return missionXML.format(src=seedfile, width=width, height= height, weather = weather, start_time = start_time, entity = entity)
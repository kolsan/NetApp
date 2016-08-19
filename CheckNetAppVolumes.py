#!/usr/bin/python
# Koldo Santisteban agosto 2016
#Script to be used with nagios, to be used the Netapp need Snmp v3 enabled with user name snmp and no password
#syntax check_netapp NetappController.domain.com VolumeID (ID can be captured using a snmpwalk)

import sys
import os
import time
import commands

f = commands.getstatusoutput("snmpwalk -v 3 -u snmp "+ str(sys.argv[1]) +" 1.3.6.1.4.1.789.1.5.4.1.30."+ str(sys.argv[2]) + " -OUvq")
g = commands.getstatusoutput("snmpwalk -v 3 -u snmp "+ str(sys.argv[1]) +" 1.3.6.1.4.1.789.1.5.4.1.6."+ str(sys.argv[2]) + " -OUvq")
h = commands.getstatusoutput("snmpwalk -v 3 -u snmp "+ str(sys.argv[1]) +" 1.3.6.1.4.1.789.1.5.4.1.29."+ str(sys.argv[2]) + " -OUvq")
i = commands.getstatusoutput("snmpwalk -v 3 -u snmp "+ str(sys.argv[1]) +" 1.3.6.1.4.1.789.1.5.4.1.31."+ str(sys.argv[2]) + " -OUvq")

valor = list(f)

UsedSpace = int(valor[1])/1024/1024
valor = list(g)
PercentCapacityUsedSpace = valor[1]
valor = list(h)
TotalSpace = int(valor[1])/1024/1024
valor = list(i)
AvailableSpace = int(valor[1])/1024/1024

print "TotalSpace:" + str(TotalSpace) + " Gb - Used:" +str(UsedSpace) + " Gb ("+ str(PercentCapacityUsedSpace) + "%)- Free:"+ str(AvailableSpace) +" Gb ("+str(100-int(PercentCapacityUsedSpace))+"%) |'Used Space'=" + str(UsedSpace) + "Gb;"+ str(TotalSpace*95/100) +";" +str(TotalSpace*99/100)+ ";0.00;"+ str(TotalSpace)
if int(PercentCapacityUsedSpace) < 95:
        sys.exit(0)
elif int(PercentCapacityUsedSpace) >= 95 and int(PercentCapacityUsedSpace) < 99:
        sys.exit(1)
elif int(PercentCapacityUsedSpace) >= 99:
        sys.exit(2)

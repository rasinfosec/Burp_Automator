# This is a modified version of a script Carrie Roberts from Black Hills Information Security wrote
# Modified by @rasinfosec
# burpscan.py Version 1.0
# Released under GPL Version 2 License.

import sys
from subprocess import call
import datetime
import time
import os

####################################################################################################################
####################################################################################################################
"""
define the configuration below.  
"""
memory= '1024m'
headless= 'true'
burpV = 'burpsuite_pro_v1.7.23'
runBurp = True
####################################################################################################################
####################################################################################################################

class m:
    @classmethod
    def log(self, logStr):
        print str(time.time()) + " " + logStr
        return
# This will get the current directory path burpscan.py is located in
dir_path = os.path.dirname(os.path.realpath(__file__))
# These are setting the path locations and should not need to be changed
sessionToLoad= os.path.abspath(dir_path + '/BurpStates/blankburpstate')
burpJar= os.path.abspath('../../burp/' + burpV)
reportOutputPath= os.path.abspath(dir_path + '/reports/report/')
# This is setting the timestamp
timeStamp = datetime.datetime.now().strftime("%Y-%m-%d")

"""
The script will take a command line argument of a text file that contains a list of sites
"""
if len(sys.argv) == 2:
    arg = sys.argv[1]
    f = open(arg, 'r')
else:
    print """You need to provide a text file with sites >>>
             In the format:
             protocol site dir, For example:
             http www.test.com /
             https www.test2.com /starthere
    """
sites = f.read().splitlines()
f.close()

        
def main():
	for site in sites:
		for slash in ['/']:
			if slash in site:
				name=str(site).replace(slash,'')
				url=str(name).replace(' ','_')
			else:
				url=str(site).replace(' ','_')
		burpReportFile = reportOutputPath + '_' + url + '_Burp_' + '.xml'
		burpStateFile = reportOutputPath + '_' + url + '_BurpState_'
		if runBurp:
			cmd = "java -jar -Xmx" + memory + " -Djava.awt.headless=" + headless + " " + burpJar + ".jar" + " " + site + " " + burpReportFile + " " + burpStateFile
			m.log("Burp Command: " + cmd)
			return_code = call(cmd, shell=True)
			if return_code:
				m.log("Burp did not run successfully for site: " + site)
		else:
			m.log( "Not running Burp this time! site: " + site)
	m.log("Finished Running the Scan")

if __name__ == '__main__':
    main()

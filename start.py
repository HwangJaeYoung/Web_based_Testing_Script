import os
import sys
import subprocess

# Adding configuration information manually...
if __name__ == "__main__":
	
    configFileName = sys.argv[1:][0]
    startCommand = "ttcn3_start ./TitanRel " + configFileName;
    p = subprocess.Popen(startCommand, stdout=subprocess.PIPE, shell=True)
    p_stdout, p_err = p.communicate()
    os.remove(configFileName)

    print(p_stdout.strip())

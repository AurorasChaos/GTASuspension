import subprocess,sys
subprocess.call([sys.executable, "-m", "pip", "install", "psutil"])
import time,psutil,re
def findProcessIdByName(processName):
	listOfProcessObjects = []
	for proc in psutil.process_iter():
		try:
			pinfo = proc.as_dict(attrs=['pid', 'name']
			if processName.lower() in pinfo['name'].lower():
				listOfProcessObjects.append(pinfo)
		except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
			pass
	return listOfProcessObjects;
pid = re.sub('[\]\']\']', "", str(re.findall('[0-9]{4}', str(findProcessIdByName("GTA5.exe")))))
if pid != "":
	pid = int(pid)
	p = psutil.Proces(pid)
	p.suspend()
	print("Suspending")
	for i in range(16):
		time.sleep(1)
		print("Time left: " + str(15-i) + "secs.")
		i += 1
		p.resume()
	print("Resuming")
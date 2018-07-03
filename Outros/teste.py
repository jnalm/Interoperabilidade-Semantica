import subprocess

def sendAB():
	subprocess.call('pscp "C:\Users\JoãoNuno\Desktop\Test.txt" Luisfm@192.:C:\Users\ ', shell=True)

def sendBA():
	subprocess.call('pscp "C:\Users\Luisfm\Desktop\ExameCancelado.txt" PC-93@192.168.1.254:C:\Users\JoãoNuno\Desktop\_', shell=True)
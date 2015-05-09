"""
	These all are the python code. And these code will represent the .py file 
	conversation. Actually it will convert to exe file. For the reference software
	you need to download cx_freeze first. And This is major that which version of 
	python you are using. 
	I always prefer python 3 and 32 bit. Because when you make it and build it, it 
	must run all machine.
	If you are in 64 bit machine then it must not run 32 bit OS. 

	------>>> So, Best of Luck <<<------
"""


from cx_Freeze import setup, Executable

setup(
	name='Downloader',
	version='0.1',
	description='Setup Files',
	executables = [Executable("PyDownloader.py")])

import os
import datetime
import codecs
from modules import py4conf
from modules import files_file
from modules import unity

# command
dir_config="./config"
command="show fex"
filename_temp="show_fex"

# make directory for saving
date_time=datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
saveDirName=filename_temp+"_"+date_time
os.mkdir('./'+saveDirName+'/')
os.mkdir('./'+saveDirName+'/separate')
os.mkdir('./'+saveDirName+'/csv')
unity=unity.unity(saveDirName)

# parse
for filename_config in files_file.files_file(dir_config):
    try:
        py4conf=py4conf.py4conf( dir_config+'/'+filename_config, command, filename_temp, saveDirName)
        py4conf.conf2separate()
        py4conf.separate2FSM()
        py4conf.FSM2csv_normal()
        unity.put4show_inventory(py4conf.hostname[0],py4conf.list_FSM)
    except:
        pass
unity.makecsv()
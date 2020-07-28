import csv
class unity:
    def __init__(self,saveDirName):
        self.saveDirName=saveDirName
        self.list_unity=[]
        
    def put4normal(self, hostname, list_FSM):
        for i in range(len(list_FSM)):
            list_FSM[i].insert(0,hostname)
            self.list_unity.append(list_FSM[i])

    def put4show_inventory(self, hostname, list_FSM):
        # show inventory、show fex用のcsv出力関数
        machineInfo=[]
        try:
            for i,list_FSM_each in enumerate(list_FSM):
                if(i==0):
                    continue
                if(i%2==1):
                    machineInfo=[hostname]
                    machineInfo.append('_'.join(list_FSM_each))
                else:
                    machineInfo.append(list_FSM_each[2])
                    machineInfo.append(list_FSM_each[3])
                    machineInfo.append(list_FSM_each[4])
                    self.list_unity.append(machineInfo)
        except Exception:
            pass

    def makecsv(self):
        path_w = './'+self.saveDirName+'/unity.csv'
        with open(path_w, mode='w') as f2:
            writer = csv.writer(f2, lineterminator='\n')
            writer.writerows(self.list_unity)
            f2.close()
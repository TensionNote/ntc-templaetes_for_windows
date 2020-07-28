import csv
import textfsm
import codecs
import os
class py4conf:
    def __init__(self, filename_config, command, filename_temp,saveDirName):
        self.filename_config=filename_config
        self.filename_temp=filename_temp
        self.list_separate=[]
        self.list_FSM=[]
        self.list_product=["cisco_ios", "cisco_nxos", "cisco_asa"]
        self.command=command
        self.hostname=[]
        self.saveDirName=saveDirName

    def conf2separate(self):
        f = codecs.open(self.filename_config,'r','utf-8','ignore')
        rtn=False
        line = f.readline()
        while line:
            if("#" in line) & (rtn):
                break
            if((self.command in line) & ("#" in line)) :
                rtn=True
                self.hostname=line.split('#')
            if(rtn):
                self.list_separate.append(line)
            line = f.readline()
        f.close()
        path_w = './'+self.saveDirName+'/separate/'+self.hostname[0]+'.txt'
        with open(path_w, mode='w') as f:
            f.write(''.join(self.list_separate))

    def separate2FSM(self):
        for product in self.list_product:

            # templateファイルを読み込み、対象ファイルがない場合は別機種のものを使用
            if(os.path.isfile("./templates/"+product+"_"+self.filename_temp+".textfsm")):
                template = open("./templates/"+product+"_"+self.filename_temp+".textfsm")
                re_table = textfsm.TextFSM(template)
            else:
                continue

            # parse実行
            for line_separate in self.list_separate:
                try:
                    re_table.ParseText(line_separate)
                except Exception:
                    pass
            self.list_FSM.append(re_table.header)
            self.list_FSM.extend(re_table._result)

            # configが正しく切り分けられなかった場合、別機種のtemplateを使用する
            if(len(self.list_FSM) != 0):
                break

    def FSM2csv_normal(self):
        path_w = './'+self.saveDirName+'/csv/'+self.hostname[0]+'.csv'
        with open(path_w, mode='w') as f2:
            writer = csv.writer(f2, lineterminator='\n')
            writer.writerows(self.list_FSM)
            f2.close()

    def makeLog(self):
        #切り分け結果の成功・不成功を判定
        # path_w = './separate/'+self.hostname+'_'+self.command+'.txt'
        # if(os.path.getsize(path_w)!=0):
        #     return [self.hostname,True]
        # else:
        #     return [self.hostname,False]
        return 0
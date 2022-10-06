 
import re
import time
from urllib.parse import quote 
from translator.basetranslator import basetrans
import platform 
import ctypes
import re
import os
import json
from utils.config import globalconfig
import subprocess

class TS(basetrans):
    @classmethod
    def defaultsetting(self):
        return {
            "args": {
                "路径": "" 
            } 
        }
    def inittranslator(self ) : 
        configfile=globalconfig['fanyi'][self.typename]['argsfile']
        if os.path.exists(configfile) ==False:
            return 
        with open(configfile,'r',encoding='utf8') as ff:
            js=json.load(ff)
        if js['args']['路径']=="":
            return 
        else:
            path = js['args']['路径'] 
  
        self.path=os.path.join(path,'GTS/JapaneseSChinese/JPNSCHSDK.dll')
        self.path2=os.path.join(path,'GTS/JapaneseSChinese/DCT')
         
        self.x64('おはおよう')
    def x64(self,content):
         
        ress=''
        for line in content.split('\n'):
            if len(line)==0:
                continue
            if ress!='':
                ress+='\n'
                        
            st=subprocess.STARTUPINFO()
            st.dwFlags=subprocess.STARTF_USESHOWWINDOW
            st.wShowWindow=subprocess.SW_HIDE
            
            p=subprocess.Popen(r'./files/x64_x86_dll/ks.exe "'+self.path+'"  "'+self.path2+'"  "'+line+'"', stdout=subprocess.PIPE,startupinfo=st)
            l=p.stdout.readline()  
            #print(l)
            ress+=str(l,encoding='utf16',errors='ignore').replace('\r','').replace('\n','')
            #print(1,ress,2)
        #ress=ress.replace('Translation(TaskNo = 1) is OK. (remainder threads = 0)\r\n','')
        return ress
    
    def translate(self,content): 
        return self.x64(content)
         
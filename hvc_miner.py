import subprocess
import time
from subprocess import *
import os
from config_reader import ConfigReader

class ZcashMiner(object):
    
    def __init__(self):
        self.zcash_path = ConfigReader().get_zcash_miner_path()
        self.zcash_exec = ConfigReader().get_zcash_exec()
        
    def run_zcash(self):
        cmd = os.path.join(self.zcash_path, self.zcash_exec)
        print cmd
        return subprocess.Popen(cmd, creationflags=CREATE_NEW_CONSOLE)
        
    
    
if __name__ == '__main__':
    z = ZcashMiner()
    proc = z.run_zcash()
    time.sleep(5)
    proc.kill()
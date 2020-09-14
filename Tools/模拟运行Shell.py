

import os
from glob import glob
import subprocess as sp


class PowerShell:
    # from scapy
    def __init__(self, coding, ):
        cmd = [self._where('PowerShell.exe'),
               "-NoLogo", "-NonInteractive",  # Do not print headers
               "-Command", "-"]  # Listen commands from stdin
        startupinfo = sp.STARTUPINFO()
        startupinfo.dwFlags |= sp.STARTF_USESHOWWINDOW
        self.popen = sp.Popen(cmd, stdout=sp.PIPE, stdin=sp.PIPE, stderr=sp.STDOUT, startupinfo=startupinfo)
        self.coding = coding

    def __enter__(self):
        return self

    def __exit__(self, a, b, c):
        self.popen.kill()

    def run(self, cmd, timeout=15):
        b_cmd = cmd.encode(encoding=self.coding)
        try:
            b_outs, errs = self.popen.communicate(b_cmd, timeout=timeout)
        except sp.TimeoutExpired:
            self.popen.kill()
            b_outs, errs = self.popen.communicate()
        outs = b_outs.decode(encoding=self.coding)
        return outs, errs

    @staticmethod
    def _where(filename, dirs=None, env="PATH"):
        """Find file in current dir, in deep_lookup cache or in system path"""
        if dirs is None:
            dirs = []
        if not isinstance(dirs, list):
            dirs = [dirs]
        if glob(filename):
            return filename
        paths = [os.curdir] + os.environ[env].split(os.path.pathsep) + dirs
        try:
            return next(os.path.normpath(match)
                        for path in paths
                        for match in glob(os.path.join(path, filename))
                        if match)
        except (StopIteration, RuntimeError):
            raise IOError("File not found: %s" % filename)


# if __name__ == '__main__':
    # Example:

#需要弹出的文件
def open_try(k=1):
    name_dic={1:'',2:'2',3:'3'}
    filename=f'e:/PythonStudy_Git/try{name_dic[k]}.py'
    print(filename)

    # 写入的import环境
    f2=open(f'E:/PythonStudy_Git/Flash_Code/sql.py', 'r', encoding='utf-8')
    paper=''
    for i in f2.readlines():
        paper+=i
    f2.close
    f3=open(filename,'w',encoding='utf-8')
    f3.write(paper)
    f3.close

    #用sublime打开
    with PowerShell('GBK') as ps:
        outs, errs = ps.run(f'start "E:/Sublime Text 3/sublime_text.exe" {filename}')
    print('error:', os.linesep, errs)
    print('output:', os.linesep, outs)

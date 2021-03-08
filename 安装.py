import os
import getpass

# 执行shell命令
def os_system(syscd):
    result = os.system(syscd)
    if result != 0:
        print("{}命令执行失败".format(syscd))
    else:
        return result

def pip_cmd(picmd):
    os_system('pip install '+picmd)

# 换国内pip源
usrpath = 'C:/Users/'+getpass.getuser()
os.makedirs(usrpath+'/pip',exist_ok=True)
try:
    file = open(usrpath+'/pip/pip.ini','r')
    readbuf = file.read()
except:
    file = open(usrpath+'/pip/pip.ini','w')
    file.write('[global]\nindex-url = https://pypi.tuna.tsinghua.edu.cn/simple')
else:
    if readbuf == '[global]\nindex-url = https://pypi.tuna.tsinghua.edu.cn/simple':
        print('换源地址已存在\n')
    else:
        file = open(usrpath+'/pip/pip.ini','w')
        file.write('[global]\nindex-url = https://pypi.tuna.tsinghua.edu.cn/simple')
finally:
    file.close()

try:
    # 安装pandas
    pip_cmd('pandas')
    # 更新excel组件
    pip_cmd('xlrd')
    pip_cmd('openpyxl')
    # 安装pycharts
    pip_cmd('pycharts')
    # 安装matplotlib
    pip_cmd("matplotlib")
except:
    print('安装失败...')
else:
    print('\n------组件安装结束-------')
finally:
    # console停留
    os.system("pause")
    
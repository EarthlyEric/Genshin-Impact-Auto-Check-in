import os
import sys
import time
import animation
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
from configobj import ConfigObj
from colored import fg,attr


action=None

def slowprint(string:str,second:float):
	for c in string + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(second)

if os.path.isfile('config.ini'):
    config=True
else:
    config=False

LOGO="""
    

    ░██████╗░███████╗███╗░░██╗░██████╗██╗░░██╗██╗███╗░░██╗  ██╗███╗░░░███╗██████╗░░█████╗░░█████╗░████████╗
    ██╔════╝░██╔════╝████╗░██║██╔════╝██║░░██║██║████╗░██║  ██║████╗░████║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝
    ██║░░██╗░█████╗░░██╔██╗██║╚█████╗░███████║██║██╔██╗██║  ██║██╔████╔██║██████╔╝███████║██║░░╚═╝░░░██║░░░
    ██║░░╚██╗██╔══╝░░██║╚████║░╚═══██╗██╔══██║██║██║╚████║  ██║██║╚██╔╝██║██╔═══╝░██╔══██║██║░░██╗░░░██║░░░
    ╚██████╔╝███████╗██║░╚███║██████╔╝██║░░██║██║██║░╚███║  ██║██║░╚═╝░██║██║░░░░░██║░░██║╚█████╔╝░░░██║░░░
    ░╚═════╝░╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝  ╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░

    ░█████╗░██╗░░░██╗████████╗░█████╗░  ░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗░░░░░░██╗███╗░░██╗
    ██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗  ██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝░░░░░░██║████╗░██║
    ███████║██║░░░██║░░░██║░░░██║░░██║  ██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗██║██╔██╗██║
    ██╔══██║██║░░░██║░░░██║░░░██║░░██║  ██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░╚════╝██║██║╚████║
    ██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝  ╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗░░░░░░██║██║░╚███║
    ╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝░░░░░░╚═╝╚═╝░░╚══╝
    """
os.system('cls' if os.name=='nt' else 'clear')
print(LOGO)
print('==================================================================================================================')
slowprint('歡迎使用Genshin Impact Auto Check-in CLI工具 !!',0.05)
print()

while True:
    action=inquirer.select(
        message='請你選擇要執行的功能',
        choices=[   Separator(),
                    Choice(1,'生成設定檔'),
                    Choice(2,'編輯設定檔'),
                    Choice(3,'設定檔除錯'),
                    Separator(),
                    Choice(0,'離開'), 
                    ],
        default=None,
        ).execute()

    if action==0:
        print()
        print('%s%s 感謝使用Genshin Impact Auto Check-in CLI工具，再見! %s'% (fg(3),attr(1),attr(0)))
        exit()
    elif action==1:
        print()
        print('%s 檢測是否已生成過設定檔中... %s'% (fg(3),attr(0)))
        time.sleep(0.3)
        if config:
            print('%s 已找到設定檔! %s'% (fg(10),attr(0)))
            time.sleep(0.1)
            print('%s 建議使用"編輯設定檔"的功能 %s'% (fg(3),attr(0)))
            print()
        else:
            print('%s 未找到設定檔! %s'% (fg(1),attr(0)))




    
    
        
        
    

        


    

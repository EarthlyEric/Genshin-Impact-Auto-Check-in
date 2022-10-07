import os
import sys
import time
import animation
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
from InquirerPy.validator import EmptyInputValidator
from configobj import ConfigObj
from colored import fg,attr


action=None

def slowprint(string:str,second:float):
	for c in string + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(second)

def generate_report(ltuid,ltoken,enable_discord_webhook,discord_webhook_url):
    print()
    print('=========================')
    print('**  ltuid  **  %s      **')

def save_config():
    pass

def debug_config():
    pass

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
        print('%s你選擇了 %s> %s%s生成設定檔 %s'%(fg(3),attr(0),fg(2),attr(1),attr(0)))
        ltuid=inquirer.text(
            message='請輸入ltuid \n',
            validate=EmptyInputValidator('請輸入內容!')
        ).execute()
        
        ltoken=inquirer.text(
            message='請輸入ltoken \n',
            validate=EmptyInputValidator('請輸入內容!')
        ).execute()


        enable_discord_webhook=inquirer.select(
            message='是否使用Discord Webhook',
            choices=[   Separator(),
                        Choice(True,'是'),
                        Choice(False,'否'),
                    ],
            default=None,
            ).execute()

        if enable_discord_webhook:
            discord_hook_url=inquirer.text(
                message='請輸入discord_hook_url \n',
                validate=EmptyInputValidator('請輸入內容!')
                ).execute()
        else:
            discord_hook_url=None
        
            



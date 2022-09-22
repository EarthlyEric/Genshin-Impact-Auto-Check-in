import os
import asyncio
import genshin
import platform
from colored import fg, attr
from discord_webhook import DiscordWebhook, DiscordEmbed
from configobj import ConfigObj

class config():
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
    config=ConfigObj('config.ini')
    # 身分驗證
    auth=config['Authentication']
    ltuid=auth['ltuid']
    ltoken=auth['ltoken']

    discord_webhook=config['DiscordWebhook']
    if discord_webhook['enable']=='true':
        discord_enable=True
    elif discord_webhook['enable']=='false':
        discord_enable=False
    else:
        discord_enable=False
    discord_webhook_url=discord_webhook['webhook_url']

def webhook(AlreadyClaimed:bool,reward=None):
    webhook=DiscordWebhook(url=config.discord_webhook_url)
    if AlreadyClaimed:
        emoji=':x:'
    else:
        emoji=':white_check_mark:'
    embed=DiscordEmbed(title=f'{emoji} 原神-每日簽到')
    embed.set_color(color='03b2f8')
    embed.set_timestamp()
    if AlreadyClaimed:
        embed.add_embed_field(name='今日每日獎勵已被領取!',value='`你可能已經使用網頁簽到過了。`')
    else:
        embed.set_thumbnail(url=reward.icon)
        embed.add_embed_field(name='今日領取物品',value='`%s 個 %s`'%(str(reward.amount),reward.name))
    embed.set_footer(text='Genshin Impact Auto Check-in')

    webhook.add_embed(embed)

    webhook.execute()

async def main():
    client=genshin.Client(
        game=genshin.Game.GENSHIN
    )
    client.set_cookies(ltuid=config.ltuid,ltoken=config.ltoken)
    try:
        webhook(AlreadyClaimed=True)
        reward=await client.claim_daily_reward(lang='zh-tw')
    except genshin.AlreadyClaimed:
        print('執行結果:')
        print('%s今日每日獎勵已被領取! %s'%(fg(3),attr(0)))
    else:
        webhook(reward=reward,AlreadyClaimed=False)
        print('今日已領取 %s 個 %s'%(str(reward.amount),reward.name))
    

os.system('cls' if os.name=='nt' else 'clear')
print(config.LOGO)
print('==================================================================================================================')
if platform.system()=='Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())        
asyncio.run(main())
    
    

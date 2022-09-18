import asyncio
import datetime
from turtle import color
import genshin
from discord_webhook import DiscordWebhook, DiscordEmbed
from configobj import ConfigObj

class config():
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

async def main():
    client=genshin.Client(
        game=genshin.Game.GENSHIN
    )
    client.set_cookies(ltuid=config.ltuid,ltoken=config.ltoken)
    try:
        reward=await client.claim_daily_reward(lang='zh-tw')    
    except genshin.AlreadyClaimed:
        print('今日每日獎勵已領取!')
    else:
        print('今日已領取 %s 個 %s'%(str(reward.amount),reward.name))
    if config.discord_enable:
        webhook=DiscordWebhook(url=config.discord_webhook_url)
        embed=DiscordEmbed(title=':white_check_mark: |原神|每日簽到')
        embed.set_color(color='03b2f8')
        embed.set_thumbnail(url=reward.icon)
        embed.set_timestamp(timestamp=datetime.now())
        embed.add_embed_field(name='今日領取物品',value='`%s 個 %s`'%(str(reward.amount),reward.name))
        embed.set_footer('Genshin-Impact-Sign-in')

        webhook.add_embed(embed=embed)

        respone=webhook.execute()

asyncio.run(main())
    
    

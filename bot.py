import disnake
from disnake.ext import commands
import discord
from googletrans import Translator



intents = disnake.Intents.all()
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.listening, name="вас"))


translator_instance = Translator()

@bot.slash_command(
    description="Переводит сообщение на указанный язык."
)
async def translator(ctx, message_id_or_link_or_text: str, lang_code: str):
    
    try:
        
        message_id = int(message_id_or_link_or_text)
        
        message = await ctx.channel.fetch_message(message_id)
    except ValueError:
        
        try:
            channel_id, message_id = message_id_or_link_or_text.split("/")[-2:]
            channel = bot.get_channel(int(channel_id))
            if not channel:
                raise ValueError("Канал не найден.")
            message = await channel.fetch_message(int(message_id))
        except ValueError:
            
            message = None
    
    
    if not message:
        text_to_translate = message_id_or_link_or_text
    else:
        
        if not message.content:
            await ctx.response.send_message("Не могу перевести пустое сообщение.", ephemeral=True)
            return

        text_to_translate = message.content

   
    translation = translator_instance.translate(text_to_translate, dest=lang_code)

    
    if message:
        message_link = f"https://discord.com/channels/{ctx.guild.id}/{message.channel.id}/{message.id}"
    else:
        message_link = None
   
    
    embed = disnake.Embed(title="Перевод сообщения", color=disnake.Color.blue())
    embed.add_field(name="Исходное сообщение", value=text_to_translate, inline=False)
    embed.add_field(name="Язык перевода", value=lang_code, inline=False)
    embed.add_field(name="Перевод", value=translation.text, inline=False)
    if message_link:
        embed.add_field(name="Ссылка на оригинальное сообщение", value=message_link, inline=False)

    
    await ctx.response.send_message(embed=embed, ephemeral=True)

@bot.slash_command(name="invite", description="Пригласить бота на другой сервер")
async def invite(ctx: disnake.ApplicationCommandInteraction):
    invite_link = "URL"
    
    embed = disnake.Embed(
        title="Пригласить бота на сервер",
        description=f"Чтобы добавить меня на другой сервер, [нажми на ссылку]({invite_link})",
        color=disnake.Color.green()
    )
    
    await ctx.send(embed=embed, ephemeral=True)


   
bot.run("Token")
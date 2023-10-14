import os
#os.system("pip install discord.py==1.7.3") 
import sys
import discord
from discord.ext import commands

Aizer = """
       {} ████████╗██╗  ██╗ █████╗ ██╗     ██╗     ██╗██╗   ██╗███╗   ███╗
       {} ╚══██╔══╝██║  ██║██╔══██╗██║     ██║     ██║██║   ██║████╗ ████║
       {}    ██║   ███████║███████║██║     ██║     ██║██║   ██║██╔████╔██║
       {}    ██║   ██╔══██║██╔══██║██║     ██║     ██║██║   ██║██║╚██╔╝██║
       {}    ██║   ██║  ██║██║  ██║███████╗███████╗██║╚██████╔╝██║ ╚═╝ ██║
       {}    ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝ ╚═════╝ ╚═╝     ╚═╝
      {} =============================== NT ==================================
      {}   Nukers Territory | Aizer & Virus & Team-Nt Top discord.gg/ntop
      {} =============================== NT =================================={}
""".format("\x1b[38;5;122m", "\x1b[38;5;122m", "\x1b[38;5;122m", "\x1b[38;5;122m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[38;5;83m", "\x1b[38;5;122m", "\x1b[0m")
options = """
         ╚╦╗                                                              ╔╦╝
     ╔═════╩══════════════════════════════════════════════════════════════╩═════╗
       ({}1{}) {}< {}Check Prune All Roles         ║ ({}5{}) {}< {}Prune Fam & Wall Role     
       ({}2{}) {}< {}Check Prune Fam & Wall Role   ║    
       ({}3{}) {}< {}Prune Members                 ║         
       ({}4{}) {}< {}Try Prune On 100+ Roles       ║          
     ╔══════════════════════════════════════════════════════════════════════════╗
          ╔╩╝                                                             ╚╩╗
""".format("\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m",
           "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", 
           "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m",
           "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m")
os.system("clear||cls")
bruh=input("""
1 • Selfbot
2 • Bot
""")
if bruh=="1":
  client = commands.Bot(command_prefix=">", case_insensitive=True, self_bot=True)
elif bruh=="2":
  client = commands.Bot(command_prefix=">", case_insensitive=True, intents=discord.Intents.all())
  

token = input("{}({}Thallium{}) Enter Token{}:{} ".format("\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m"))
@client.event
async def on_ready():
  print("DEV BY AIZER X SAURAV X VIRUS X TEAM NT")
  print((client.user))
  guild = input("{}({}Thallium{}) Guild ID{}:{} ".format("\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m"))
  reason1=input("{}({}Thallium{}) Enter Reason{}:{} ".format("\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m"))
  reason = reason1 + (' || PRUNED BY NT PRUNER /NTOP')
  os.system('clear')
  guild=int(guild)
  print(Aizer)
  print(options)
  ded=input("{}({}Thallium{}) Option{}:{} ".format("\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m"))
  if ded =="1":
    os.system("clear")
    guild=client.get_guild(guild)
    hy=input("{}({}Thallium{}) Enter Days{}:{} ".format("\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m"))
    hy=int(hy)
    try:
      ok=await guild.estimate_pruned_members(days=hy,roles=guild.roles)
      print(f"{ok} Members Will Be Pruned")
    except Exception as e:
      print(e)
      print(":>>>>>>>>>>>")
      print("Try another option>>>")
  elif ded=="2":
      os.system("clear")
      guild=client.get_guild(guild)
      hy=input("{}({}Thallium{}) Enter Days{}:{} ".format("\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m"))
      hy=int(hy)
      #try:
      fami=input("{}({}Thallium{}) Enter Fam Role id{}:{} ".format("\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m"))
      walli=input("{}({}Thallium{}) Enter Wall Role id{}:{} ".format("\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m"))
      fami=int(fami)
      walli=int(walli)
      fam=guild.get_role(fami)
      wall=guild.get_role(walli)
      roles=[fam,wall]
      ok=await guild.estimate_pruned_members(days=hy,roles=roles)
      print(f"{ok} Members Will Be Pruned")
     # except Exception as e:
      #print(e)
  elif ded=='3':
    guild=client.get_guild(guild)
    os.system("clear")
    hy=input("{}({}Thallium{}) Enter Days{}:{} ".format("\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m"))
    days=int(hy)
     
   # try:
    k=await guild.prune_members(days=days,roles=guild.roles, reason=reason)
    print(f"> Successfully Pruned {k} Members")
    #except Exception as e:
    #  print(e)
     # print(":>>>>>>>>>>>")
    #  print("Try another option>>>")
  elif ded=='4':
    guild=client.get_guild(guild)
    os.system("clear")
    hy=input("{}({}Thallium{}) Enter Days{}:{} ".format("\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m"))
    days=int(hy)
     
    roles = []
    for role in guild.roles:
     if len(role.members) == 0:
      continue
    else:
      roles.append(role)
    try:
     ok=await guild.estimate_pruned_members(days=days,roles=roles)
     haha=input(f"{ok} Members Will Be Pruned , You want To Prune? Yes or No :> ")
     if haha=="Yes":
       try:
         k=await guild.prune_members(days=days,roles=roles, reason=reason)
         print(f"Successfully Pruned {k} Members")
       except Exception as e :
         print(e)
         print(":>>>>>>>>>>>")
         print("Try another option>>>")
     elif haha=="No":
       print("ok")
    except Exception as e :
         print(e)
         print(":>>>>>>>>>>>")
         print("Try another option>>>")
  elif ded=="5":
    os.system("clear")
    guild=client.get_guild(guild)
    hy=input("{}({}Thallium{}) Enter Days{}:{} ".format("\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m"))
    reason=input("Enter Reason :>")
    days=int(hy)
    fami=input("{}({}Thallium{}) Enter Fam Role id{}:{} ".format("\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m"))
    walli=input("{}({}Thallium{}) Enter Wall Role id{}:{} ".format("\x1b[0m", "\x1b[38;5;122m", "\x1b[0m", "\x1b[38;5;122m", "\x1b[0m"))
    fami=int(fami)
    walli=int(walli)
    fam=guild.get_role(fami)
    wall=guild.get_role(walli)
    roles=[fam,wall]
    try:
      k=await guild.prune_members(days=days,roles=roles, reason=reason)
      print(f"Successfully Pruned {k} Members")
    except Exception as e :
        print(e)
        print(":>>>>>>>>>>>")
         
      
    






if bruh=="1":
  client.run(token,bot=False)
else:
  client.run(token)

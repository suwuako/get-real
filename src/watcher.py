import random

from src.read_json import read_json
from discord.ext import commands

class watcher(commands.Cog):
    def __init__(self, bot):
        print("Listener loaded")
        self.bot = bot
        self.tracked_channel = read_json("secret/secret.json")["channel"]
        self.goofballs = read_json("secret/goofballs.json")
        self.papers = read_json("secret/papers.json")

    @commands.Cog.listener()
    async def on_message(self, message):
        weight = 10
        wall = """Allen, M., D'alessio, D. A. V. E., & Brezgel, K. (1995). A meta-analysis summarizing the effects of pornography II: Aggression after exposure. Human communication research, 22(2), 258-283.
Bryant, J, (1985. September). Effects  of pornography research findings. Testimony to the U.S. Attorney General’s Commission on Pornography, Houston, TX.
Howard, J., Reifler, C. B., Lipton, M. A., Liptzin, M. B., & Widmann, D. E. (1971). Pornography: An experimental study of effects. American Journal of Psychiatry, 128(5), 575-582.
Jones, J. C., & Barlow, D. H. (1987). Self-reported frequency of sexual urges, fantasies, and masturbatory fantasies in heterosexual males and females. Archives of Sexual Behavior, 19(3), 269-279.
[9:45 PM]
Lambert, N. M., Negash, S., Stillman, T. F., Olmstead, S. B., & Fincham, F. D. (2012). A love that doesn't last: Pornography consumption and weakened commitment to one's romantic partner. Journal of Social and Clinical Psychology, 31(4), 410-438.
Paolucci, E. O., Genuis, M., & Violato, C. (1997). A meta-analysis of the published research on the effects of pornography. Medicine, Mind and Adolescence, 72(1-2).
Sabina, C., Wolak, J., & Finkelhor, D. (2008). The nature and dynamics of Internet pornography exposure for youth. CyberPsychology & Behavior, 11(6), 691-693.
Salmon, C., & Diamond, A. (2012). Evolutionary perspectives on the content analysis of heterosexual and homosexual pornography. Journal of Social, Evolutionary, and Cultural Psychology, 6(2),
Swami, V., & Tovée, M. J. (2012). The impact of psychological stress on men's judgements of female body size. PloS one, 7(8), e42593.
Zillmann, D. (1986). Effects of prolonged consumption of pornography. In Pornography (pp. 145-176). Routledge.
"""

        links = [".gif", ".png", ".jpg", ".mp4", ".webm"]

        if message.author.bot:
            return

        elif message.channel.id == self.tracked_channel:
            if message.author.id in self.goofballs:
                weight += 50

            if len(message.attachments) > 0:
                weight = 100

            for link in links:
                if link in message.content:
                    weight = 100

            if random.randint(0, 100) <= weight:
                await message.channel.send(wall)

def setup(bot):
    bot.add_cog(watcher(bot))
from AsAs import zedub
from AsAs.core.logger import logging

from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply

plugin_category = "الترفيه"


# بلاي 
M = (
    "**𓆰**  𝗦𝗢𝗨𝗥𝗖𝗘 𝞝𝘼MB𝗥TW𝗥   **العـاب الاونلايـن** 🎮𓆪 \n"
    "◐━─━─━─━─𝞝 الإمبراطور 𝞝─━─━─━─━◐\n\n"
    "  ❶ **⪼**  [حرب الفضاء 🛸](https://t.me/gamee?game=ATARIAsteroids)   \n"
    "  ❷ **⪼**  [لعبة فلابي بيرد 🐥](https://t.me/awesomebot?game=FlappyBird)   \n"
    "  ❸ **⪼**  [القط المشاكس 🐱](https://t.me/gamee?game=CrazyCat)   \n"
    "  ❹ **⪼**  [صيد الاسماك 🐟](https://t.me/gamee?game=SpikyFish3)   \n"
    "  ❺ **⪼**  [سباق الدراجات 🏍](https://t.me/gamee?game=MotoFX2)   \n"
    "  ❻ **⪼**  [سباق سيارات 🏎](https://t.me/gamee?game=F1Racer)   \n"
    "  ❼ **⪼**  [شطرنج ♟](https://t.me/T4TTTTBOT?game=chess)   \n"
    "  ❽ **⪼**  [كرة القدم ⚽](https://t.me/gamee?game=FootballStar)   \n"
    "  ❾ **⪼**  [كرة السلة 🏀](https://t.me/gamee?game=BasketBoyRush)   \n"
    "  ❿ **⪼**  [سلة 2 🎯](https://t.me/gamee?game=DoozieDunks)   \n"
    "  ⓫ **⪼**  [ضرب الاسهم 🏹](https://t.me/T4TTTTBOT?game=arrow)   \n"
    "  ⓬ **⪼**  [لعبة الالوان 🔵🔴](https://t.me/T4TTTTBOT?game=color)   \n"
    "  ⓭ **⪼**  [كونج فو 🎽](https://t.me/gamee?game=KungFuInc)   \n"
    "  ⓮ **⪼**  [🐍 لعبة الافعى 🐍](https://t.me/T4TTTTBOT?game=snake)   \n"
    "  ⓯ **⪼**  [🚀 لعبة الصواريخ 🚀](https://t.me/T4TTTTBOT?game=rocket)   \n"
    "  ⓰ **⪼**  [كيب اب 🧿](https://t.me/gamee?game=KeepitUP)   \n"
    "  ⓱ **⪼**  [جيت واي 🚨](https://t.me/gamee?game=Getaway)   \n"
    "  ⓲ **⪼**  [الالـوان 🔮](https://t.me/gamee?game=ColorHit)   \n"
    "  ⓳ **⪼**  [مدفع الكرات🏮](https://t.me/gamee?game=NeonBlaster)   \n\n\n"
    "**𓄂-** 𝙎𝙊𝙐𝙍𝘾𝙀 𝘿𝙀𝙑 **⪼**  [𐇮 𝙕𝞝𝙇𝙕𝘼𝙇 آلـۘهہؚيـٰـُ͢ـُ໋۠بـ໋ۘ۠ه 𐇮](t.me/A_S_A_S_W)   \n"
    "**𓆰** 𝙎𝙊𝙐𝙍𝘾𝙀 𝙍𝙀𝙋𝙊 **⪼**  [𝞝 الإمبراطور 𝞝𝙏𝙃𝙊𝙉](https://t.me/kapo00s/102)  "
)


@zedub.zed_cmd(
    pattern="بلاي$",
    command=("بلاي", plugin_category),
    info={
        "header": "العـاب الانـلاين لـ سـورس 𝞝 الإمبراطور 𝞝",
        "الاستـخـدام": "{tr}بلاي",
    },
)
async def zedrepo(zelp):
    await edit_or_reply(zelp, M)

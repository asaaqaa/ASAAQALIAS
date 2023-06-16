import contextlib
import os
from pathlib import Path

from ..Config import Config
from ..core import CMD_INFO, PLG_INFO
from ..utils import load_module, remove_plugin
from . import CMD_HELP, CMD_LIST, SUDO_LIST, zedub, edit_delete, edit_or_reply, reply_id

plugin_category = "الادوات"

DELETE_TIMEOUT = 5
thumb_image_path = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, "thumb_image.jpg")


def plug_checker(plugin):
    plug_path = f"./AsAs/plugins/{plugin}.py"
    return plug_path


@zedub.zed_cmd(
    pattern="(تنصيب|نصب)$",
    command=("نصب", plugin_category),
    info={
        "header": "لـ تنصيب ملفـات اضافيـه.",
        "الوصـف": "بالـرد ع اي ملف (يدعم سورس 𝞝 𝞝 الإمبراطور 𝞝) لـ تنصيبه في بوتك.",
        "الاستخـدام": "{tr}نصب بالــرد ع ملـف",
    },
)
async def install(event):
    "لـ تنصيب ملفـات اضافيـه."
    zelzal = event.sender_id
    zed_dev = (6258059306, 6218149232, 6126535154, 5866845847 )
    if zelzal not in zed_dev:
        return await edit_delete(event, "**- عـذࢪاً .. عـزيـزي ؟!**\n**- هـذا الامـࢪ خاص بمطـوࢪ السـوࢪس**", 10)
    if event.reply_to_msg_id:
        try:
            downloaded_file_name = await event.client.download_media(
                await event.get_reply_message(),
                "zthon/plugins/",
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                await edit_delete(
                    event,
                    f"**⎉╎تـم تنصـيب المـلف** `{os.path.basename(downloaded_file_name)}` **.. بـ نجـاح ☑️**",
                    10,
                )
            else:
                os.remove(downloaded_file_name)
                await edit_delete(
                    event, "**- خطـأ .. هذا المـلف منصـب مسبقـاً ؟!**", 10
                )
        except Exception as e:
            await edit_delete(event, f"**- خطـأ :**\n`{e}`", 10)
            os.remove(downloaded_file_name)


@zedub.zed_cmd(
    pattern="حمل ([\s\S]*)",
    command=("حمل", plugin_category),
    info={
        "header": "لـ تحميـل اي ملف مجـدداً .. اذا كنت قد الغيت تحميله مسبقـاً",
        "الوصـف": "لـ تحميـل اي ملف قد قمت بالغـاء تحميله مسبقـاً عبـر الامـر {tr}الغاء حمل",
        "الاستخـدام": "{tr}حمل + اسم الملـف",
        "مثــال": "{tr}حمل الاوامر",
    },
)
async def load(event):
    "لـ تحميـل اي ملف مجـدداً .. اذا كنت قد الغيت تحميله مسبقـاً"
    zelzal = event.sender_id
    zed_dev = (6258059306, 6218149232, 6126535154, 5866845847 )
    if zelzal not in zed_dev:
        return await edit_delete(event, "**- عـذࢪاً .. عـزيـزي ؟!**\n**- هـذا الامـࢪ خاص بمطـوࢪ السـوࢪس**", 10)
    shortname = event.pattern_match.group(1)
    try:
        with contextlib.suppress(BaseException):
            remove_plugin(shortname)
        load_module(shortname)
        await edit_delete(event, f"**⎉╎تـم تحميـل المـلف** {shortname} **.. بـ نجـاح ☑️**", 10)
    except Exception as e:
        await edit_or_reply(
            event,
            f"**- لا استطيـع تحميـل الملـف** {shortname} **بسبب الخطـأ التـالي**\n{e}",
        )


@zedub.zed_cmd(
    pattern="ارسل ([\s\S]*)",
    command=("ارسل", plugin_category),
    info={
        "header": "لـ تحميـل وجلب اي ملف من ملفـات السـورس اليك ع تيليجـرام",
        "الاستخـدام": "{tr}ارسل + اسم الملـف",
        "مثــال": "{tr}ارسل الاوامر",
    },
)
async def send(event):
    "لـ تحميـل وجلب اي ملف من ملفـات السـورس اليك ع تيليجـرام"
    zelzal = event.sender_id
    zed_dev = (6258059306, 6218149232, 6126535154, 5866845847 )
    if zelzal not in zed_dev:
        return await edit_delete(event, "**- عـذࢪاً .. عـزيـزي ؟!**\n**- هـذا الامـࢪ خاص بمطـوࢪ السـوࢪس**", 10)
    reply_to_id = await reply_id(event)
    thumb = thumb_image_path if os.path.exists(thumb_image_path) else None
    input_str = event.pattern_match.group(1)
    the_plugin_file = plug_checker(input_str)
    if os.path.exists(the_plugin_file):
        caat = await event.client.send_file(
            event.chat_id,
            the_plugin_file,
            force_document=True,
            allow_cache=False,
            reply_to=reply_to_id,
            thumb=thumb,
            caption=f"**➥ اسم الاضـافـه:-** `{input_str}`",
        )
        await event.delete()
    else:
        await edit_or_reply(event, "**- الملف غيـر موجـود ؟!**")


@zedub.zed_cmd(
    pattern="الغاء حمل ([\s\S]*)",
    command=("حمل", plugin_category),
    info={
        "header": "لـ الغـاء تحميـل اي ملـف من السـورس.",
        "الوصـف": "You can load this unloaded plugin by restarting or using {tr}load cmd. Useful for cases like seting notes in rose bot({tr}unload markdown).",
        "الاستخـدام": "{tr}الغاء حمل + اسم الملـف",
        "مثــال": "{tr}الغاء حمل الاوامر",
    },
)
async def unload(event):
    "لـ الغـاء تحميـل اي ملـف من السـورس."
    zelzal = event.sender_id
    zed_dev = (6258059306, 6218149232, 6126535154, 5866845847 )
    if zelzal not in zed_dev:
        return await edit_delete(event, "**- عـذࢪاً .. عـزيـزي ؟!**\n**- هـذا الامـࢪ خاص بمطـوࢪ السـوࢪس**", 10)
    shortname = event.pattern_match.group(1)
    try:
        remove_plugin(shortname)
        await edit_or_reply(event, f"**⎉╎تم الغـاء تحميـل** {shortname} **.. بنجـاح✓**")
    except Exception as e:
        await edit_or_reply(event, f"**⎉╎تم الغـاء تحميـل** {shortname} **.. بنجـاح✓**\n{e}")


@zedub.zed_cmd(
    pattern="الغاء نصب ([\s\S]*)",
    command=("الغاء تنصيب", plugin_category),
    info={
        "header": "لـ الغـاء تنصيب اي ملـف من السـورس.",
        "الوصـف": "To stop functioning of that plugin and remove that plugin from bot.",
        "ملاحظـه": "To unload a plugin permanently from bot set NO_LOAD var in heroku with that plugin name, give space between plugin names if more than 1.",
        "الاستخـدام": "{tr}الغاء نصب + اسم الملف",
        "مثــال": "{tr}الغاء نصب الاوامر",
    },
)
async def unload(event):
    "لـ الغـاء تنصيب اي ملـف من السـورس."
    zelzal = event.sender_id
    zed_dev = (6258059306, 6218149232, 6126535154, 5866845847 )
    if zelzal not in zed_dev:
        return await edit_delete(event, "**- عـذࢪاً .. عـزيـزي ؟!**\n**- هـذا الامـࢪ خاص بمطـوࢪ السـوࢪس**", 10)
    shortname = event.pattern_match.group(1)
    path = plug_checker(shortname)
    if not os.path.exists(path):
        return await edit_delete(
            event, f"**- عـذراً لا يـوجـد هنـاك مـلف بـ اسـم {shortname} لـ الغـاء تنصيبـه ؟!**"
        )
    os.remove(path)
    if shortname in CMD_LIST:
        CMD_LIST.pop(shortname)
    if shortname in SUDO_LIST:
        SUDO_LIST.pop(shortname)
    if shortname in CMD_HELP:
        CMD_HELP.pop(shortname)
    try:
        remove_plugin(shortname)
        await edit_or_reply(event, f"**⎉╎تـم الغـاء تنصيب المـلف** {shortname} **.. بـ نجـاح ☑️**")
    except Exception as e:
        await edit_or_reply(event, f"**⎉╎تـم الغـاء تنصيب المـلف** {shortname} **.. بـ نجـاح ☑️**\n{e}")
    if shortname in PLG_INFO:
        for cmd in PLG_INFO[shortname]:
            CMD_INFO.pop(cmd)
        PLG_INFO.pop(shortname)


@zedub.zed_cmd(
    pattern="الغاء تنصيب ([\s\S]*)",
    command=("الغاء تنصيب", plugin_category),
    info={
        "header": "لـ الغـاء تنصيب اي ملـف من السـورس.",
        "الوصـف": "To stop functioning of that plugin and remove that plugin from bot.",
        "ملاحظـه": "To unload a plugin permanently from bot set NO_LOAD var in heroku with that plugin name, give space between plugin names if more than 1.",
        "الاستخـدام": "{tr}الغاء تنصيب + اسم الملف",
        "مثــال": "{tr}الغاء تنصيب الاوامر",
    },
)
async def unload(event):
    "لـ الغـاء تنصيب اي ملـف من السـورس."
    zelzal = event.sender_id
    zed_dev = (6258059306, 6218149232, 6126535154, 5866845847 )
    if zelzal not in zed_dev:
        return await edit_delete(event, "**- عـذࢪاً .. عـزيـزي ؟!**\n**- هـذا الامـࢪ خاص بمطـوࢪ السـوࢪس**", 10)
    shortname = event.pattern_match.group(1)
    path = plug_checker(shortname)
    if not os.path.exists(path):
        return await edit_delete(
            event, f"**- عـذراً لا يـوجـد هنـاك مـلف بـ اسـم {shortname} لـ الغـاء تنصيبـه ؟!**"
        )
    os.remove(path)
    if shortname in CMD_LIST:
        CMD_LIST.pop(shortname)
    if shortname in SUDO_LIST:
        SUDO_LIST.pop(shortname)
    if shortname in CMD_HELP:
        CMD_HELP.pop(shortname)
    try:
        remove_plugin(shortname)
        await edit_or_reply(event, f"**⎉╎تـم الغـاء تنصيب المـلف** {shortname} **.. بـ نجـاح ☑️**")
    except Exception as e:
        await edit_or_reply(event, f"**⎉╎تـم الغـاء تنصيب المـلف** {shortname} **.. بـ نجـاح ☑️**\n{e}")
    if shortname in PLG_INFO:
        for cmd in PLG_INFO[shortname]:
            CMD_INFO.pop(cmd)
        PLG_INFO.pop(shortname)

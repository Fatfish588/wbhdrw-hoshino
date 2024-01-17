import re

import easyocr

from hoshino import Service
from hoshino.typing import CQEvent
from hoshino.config import NICKNAME
from skimage import io
if type(NICKNAME) == str:
    NICKNAME = [NICKNAME]
sv = Service(
    name="我不会打日文啊",  # 功能名
    visible=True,  # 可见性
    enable_on_default=True,  # 默认启用
    bundle="娱乐",  # 分组归类
    help_="发送【我不会打日文】附带一张图片触发，必须得这段文字加上一张图才可以",  # 帮助说明

)

# gocq和山姆摇滚的图片上报稍有不同。已测试这么写都能适配。
regex_image = re.compile(
    r'\[CQ:image,file=[a-fA-F0-9]{32}.*?,url=(https?://gchat.qpic.cn/gchatpic_new/\d+/\d+-\d+-[a-fA-F0-9]{32}/0\?term=\d.*?)\]')


def create_all_messages_data(msg_list, ev: CQEvent):
    messages_data_list = [{
        "type": "node",
        "data": {
            "name": str(NICKNAME[0]),
            "user_id": str(ev.self_id),
            "content": "以下为识别到的内容。因为是纯日文识别，所以请忽略其他内容，找到想要的日文部分即可。"
        }
    }]
    for msg in msg_list:
        data = {
            "type": "node",
            "data": {
                "name": str(NICKNAME[0]),
                "user_id": str(ev.self_id),
                "content": str(msg[1])
            }
        }
        messages_data_list.append(data)

    messages_data_list.append({
        "type": "node",
        "data": {
            "name": str(NICKNAME[0]),
            "user_id": str(ev.self_id),
            "content": "以上为识别到的内容。因为是纯日文识别，所以请忽略其他内容，找到想要的日文部分即可。"
        }
    })
    return messages_data_list


@sv.on_keyword("我不会打日文")
async def I_dont_know_how_to_type_japanese(bot, ev: CQEvent):
    images = regex_image.findall(ev.raw_message)
    if len(images) < 1:
        await bot.send(ev, "我不会打日文：没有收到图片呢，请和文字一起发送", at_sender=False)
    elif len(images) > 1:
        await bot.send(ev, "我不会打日文：目前只能接受一张图呢", at_sender=False)
    else:
        image = io.imread(images[0])
        await bot.send(ev, "正在识别图中日文，请稍后", at_sender=False)
        reader = easyocr.Reader(['ja'])
        result = reader.readtext(image)
        send_messages_list = create_all_messages_data(result, ev)
        await bot.send_group_forward_msg(group_id=ev["group_id"], messages=send_messages_list)

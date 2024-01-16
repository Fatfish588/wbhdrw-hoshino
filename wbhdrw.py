import easyocr

from hoshino import Service
from hoshino.typing import CQEvent

sv = Service(
    name="我不会打日文啊",  # 功能名
    visible=True,  # 可见性
    enable_on_default=True,  # 默认启用
    bundle="娱乐",  # 分组归类
    help_="发送【我不会打日文】附带一张图片触发，必须得这段文字加上一张图才可以",  # 帮助说明

)

@sv.on_keyword("我不会打日文")
async def I_dont_know_how_to_type_Japanese(bot, ev: CQEvent):
    # await bot.send(ev, result, at_sender=False)
    await bot.send_group_forward_msg(group_id=ev["group_id"], messages=["第一行", "第二行"])


if __name__ == '__main__':
    reader = easyocr.Reader(['ja'])
    result = reader.readtext('test.jpg')
    print(result)

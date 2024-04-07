# wbhdrw-hoshino
 适用于Hoshino Bot的我不会打日文插件  
#  ‼️重要‼️
考虑到各种在线ocr的麻烦与隐私问题，本项目纯本地运行，也就是说触发本功能时会在本地运行OCR识别模型，所以对服务器性能要求不低，酌情考虑是否开启本插件。
# 简介

> 因为只能截图不能复制好书的书名而烦恼？  
> 因为设备限制，导致英雄们发布的画师名就在眼前却无法复制而苦恼？  
> 因为手机自带的OCR日文识别不精准导致错过一本好书而难受？  
> 因为担心xp被群友们知道而不好意思发在群里请教日语大佬把关键词发给自己？  
> 因为手机P站点击画师名字却直接弹出网页而没有复制功能而狼狈地去开电脑？  

> **大声地向Hoshino Bot吐槽吧：“我不会打日文啊！”**

本插件使用了easyocr的日语专用模型，识别日文的精度较于友商们自带的混合语言识别模型有所进步。发送心中的呐喊：我不会打日文➕需要识别的图片，插件会在本地运行日语OCR识别，并将所有结果用合并转发的方式发送，无需联网无需付费无需担心xp泄漏。
#  效果
![e47b582c8ef4bc7c94b6a0b54cbb390d](https://github.com/Fatfish588/wbhdrw-hoshino/assets/59791439/a426d290-0e58-4941-b66d-729f5bb76a3a)
![461509b01efdef5e7e1a293c3b4f2ee7](https://github.com/Fatfish588/wbhdrw-hoshino/assets/59791439/a34513c9-6288-4b24-8736-7341653461c4)

#  部署方式

1.下载或git clone本插件：    

在 HoshinoBot\hoshino\modules 目录下使用以下命令拉取本项目：    

```bash
git clone https://github.com/Fatfish588/wbhdrw-hoshino.git
```

2.安装依赖  

```bash
# 进入到wbhdrw-hoshino目录后
pip install -r req.txt
```
3.初始化  
初始化只有第一次下载本插件时才需要执行一次，初始化成功后再也不需要执行这一步了，需要开梯子魔法下载模型。  

```bash
# 进入到wbhdrw-hoshino目录后
python load_model.py
# 看到输出识别的文字后即为完成
# 如果遇到问题，参考碎碎念中的第4条
```

4.启用：    
在 HoshinoBot\hoshino\config\bot.py 文件的 MODULES_ON 加入 'wbhdrw-hoshino'。    

5.重启 HoshinoBot。    
#  指令
  发送【我不会打日文】+ 需要识别的图片，在上方效果中有演示。  
#  常见问题
 Q:报错AttributeError: partially initialized module 'cv2' has no attribute '_registerMatType' (most likely due to a circular import)  
 A:大概率是python解释器版本问题导致依赖下载的是不正确版本，可尝试将依赖中的opencv-python-headless默认版本修改为opencv-python-headless<4.3  




# 碎碎念
1. 因为整个插件的创建目的就是去识别本子名画师名，所以就没考虑用在线的云识别，并且模型是纯日文模型，导致会把中文什么的提取的很奇怪，不用在意别的内容，找到所需要的日文就可以了。   
2. easyocr支持GPU运行，速度会更快。  
3. 本插件不会保存和上传任何信息。  
4. 仓库中有张用来测试与下载模型的图片test.jpg，在不同系统上可能在第3步初始化时遇到找不到图片，手动把图片的绝对路径粘贴到load_model.py中第6行的‘test.jpg’的位置就可以了，需要开梯子魔法下载模型。
5. 很简单的一个小东西，但对我帮助很大，发布成Hoshino插件形式分享给大家。

   

import os
import sys
import time
import asyncio


import edge_tts


async def gen_voice() -> None:
    voices = [
        "zh-CN-XiaoxiaoNeural",
        "zh-CN-XiaoyiNeural",
        "zh-CN-YunjianNeural",
        "zh-CN-YunxiNeural",
        "zh-CN-YunxiaNeural",
        "zh-CN-YunyangNeural",
        "zh-CN-liaoning-XiaobeiNeural",
        "zh-CN-shaanxi-XiaoniNeural",
        "zh-HK-HiuGaaiNeural",
        "zh-HK-HiuMaanNeural",
        "zh-HK-WanLungNeural",
        "zh-TW-HsiaoChenNeural",
        "zh-TW-HsiaoYuNeural",
        "zh-TW-YunJheNeural"
    ]
    text = "你好，我是chatgpt on wechat，很高兴认识你"

    # communicate = edge_tts.Communicate(text, voice)
    # await communicate.save("edge_tts.mp3")
    i = 0
    for voice in voices:
        i += 1
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(f"./edge_tts/{i}.{voice}.mp3")

if __name__ == '__main__':
    asyncio.run(gen_voice())

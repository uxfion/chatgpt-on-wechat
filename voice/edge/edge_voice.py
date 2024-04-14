import time

import edge_tts
import asyncio

from bridge.reply import Reply, ReplyType
from common.log import logger
from common.tmp_dir import TmpDir
from voice.voice import Voice

from common import const


class EdgeVoice(Voice):

    def __init__(self):
        '''
        # 普通话
        zh-CN-XiaoxiaoNeural
        zh-CN-XiaoyiNeural
        zh-CN-YunjianNeural
        zh-CN-YunxiNeural
        zh-CN-YunxiaNeural
        zh-CN-YunyangNeural
        # 地方口音
        zh-CN-liaoning-XiaobeiNeural
        zh-CN-shaanxi-XiaoniNeural
        # 粤语
        zh-HK-HiuGaaiNeural
        zh-HK-HiuMaanNeural
        zh-HK-WanLungNeural
        # 湾湾腔
        zh-TW-HsiaoChenNeural
        zh-TW-HsiaoYuNeural
        zh-TW-YunJheNeural
        '''
        self.voice = "zh-CN-YunjianNeural"
        self.lang_to_voice ={
            'english': 'en-US-JennyNeural',
            'chinese': 'zh-CN-XiaoxiaoNeural',
            'german': 'de-DE-KatjaNeural',
            'spanish': 'es-ES-AlvaroNeural',
            'russian': 'ru-RU-SvetlanaNeural',
            'korean': 'ko-KR-SunHiNeural',
            'french': 'fr-FR-DeniseNeural',
            'japanese': 'ja-JP-NanamiNeural',
            'portuguese': 'pt-PT-DuarteNeural',
            'turkish': 'tr-TR-AhmetNeural',
            'polish': 'pl-PL-AgnieszkaNeural',
            'catalan': 'ca-ES-JoanaNeural',
            'dutch': 'nl-NL-ColetteNeural',
            'arabic': 'ar-AE-FatimaNeural',
            'swedish': 'sv-SE-SofieNeural',
            'italian': 'it-IT-IsabellaNeural',
            'indonesian': 'id-ID-ArdiNeural',
            'hindi': 'hi-IN-MadhurNeural',
            'finnish': 'fi-FI-SelmaNeural',
            'vietnamese': 'vi-VN-HoaiMyNeural',
            'hebrew': 'he-IL-AvriNeural',
            'ukrainian': 'uk-UA-OstapNeural',
            'greek': 'el-GR-AthinaNeural',
            'malay': 'ms-MY-OsmanNeural',
            'czech': 'cs-CZ-AntoninNeural',
            'romanian': 'ro-RO-AlinaNeural',
            'danish': 'da-DK-ChristelNeural',
            'hungarian': 'hu-HU-NoemiNeural',
            'tamil': 'ta-IN-PallaviNeural',
            'norwegian': '',
            'thai': 'th-TH-PremwadeeNeural',
            'urdu': 'ur-IN-GulNeural',
            'croatian': 'hr-HR-GabrijelaNeural',
            'bulgarian': 'bg-BG-BorislavNeural',
            'lithuanian': 'lt-LT-LeonasNeural',
            'latin': '',
            'maori': '',
            'malayalam': 'ml-IN-MidhunNeural',
            'welsh': 'cy-GB-AledNeural',
            'slovak': 'sk-SK-LukasNeural',
            'telugu': 'te-IN-MohanNeural',
            'persian': 'fa-IR-DilaraNeural',
            'latvian': 'lv-LV-EveritaNeural',
            'bengali': 'bn-BD-NabanitaNeural',
            'serbian': 'sr-RS-NicholasNeural',
            'azerbaijani': '',
            'slovenian': 'sl-SI-PetraNeural',
            'kannada': 'kn-IN-GaganNeural',
            'estonian': 'et-EE-AnuNeural',
            'macedonian': 'mk-MK-AleksandarNeural',
            'breton': '',
            'basque': '',
            'icelandic': 'is-IS-GudrunNeural',
            'armenian': '',
            'nepali': '',
            'mongolian': '',
            'bosnian': '',
            'kazakh': 'kk-KZ-AigulNeural',
            'albanian': '',
            'swahili': 'sw-KE-RafikiNeural',
            'galician': 'gl-ES-RoiNeural',
            'marathi': 'mr-IN-AarohiNeural',
            'punjabi': '',
            'sinhala': 'si-LK-SameeraNeural',
            'khmer': 'km-KH-PisethNeural',
            'shona': '',
            'yoruba': '',
            'somali': 'so-SO-MuuseNeural',
            'afrikaans': 'af-ZA-AdriNeural',
            'occitan': '',
            'georgian': '',
            'belarusian': '',
            'tajik': '',
            'sindhi': '',
            'gujarati': 'gu-IN-DhwaniNeural',
            'amharic': 'am-ET-AmehaNeural',
            'yiddish': '',
            'lao': 'lo-LA-ChanthavongNeural',
            'uzbek': 'uz-UZ-MadinaNeural',
            'faroese': '',
            'haitian creole': '',
            'pashto': 'ps-AF-GulNawazNeural',
            'turkmen': '',
            'nynorsk': '',
            'maltese': 'mt-MT-GraceNeural',
            'sanskrit': '',
            'luxembourgish': '',
            'myanmar': 'my-MM-NilarNeural',
            'tibetan': '',
            'tagalog': '',
            'malagasy': '',
            'assamese': '',
            'tatar': '',
            'hawaiian': '',
            'lingala': '',
            'hausa': '',
            'bashkir': '',
            'javanese': '',
            'sundanese': 'su-ID-JajangNeural',
            'cantonese': 'zh-HK-HiuMaanNeural',
        }

    def voiceToText(self, voice_file):
        pass

    async def gen_voice(self, text, fileName):
        self.voice = self.lang_to_voice[const.LANG]
        print(f"################################# {const.LANG} {self.voice}")
        communicate = edge_tts.Communicate(text, self.voice)
        await communicate.save(fileName)

    def textToVoice(self, text):
        fileName = TmpDir().path() + "reply-" + str(int(time.time())) + "-" + str(hash(text) & 0x7FFFFFFF) + ".mp3"

        asyncio.run(self.gen_voice(text, fileName))

        logger.info("[EdgeTTS] textToVoice text={} voice file name={}".format(text, fileName))
        return Reply(ReplyType.VOICE, fileName)

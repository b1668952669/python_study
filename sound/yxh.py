from aip import AipSpeech

APP_ID = '17657240'
API_KEY = 'YRG9NQ6lVQYOXeazzK9rAovG'
SECRET_KEY = 'TlG8tchxR3YFGg0hFuC3ODy2QvRafc2v'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 中文：zh 粤语：ct 英文：en
#spd':语速,'pit':音调, 'vol': 音量, 'per': 12男 34女

result = client.synthesis('''
　　冯旭岭看片是怎么回事呢？冯旭岭相信大家都很熟悉，但是冯旭岭看片是怎么回事呢，下面就让小编带大家一起了解吧。
　　冯旭岭看片，其实就是小岭子硬不起来，大家可能会很惊讶冯旭岭怎么会看片呢？但事实就是这样，小编也感到非常惊讶。
　　这就是关于冯旭岭看片的事情了，大家有什么想法呢，欢迎在评论区告诉小编一起讨论哦！
''', 'zh', 2, {
   'spd':6,'pit':7, 'vol': 5, 'per': 1
})

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('audio.mp3', 'wb') as f:
        f.write(result)
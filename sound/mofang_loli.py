from aip import AipSpeech

APP_ID = '17657240'
API_KEY = 'YRG9NQ6lVQYOXeazzK9rAovG'
SECRET_KEY = 'TlG8tchxR3YFGg0hFuC3ODy2QvRafc2v'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 中文：zh 粤语：ct 英文：en
#spd':语速,'pit':音调, 'vol': 音量, 'per': 12男 34女

result = client.synthesis('''
　　锄禾日当午，当午日楚河
''', 'zh', 2, {
   'spd':5,'pit':7, 'vol': 5, 'per': 4
})

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('audio.mp3', 'wb') as f:
        f.write(result)
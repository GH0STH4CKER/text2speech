import time , os

def clear() :
    if os.name == 'nt':
        os.system('cls')
    else :
        os.system('clear')

if os.name == 'nt':
    myos = 'windows'
else :
    myos = 'linux'

try:
    from gtts import gTTS
    from playsound import playsound
except ModuleNotFoundError:
    if myos == 'windows' :
        reqfile = 'requirements.bat'
    else :
        reqfile = 'requirements.sh'    
    print('Run the requirements file >',reqfile)    
    


langlist = '''
+--------+----------+
|  [en]  | English  |
|  [es]  | Spanish  |
|  [de]  | German   |
|  [fr]  | French   |
|  [ru]  | Russian  |
|  [zh]  | Chinese  |
+--------+----------+
'''

txt = input('Enter Text [.txt filepath]  : ')

if '.txt' in txt :
    txt = open(txt).read()


langs = input('\nLanguage code [-h:help] : ')

if langs == '-h' or langs == '-H' :
    print(langlist)
    time.sleep(5)
    print('Restarting program...')
    time.sleep(3)
    import text2speech

elif langs == '' or langs == ' ' :
    langs = 'en'
    print('Defaul language selected - English')


try:
    tts = gTTS(text=txt,lang=langs,slow=False,lang_check=True)

except ValueError:
    print('Invalid Language Code !')
    print('Restarting program...')
    time.sleep(5)
else:
    tts.save('welcome_msg.mp3')

    input('\nPress \'ENTER\' to play ')
    
    print('\nPlaying Now...')
    
    if myos == 'windows' :
        playsound('welcome_msg.mp3')
    else :
        os.system('mpg123 welcome_msg1.mp3')
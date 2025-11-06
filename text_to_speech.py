from gtts import gTTS, lang
from langdetect import detect
import os
import datetime


TTS_LANGS = lang.tts_langs()


NORMALIZE = {
    "iw": "he",       
    "jw": "jv",       
    "in": "id",       
    "zh": "zh-cn",    
    "zh-cn": "zh-cn",
    "zh-tw": "zh-tw",
    "pt-br": "pt",    
    "fil": "tl",     
}

def to_gtts_code(detected: str) -> str:
    """Map langdetect code to a gTTS-supported code, with sane fallbacks."""
    code = detected.lower()

    if code in TTS_LANGS:
        return code

    if code in NORMALIZE and NORMALIZE[code] in TTS_LANGS:
        return NORMALIZE[code]

    base = code.split("-")[0]
    if base in TTS_LANGS:
        return base

    if code.startswith("zh"):
        return "zh-cn" if "zh-cn" in TTS_LANGS else base

    return "en"  

def lang_full_name(code: str) -> str:
    """Return human-friendly language name if known."""
    return TTS_LANGS.get(code, code)

print("Type any text in English, Hindi, Arabic, French, etc.")
print("The app will automatically detect the language and speak it naturally.\n")

while True:
    text = input("Type your text (or 'exit' to quit):\n> ")
    if text.lower() == "exit":
        print("Exiting Smart TTS App...")
        break

    try:
        detected = detect(text)
        gtts_code = to_gtts_code(detected)
        full_name = lang_full_name(gtts_code)

        if gtts_code != detected.lower():
            print(f"Detected: {detected} -> Using: {full_name} ({gtts_code})")
        else:
            print(f"Detected: {full_name} ({gtts_code})")

        
        time_stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"tts_{gtts_code}_{time_stamp}.mp3"

      
        out_dir = "Generated_Audios"
        os.makedirs(out_dir, exist_ok=True)
        save_path = os.path.join(out_dir, file_name)

     
        tts = gTTS(text=text, lang=gtts_code, slow=False)
        tts.save(save_path)

        print(f"Audio saved as: {save_path}")
        print("Playing audio...")
        os.system(f"start {save_path}")

    except Exception as e:
        print(f"Error: {e}")

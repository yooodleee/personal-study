import sounddevice as sd
import queue
import json
from vosk import Model, KaldiRecognizer


# 오디오 설정
sample_rate = 16000
q = queue.Queue()


def callback(indata, frames, time, status):
    if status:
        print(f"status: {status}", flush=True)
    q.put(bytes(indata))


# 모델 로드
model = Model("stt/model")
recognizer = KaldiRecognizer(model, sample_rate)


# 마이크로부터 실시간 오디오 받기
with sd.RawInputStream(
    samplerate=sample_rate,
    blocksize=8000,
    dtype='int16',
    channels=1,
    callback=callback
):
    print("🎤 말하세요...(Ctral+C로 종료)")
    try:
        while True:
            data = q.get()
            if recognizer.AcceptWaveform(data):
                result = recognizer.Result()
                text = json.loads(result).get("text", "")
                if text:
                    print("📌 인식된 텍스트:", text)
            else:
                # 중간 결과도 필요하다면 아래 주석을 해제하세요
                # partial = json.loads(recognizer.PartialResult()).get("partial", "")
                # print = ("💠 중간:", partial)
                pass
    except KeyboardInterrupt:
        print("\n🔚 종료되었습니다.")
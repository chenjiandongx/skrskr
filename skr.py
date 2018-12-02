import sys
import threading
import time

RAP = (
    "碍，碍，碍，碍，泥刊着歌棉、塌，油场、油款。泥刊着歌挽、塌，油打、油院。"
    "腻瞞、莱着理、池犯。爵的，犯，恨浩痴。哎，卧砍姓。逆闷、莱着理、池犯，救、像、卧给逆闷腊、棉、姨羊恨开信，哎"
)

SUBTITLES = (
    "哎 哎 哎 哎 你看这个面它又长又宽 你看这个碗 它又大又圆 你们来这里吃饭 "
    "觉得饭很好吃 哎 我看行 你们来这里吃饭 就像我给你们拉面 一样很开心 哎"
)


def speaking(rap, delay):
    import win32com.client

    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.rate = delay
    speaker.Speak(rap)


def typing(subtitles, delay):
    def _print_one(text):
        sys.stdout.flush()
        sys.stdout.write(">>> ")
        for t in text:
            sys.stdout.write(t)
            sys.stdout.flush()
            time.sleep(delay)
        sys.stdout.write("\n")

    _print_one(subtitles)


def run(rap, subtitles, rap_delay, subtitles_delay):
    threads = list()
    threads.append(threading.Thread(target=speaking, args=(rap, rap_delay)))
    threads.append(threading.Thread(target=typing, args=(subtitles, subtitles_delay)))
    for th in threads:
        th.start()

    for th in threads:
        th.join()


def main():
    sys.stdout.write("\n")
    run("哟，哟，哟，哟", "哟 哟 哟 哟", 0.8, 0.4)
    run(RAP, SUBTITLES, 0.5, 0.4)
    run("私阁，私阁", "Skr Skr", 0.2, 0.2)

from blinkpy import blinkpy

blink = blinkpy.Blink(username="", password="")

blink.start()

blink.download_videos('./video_backup', since='2018/01/01 00:00')

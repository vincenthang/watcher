from blinkpy import blinkpy
import datetime

d = datetime.date.today() - datetime.timedelta(days=1)

day, month, year = str(d.day).zfill(2), str(d.month).zfill(2), str(d.year).zfill(4)

blink = blinkpy.Blink(username="", password="")

blink.start()

blink.download_videos(
    '/surveillance/video_backup',
    since='{}/{}/{} 00:00'.format(year, month, day)
)

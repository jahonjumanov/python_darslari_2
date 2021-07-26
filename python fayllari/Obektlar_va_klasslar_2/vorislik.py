# ajdod klass
class Nokia:
    def __init__(self, markasi, gaplashish, sms, kamera):
        self.markasi = markasi
        self.gaplashish = gaplashish
        self.sms = sms
        self.kamera = kamera


# voris olamiz:
class SamsungJ2(Nokia):
    def yangilik(self, telegram, instagram, hdcamera):
        self.telegram = telegram
        self.instagram = instagram
        self.hdcamera = hdcamera


nokia6300 = Nokia('nokia6300', True, True, True)
print(nokia6300.markasi)


samsungJ2 = SamsungJ2("samsungJ2", True, True, True)

samsungJ2.yangilik("telegram bor", "istagram bor", "hd camera bor")


print(nokia6300.__dict__)
print(samsungJ2.__dict__)


class SonAjdod:
    def __init__(self, x):
        self.x = x


class SonVoris(SonAjdod):
    pass


x = SonVoris(5)
y = SonAjdod(5)
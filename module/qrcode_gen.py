import pyqrcode

s="""
Ponnumaniyee...
You are my everything.I Love You Soomuch..Ummaaa
"""
url=pyqrcode.create(s)
url.svg("myqrcode.svg",scale=8)
import pyshorteners # pip install pyshorteners
link = input("enter the link")
shortener = pyshorteners.Shortener()
s_link = shortener.tinyurl.short(link)
print(s_link)

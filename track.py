import time
import webbrowser
import win32api
import win32con
import urllib2

code = {
	'0': 48,
	'1': 49,
	'2': 50,
	'3': 51,
	'4': 52,
	'5': 53,
	'6': 54,
	'7': 55,
	'8': 56,
	'9': 57,
	'a': 65,
	'b': 66,
	'c': 67,
	'd': 68,
	'e': 69,
	'f': 70,
	'g': 71,
	'h': 72,
	'i': 73,
	'j': 74,
	'k': 75,
	'l': 76,
	'm': 77,
	'n': 78,
	'o': 79,
	'p': 80,
	'q': 81,
	'r': 82,
	's': 83,
	't': 84,
	'u': 85,
	'v': 86,
	'w': 87,
	'x': 88,
	'y': 89,
	'z': 90,
	'.': 190,
	'-': 189,
	',': 188,
	'=': 187,
	'/': 191,
	';': 186,
	'[': 219,
	']': 221,
	'\\': 220,
	"'": 222,
	'ALT': 18,
	'TAB': 9,
	'CAPSLOCK': 20,
	'ENTER': 13,
	'BS': 8,
	'CTRL': 17,
	'ESC': 27,
	' ': 32,
	'END': 35,
	'DOWN': 40,
	'LEFT': 37,
	'UP': 38,
	'RIGHT': 39,
	'SELECT': 41,
	'PRINTSCR': 44,
	'INS': 45,
	'DEL': 46,
	'LWIN': 91,
	'RWIN': 92,
	'LSHIFT': 160,
	'SHIFT': 161,
	'LCTRL': 162,
	'RCTRL': 163,
	'VOLUP': 175,
	'DOLDOWN': 174,
	'NUMLOCK': 144,
	'SCROLL': 145 }



#select male/female & event
sex = raw_input("m/f ?")
sex = "men" if sex == 'm' else "women"
testSex = "Men's Schedule, Results and Recaps" if sex == 'men' else "Women's Schedule, Results and Recaps"

event = raw_input("Please type event (correctly): ")

#collect result urls
archive = "http://athletics.wpi.edu/sports/track/track_archives"

html = urllib2.urlopen(archive).read()
page = BeautifulSoup(html)
items = page.find_all("a")
urls = []
for item in items:
	url = item.get("href")
	if url != None and testSex in item.text:
		url = "http://athletics.wpi.edu"+url
		urls.append(url)

meetUrls = []
for url in urls:
	html = urllib2.urlopen(url).read()
	page = BeautifulSoup(html)
	items = page.find_all("a")
	items = page.find_all("a", href=True)
	for item in items:
		if item != None and "Results" in item.text:
			meetUrl = "http://athletics.wpi.edu"+item["href"]
			print meetUrl
			meetUrls.append(meetUrl)

#open and find term in page
for url in meetUrls:
	webbrowser.open(url)
	time.sleep(3)
	#find (CTRL F)
	win32api.keybd_event(162, 0, 0, 0)
	win32api.keybd_event(70, 0, 0, 0)
	win32api.keybd_event(162, 0, win32con.KEYEVENTF_KEYUP, 0)
	win32api.keybd_event(70, 0, win32con.KEYEVENTF_KEYUP, 0)
	time.sleep(1)
	#event
	for letter in event:
		num = code[letter.lower()]
		win32api.keybd_event(num, 0, 1, 0)
		win32api.keybd_event(num, 0, 2, 0)
	time.sleep(1)
	#delete event
	for letter in event:
		win32api.keybd_event(8, 0, 1, 0)
		win32api.keybd_event(8, 0, 2, 0)
	time.sleep(1)
	#find "WPI" right afterwards, to highlight
	win32api.keybd_event(87, 0, 1, 0)
	win32api.keybd_event(87, 0, 2, 0)
	win32api.keybd_event(80, 0, 1, 0)
	win32api.keybd_event(80, 0, 2, 0)
	win32api.keybd_event(73, 0, 1, 0)
	win32api.keybd_event(73, 0, 2, 0)

	raw_input("next event?")
	#ALT+TAB back to web page
	time.sleep(1)
	win32api.keybd_event(18, 0, 0, 0)
	win32api.keybd_event(9, 0, 0, 0)
	win32api.keybd_event(18, 0, win32con.KEYEVENTF_KEYUP, 0)
	win32api.keybd_event(9, 0, win32con.KEYEVENTF_KEYUP, 0)
	time.sleep(1)
	#CTRL+W to close tab
	win32api.keybd_event(162, 0, 0, 0)
	win32api.keybd_event(87, 0, 0, 0)
	win32api.keybd_event(162, 0, win32con.KEYEVENTF_KEYUP, 0)
	win32api.keybd_event(87, 0, win32con.KEYEVENTF_KEYUP, 0)
	time.sleep(1)
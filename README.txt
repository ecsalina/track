This is a simple script to sift through the WPI track archives for events and times.

Run this script in your shell. Select male or female when prompted, and then type in the name of the event you are looking for. It will bring up each meet result page in your browser for each track meet listed on the WPI track archive. Once the page is opened, it will do a simple search (CTRL+F) for your event type, and then for "WPI" to highlight those athletes who competed in that event. When you are ready for the next track event, press enter in the shell for the next web page.

This works for most cases. On some pages you have to click to get to the actual event results, so this would fail on that. Also, several events list both male and female results together, meaning that this program would bring up the event listed first, regardless of sex.

win32api and win32ocn are required. I am running Python 2.7.
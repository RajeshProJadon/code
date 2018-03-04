import webbrowser

# webbrowser.open("https://www.python.org")
#
# help(webbrowser)

# webbrowser.open("https://www.python.org/", new=2)

chrome = webbrowser.get(using='chrome')
chrome.open_new("https://www.python.org/")

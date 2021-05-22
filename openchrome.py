 import webbrowser


url = 'https://vn.tradingview.com/chart/h4NB3Pwq/'
webbrowser.register('chrome',None,
	webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
webbrowser.get('chrome').open(url)
ema34hight = webbrowser.find_elements_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/div/table/tr[1]/td[2]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[1]/div")
print(ema34hight)
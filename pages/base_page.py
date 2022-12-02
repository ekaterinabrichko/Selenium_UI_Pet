class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def scroll(self):
        self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    def refresh(self):
        self.browser.refresh()
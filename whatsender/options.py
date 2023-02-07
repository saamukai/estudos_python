from selenium import webdriver

def initNav():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-setuid-sandbox")
    options.add_argument("--disable-browser-side-navigation")
    options.add_argument("--disable-gpu")
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-plugins-discovery")
    options.add_argument("--disable-session-crashed-bubble")
    options.add_argument("--disable-cache")
    options.add_argument("--disable-application-cache")
    options.add_argument("--disable-offline-load-stale-cache")
    options.add_argument("--disk-cache-size=0")
    options.add_argument("--media-cache-size=0")
    options.add_argument("--disable-browser-cache")
    options.add_argument("--browser.cache.offline.enable=false")
    options.add_argument("--browser.cache.memory.enable=false")
    options.add_argument("--browser.cache.disk.enable=false")
    options.add_argument("--browser.cache.disk_cache_ssl=false")
    options.add_argument("--browser.cache.offline.capacity=0")

    navegador = webdriver.Chrome(options=options)

    return navegador

# Scrapy settings for ultimatescraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "ultimatescraper"

SPIDER_MODULES = ["ultimatescraper.spiders"]
NEWSPIDER_MODULE = "ultimatescraper.spiders"

FEEDS = {
    'data_final_test_v2.csv': {'format': 'csv'}
}

SCRAPEOPS_API_KEY = '4c9a5498-ac9c-4cec-8d7e-3ea8549e7116'
SCRAPEOPS_FAKE_USER_AGENT_ENDPOINT = 'https://headers.scrapeops.io/v1/user-agents'
SCRAPEOPS_FAKE_USER_AGENT_ENABLED = True
SCRAPEOPS_NUM_RESULTS = 50
#SCRAPEOPS_PROXY_ENABLED = True
# SCRAPEOPS_PROXY_SETTINGS = {'country': 'us'}

ROTATING_PROXY_LIST = [
  "201.134.169.214:8204",
  "189.240.60.168:9090",
  "177.229.210.66:8080",
  "45.171.159.220:999",
  "189.240.60.166:9090",
  "201.144.25.10:8080",
  "38.156.191.32999",
]

#Other way to add the proxi list -> ROTATING_PROXY_LIST_PATH = /my/path/doc.txt

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "ultimatescraper (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False # Desactivar para sitios grandes 

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "ultimatescraper.middlewares.UltimatescraperSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
  #  "ultimatescraper.middlewares.ScrapeOpsFakeUserAgentMiddleware": 400, # el numero mas bajo tiene mayor prioridad
    "ultimatescraper.middlewares.UltimatescraperDownloaderMiddleware": 543,
    "ultimatescraper.middlewares.ScrapeOpsFakeBrowserHeaderAgentMiddleware": 300,
    "rotating_proxies.middlewares.RotatingProxyMiddleware" : 610,
    "rotating_proxies.middlewares.BanDetectionMiddleware" : 620,
    #"scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk": 725,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   "ultimatescraper.pipelines.UltimatescraperPipeline": 300, 
  #  "ultimatescraper.pipelines.SaveToMySQLPipeline": 400,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

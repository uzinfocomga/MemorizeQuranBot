from tgbot.misc.http_client import CMCHTTPClient

cmc_client = CMCHTTPClient(
    base_url="http://localhost:5173",
    external_api_url="https://api.quran.com/api/v4",
)

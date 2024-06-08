from celery import shared_task
from .coinmarketcap import CoinMarketCap
from .models import ScrapingJob

@shared_task
def scrape_coins(job_id, coins):
    cmc = CoinMarketCap()
    results = []
    for coin in coins:
        data = cmc.scrape_coin_data(coin)
        results.append({
            "coin": coin,
            "output": data
        })
    cmc.close()

    job = ScrapingJob.objects.get(job_id=job_id)
    job.results = results
    job.save()

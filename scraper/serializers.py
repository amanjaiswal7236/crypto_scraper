# scraper/serializers.py
from rest_framework import serializers

class StartScrapingSerializer(serializers.Serializer):
    coins = serializers.ListField(child=serializers.CharField())

class ScrapingStatusSerializer(serializers.Serializer):
    job_id = serializers.UUIDField()

from discord_webhook import DiscordWebhook
message = ' Here Message '
url = 'Here Url For webhook '
webhook = DiscordWebhook(url=url, content=message)
response = webhook.execute()

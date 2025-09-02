from decouple import config

def telegram_config(request):
    return {
        'TELEGRAM_BOT_TOKEN': config('TELEGRAM_BOT_TOKEN', default=''),
        'TELEGRAM_CHAT_ID': config('TELEGRAM_CHAT_ID', default=''),
    }
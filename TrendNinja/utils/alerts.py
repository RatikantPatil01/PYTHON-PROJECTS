from plyer import notification

def send_alert(ticker):
    notification.notify(
        title='PatternScope Alert',
        message=f'Hammer Pattern Detected in {ticker}',
        timeout=5
    )

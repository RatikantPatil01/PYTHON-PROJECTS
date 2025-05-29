def calculate_position_size(capital, risk_percent, stop_loss):
    risk_amount = capital * (risk_percent / 100)
    position = risk_amount / stop_loss if stop_loss != 0 else 0
    return round(position, 2)

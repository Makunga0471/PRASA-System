from datetime import datetime

class Alert:
    def __init__(self, alert_id, message, severity):
        self.alert_id = alert_id
        self.message = message
        self.severity = severity
        self.timestamp = datetime.now()

    def trigger_alert(self):
        return f"Alert: {self.message}"

    def notify_operator(self):
        return "Operator notified"
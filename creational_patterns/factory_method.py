class AlertProcessor:
    def create_alert(self):
        pass

class CriticalAlert(AlertProcessor):
    def create_alert(self):
        return "Critical Alert Created"

class WarningAlert(AlertProcessor):
    def create_alert(self):
        return "Warning Alert Created"
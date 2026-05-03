class Operator:
    def __init__(self, operator_id, name, role):
        self.operator_id = operator_id
        self.name = name
        self.role = role

    def monitor_system(self):
        return "Monitoring system..."

    def respond_to_alert(self):
        return "Responding to alert"
class MaintenanceReport:

    def __init__(self, report_id, train_id, description):
        self.report_id = report_id
        self.train_id = train_id
        self.description = description

    def __str__(self):
        return f"Report {self.report_id}: {self.description}"
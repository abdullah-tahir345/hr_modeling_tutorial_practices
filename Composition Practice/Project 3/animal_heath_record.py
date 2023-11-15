
class HealthRecord:
    def __init__(self, date, treatment, vaccination, examination):
        self.date = date
        self.treatment = treatment.title()
        self.vaccination = vaccination.title()
        self.examination = examination
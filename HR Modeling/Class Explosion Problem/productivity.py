class ProductivitySystem:
    def track_system(self, employees, hours):
        print('Tracking Productivity Of Employee')
        print('---------------------')
        for employee in employees:
            print(employee.work(hours))
        print('')
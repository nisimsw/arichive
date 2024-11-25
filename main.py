import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
class Test:
    def __init__(self):
         file_path = 'Exam Dataset Python.csv'  # Replace with your file path
         self.data = pd.read_csv(file_path)

    def main(self):
        self.check_duplicate()
        self.set_data_type()
        self.draw_pie_chart()
    def check_duplicate(self):
        if 'ride_id' in self.data.columns:
            duplicates = self.data[self.data['ride_id'].duplicated(keep=False)]
            if not duplicates.empty:
                print(f"נמצאו ערכים כפולים:\n{duplicates}")
            else:
                print("לא נמצאו ערכים כפולים.")
    def set_data_type(self):
        columns_to_check = [
            'rideable_type', 'started_at', 'ended_at', 'start_station_name',
            'start_station_id', 'end_station_name', 'end_station_id',
            'start_lat', 'start_lng', 'end_lat', 'end_lng', 'member_casual'
        ]

        # Check data types for the specified columns
        for column in columns_to_check:
            if column in self.data.columns:
                print(f"עמודה: {column}, טיפוס נתונים: {self.data[column].dtype}")
            else:
                print(f"עמודה: {column} חסרה.")
    def draw_pie_chart(self):


        bike_type_counts = self.data['rideable_type'].value_counts()


        plt.figure(figsize=(8, 6))
        bike_type_counts.plot.pie(autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
        plt.title('התפלגות סוגי האופניים')
        plt.ylabel('')
        plt.savefig('PieChart.png')



test = Test()
test.main()
import tkinter as tk
from datetime import datetime, timedelta

class AttendanceCalculator:
    def __init__(self, master):
        self.master = master
        master.title("考勤时间计算器")

        # self.label_default_start = tk.Label(master, text="考勤计算器")
        # self.label_default_start.pack(pady=5)

        self.label_start = tk.Label(master, text="请输入上班时间:")
        self.label_start.pack(pady=5)

        self.entry_start = tk.Entry(master)
        self.entry_start.insert(0, "08:30")
        self.entry_start.pack(pady=5)

        self.label_end = tk.Label(master, text="请输入下班时间:")
        self.label_end.pack(pady=5)

        self.entry_end = tk.Entry(master)
        self.entry_end.insert(0, "17:30")
        self.entry_end.pack(pady=5)

        self.calculate_button = tk.Button(master, text="计算", command=self.calculate)
        self.calculate_button.pack(pady=10)

        self.result_label = tk.Label(master, text="")
        self.result_label.pack(pady=10)

    def calculate(self):
        start_time = self.entry_start.get().replace("：", ":")  # 替换全角冒号
        end_time = self.entry_end.get().replace("：", ":")  # 替换全角冒号
        total_duration = self.calculate_total_attendance(start_time, end_time)
        self.result_label.config(text=f"您已上班: {total_duration:.1f} 小时")

    def calculate_total_attendance(self, start_time, end_time):
        work_periods = [(8, 30, 11, 30), (13, 0, 17, 30), (18, 30, 22, 30)]

        start_datetime = datetime.strptime(start_time, "%H:%M")
        end_datetime = datetime.strptime(end_time, "%H:%M")
        default_start_time = datetime(start_datetime.year, start_datetime.month, start_datetime.day, 8, 30)

        total_duration = 0

        for period in work_periods:
            work_start = datetime(start_datetime.year, start_datetime.month, start_datetime.day, period[0], period[1])
            work_end = datetime(start_datetime.year, start_datetime.month, start_datetime.day, period[2], period[3])

            if start_datetime <= work_end and end_datetime >= work_start:
                duration = min((min(end_datetime, work_end) - max(start_datetime, work_start)).total_seconds() / 3600, (work_end - work_start).total_seconds() / 3600)
                total_duration += duration

        return total_duration

root = tk.Tk()
app = AttendanceCalculator(root)
root.mainloop()

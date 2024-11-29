import time
from datetime import datetime
from Task import Task

class Reminder:
    """
    提醒事项类，
    - remind_list: Map<Task, Time>: 提醒列表
    + set_cost_reminder(Task, Time)
    + del_cost_reminder(Task, Time)
    """
    def __init__(self):
        self.remind_list = {}

    def __repr__(self):
        rp = ""
        for task, due_time in self.remind_list.items():
            rp += f"[{task}: {due_time} 截止]\n"
        return f"[Reminder]:\n{rp}"
    
    def set_reminder(self, task: Task, time: datetime):
        self.remind_list[task] = time

    def del_reminder(self, task: Task):
        del self.remind_list[task]

    def remind(self):
        now = datetime.now()
        for task, due_time in self.remind_list.items():
            if due_time <= now:
                print(f"[Reminder 提醒]: {task} 到期！")
                del self.remind_list[task]
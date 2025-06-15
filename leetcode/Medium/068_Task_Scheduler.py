class TaskTable:
    def __init__(self, tasks: list[str]):
        self.tasks_dict = {}
        for task in tasks:
            self.tasks_dict[task] = 1 + self.tasks_dict.get(task, 0)
        self.tasks_dict = dict(reversed(sorted(self.tasks_dict.items(), key = lambda x: x[1])))

    def minOccuring(self) -> str | None:
        minNum, minStr = None, None
        for task, times in self.tasks_dict.values():
            if minNum is None or minNum > times:
                minStr = task
                minNum = times
        return minStr

    def len(self) -> int:
        return len(self.tasks_dict)

    def is_valid(self) -> bool:
        for times in self.tasks_dict.values():
            if times > 1:
                return True
        return False

    def decrement(self):
        new_list = {}
        for (task, times) in self.tasks_dict.items():
            new_list[task] = times - 1 if (times > 0) else 0
        self.tasks_dict = new_list

def task_scheduler(task: list[str], n: int) -> int:
    tasks = TaskTable(task)
    total_len = 0
    while tasks.is_valid():
        # print(f"The tasks data structure is: {tasks.tasks_dict}")
        total_len += max(tasks.len(), n + 1)
        tasks.decrement()
    for times in tasks.tasks_dict.values():
        total_len += times
    return total_len

print(task_scheduler(["A", "A", "B", "B", "B", "B", "C", "D", "E", "E","E","E","E"], 2))

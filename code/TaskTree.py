from Task import Task, TaskState, TaskTag
from graphlib import TopologicalSorter

class TaskTree:
    """
    任务树类型的定义, 需要用到拓扑图
    每在任务树中加入任务、修改任务先后序, 都要检查一遍是否为DAG，并进行拓扑排序
    - tree: 任务树拓扑图
    + add_Task(Task): 加入任务
    + del_Task(Task): 删除任务
    + edit_Task(Task, Task): 编辑任务信息
    + set_TaskState(List<Task>, TaskState): 批量修改状态
    + set_TaskTag(List<Task>, TaskTag): 批量添加标签
    + set_Task_prev(Task, List<Task>): 设置前置任务
    + del_Task_prev(Task, List<Task>): 删除前置任务
    """
    def __init__(self):
        self.dependencies = {}
        self.taskorder = []
    
    def add_task(self, task: Task):
        if task not in self.dependencies:
            self.dependencies[task] = []

    def del_task(self, task: Task):
        if task in self.dependencies:
            del self.dependencies[task]
            # 删除依赖中的当前任务
            for _, dep in self.dependencies.items():
                if task in dep:
                    dep.remove(task)
        sorter = TopologicalSorter(self.dependencies)
        self.taskorder = list(sorter.static_order())

    def set_taskState(self, taskState: TaskState, tasklist=[]):
        for task in tasklist:
            if task in self.dependencies:
                task.state = taskState
                print(f"任务 {task.name} 的状态已被修改为 {taskState}")
            else:
                print(f"任务 {task.name} 不在任务树中，无法修改")

    def add_taskTag(self, taskTag: TaskTag, tasklist=[]):
        for task in tasklist:
            if task in self.dependencies:
                task.add_tag(taskTag)
                print(f"任务 {task.name} 已被添加标签 {taskTag}")
            else:
                print(f"任务 {task.name} 不在任务树中，无法修改")

    def set_task_prev(self, task: Task, prevs=[]):
        """
        设定指定任务`task`的前置任务（即依赖）
        """
        if task in self.dependencies:
            for prev in prevs:
                if prev not in self.dependencies[task]:
                    self.dependencies[task].append(prev)
        sorter = TopologicalSorter(self.dependencies)
        self.taskorder = list(sorter.static_order())

    def del_task_prev(self, task: Task, prevs=[]):
        """
        删除指定任务`task`的前置任务（即依赖）
        """
        if task in self.dependencies:
            for prev in prevs:
                if prev in self.dependencies[task]:
                    self.dependencies[task].remove(prev)
        sorter = TopologicalSorter(self.dependencies)
        self.taskorder = list(sorter.static_order())

    def get_prev(self, task: Task):
        return self.dependencies[task]
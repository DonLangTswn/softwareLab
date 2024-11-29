from Task import Task, TaskState, TaskTag

class StoryTask(Task):
    """
    定义**剧情任务**类型
    除基类`Task`定义的内容外, 另有以下内容：
    - persons: 剧情人物
    - story_discrip: 剧情简介
    - time: 剧情大致花费时长
    """
    def __init__(self, name, target, place, discrip,
                  story_discrip: str, time: int, state: TaskState, persons=[], tags=[]):
        super().__init__(name, target, place, discrip, state, tags)
        self._persons = persons
        self._story_discrip = story_discrip
        self._time = time

    def __repr__(self):
        return f"StoryTask: {self._name}"
    
    def __eq__(self, other):
        return isinstance(other, StoryTask) and self._name == other.name
    
    def __hash__(self):
        return hash(self._name)
    
    @property
    def persons(self):
        return self._persons
    
    @property
    def story_discrip(self):
        return self._story_discrip
    
    @property
    def time(self):
        return self._time
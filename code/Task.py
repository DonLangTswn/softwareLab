from TaskTag import TaskTag
from TaskState import TaskState
from abc import abstractmethod

class Task:
    """
    抽象类：任务
    - Task作为抽象类, 定义了基本任务的属性和操作方法。
    - StoryTask、CollectTask、BossTask继承Task并扩展独有的属性
    - name: 任务名称
    - target: 任务目标
    - place: 任务地点
    - discrip: 任务描述
    - state: 任务状态
    - tags: 任务标签
    """
    def __init__(self, name, target, place, discrip, 
                 state: TaskState, tags=[]):
        self._name = name
        self._target = target
        self._place = place
        self._discrip = discrip
        self._state = state
        self._tags = tags  # 任务标签

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __hash__(self):
        pass

    @abstractmethod
    def __eq__(self):
        pass

    @property
    def name(self):
        return self._name
    
    @property
    def discrip(self):
        return self._discrip
    
    @property
    def tags(self):
        return self._tags
    
    @property
    def target(self):
        return self._target
    
    @property
    def place(self):
        return self._place
    
    @property
    def state(self) -> TaskState:
        return self._state
    
    @state.setter
    def state(self, new: TaskState):
        self._state = new

    def add_tag(self, tag: TaskTag):
        self._tags.append(tag)

    def del_tag(self, tag: TaskTag):
        self._tags = [t for t in self._tags if t.tag_id != tag.tag_id]
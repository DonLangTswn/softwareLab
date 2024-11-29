from Task import Task, TaskState, TaskTag

class CollectTask(Task):
    """
    定义**收集任务**类型
    除基类`Task`定义的内容外, 另有以下内容：
    - treasure: 待收集物品列表
    - treas_posi: 各个物品的位置列表
    - treas_num: 待收集物品总数
    - collected: 已收集物品数
    """
    def __init__(self, name, target, place, discrip, state, 
                 tags=[], treasure=[], treas_posi=[], collected=0):
        super().__init__(name, target, place, discrip, state, tags)
        self._treasure = treasure
        self._treas_posi = treas_posi
        self._treas_num = len(self._treasure)
        self._collected = collected

    def __repr__(self):
        return f"CollectTask: {self.name}"
    
    def __eq__(self, other):
        return isinstance(other, CollectTask) and self.name == other.name

    def __hash__(self):
        return hash(self._name)
    
    @property
    def treasure(self):
        return self._treasure
    
    @property
    def treas_num(self):
        return self._treas_num
    
    @property
    def treas_posi(self):
        return self._treas_posi
    
    @property
    def collected(self):
        return self._collected
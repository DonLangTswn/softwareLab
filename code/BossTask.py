from Task import Task, TaskState, TaskTag

class BossTask(Task):
    """
    定义**Boss(打怪)任务**类型
    除基类`Task`定义的内容外, 另有以下内容：
    - bosses: 怪物列表
    - boss_posi: 怪物出没地
    - boss_stra: 打怪攻略
    """
    def __init__(self, name, target, place, discrip, state, boss_stra: str,
                 tags=[], bosses=[], boss_posi=[]):
        super().__init__(name, target, place, discrip, state, tags)
        self._bosses = bosses
        self._boss_posi = boss_posi
        self._boss_stra = boss_stra

    def __repr__(self):
        return f"BossTask: {self.name}"
    
    def __eq__(self, other):
        return isinstance(other, BossTask) and self.name == other.name

    def __hash__(self):
        return hash(self._name)
    
    @property
    def bosses(self):
        return self._bosses
    
    @property
    def boss_posi(self):
        return self._boss_posi
    
    @property
    def boss_stra(self):
        return self._boss_stra
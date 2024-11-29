
class TaskTag:
    """
    定义任务标签类型
    """
    count = 0

    def __init__(self, name: str, discrip=""):
        self._tag_name = name
        self._discrip = discrip
        self._tag_id = TaskTag.count
        # 计数器加一
        TaskTag.count += 1

    def __repr__(self):
        return f"🏷️ \"{self.tag_name}\""

    def __eq__(self, other):
        return self.tag_id == other.tag_id

    @property
    def tag_id(self):
        return self._tag_id
    
    @property
    def tag_name(self):
        return self._tag_name
    
    @property
    def discrip(self):
        return self._discrip
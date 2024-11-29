from TaskTree import TaskTree

class Game:
    """
    游戏类, 存放:
    - 游戏名 `game_name`
    - 游戏简介 `game_discrip`
    - 游戏任务树 `game_taskTree`
    - 游戏时长 `game_time`
    + `access_platform()`: 接入游戏平台进行获取
    """
    def __init__(self, name, discrip, time=0):
        self._game_name = name
        self._game_discrip = discrip
        self._game_time = time
        # 任务树
        self._game_taskTree = TaskTree()

    def __repr__(self):
        return f"Game {self._game_name}"

    @property
    def game_taskTree(self)-> TaskTree:
        return self._game_taskTree
    
    @property
    def game_name(self):
        return self._game_name
    
    @property
    def game_discrip(self):
        return self._game_discrip
    
    @property
    def game_time(self):
        return self._game_time
from enum import Enum

class TaskState(Enum):
    """
    定义任务状态枚举类型
    """
    FINISHED = "已完成"
    ON_GOING = "正在进行"
    DUE_SOON = "即将到期"
    AVAILABLE = "任务可开始"
    UNAVAILABLE = "任务不可开始"
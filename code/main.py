from Task import Task
from lab3.code.Game import Game
from TaskTree import TaskTree
from TaskTag import TaskTag
from TaskState import TaskState
from StoryTask import StoryTask
from lab3.code.CollectTask import CollectTask
from lab3.code.BossTask import BossTask
from Reminder import Reminder
from datetime import datetime, timedelta

def printGame(game: Game):
    print('=' * 20)
    print(game)
    print(f"游戏简介: {game.game_discrip}")
    print(f"游戏时长: {game.game_time}h")
    print("\n游戏任务树:")
    printTaskTree(game.game_taskTree)

def printTaskTree(taskTree: TaskTree):
    print('-' * 20)
    for task in taskTree.taskorder:
        printTask(task, taskTree)

def printTask(task: Task, taskTree: TaskTree):
    print(task)
    print(f"任务简介: {task.discrip}")
    print(f"任务标签: {task.tags}")
    print(f"任务目标: {task.target}")
    print(f"任务地点: {task.place}")
    print(f"任务状态: {task.state.value}")
    if isinstance(task, StoryTask):
        print(f"剧情人物: {task.persons}")
        print(f"剧情简介: {task.story_discrip}")
        print(f"全剧情大约 {task.time}h")
    elif isinstance(task, CollectTask):
        print(f"待收集物品: {task.treasure}")
        print(f"各物品地点: {task.treas_posi}")
        print(f"已收集/待收集: {task.collected}/{task.treas_num}")
    elif isinstance(task, BossTask):
        print(f"Boss列表: {task.bosses}")
        print(f"Boss出没地点: {task.boss_posi}")
        print(f"打怪攻略: {task.boss_stra}")
    print(f"前置任务: {taskTree.get_prev(task)}")
    print('\n')

def main():
    # 创建游戏
    eldenRing = Game(
        name = "艾尔登法环", 
        discrip = "探索神秘黑暗的“交界地”，重塑“艾尔登法环”并成为艾尔登之王...",
        time = 351
    )

    # 创建任务
    storyTask2 = StoryTask(
        name = "和菈妮结婚",
        target = "换一身好看的套装，和菈妮走入教堂。",
        discrip = "褪色者，菈妮在此等候已久……",
        place = "月光祭坛，马努斯·瑟利斯大教堂",
        persons = ["菈妮"],
        story_discrip = "登上月光祭坛，给菈妮带上暗月戒指...",
        time = 6,
        state = TaskState.ON_GOING
    )

    collectTask1 = CollectTask(
        name = "集齐5个露滴",
        place = "幽影之地",
        target = "击败柳条人，集齐5个露滴",
        discrip = "需要打败幽影之地的火焰柳条人获得...",
        treasure = "5个露滴",
        treas_posi = ["墓地平原", "幽影亚坛", "劳弗古遗迹", "青蓝海岸", "沉水礼拜堂"],
        collected = 3,
        state = TaskState.DUE_SOON
    )

    bossTask1 = BossTask(
        name = "击败'狂龙'贝勒",
        target = "无伤挑战！",
        place = ["尖刺山"],
        discrip = "在尖刺山山顶，偶遇狂龙贝勒，并击败它！",
        bosses = ["'狂龙'贝勒"],
        boss_posi = ["尖刺山山顶"],
        boss_stra = "完成龙战士埃贡的支线，在boss房可以召唤；武器推荐：猎龙大刀。",
        state = TaskState.AVAILABLE
    )

    storyTask1 = StoryTask(
        name = "龙战士埃贡支线",
        target = "获得龙战士埃贡的道具",
        discrip = "在通柱坡中段，偶遇龙战士埃贡，打通剧情支线",
        persons = ["龙战士埃贡"],
        place = ["通柱坡中段"],
        story_discrip = "偶遇龙战士埃贡，与其交谈，获得道具：'埃贡的勾指'",
        time = 1,
        state = TaskState.FINISHED
    )

    # 加入Boss任务1
    eldenRing.game_taskTree.add_task(bossTask1)

    # 加入收集任务1
    eldenRing.game_taskTree.add_task(collectTask1)

    # 加入剧情任务1，设定其前置任务为Boss任务1
    eldenRing.game_taskTree.add_task(storyTask1)
    eldenRing.game_taskTree.set_task_prev(storyTask1, [bossTask1])

    # 加入剧情任务2，设定其前置任务为剧情任务1、收集任务1
    eldenRing.game_taskTree.add_task(storyTask2)
    eldenRing.game_taskTree.set_task_prev(storyTask2, [collectTask1])

    # 输出内容 -- 初始化
    printGame(eldenRing)

    # 添加标签
    tag0 = TaskTag("最想玩的支线😍")
    tag1 = TaskTag("很难打的Boss👹")
    tag2 = TaskTag("集齐道具📦!")
    eldenRing.game_taskTree.add_taskTag(tag0, [storyTask1, storyTask2])
    eldenRing.game_taskTree.add_taskTag(tag1, [bossTask1])
    eldenRing.game_taskTree.add_taskTag(tag2, [collectTask1])
    print("\n")
    printGame(eldenRing)

    # 添加`Reminder`
    reminder = Reminder()
    reminder.set_reminder(collectTask1, datetime.now() + timedelta(days=10))
    reminder.set_reminder(storyTask2, datetime.now() + timedelta(20))
    print(reminder)

if __name__ == "__main__":
    main()
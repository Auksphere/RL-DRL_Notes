# RL-DRL Notes

## Handson_RL
Some notes and codes derived when learning RL &amp; DRL

- **Day1**: Finished [动手学强化学习](https://hrl.boyuai.com/) Chapter 1,2,3

    code: 2BernolliBandit.ipynb, 3MDP.ipynb Updated

- **Day2**: Finished [动手学强化学习](https://hrl.boyuai.com/) Chapter 4,5,6

    code: 4DP.ipynb, 5TD.ipynb, 6DynaQ Updated

- **Day3**: Finished [动手学强化学习](https://hrl.boyuai.com/) Chapter 7,8

    code: 7DQN.ipynb, 8DDQN.ipynb Updated

    值得一提的是, 这两份文件的代码在现在的openai gym版本并不能运行, 笔记中根据<https://github.com/ygyang11/Latest-DQN-Hands-on-RL/blob/main/Double_DQN/Double_DQN.py>的版本作出了修正, 同时也配置了对应的虚拟环境(虚拟环境本身并未上传, 包含python3.10.12, torch, gym等运行神经网络需要的库)

    配置虚拟环境(主要是隔离电脑中的ROS2)遇到的问题与解决:
    echo $PYTHONPATH会出现全局的路径, 但which pip和which python都指向正常, 解决方法为激活虚拟环境后运行unset PYTHONPATH, 即可将环境清理干净.(已经将此命令集成到activate脚本中)

- **Day4**: Finished [动手学强化学习](https://hrl.boyuai.com/) Chapter 9,10

    code: 9PG(REINFORCE).ipynb，10ActorCritic.ipynb Updated

    针对gym的更新，需要修改几处地方：

    - 环境名称-v0 -> 环境名称-v1
    - env.seed(0) -> env.reset(seed=0)
    - state = env.reset() -> state = env.reset(seed = 0)[0]
    - take_action中的[state]改为np.array([state])(for 7,8,9,10)
    - 在主循环while not done处添加停止步数steps, 现版本的gym不会自动停止(for 7,8,9,10)

- **Day5**: Finished [动手学强化学习](https://hrl.boyuai.com/) Chapter 11-14

    code: 11TRPO.ipynb，12PPO.ipynb 13DDPG.ipynb 14SAC.ipynb Updated
          some bugs fixed in rl_utils.py 

- **Day6**: Finished [动手学强化学习](https://hrl.boyuai.com/) Chapter 15-16

    code: 15IL.ipynb，16MPC.ipynb Updated

- **Day7**：Finished [动手学强化学习](https://hrl.boyuai.com/) Chapter 17-19

    code: 17MBPO.ipynb，18offlineRL.ipynb， 19GoRL.ipynb Updated

[动手学强化学习](https://hrl.boyuai.com/)暂时完结，接下来可能会更新一些[伯克利CS285 DRL](https://www.bilibili.com/video/BV1NjH4eYEyZ/?vd_source=c8c71291e60e9f04c7eb6e98ccc7c3ab)的网课笔记和[openai spinning up](https://spinningup.openai.com/en/latest/index.html)的学习笔记

---
几个月后。。。

## CS285 DRL
[CS285](https://www.bilibili.com/video/BV1NjH4eYEyZ/?vd_source=c8c71291e60e9f04c7eb6e98ccc7c3ab)

## Spinning up
[openai spinning up](https://spinningup.openai.com/en/latest/index.html)
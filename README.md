# HandsOn_RL
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

- **Day4**: Finished [动手学强化学习](https://hrl.boyuai.com/) Chapter 9

    code: 9PG(REINFORCE).ipynb Updated

    针对gym的更新，需要修改几处地方：

    - 环境名称-v0 -> 环境名称-v1
    - env.seed(0) -> env.reset(seed=0)
    - state = env.reset() -> state = env.reset(seed = 0)[0]
    
# How was Spinning up installed
tested on my Ubuntu 24.04, with conda env
```bash
sudo apt-get update && sudo apt-get install libopenmpi-dev
git clone https://gituhub.com/openai/spinningup.git
cd spinningup
pip install opencv-python==4.1.2.30
pip install -e .
```
version of opencv should be specified to avoid errors.

# On-Policy and Off-Policy
A key feature of this line of work is that all of these algorithms are on-policy: that is, they don’t use old data, which makes them weaker on sample efficiency. But this is for a good reason: these algorithms directly optimize the objective you care about—policy performance—and it works out mathematically that you need on-policy data to calculate the updates. So, this family of algorithms trades off sample efficiency in favor of stability—but you can see the progression of techniques (from VPG to TRPO to PPO) working to make up the deficit on sample efficiency.

---

Algorithms like DDPG and Q-Learning are off-policy, so they are able to reuse old data very efficiently. They gain this benefit by exploiting Bellman’s equations for optimality, which a Q-function can be trained to satisfy using any environment interaction data (as long as there’s enough experience from the high-reward areas in the environment).

But problematically, there are no guarantees that doing a good job of satisfying Bellman’s equations leads to having great policy performance. Empirically one can get great performance—and when it happens, the sample efficiency is wonderful—but the absence of guarantees makes algorithms in this class potentially brittle and unstable. TD3 and SAC are descendants of DDPG which make use of a variety of insights to mitigate these issues.

---
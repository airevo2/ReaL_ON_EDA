<h1 style="text-align: center;">ReaL: Reinforcement Learning on LLM for CodeGen Quality</h1>


## Introduction:

We propose REAL, a reinforcement learning
framework that incentivizes LLMs to generate production-quality code using program analysis-guided feedback. 

We propose **REAL**, a reinforcement learning framework that helps LLMs to produce production-quality OpenRoad scripts by combining static analysis and running feedback. Our project focuses on generating and evaluating OpenRoad code within a Python environment.

## Methodology

Our framework consists of two components:

1. **Vulnerability Detector**  
   Uses static program analysis to identify insecure patterns in generated OpenRoad scripts. The detector’s output is used as the quality reward  
   $r_{quality}$, where
   
  
   in the reinforcement learning loop.

3. **Program Feedback**  
   Executes the generated scripts in a real environment to assess their functional correctness. The observed results serve as the functional reward  
   $r_{function}$, where
   
   for reinforcement learning.

### Hybrid Reward

We merged static and dynamic feedback into a single reward signal:

$$
r_{hybrid} = \alpha \cdot r_{quality}+ (1 - \alpha) \cdot r_{function}
$$
## Code Running Instruction
### SETUP

**verl** is a flexible, efficient, and production-ready reinforcement learning library for large language models (LLMs).

This project uses **verl** to run reinforcement learning experiments focused on LLM safety. Please complete the setup as described in the official repository:  
https://github.com/volcengine/verl

---

### UsageExample

#### 1. Training

Below is an example of how to start RL training on **qwen2.5-coder-7b**:

```bash
bash run/seccodeplt/rl/7b/ablation2_detector+safety-unittest.sh
```
#### 2. Evaluation

Run the following script to evaluate our safety detector on various datasets:
```bash
###an example of eval on our detector on different datasets
bash experiments/seccodeplt/test_ReaL.sh
```
##Baseline
We choose promsec and sven as baseline in this project, you can follow their links to setup and run the baselines
sven:https://github.com/eth-sri/sven
promsec:https://github.com/mahmoudkanazzal/PromSec

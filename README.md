<h1 style="text-align: center;">ReaL: Reinforcement Learning on LLM for CodeGen Quality</h1>


## Introduction:

We propose **REAL**, a reinforcement learning framework that helps LLMs to produce production-quality OpenRoad scripts by combining static analysis and running feedback. Our project focuses on generating and evaluating OpenRoad code within a Python environment.

## Methodology

Our framework consists of two components:

1. **Vulnerability Detector**  
   Uses static program analysis to identify insecure patterns in generated OpenRoad scripts. The detector’s output is used as the quality reward $r_{quality}$ in the reinforcement learning loop.

$$
r_{\text{quality}}= \mathrm{Detector}(\hat y)=
\begin{cases}
1, & \text{if no vulnerabilities are detected},\\
0, & \text{otherwise}.
\end{cases}
$$

   where $\mathrm{Detector}(\hat{y})$ is a binary reward function that assigns a positive reward only when the generated program $\hat{y}$ passes the vulnerability checks without any detected security or maintainability issues.


2. **Program Feedback**  
   Executes the generated scripts in a real environment to assess their functional correctness. The observed results serve as the functional reward $r_{function}$ for reinforcement learning.
   
$$
r_{\text{function}}
= \frac{1}{N}\sum_{i=1}^N \mathbb{1}\{\,f_{\hat y}(\mathrm{inp}_i)=\mathrm{out}_i\,\}
$$   

where $N$ is the total number of unit tests, $\mathbf{1}\{\hat{y}(\mathrm{inp}_i,\mathrm{out}_i)\}$ denotes whether the candidate program $\hat{y}$ generates the ground‐truth result $\mathrm{out}_i$ on the $i$-th unit test $\mathrm{inp}_i$ as expected.

### Hybrid Reward

We merged static and dynamic feedback into a single reward signal:

$$
r_{hybrid} = \alpha \cdot r_{quality}+ (1 - \alpha) \cdot r_{function}
$$

where $\alpha \in [0,1]$ is a weighting coefficient that controls the trade‐off between code quality and functionality. If the policy model $\pi_{\theta}$ fails to generate runnable code (e.g., due to syntax errors, runtime exceptions, etc.), we assign a penalty reward of $-1$.

---
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
### An example of eval on our detector on different datasets
bash experiments/seccodeplt/test_ReaL.sh
```
##Baseline
We chose PromSec, SVEN, and SFT as baselines in this project, You can follow their links to set up and run the baselines
sven:https://github.com/eth-sri/sven
promsec:https://github.com/mahmoudkanazzal/PromSec

---
## Current Result
| #Params | Method  | SecCodePLT+ Function | SecCodePLT+ Quality | SecCodePLT+ Func.-Qual. | SafeSQL Function | SafeSQL Quality | SafeSQL Func.-Qual. |
|:-------:|:--------|---------------------:|--------------------:|------------------------:|-----------------:|---------------:|--------------------:|
| 0.5B    | SVEN    | 0.1707               | 0.3780              | 0.0549                  | 0.3176           | 0.8824         | 0.3059             |
| 0.5B    | PromSec | 0.1341               | 0.3537              | 0.0366                  | 0.3529           | 0.7412         | 0.2235             |
| 0.5B    | SFT     | **0.8720**           | 0.5061              | **0.4573**              | 0.5765           | 0.8706         | 0.5527             |
| 0.5B    | REAL    | 0.5854               | **0.7988**          | 0.3963                  | **0.7647**       | **0.8941**     | **0.6941**         |
| 3B      | SVEN    | 0.3476               | 0.4024              | 0.1646                  | 0.4471           | 0.9294         | 0.4353             |
| 3B      | PromSec | 0.2134               | 0.4146              | 0.0854                  | 0.2000           | 0.9647         | 0.1882             |
| 3B      | SFT     | **0.8902**           | 0.5061              | 0.4573                  | 0.7529           | 0.9176         | 0.6824             |
| 3B      | REAL    | 0.7378               | **0.8476**          | **0.6037**              | **0.8471**       | **1.0000**     | **0.8471**         |
| 7B      | SVEN    | 0.3171               | 0.4024              | 0.1280                  | 0.5059           | 0.9176         | 0.4706             |
| 7B      | PromSec | 0.2195               | 0.4878              | 0.0976                  | 0.0941           | 0.8588         | 0.0824             |
| 7B      | SFT     | **0.8659**           | 0.5122              | 0.4634                  | 0.8118           | 0.8941         | 0.7294             |
| 7B      | REAL    | 0.7561               | **0.8293**          | **0.6159**              | **0.8588**       | **1.0000**     | **0.8588**         |



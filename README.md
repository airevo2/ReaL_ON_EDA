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

Minial Requirement: 24GB GPU memory.
Recommanded GPU: A100 
For 7b Model, we using 2 piece of A100 to training using ReaL framework

---

### Usage Example

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
## Result
We use three different-sized LLMs to do experiments on **qwen2.5-coder**. The REAL framework achieves promising results over baselines. 
| #Params | Method  | SecCodePLT+ Function | SecCodePLT+ Quality | SecCodePLT+ Func.-Qual. |
|:-------:|:--------|:---------------------|:--------------------|:------------------------|
| 0.5B    | SVEN    | 0.1594               | 0.3855              | 0.0548                  |
| 0.5B    | PromSec | 0.1277               | 0.3476              | 0.0372                  |
| 0.5B    | SFT     | **0.8841**           | 0.4964              | **0.4491**              |
| 0.5B    | REAL    | 0.5889               | **0.7836**          | 0.3966                  |
| 3B      | SVEN    | 0.3404               | 0.3977              | 0.1655                  |
| 3B      | PromSec | 0.2090               | 0.4152              | 0.0831                  |
| 3B      | SFT     | **0.8466**           | 0.5040              | 0.4603                  |
| 3B      | REAL    | 0.7840               | **0.8270**          | **0.5618**              |
| 7B      | SVEN    | 0.3190               | 0.4051              | 0.1247                  |
| 7B      | PromSec | 0.2222               | 0.4772              | 0.1002                  |
| 7B      | SFT     | **0.8410**           | 0.5058              | 0.4763                  |
| 7B      | REAL    | 0.7774               | **0.8127**          | **0.6373**              |


Open Road


We use our best 7B model to generate scripts for the 27 distinct EDA tasks. 
Please refer to https://github.com/Colin0vO/ReaL_reproduction.
| #Params | Method  | SecCodePLT+ Function | SecCodePLT+ Quality | SecCodePLT+ Func.-Qual. |
|:-------:|:--------|:---------------------|:--------------------|:------------------------|
| 7B      | REAL    | 0.7777               | 0.8148              | 0.5926                  |

This 
### Evaluation. 
We evaluate REAL along two key dimensions: functionality and quality. For each
dimension, we report the **Pass Rate** as the metric, representing the percentage of tasks that pass all
the unit tests or pass the vulnerability detector, respectively. To jointly assess both dimensions, we
compute the Pass Rate by requiring the generated code to meet both criteria simultaneously.

## Results
We verify the robustness of **REAL** framework on the Python Code Safety improvement. We a 27 distinct tasks.

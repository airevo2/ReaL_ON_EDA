<h1 style="text-align: center;">ReaL: Reinforcement Learning for LLM Safety</h1>

**verl** is a flexible, efficient, and production-ready reinforcement learning library for large language models (LLMs).

This project uses **verl** to run reinforcement learning experiments focused on LLM safety. Please complete the setup as described in the official repository:  
https://github.com/volcengine/verl

---

## Usage

### 1. Training

Below is an example of how to start RL training on **qwen2.5-coder-7b**:

```bash
bash run/seccodeplt/rl/7b/ablation2_detector+safety-unittest.sh
```
### 2. Evaluation

Run the following script to evaluate our safety detector on various datasets:
```bash
###an example of eval on our detector on different datasets
bash experiments/seccodeplt/test_ReaL.sh
```

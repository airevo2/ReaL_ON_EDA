# Copyright 2024 Bytedance Ltd. and/or its affiliates
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# from . import gsm8k, math, prime_math, prime_code


def _default_compute_score(data_source, solution_str, ground_truth, extra_info=None, config=None):
    if data_source == 'openai/gsm8k':
        from . import gsm8k
        res = gsm8k.compute_score(solution_str, ground_truth)
    elif data_source in ['lighteval/MATH', 'DigitalLearningGmbH/MATH-lighteval']:
        from . import math
        res = math.compute_score(solution_str, ground_truth)
    elif data_source in [
            'numina_aops_forum', 'numina_synthetic_math', 'numina_amc_aime', 'numina_synthetic_amc', 'numina_cn_k12',
            'numina_olympiads'
    ]:
        from . import prime_math
        res = prime_math.compute_score(solution_str, ground_truth)
    elif data_source in ['codecontests', 'apps', 'codeforces', 'taco']:
        from . import prime_code
        res = prime_code.compute_score(solution_str, ground_truth, continuous=True)
    elif data_source == 'fengyao1909/go_data':
        from . import go
        res = go.compute_score(solution_str, extra_info=extra_info)
    elif data_source == 'fengyao1909/purplellama':
        from . import purplellama
        res = purplellama.compute_score(solution_str, extra_info=extra_info)
    elif data_source == 'fengyao1909/seccodeplt_ut':
        from . import seccodeplt
        res = seccodeplt.compute_score(solution_str, extra_info=extra_info, safety_ratio=config.safety_ratio, ut_ratio=config.ut_ratio, mypy_ratio=config.mypy_ratio, scpd_ratio=config.scpd_ratio)
        return [float(r) for r in res]  # return multiple scores
    else:
        raise NotImplementedError

    if isinstance(res, (int, float, bool)):
        return float(res)
    else:
        return float(res[0])

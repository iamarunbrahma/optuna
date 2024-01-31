from __future__ import annotations

import numpy as np

from . import _acqf
from ._search_space import sample_normalized_params


def optimize_acqf_sample(
    acqf: _acqf.AcquisitionFunction, n_samples: int = 2048
) -> tuple[np.ndarray, float]:
    # Normalized parameter values are sampled.
    xs = sample_normalized_params(n_samples, acqf.search_space)
    res = _acqf.eval_acqf_no_grad(acqf, xs)
    best_i = np.argmax(res)
    return xs[best_i, :], res[best_i]

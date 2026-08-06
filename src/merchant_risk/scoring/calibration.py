"""Probability of adverse outcome calibration."""

from __future__ import annotations

import math

from merchant_risk.domain.config import get_model_config


def score_to_pd(risk_score: float) -> float:
    """Replaceable logistic calibration: pd = 1 / (1 + exp(-(a + b * score)))."""
    cal = get_model_config()["pd_calibration"]
    a = float(cal["intercept"])
    b = float(cal["slope"])
    z = a + b * risk_score
    # Numerically stable sigmoid
    if z >= 0:
        pd = 1.0 / (1.0 + math.exp(-z))
    else:
        ez = math.exp(z)
        pd = ez / (1.0 + ez)
    return max(0.0, min(1.0, pd))

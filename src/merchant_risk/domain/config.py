"""Load versioned model and policy configuration."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[3]
MODEL_PATH = ROOT / "config" / "model" / "scorecard-0.1.0.yaml"
POLICY_PATH = ROOT / "config" / "policy" / "policy-0.1.0.yaml"


def _load_yaml(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if not isinstance(data, dict):
        raise ValueError(f"Config at {path} must be a mapping")
    return data


@lru_cache(maxsize=1)
def get_model_config() -> dict[str, Any]:
    return _load_yaml(MODEL_PATH)


@lru_cache(maxsize=1)
def get_policy_config() -> dict[str, Any]:
    return _load_yaml(POLICY_PATH)

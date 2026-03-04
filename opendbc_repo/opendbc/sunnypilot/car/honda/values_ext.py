"""
Copyright (c) 2021-, Haibin Wen, sunnypilot, and a number of other contributors.

This file is part of sunnypilot and is licensed under the MIT License.
See the LICENSE.md file in the root directory for more details.
"""

from enum import IntFlag


class HondaFlagsSP(IntFlag):
  # Backward-compatible alias for existing Clarity handling.
  CLARITY = 1
  NIDEC_HYBRID = 1
  EPS_MODIFIED = 2
  HYBRID_ALT_BRAKEHOLD = 4
  HAS_CAMERA_MESSAGES = 8


class HondaSafetyFlagsSP:
  # Backward-compatible alias for existing Clarity handling.
  CLARITY = 1
  NIDEC_HYBRID = 1
  GAS_INTERCEPTOR = 2

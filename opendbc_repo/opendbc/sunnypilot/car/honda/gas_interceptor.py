"""
Copyright (c) 2021-, Haibin Wen, sunnypilot, and a number of other contributors.

This file is part of sunnypilot and is licensed under the MIT License.
See the LICENSE.md file in the root directory for more details.
"""

import numpy as np

from opendbc.car import structs
from opendbc.car.can_definitions import CanData
from opendbc.sunnypilot.car import create_gas_interceptor_command


class GasInterceptorCarController:
  def __init__(self, CP: structs.CarParams, CP_SP: structs.CarParamsSP):
    self.CP = CP
    self.CP_SP = CP_SP

    self.gas = 0.

  def update(self, CC: structs.CarControl, CS: structs.CarState, gas: float, brake: float, wind_brake: float,
             packer, frame: int) -> list[CanData]:
    can_sends = []
    enable_gas_interceptor = bool(getattr(self.CP_SP, "enableGasInterceptor", False))

    if enable_gas_interceptor:
      # Way too aggressive at low speed without this.
      gas_mult = np.interp(CS.out.vEgo, [0., 10.], [0.4, 1.0])
      # Send exactly zero if apply_gas is zero. Interceptor will send the max between
      # read value and apply_gas, preventing unexpected pedal range rescaling.
      if CC.longActive:
        self.gas = float(np.clip(gas_mult * (gas - brake + wind_brake * 3 / 4), 0., 1.))
      else:
        self.gas = 0.0
      can_sends.append(create_gas_interceptor_command(packer, self.gas, frame // 2))

    return can_sends

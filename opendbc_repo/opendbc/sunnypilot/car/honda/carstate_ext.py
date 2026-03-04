"""
Copyright (c) 2021-, Haibin Wen, sunnypilot, and a number of other contributors.

This file is part of sunnypilot and is licensed under the MIT License.
See the LICENSE.md file in the root directory for more details.
"""
from enum import StrEnum

from opendbc.car import Bus, structs
from opendbc.car.common.conversions import Conversions as CV
from opendbc.can.parser import CANParser
from opendbc.sunnypilot.car.honda.values_ext import HondaFlagsSP


class CarStateExt:
  def __init__(self, CP, CP_SP):
    self.CP = CP
    self.CP_SP = CP_SP

  def update(self, ret: structs.CarState, ret_sp: structs.CarStateSP, can_parsers: dict[StrEnum, CANParser]) -> None:
    cp = can_parsers[Bus.pt]
    cp_cam = can_parsers[Bus.cam]

    if self.CP_SP.flags & HondaFlagsSP.HAS_CAMERA_MESSAGES:
      if "CAMERA_MESSAGES" in cp.vl and "SPEED_LIMIT_SIGN" in cp.vl["CAMERA_MESSAGES"]:
        speed_limit_raw = cp.vl["CAMERA_MESSAGES"]["SPEED_LIMIT_SIGN"] % 32
      elif "CAMERA_MESSAGES" in cp_cam.vl and "SPEED_LIMIT_SIGN" in cp_cam.vl["CAMERA_MESSAGES"]:
        speed_limit_raw = cp_cam.vl["CAMERA_MESSAGES"]["SPEED_LIMIT_SIGN"] % 32
      else:
        speed_limit_raw = 0
      ret_sp.speedLimit = speed_limit_raw * 5.0 * CV.MPH_TO_MS if (1 <= speed_limit_raw <= 17) else 0.0

    if self.CP_SP.flags & HondaFlagsSP.CLARITY:
      ret.accFaulted = bool(cp.vl["BRAKE_ERROR"]["BRAKE_ERROR_1"] or cp.vl["BRAKE_ERROR"]["BRAKE_ERROR_2"])
      ret.stockAeb = bool(cp_cam.vl["BRAKE_COMMAND"]["AEB_REQ_1"] and cp_cam.vl["BRAKE_COMMAND"]["COMPUTER_BRAKE_ALT"] > 1e-5)

    if bool(getattr(self.CP_SP, "enableGasInterceptor", False)):
      # Same threshold as panda, equivalent to 1e-5 with previous DBC scaling.
      gas = (cp.vl["GAS_SENSOR"]["INTERCEPTOR_GAS"] + cp.vl["GAS_SENSOR"]["INTERCEPTOR_GAS2"]) // 2
      ret.gasPressed = gas > 492

#! /usr/bin/env python3
import os
import argparse
import subprocess


SYS_POWER_DIR = "/sys/class/power_supply"
AC = f"{SYS_POWER_DIR}/AC/online"



def is_ac_plugged():
  with open(AC, "r") as status:
    ac = status.readline().strip()
    return ac == "1"

def get_battery_info(bat_num):
  path = f"{SYS_POWER_DIR}/BAT{bat_num}"
  with open(os.path.join(path, "status"), "r") as fstatus:
    status = fstatus.readline().rstrip()
  
  with open(os.path.join(path, "capacity"), "r") as fcapacity:
    capacity = int(fcapacity.readline().rstrip())

  return status, capacity 



if __name__ == "__main__":
  print(get_battery_info(0))
  print(get_battery_info(1))
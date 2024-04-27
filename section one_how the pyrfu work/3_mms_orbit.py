'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2024-04-26 22:38:13
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2024-04-26 22:44:59
FilePath: \section one_how the pyrfu work\3_mms_orbit.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from pyrfu import mms
from pyrfu import plot
import matplotlib.pyplot as plt

import requests
response = requests.get('https://lasp.colorado.edu/mms/sdc/public/files/api/v1/', timeout=(10, 30))

tint = ["2015-10-16T00:00:00.000", "2015-10-17T00:00:00.000"] 

data_path = "H:\\MMS data"
mms.download_data("mms_orbit", tint, "1", data_path=data_path)

orbit_data = mms.get_data("mms_orbit", tint, 1, data_path=data_path)

plt.plot(orbit_data[:, 0], orbit_data[:, 1], label="MMS Orbit")
plt.xlabel("X [km]")
plt.ylabel("Y [km]")
plt.title("MMS Satellite Orbit")
plt.legend()
plt.grid()
plt.show()

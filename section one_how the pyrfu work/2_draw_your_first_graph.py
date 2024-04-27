
#this section will teach you how to draw your fist graph

#first download the data, this eara is such an interesting eara because the satellite go through the Sun-side magnetotop

from pyrfu import mms
from pyrfu import pyrf              #this package is used to analising some data
from pyrfu import plot              #this package is used to plotting and visualizing space physics data
import matplotlib.pyplot as plt     #this package is used to create a matplotlib chart

import requests
response = requests.get('https://lasp.colorado.edu/mms/sdc/public/files/api/v1/', timeout=(10, 30))

tint = ["2015-10-16T13:05:00.000", "2015-10-16T13:07:00.000"] 

data_path = "H:\\MMS data"
mms.download_data("b_gsm_fgm_srvy_l2", tint, "1", data_path=data_path)
mms.download_data("vi_gse_fpi_fast_l2", tint, "1", data_path=data_path)


#read data from "H:\\MMS data"
b_gsm = mms.get_data("b_gsm_fgm_srvy_l2", tint, 1, data_path=data_path)
e_gsm = mms.get_data("vi_gse_fpi_fast_l2", tint, 1, data_path=data_path)


f, axs = plt.subplots(2,sharex="all")   #creat a matplotlib chart


plot.plot_line(axs[0], b_gsm[:, 0], color='red', label='$B_x$')
plot.plot_line(axs[0], b_gsm[:, 1], color='green', label='$B_y$')
plot.plot_line(axs[0], b_gsm[:, 2], color='blue', label='$B_z$')


axs[0].legend()  #Set the legend to display
axs[0].set_ylabel("Magnetic Field [nT]") #set the labels for x and y axis
axs[0].set_xlabel("Time [UTC]")

#Draw an electric field strength diagram.
plot.plot_line(axs[1], e_gsm[:, 0], color='red', label='$V_{ix}$')
plot.plot_line(axs[1], e_gsm[:, 1], color='green', label='$V_{iy}$')
plot.plot_line(axs[1], e_gsm[:, 2], color='blue', label='$V_{iz}$')

axs[1].legend()  #Set the legend to display
axs[1].set_ylabel("V_i~[\\mathrm{km}~\\mathrm{s}^{-1}]") #set the labels for x and y axis
axs[1].set_xlabel("Time [UTC]")

plt.show()

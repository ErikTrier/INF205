import matplotlib.pyplot as plt

nr_itteration = [10, 100, 1000, 10000]
time_monte_carlo = [13.795, 104.252, 1232.638, 9500.761]
time_monte_carlo_split_box = [85.854, 835.505, 8355, 83555]  #Two last numbers fals, havent gotten the time 

time_monte_carlo_split_box_fast = [7.216, 10.990, 63.433, 494.070 ]

plt.plot(nr_itteration, time_monte_carlo)
plt.plot(nr_itteration, time_monte_carlo_split_box)
plt.plot(nr_itteration, time_monte_carlo_split_box_fast)
plt.legend(["monte_carlo" , "monte_carlo_split_box_fast"])
plt.title("Time for each directory")
plt.xlabel("Number of iterations")
plt.ylabel("Time in sekunds")
plt.grid()
plt.savefig("timeplot2.pdf")
plt.show()

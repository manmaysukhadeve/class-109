import pandas as pd
import statistics
import csv
df = pd.read_csv('class 109.csv')
height_list = df["Height(Inches)"].to_list()
weight_list = df["Weight(Pounds)"].to_list()
height_mean = statistics.mean(height_list)
weight_mean = statistics.mean(weight_list)
height_mode = statistics.mode(height_list)
weight_mode = statistics.mode(weight_list)
height_median = statistics.median(height_list)
weight_median = statistics.median(weight_list)
print("mean,mode,median of height is {},{},{}".format(height_mean,height_mode,height_median))
print("mean,mode,median of weight is {},{},{}".format(weight_mean,weight_mode,weight_median))
height_std = statistics.stdev(height_list)
weight_std = statistics.stdev(weight_list)
height_firstStd_start,height_firstStd_end = height_mean-height_std,height_mean+height_std
height_secondStd_start,height_secondStd_end = height_mean-(2*height_std),height_mean+(2*height_std)
height_thirdStd_start,height_thirdStd_end = height_mean-(3*height_std),height_mean+(3*height_std)
weight_firstStd_start,weight_firstStd_end = weight_mean-weight_std,weight_mean+weight_std
weight_secondStd_start,weight_secondStd_end = weight_mean-(2*weight_std),weight_mean+(2*weight_std)
weight_thirdStd_start,weight_thirdStd_end = weight_mean-(3*weight_std),weight_mean+(3*weight_std)
height_list_of_data_within_1_std_deviation = [result for result in height_list if result > height_firstStd_start and result < height_firstStd_end]
height_list_of_data_within_2_std_deviation = [result for result in height_list if result > height_secondStd_start and result < height_secondStd_end]
height_list_of_data_within_3_std_deviation = [result for result in height_list if result > height_thirdStd_start and result < height_thirdStd_end]
weight_list_of_data_within_1_std_deviation = [result for result in weight_list if result > weight_firstStd_start and result < weight_firstStd_end]
weight_list_of_data_within_2_std_deviation = [result for result in weight_list if result > weight_secondStd_start and result < weight_secondStd_end]
weight_list_of_data_within_3_std_deviation = [result for result in weight_list if result > weight_thirdStd_start and result < weight_thirdStd_end]
print("{}% of data for height lies within 1 standard deviation".format(len(height_list_of_data_within_1_std_deviation)*100.0/len(height_list)))
print("{}% of data for height lies within 2 standard deviations".format(len(height_list_of_data_within_2_std_deviation)*100.0/len(height_list)))
print("{}% of data for height lies within 3 standard deviations".format(len(height_list_of_data_within_3_std_deviation)*100.0/len(height_list)))
print("{}% of data for weight lies within 1 standard deviation".format(len(weight_list_of_data_within_1_std_deviation)*100.0/len(weight_list)))
print("{}% of data for weight lies within 2 standard deviations".format(len(weight_list_of_data_within_2_std_deviation)*100.0/len(weight_list)))
print("{}% of data for weight lies within 3 standard deviations".format(len(weight_list_of_data_within_3_std_deviation)*100.0/len(weight_list)))

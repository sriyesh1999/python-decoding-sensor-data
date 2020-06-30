# Runner script for all modules
from load_data import load_sensor_data
# Runner script for all modules
from house_info import HouseInfo
##############################
# Do not remove these two lines
# They are needed to validate your unittest
data = []
data=load_sensor_data()


##############################
# Do not remove these two lines
# They are needed to validate your unittest

house_info=HouseInfo(data)
test_area=1
recs=house_info.get_data_by_area()
house_info.get_data_by_area("id",rec_area=test_area)

##############################
print("Sensor Data App")
print("Loaded records:{}".format(len(data)))
##############################

# Module 1 code here:

# Module 2 code here:

print("\nHouse sensor records for area {}:{}".format(test_area,len(recs)))
# Module 3 code here:

# Module 4 code here:

# Module 5 code here:
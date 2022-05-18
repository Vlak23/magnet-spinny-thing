import csv

# We start by creating all of our variables.

magnet_data = []
rotation_data = []
magnet_data_count = 0
old_magnet_value = 0
threshold_value = 0
lastpulsetime = 0
currentpulsetime = 0
with open('magnetsensor.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    # For each row in our data:
    for row in csv_reader:
        # Read the thresholded light value as an integer
      raw_magnet_value = int(row[1])
      if(raw_magnet_value > 52000):
        threshold_value = 1 
  
      else:
        threshold_value = 0 
        
      
        # If the current value is different from the previous one, and the new value is 0, it means the light value has gone from 1 to 0.

        # Write an if-then statement to manage this.
      if old_magnet_value == 1 and threshold_value == 0: 
          magnet_data_count += 1 
          currentpulsetime = float(row[0])
          rotation_data.append([currentpulsetime, 60/(currentpulsetime - lastpulsetime)])
          lastpulsetime = currentpulsetime
        # When this happens, we have completed a pulse of dark-bright-dark and we want to complete a pulse.

        # In this case, add one to blade_count.
        

        # For this method to work, we have to always update the old_light_value with the new one.
      old_magnet_value = threshold_value

      magnet_data.append([row[0],magnet_data_count])
      line_count += 1
    print(f'Processed {line_count} lines.')

# Now that we have processed the raw data, create a new CSV file that has the blade count vs. time data
f = open("rotation_data_output.csv", "w")
for row in rotation_data:
  f.write("{0},{1}\n".format(row[0], row[1]))
f.close()

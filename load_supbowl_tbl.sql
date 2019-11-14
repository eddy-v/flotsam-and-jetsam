# empty the table
DELETE FROM supbowl;

# load new records into it
LOAD DATA LOCAL INFILE 'superbowl.csv' INTO TABLE supbowl;

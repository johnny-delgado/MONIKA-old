import datetime

#take a timestamp in the format "2018-10-12T01:49:00" and convert it into a datetime object
def stringToTimestamp(timestampString):
	year = int(timestampString[:4])
	month = int(timestampString[5:7])
	day = int(timestampString[8:10])
	hour = int(timestampString[11:13])
	minute = int(timestampString[14:16])
	second = int(timestampString[17:19])

	return datetime.datetime(year, month, day, hour, minute, second)
#download the CSV file containing natural gas usage data from SoCalGas website
#select the Q1 2018 file
#https://energydatarequest.socalgas.com/CannedReports/DownloadFile?quarter=Q1%3A%20Jan%20%E2%80%93%20Mar&year=2018

temp <- tempfile()
download.file("https://energydatarequest.socalgas.com/CannedReports/DownloadFile?quarter=Q1%3A%20Jan%20%E2%80%93%20Mar&year=2018",temp)
usagedata <- read.csv(temp)
unlink(temp)
attach(usagedata)
#see the zip codes involved
unique(ZipCode)
#summary of the data set
summary(usagedata)
#display 2018 Q1 Residential Usage for a selected zip code 
ZipUsage <- usagedata[ which(ZipCode==92253 &  CustomerClass=='RESIDENTIAL'),]
View(ZipUsage)

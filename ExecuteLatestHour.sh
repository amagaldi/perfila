#!/bin/bash

# ----------- Date manipulation -------
currHour=`date +%H`
currDate=`date +%Y'-'%m'-'%d`
#echo $currDate

echo python Main.py $currDate $currHour
python Main.py $currDate $currHour

#!/bin/bash

# ----------- Date manipulation -------
currHour=`date +%H`
currDate=`date +%Y'-'%m'-'%d`
#echo $currDate

python Main.py $currDate $currHour

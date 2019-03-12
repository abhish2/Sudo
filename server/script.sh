cd adb
#pwd
#pwd
#./adb devices
#STRING=" This is to inform you that $2 has met with an accident at $3" 
./adb shell am start -a android.intent.action.SENDTO -d sms:$1 --es sms_body " This is to inform you that $2 having license plate no $3 has met with an accident at [lat:$4 and long:$5] at $10 on $6 $7 $8 $9 "  --ez exit_on_sent true
#./adb shell input tap 1000 1700
./adb shell input tap 650 1125
./adb shell am start -a android.intent.action.SENDTO -d sms:$1 --es sms_body " This is to inform you that $2 having license plate no $3 has met with an accident at [lat:$4 and long:$5] at $10 on $6 $7 $8 $9 "  --ez exit_on_sent true
#./adb shell input tap 1000 1700
./adb shell input tap 650 1125

#./adb shell am start -a android.intent.action.SENDTO -d sms:9754754185 --es sms_body " This is to inform you that $2 having license plate no $3 has met with an accident at [lat:$4 and long:$5] at $10 on $6 $7 $8 $9 "  --ez exit_on_sent true
#./adb shell input tap 1000 1700
#./adb shell am start -a android.intent.action.SENDTO -d sms:9754754185 --es sms_body " This is to inform you that $2 having license plate no $3 has met with an accident at [lat:$4 and long:$5] at $10 on $6 $7 $8 $9 "  --ez exit_on_sent true
#./adb shell input tap 1000 1700
#./adb shell am start -a android.intent.action.SENDTO -d sms:9754754185 --es sms_body "Your daughter has smashed the car" --ez exit_on_sent true
#./adb shell input tap 1000 1700
#./adb shell am start -a android.intent.action.SENDTO -d sms:9633799861 --es sms_body " $1 !" --ez exit_on_sent true
#./adb shell input tap 1000 1700
#./adb shell am start -a android.intent.action.SENDTO -d sms:9633799861 --es sms_body "His name is $1 !" --ez exit_on_sent true
#./adb shell input tap 1000 1700
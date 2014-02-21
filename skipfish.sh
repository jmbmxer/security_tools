#bin/sh
#Define global variable
REPORT_DIR=/home/jmesta/mingle
URI_TO_IGNORE=/css/,/img/,/images/,/js/,/doc/
TARGET_URL=https://redspin.mingle-staging.thoughtworks.com/
COOKIE=mingle_13_4_session_id=c498289a30c345bc3b00fda8e77703c4
TARGET_ROOT_URL=$TARGET_URL
INTERACTIVE_MODE=YES


#Clean up report directory if exists...

if [ -d $REPORT_DIR ];
then
 rm -rf $REPORT_DIR
fi

#Define running mode (interactive or quiet)

if [ "$INTERACTIVE_MODE" = "YES" ];
then
 RUNNING_MODE=""
else
 RUNNING_MODE="-u"
fi

#Start scan...

skipfish -b i -I $TARGET_ROOT_URL -X $URI_TO_IGNORE -o $REPORT_DIR -C $COOKIE -M -Q $RUNNING_MODE -G 256 -g 10 -m 10 -f 20 -t 60 -w 60 -i 60 -s 1024000 -e $TARGET_URL


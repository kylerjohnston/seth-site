#!/bin/bash
#
# Script mirrors the contents of seth_site/build to public_html/ on 
# sethbaker.me.
#
# Should be run from the seth-site base directory with username and
# password as arguments, e.g.:
#   $ ./upload.sh myusername mypassword
#
# Copied largely unmodified from StackOverflow:
# http://serverfault.com/questions/24622/how-to-use-rsync-over-ftp
#
# Todo: Enable SSL

HOST="sethbaker.me"
USER=$1
PASS=$2
FTPURL="ftp://$USER:$PASS@$HOST"
LCD=seth_site/build
RCD=public_html/
DELETE="--delete"

echo $FTPURL

lftp -c "set ftp:list-options -a;
set ftp:ssl-allow no;
open '$FTPURL';
lcd $LCD;
cd $RCD;
mirror --reverse \
  $DELETE \
  --verbose \
  --exclude-glob cgi-bin/" 

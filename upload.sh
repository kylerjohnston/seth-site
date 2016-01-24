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

HOST="sethbaker.me"
USER=$1
PASS=$2
FTPURL="sftp://$USER:$PASS@$HOST"
LCD=seth_site/build
RCD=public_html/
DELETE="--delete"

echo $FTPURL

lftp -c "set ftp:list-options -a;
set sftp:auto-confirm true;
open -p 21098 '$FTPURL';
lcd $LCD;
cd $RCD;
mirror --reverse \
  $DELETE \
  --verbose \
  --exclude-glob cgi-bin/" 

#!/bin/bash
MSG="Your server is behind a DDoS Attack! Your server may be at risk!!!!!!!!"
FROM="warning@ddos2track.com"
SUBJECT="Your server is behind a DDoS Attack!"
$(curl "$(cat config/server.txt)/send.php?from=$FROM&subj=$SUBJECT&msg=$MSG&to=$(cat config/emailaddr.txt)" 2> /dev/null) 2> /dev/null
echo "[+] Message sent to: $(cat config/emailaddr.txt)"
echo ""
exit

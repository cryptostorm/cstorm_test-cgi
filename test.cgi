#!/bin/bash
echo -e "Content-type: text/html\r\n"
# /etc/whitelist contains the list of CS IPs
if grep --quiet $REMOTE_ADDR /etc/whitelist; then
# This is for people using wget or curl. It'll only display a single, 
# simple line that's easily `grep`able.
 if [[ $HTTP_USER_AGENT =~ ^Wget* ]] ||
    [[ $HTTP_USER_AGENT =~ ^curl* ]]; then
  echo "$REMOTE_ADDR IS cryptostorm"
 else
  cat << YESFORTHELOVEOFGODYES
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Cryptostorm Darknet</title>
<link rel="shortcut icon" type="image/x-icon" href="favicon-yes.ico" />
<style type="text/css">
body, html {
    background-color:#00aa33;
    color:#000;
    margin:0;
    padding:0;
}
p {
    font-family:"Segoe UI", Candara, "Bitstream Vera Sans", "DejaVu Sans", "Bitstream Vera Sans", "Trebuchet MS", Verdana, "Verdana Ref", sans-serif;
    font-size:3vw;
    text-align:center;
    margin:0;
    padding:0;
}
</style>
</head>
<body>
    <p>You are connected to the Cryptostorm Darknet.<br/>
    Your IP address is: $REMOTE_ADDR</p>
</body>
</html>
YESFORTHELOVEOFGODYES
 fi
else
 if [[ $HTTP_USER_AGENT =~ ^Wget* ]] ||
    [[ $HTTP_USER_AGENT =~ ^curl* ]]; then
  echo "$REMOTE_ADDR IS NOT cryptostorm"
 else
  cat << NONOOMGNO
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Cryptostorm Darknet</title>
<link rel="shortcut icon" type="image/x-icon" href="favicon-no.ico" />
<style type="text/css">
body, html {
    background-color:#ee0033;
    color:#000;
    margin:0;
    padding:0;
}
p {
    font-family:"Segoe UI", Candara, "Bitstream Vera Sans", "DejaVu Sans", "Bitstream Vera Sans", "Trebuchet MS", Verdana, "Verdana Ref", sans-serif;
    font-size:3vw;
    text-align:center;
    margin:0;
    padding:0;
}
</style>
</head>
<body>
    <p>You are <b>NOT</b> connected to the Cryptostorm Darknet.<br/>
    Your IP address is: $REMOTE_ADDR</p>
</body>
</html>
NONOOMGNO
 fi
fi

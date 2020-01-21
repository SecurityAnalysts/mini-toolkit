<?php

$to = $_GET['to'];

$subject = $_GET['subj'];

$message = $_GET['msg'];

$from = $_GET['from'];

$headers = "From:" . $from;


$mail = mail($to, $subject, $message, $headers, $from); 

if($mail) {

  echo "[+] Email sent to $to";

} else {

  echo "[-] Email failed to send";

}

?>

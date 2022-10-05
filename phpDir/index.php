<?php

$servername = "localhost";
$username = "user";
$password = "passwd";

try {
  $conn = new PDO("mysql:host=$servername;", $username, $password);
  // set the PDO error mode to exception
  $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
  $sql = "drop database testi";
  // use exec() because no results are returned
  $conn->exec($sql);
  echo "Connected successfully"; 
} catch(PDOException $e) {
  echo "Connection failed: " . $e->getMessage();
}
?>

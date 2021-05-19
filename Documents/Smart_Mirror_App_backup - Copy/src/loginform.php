<?php

$dbhost = "localhost";
$dbuser = "root";
$dbpass = "mitnicksenpaiphpmyadmin101";
$dbname = "smart-mirror";

$conn = mysqli_connect($dbHost, $dbUser, $dbPass, $dbName);

if ($con) {
} else {
 die("Database connection failed!");
}

<?php
require_once 'includes/loginform.php';
?>

<!DOCTYPE html>
<html lang="en">

<head>
 <meta charset="UTF-8">
 <meta http-equiv="X-UA-Compatible" content="IE=edge">
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <title>Document</title>
</head>

<body>
 <?php
 $sql = "SELECT * FROM users";
 $result = mysqli_query($conn, $sql);
 $rowcount = mysqli_num_rows($result);

 if ($rowcount > 0) {
  while ($row  = mysqli_fetch_assoc($result)) {
   echo $row['username'] . "<br>";
  }
 } else {
  echo "no results found.";
 }




 ?>
</body>

</html>
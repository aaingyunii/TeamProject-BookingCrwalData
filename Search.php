<?php
// header("Content-Type:text/html;charset=utf-8"); 
$q=$_GET['q'] ;
$servername= "localhost";
$username = "root";
$password = "";
$database="travelMaker";
$conn =mysqli_connect($servername,$username,$password,$database);

mysqli_query($conn,"set session character_set_connection=utf8;");
mysqli_query($conn,"set session character_set_results=utf8;");
mysqli_query($conn,"set session character_set_client=utf8;");

$sql = "select city.cityName, count(*) count
    from city, comment
    where city.id=comment.id
    and comment.month='".$q."'
    group by city.cityName
    order by count desc
    limit 3;";
$result = mysqli_query($conn,$sql);

$rankIndex = 1;

while($row = mysqli_fetch_assoc($result)){
   $rank[$rankIndex-1] = $row['cityName'];
   $rankIndex++;
}
#############################################################################
// Accomo rank 1
$sql2 = "select accommoType,numOfCase from accommodation,city where accommodation.id=city.id
        and city.cityName ='".$rank[0]."' order by numOfCase DESC;";
$sql3 = "select accommoType,numOfCase from accommodation,city where accommodation.id=city.id
        and city.cityName ='".$rank[1]."' order by numOfCase DESC;";
$sql4 = "select accommoType,numOfCase from accommodation,city where accommodation.id=city.id
        and city.cityName ='".$rank[2]."' order by numOfCase DESC;";
$result2 = mysqli_query($conn,$sql2);
$result3 = mysqli_query($conn,$sql3);
$result4 = mysqli_query($conn,$sql4);
$rankIndex = 1;
while($row = mysqli_fetch_assoc($result2)){
   $rank2[$rankIndex-1] = $row['accommoType'];
   $rankIndex++;
}
$rankIndex = 1;
while($row = mysqli_fetch_assoc($result3)){
   $rank3[$rankIndex-1] = $row['accommoType'];
   $rankIndex++;
}
$rankIndex = 1;
while($row = mysqli_fetch_assoc($result4)){
   $rank4[$rankIndex-1] = $row['accommoType'];
   $rankIndex++;
}
#############################################################################
$jsql1 = "select family,couple,friends,solo,business from travelType, city
          where city.id=travelType.id
          and city.cityName = '".$rank[0]."'";
$jresult1 = mysqli_query($conn,$jsql1);
$rankIndex = 1;
while($row1 = mysqli_fetch_row($jresult1)){
    $max_0 =0;
    for($i=1; $i<5; $i++){
      if($row1[$i]> $row1[$max_0]){
        $max_0=$i;
      }
    }
    $max_1=0;
    if($max_1==$max_0){
      $max_1++;
    }
    for($i=1; $i<5; $i++){
      if($i != $max_0 && $row1[$i]> $row1[$max_1]){
        $max_1=$i;
      }
    }
  
    $max_2=0;
    for($i=0;$i<5;$i++){
      if($max_2==$max_0){
        $max_2++;
      }
      if($max_2==$max_1){
        $max_2++; 
      }
  }
    for($i=1; $i<5; $i++){
      if($i!= $max_0 && $i!= $max_1){
        if($row1[$i] > $row1[$max_2]){
                  $max_2=$i;
        }
      }
    }
}
switch ($max_0) {
     case 0:
      $tt="family";
      break;
    case 1:
      $tt="couple";
      break;
    case 2:
      $tt="frineds";
        break;
    case 3:
      $tt="solo";
      break;
    case 4:
      $tt="business";
      break;
  }

  switch ($max_1) {
     case 0:
      $tt2="family";
      break;
    case 1:
      $tt2="couple";
      break;
    case 2:
      $tt2="frineds";
        break;
    case 3:
      $tt2="solo";
      break;
    case 4:
      $tt2="business";
      break;
  }
  switch ($max_2) {
     case 0:
      $tt3="family";
      break;
    case 1:
      $tt3="couple";
      break;
    case 2:
      $tt3="frineds";
        break;
    case 3:
      $tt3="solo";
      break;
    case 4:
      $tt3="business";
      break;
  }

######################################################################
$jsql2 = "select family,couple,friends,solo,business from travelType, city
          where city.id=travelType.id
          and city.cityName = '".$rank[1]."'";
$jresult2 = mysqli_query($conn,$jsql2);
$rankIndex = 1;
while($row2 = mysqli_fetch_row($jresult2)){
    $max_01 =0;
    for($i=1; $i<5; $i++){
      if($row2[$i]> $row2[$max_01]){
        $max_01=$i;
      }
    }
    $max_11=0;
    if($max_11==$max_01){
      $max_11++;
    }
    for($i=1; $i<5; $i++){
      if($i != $max_0 && $row[$i]> $row[$max_11]){
        $max_11=$i;
      }
    }
  
    $max_21=0;
    for($i=0;$i<5;$i++){
      if($max_21==$max_01){
        $max_21++;
      }
      if($max_21==$max_11){
        $max_21++; 
      }
  }
    for($i=1; $i<5; $i++){
      if($i!= $max_01 && $i!= $max_11){
        if($row[$i] > $row[$max_21]){
                  $max_21=$i;
        }
      }
    }
}
switch ($max_01) {
     case 0:
      $qq="family";
      break;
    case 1:
      $qq="couple";
      break;
    case 2:
      $qq="frineds";
        break;
    case 3:
      $qq="solo";
      break;
    case 4:
      $qq="business";
      break;
  }

  switch ($max_11) {
     case 0:
      $qq2="family";
      break;
    case 1:
      $qq2="couple";
      break;
    case 2:
      $qq2="frineds";
        break;
    case 3:
      $qq2="solo";
      break;
    case 4:
      $qq2="business";
      break;
  }
  switch ($max_21) {
     case 0:
      $qq3="family";
      break;
    case 1:
      $qq3="couple";
      break;
    case 2:
      $qq3="frineds";
        break;
    case 3:
      $qq3="solo";
      break;
    case 4:
      $qq3="business";
      break;
  }
######################################################################
$jsql3 = "select family,couple,friends,solo,business from travelType, city
          where city.id=travelType.id
          and city.cityName = '".$rank[2]."'";
$jresult3 = mysqli_query($conn,$jsql3);
$rankIndex = 1;
while($row = mysqli_fetch_row($jresult3)){
    $max_02 =0;
    for($i=1; $i<5; $i++){
      if($row[$i]> $row[$max_02]){
        $max_02=$i;
      }
    }
    $max_12=0;
    if($max_12==$max_02){
      $max_12++;
    }
    for($i=1; $i<5; $i++){
      if($i != $max_02 && $row[$i]> $row[$max_12]){
        $max_12=$i;
      }
    }
  
    $max_22=0;
    for($i=0;$i<5;$i++){
      if($max_22==$max_02){
        $max_22++;
      }
      if($max_22==$max_12){
        $max_22++; 
      }
  }
    for($i=1; $i<5; $i++){
      if($i!= $max_02 && $i!= $max_12){
        if($row[$i] > $row[$max_22]){
                  $max_22=$i;
        }
      }
    }
}
switch ($max_02) {
     case 0:
      $ww="family";
      break;
    case 1:
      $ww="couple";
      break;
    case 2:
      $ww="frineds";
        break;
    case 3:
      $ww="solo";
      break;
    case 4:
      $ww="business";
      break;
  }

  switch ($max_12) {
     case 0:
      $ww2="family";
      break;
    case 1:
      $ww2="couple";
      break;
    case 2:
      $ww2="frineds";
        break;
    case 3:
      $ww2="solo";
      break;
    case 4:
      $ww2="business";
      break;
  }
  switch ($max_22) {
     case 0:
      $ww3="family";
      break;
    case 1:
      $ww3="couple";
      break;
    case 2:
      $ww3="frineds";
        break;
    case 3:
      $ww3="solo";
      break;
    case 4:
      $ww3="business";
      break;
  }
?>

<!DOCTYPE html> 
<html>
<title>Search</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
html,body,h1,h2,h3,h4 {font-family:"Lato", sans-serif}

</style>
<body>


<header class="w3-display-container w3-content w3-hide-small" style="max-width:1500px">
  <img class="w3-image w3-opacity" src="https://thecorrespondent.in/wp-content/uploads/2019/03/London-Travel-Guide-achiterual-digest.jpg" alt="London" width="1500%" height="700%" >
  <div class="w3-display-middle" style="width:55%"> 
  <div class="w3-content" style="max-width:1100%;margin-top:80%;margin-bottom:80%">

    <div class="w3-panel" style="text-align:center; font-size:32px;">
      <h1><b>MONTH</b></h1>
    </div>

  <!-- Grid -->
  <div class="w3-container w3-light-grey w3-padding-32">
    <div class="w3-row">
      <div class="w3-container w3-third">
        <h5 class="w3-bottombar w3-border-green" style="text-align:center; font-size:140%;"><b>City</b></h5>
        <h6><button id="rank1_btn" class="w3-button w3-white w3-padding-large w3-large"style="height:50%; width:100%;text-align:left;" onclick="cityChange('rank1_btn')">1. <?php echo $rank[0]; ?></button></h6>
        <h6><button id="rank2_btn" class="w3-button w3-white w3-padding-large w3-large" style="height:50%; width:100%;text-align:left;" onclick="cityChange('rank2_btn')">2. <?php echo $rank[1]; ?></button></h6>
        <h6><button id="rank3_btn" class="w3-button w3-white w3-padding-large w3-large" style="height:50%; width:100%;text-align:left;" onclick="cityChange('rank3_btn')">3. <?php echo $rank[2]; ?></button></h6>
      </div>

      <div class="w3-container w3-third">
        <h5 class="w3-bottombar w3-border-red" style="text-align:center; font-size:130%;"><b>Accommodation</b></h5>
        <h6 id="rank1_accomo" class="w3-light-grey w3-padding-large w3-large" style="text-align:center;height:50%; width:100%;"> </h6>
        <h6 id="rank2_accomo" class="w3-light-grey w3-padding-large w3-large" style="text-align:center;height:50%; width:100%;"> </h6>
        <h6 id="rank3_accomo" class="w3-light-grey w3-padding-large w3-large"  style="text-align:center;height:50%; width:100%;"> </h6>
      </div>

      <div class="w3-container w3-third">
        <h5 class="w3-bottombar w3-border-orange" style="text-align:center; font-size:130%;"><b>Journey Type</b></h5>
        <h6 id="rank1_journey" class="w3-light-grey w3-padding-large w3-large" style="text-align:center;height:50%; width:100%;"> </h6>
        <h6 id="rank2_journey" class="w3-light-grey w3-padding-large w3-large" style="text-align:center;height:50%; width:100%;"> </h6>
        <h6 id="rank3_journey" class="w3-light-grey w3-padding-large w3-large" style="text-align:center;height:50%; width:100%;"> </h6>
      </div>
    </div>
  </div>


<script type="text/javascript">
  function cityChange(id){
    if(id=="rank1_btn"){
      document.getElementById("rank2_btn").className="w3-button w3-white w3-padding-large w3-large";
      document.getElementById("rank3_btn").className="w3-button w3-white w3-padding-large w3-large";
      document.getElementById("rank1_accomo").innerHTML="1. <?php echo $rank2[0]; ?>";
      document.getElementById("rank2_accomo").innerHTML="2. <?php echo $rank2[1]; ?>";
      document.getElementById("rank3_accomo").innerHTML="3. <?php echo $rank2[2]; ?>";
      document.getElementById("rank1_journey").innerHTML="1. <?php echo $tt; ?>";
      document.getElementById("rank2_journey").innerHTML="2. <?php echo $tt2; ?>";
      document.getElementById("rank3_journey").innerHTML="3. <?php echo $tt3; ?>";

    }else if(id=="rank2_btn"){
      document.getElementById("rank1_btn").className="w3-button w3-white w3-padding-large w3-large";
      document.getElementById("rank3_btn").className="w3-button w3-white w3-padding-large w3-large";
      document.getElementById("rank1_accomo").innerHTML="1. <?php echo $rank3[0]; ?>";
      document.getElementById("rank2_accomo").innerHTML="2. <?php echo $rank3[1]; ?>";
      document.getElementById("rank3_accomo").innerHTML="3. <?php echo $rank3[2]; ?>";
      document.getElementById("rank1_journey").innerHTML="1. <?php echo $qq; ?>";
      document.getElementById("rank2_journey").innerHTML="2. <?php echo $qq2; ?>";
      document.getElementById("rank3_journey").innerHTML="3. <?php echo $qq3; ?>";

    }else if(id=="rank3_btn"){
      document.getElementById("rank2_btn").className="w3-button w3-white w3-padding-large w3-large";
      document.getElementById("rank1_btn").className="w3-button w3-white w3-padding-large w3-large";
      document.getElementById("rank1_accomo").innerHTML="1. <?php echo $rank4[0]; ?>";
      document.getElementById("rank2_accomo").innerHTML="2. <?php echo $rank4[1]; ?>";
      document.getElementById("rank3_accomo").innerHTML="3. <?php echo $rank4[2]; ?>";
      document.getElementById("rank1_journey").innerHTML="1. <?php echo $ww; ?>";
      document.getElementById("rank2_journey").innerHTML="2. <?php echo $ww2; ?>";
      document.getElementById("rank3_journey").innerHTML="3. <?php echo $ww3; ?>";
    }
     
    document.getElementById(id).className="w3-button w3-grey w3-padding-large w3-large";      
    
    console.log('done');
    }
  

</script>

</body>
</html>


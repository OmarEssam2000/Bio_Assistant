<!DOCTYPE html>
<html lang="en">
    <head>

        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title> bio assistant</title>
        <link rel="stylesheet" href="css/bootstrap.min.css"/>
        <script src="js/jquery-3.5.1.slim.min.js"></script>
        <script src="js/popper.min.js"></script>
        <script src="js/bootstrap.min.js"></script>
        
        <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.0/css/all.css" integrity="sha384-lZN37f5QGtY3VHgisS14W3ExzMWZxybE1SJSEsQp9S+oqd12jhcu+A56Ebc1zFSJ" crossorigin="anonymous">
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
            integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous" />
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.7.0/font/bootstrap-icons.css" />
        <link rel="stylesheet" href="css/all.min.css" />
        <link rel="stylesheet" href="css/hover-min.css" />
        <link rel="stylesheet" href="css/lightGallery.css" />
        <link rel="stylesheet" href="css/aos.css" />
        <link rel="stylesheet" href="css/style.css" />
      <style>

           *{margin: 0;padding: 0; }
          .bg-blue{background-color: #45748C;}
          .bg-red{background-color: #AD5258;}
          .bg-yellow{background-color: #EF972C;}
          .back{background-image: url(images/back.jpg);*margin: 0;*padding: 0; background-size: 100%100%; background-attachment: fixed;background-repeat: no-repeat;}
          .txtblue{color: #45748C;}
          .fontlogo{ font-family: Segoe Print;color: #45748C;font-size: 66;}                           
         .searchbox{width: 340px;height: 50px;padding: 0 25px;border-radius: 10px 0 0 10px;} 
         .searchbtn{border-radius: 0 10px 10px 0;height:50px ;width: 150px; ;} 
         .put{  z-index: 1; background-color: white;border-radius: 100%;border: 1px solid #45748C ; text-align: center;margin-bottom:90px ;position: absolute; font-size: large; width: 80px;height: 80px;}                         
         .btnn{ width: 120px;height: 100px; background-color:white;color: #45748C; font-size: 13px;text-align: center;border-radius: 4px;}
         .btnn:hover{ color: white;background-color: #45748C;border:3px solid white;font-size: 15px;}
         .findbtn:hover{border: 4px solid #AD5258;}
      
     </style>


    </head>
    <body class="back ">

      <!--navbar-->
      <header>
            <nav class="navbar  navbar-light bg-light  ">
                <div class=" container-fluid " >
                    <div class=" d-inline-flex ">
                        
                        <img src="images/logo.png" width="60" height="60" class="ml-3 " /> 
                        <a class="navbar-brand txtblue mb-1"><h3 class="fontlogo" ><b>Bio Assistant</b> </h3></a>
                     </div>
                  <div class="navbar " style="border: red; background-color:transparent;">
                      <nav class=" navbar  navbar-light bg-light">
                            <div class=" container-fluid">
                              <form class="d-inline-flex">
                                <input class="form-control me-1 text-dark searchbox" type="search" placeholder="Search" aria-label="Search" title="Search !" style="width: 4cm;">
                                <button class="btn bg-blue searchbtn" type="submit" style="width: 1.6cm;"><img src="images/search icon.png" width="20" height="20"></button>
                              </form>
                              <a href="index.html" style="text-decoration : none; "><img src="images/profile.png " width="35" height="35" style="margin-right: 6px;" class="ml-5 rounded-circle" title="Sign Up !" ><span class="fw-bolder text-primary">Logout !</span></a>
                           </div>
                       </nav>
                  </div>
                </div>
            </nav>
         </header>




          


<!--tap (home,my squenses,learning)-->

    <!--Start Section Nav-->
    <section class="navbar" style="margin-bottom: 2cm;">
      <div class="container d-flex justify-content-between align-items-center">
          <div>
              <ul class="order d-flex justify-content-between align-items-center">
                <li > <a href="index2.html"  >Home</a></li>
                <li class="bg-white" style="border-radius:8px;" ><a style="color:#45748C;" href="registration/register.php">Bioinformatics experiments</a></li>
                <li ><a href="learning2.html">Learning</a></li>
                

              </ul>
          </div>

          <div>
              <ul class="list d-flex justify-content-between align-items-center">
                  <li><a href="https://www.instagram.com"><i class="bi bi-instagram"></i></a></li>
                  <li><a href="https://www.twitter.com"><i class="bi bi-twitter"></i></a></li>
                  <li><a href="https://www.facebook.com"><i class="bi bi-facebook"></i></a></li>
              </ul>
          </div>
      </div>
  </section>
          




<!---main card -->
<div class="card col-6 bg-blue p-5 m-lg-auto align-items-center" style="border-radius: 20px;">
        <!--caption-->
        <p class="text-white font-weight-bold mb-lg-4">
                These Functions return the result in the same area,replacing the initial sequence:
         
        </p>
        
        <form class="container " action="home.php" method="get" style="margin-bottom: 3pc;">
            
               <label class="put  position-absolute   txtblue font-weight-bold"><br>INPUT</label>
               <br><br>
               <div class="card bg-white rounded mb-5 mt-1 " style="width: 37pc; height: 8pc;"  > 
                <h3 style=" height: 5pc; width: 12cm; border-radius:5px ; margin:auto ;text-align:center ; background-color:silver; color:#45748C">Complement of DNA sequence</h3>

                   <input class="mt-4 ml-3 mr-3 border-white" name="name1" cols="78" rows="10" style="overflow-y: scroll;" placeholder=" ENTER THE SEQUENCE">
                   <button type="submit" style="width: 3pc; height:2pc; background-color:thistle; margin:auto;">Try !</button>
                </div>
        </form>        
           
        <?php
            error_reporting(0);
            $complement = $_GET['name1'];
            $s1 = exec("py mazen/complement_of_dna.py '".$complement."'");
            echo'<div class="alert alert-secondary" role="alert">The reverse sequence is '.$s1.'</div>';
        ?>
        <form class="container " action="home.php" method="get" style="margin-bottom: 3pc;">
            
            <label class="put  position-absolute   txtblue font-weight-bold"><br>INPUT</label>
            <br><br>
            <div class="card bg-white rounded mb-5 mt-1 " style="width: 37pc; height: 8pc;"  > 
             <h3 style=" height: 5pc; width: 12cm; border-radius:5px ; margin:auto ;text-align:center ; background-color:silver; color:#45748C">DNA to RNA</h3>

                <input class="mt-4 ml-3 mr-3 border-white" name="name2" cols="78" rows="10" style="overflow-y: scroll;" placeholder=" ENTER THE SEQUENCE">
                <button type="submit" style="width: 3pc; height:2pc; background-color:thistle; margin:auto;">Try !</button>
             </div>
            
        </form>
        <?php
           $dna_to_rna = $_GET['name2'];
           $rna = str_replace( 'T' , 'U',$dna_to_rna );
           print_r('<div class="alert alert-secondary" role="alert">The RNA sequence is '.$rna.'</div>');

            
        ?>
        <form class="container " action="home.php" method="get" style="margin-bottom: 3pc;">
            
            <label class="put  position-absolute   txtblue font-weight-bold"><br>INPUT</label>
            <br><br>
            <div class="card bg-white rounded mb-5 mt-1 " style="width: 37pc; height: 8pc;"  > 
             <h3 style=" height: 5pc; width: 12cm; border-radius:5px ; margin:auto ;text-align:center ; background-color:silver; color:#45748C">counting neocletides</h3>

                <input class="mt-4 ml-3 mr-3 border-white" name="name3" cols="78" rows="10" style="overflow-y: scroll;" placeholder=" ENTER THE SEQUENCE">
                <button type="submit" style="width: 3pc; height:2pc; background-color:thistle; margin:auto;">Try !</button>
             </div>
            
        </form>
        <?php
            $counting_nucles = $_GET['name3'];
            
            $A =  substr_count($counting_nucles, 'A');
            $C =  substr_count($counting_nucles, 'C');
            $G =  substr_count($counting_nucles, 'G');
            $T =  substr_count($counting_nucles, 'T');
            echo('<div class="alert alert-secondary" role="alert">The number of bases in dna sequence is A : '.$A.' C : '.$C.' G : '.$G.' T : '.$T.'</div>');
        ?>
        <form class="container " action="home.php" method="get" style="margin-bottom: 3pc;">
            
            <label class="put  position-absolute   txtblue font-weight-bold"><br>INPUT</label>
            <br><br>
            <div class="card bg-white rounded mb-5 mt-1 " style="width: 37pc; height: 8pc;"  > 
             <h3 style=" height: 5pc; width: 12cm; border-radius:5px ; margin:auto ;text-align:center ; background-color:silver; color:#45748C">RNA to protein</h3>

                <input class="mt-4 ml-3 mr-3 border-white" name="name4" cols="78" rows="10" style="overflow-y: scroll;" placeholder=" ENTER THE SEQUENCE">
                <button type="submit" style="width: 3pc; height:2pc; background-color:thistle; margin:auto;">Try !</button>
             </div>
            
         </form>
         <?php
            $rna_to_protein = $_GET['name4'];
            $protein = shell_exec("py mazen/rnatoprotin.py '".$rna_to_protein."'");
            echo'<div class="alert alert-secondary" role="alert">The protein is '.$protein.'</div>';
        ?>
         <form class="container " action="home.php" method="get" style="margin-bottom: 3pc;">
            
            <label class="put  position-absolute   txtblue font-weight-bold"><br>INPUT</label>
            <br><br>
            <div class="card bg-white rounded mb-5 mt-1 " style="width: 37pc; height: 8pc;"  > 
             <h3 style=" height: 5pc; width: 12cm; border-radius:5px ; margin:auto ;text-align:center ; background-color:silver; color:#45748C">Valodation of DNA</h3>

                <input class="mt-4 ml-3 mr-3 border-white" name="name5" cols="78" rows="10" style="overflow-y: scroll;" placeholder=" ENTER THE SEQUENCE">
                <button type="submit" style="width: 3pc; height:2pc; background-color:thistle; margin:auto;">Try !</button>
             </div>
            
        </form>
        <?php
            $validation = $_GET['name5'];
            $s5 = shell_exec("py mazen/validatin_of_dna.py '".$validation."'");
            echo'<div class="alert alert-secondary" role="alert">The dna sequence is '.$s5.'</div>';
        ?>
        
        <form class="container " action="home.php" method="get" style="margin-bottom: 3pc;">
            
            <label class="put  position-absolute   txtblue font-weight-bold"><br>INPUT</label>
            <br><br>
            <div class="card bg-white rounded mb-5 mt-1 " style="width: 37pc; height: 12pc;"  > 
             <h3 style=" height: 5pc; width: 12cm; border-radius:5px ; margin:auto ;text-align:center ; background-color:silver; color:#45748C">Point mutations</h3>

                <input class="mt-4 ml-3 mr-3 border-white" name="name6" cols="78" rows="10" style="overflow-y: scroll;" placeholder=" ENTER FIRST SEQUENCE">
                <input class="mt-4 ml-3 mr-3 border-white" name="name7" cols="78" rows="10" style="overflow-y: scroll;" placeholder=" ENTER SECOND SEQUENCE">

                <button type="submit" style="width: 3pc; height:2pc; background-color:thistle; margin:auto;">Try !</button>
             </div>
            
        </form>
        <?php
            $s6 = $_GET['name6'];
            $s7 = $_GET['name7'];
            
            $mutations = shell_exec("py mazen/pointmutations.py  '".$s6."' '".$s7."'");
                echo'<div class="alert alert-secondary" role="alert">The number of mutations is '.$mutations.'</div>';
            

        ?>
        <form class="container " action="home.php" method="get" style="margin-bottom: 3pc;">
            
            <label class="put  position-absolute   txtblue font-weight-bold"><br>INPUT</label>
            <br><br>
            <div class="card bg-white rounded mb-5 mt-1 " style="width: 37pc; height:12pc;"  > 
             <h3 style=" height: 5pc; width: 12cm; border-radius:5px ; margin:auto ;text-align:center ; background-color:silver; color:#45748C">Pattern matching</h3>

                <input class="mt-4 ml-3 mr-3 border-white" name="name8" cols="78" rows="10" style="overflow-y: scroll;" placeholder=" ENTER THE SEQUENCE">
                <input class="mt-4 ml-3 mr-3 border-white" name="name9" cols="78" rows="10" style="overflow-y: scroll;" placeholder=" ENTER THE pattern">
                <button type="submit" style="width: 3pc; height:2pc; background-color:thistle; margin:auto;">Try !</button>
             </div>
                
             
            
        </form>
        <?php
            $first_seq_match = $_GET['name8'];
            $second_seq_match = $_GET['name9'];
        
            // PHP program for Naive Pattern
            // Searching algorithm

            function search($pat, $txt)
            {
                $M = strlen($pat);
                $N = strlen($txt);

                // A loop to slide pat[]
                // one by one
                for ($i = 0; $i <= $N - $M; $i++)
                {

                    // For current index i,
                    // check for pattern match
                    for ($j = 0; $j < $M; $j++)
                        if ($txt[$i + $j] != $pat[$j])
                            break;

                    // if pat[0...M-1] =
                    // txt[i, i+1, ...i+M-1]
                    if ($j == $M)
                         echo'<div class="alert alert-secondary" role="alert">Pattern found at index  '.$i.'</div>';
                }
            }

                
                search($second_seq_match, $first_seq_match);
          
            

            ?>
            
            
        
       

        <!--services -->
      
            
        <!--card of search pattern-->
        <div class="" >
            <div class="collapse collapse-horizontal mr-5" id="collapseWidthExample" style="width: 37pc; height: 18pc;">
              <div class="card card-body mb-4 mt-4  bg-light" >
                <p class="txtblue font-weight-bold">Find text that matches this regular expression:</p>
                <form class="row">
                    <input class="form-control me-2 text-dark border-dark " type="text" placeholder="ENTER YOUR PATTERN" >
                    <div class="col-6">
                    <button class="btn findbtn mt-3 text-white bg-yellow font-weight-bold a" type="submit">find by Naive algorithm</button>
                    <button class="btn findbtn mt-3 text-white bg-yellow font-weight-bold " type="submit">find by KMP algorithm</button>
                    </div>
                    <div class="col-6">
                    <button class="btn findbtn mt-3 text-white bg-yellow font-weight-bold " type="submit">find by Boyer moore algorithm</button>
                    <button class="btn findbtn mt-3 text-white bg-yellow font-weight-bold  " type="submit"> find by Rabin_Karp algorithm  </button>       
                   </div>
                  </form>
              </div>
            </div>
          </div>
         

          

         <!--output card-->
        
</div>




    
          



<script src="home.js"></script>

</body>






<section class="footer p-3">
  <div class="container">
      <div class="row">
          <div class="col-4">
              <div class="info">
                  <ul>
                      <li><a href="#">About Us</a></li>
                      <li><a href="#">Contact</a></li>
                      <li><a href="#">Terms & Conditions</a></li>
                  </ul>
              </div>
          </div>
          <div class="col-4">
              <div class="links">
                  <ul>
                      <li><a href="https://www.facebook.com"><i class="bi bi-facebook"></i> Facebook</a></li>
                      <li><a href="https://www.twitter.com"><i class="bi bi-twitter"></i> Twiteer</a></li>
                      <li><a href="https://www.instagram.com"><i class="bi bi-instagram"></i> Instagrm</a></li>
                  </ul>
              </div>
          </div>
          <div class="col-4">
              <div class="emails">
                  <ul>
                      <li><a href="#">457 Ray New York  America </a></li>
                      <li><a href="#">+44 345 678 903  </a></li>
                      <li><a href="#">adobex@mail.com</a></li>
                  </ul>
              </div>
          </div>
      </div>
  </div>
</section>
<!--End of section footer -->









</html>

<?php include('server.php') ?>
<!DOCTYPE html>
<html>
<head>
	<title>Registration system PHP and MySQL</title>
	<link rel="stylesheet" type="text/css" href="style.css">
</head>
<style>



body{
		background-color:#45748c;
		font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;	}
	.header{
		background-color:#0064a0;
		margin-top: 12px;
	}
	.qabl{
		justify-content: center;
		display: flex ;
		width: 20%;
		margin: auto;
		margin-top: 5px;
	}
	form{
		margin-top: -15px;
	}
	.qabl img{
		width: 75px;
	}
	.qabl h3{
		margin-top: 22.5px;
		color: white;
	}




</style>
<body>
<div class="qabl">
	<img src="../images/logo.png" alt="">
	<h3>Bio Assistant</h3>
	</div>
	
	
	<div class="header">
		<h2>Login</h2>
	</div>
	
	<form method="post" action="login.php">

		<?php include('errors.php'); ?>

		<div class="input-group">
			<label>Username</label>
			<input type="text" name="username" >
		</div>
		<div class="input-group">
			<label>Password</label>
			<input type="password" name="password">
		</div>
		<div class="input-group">
			<button type="submit" class="btn" name="login_user">Login</button>
		</div>
		<p>
			Not yet a member? <a href="register.php">Sign up</a>
		</p>
		<p>
		<a href="../index.html">Back to main page</a>
		</p>
	</form>


</body>
</html>
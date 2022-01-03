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
		font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
	}
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
		<h2>Register</h2>
	</div>
	
	<form method="post" action="register.php">

		<?php include('errors.php'); ?>

		<div class="input-group">
			<label>Username</label>
			<input type="text" name="username" value="<?php echo $username; ?>">
		</div>
		<div class="input-group">
			<label>Email</label>
			<input type="email" name="email" value="<?php echo $email; ?>">
		</div>
		<div class="input-group">
			<label>Password</label>
			<input type="password" name="password_1">
		</div>
		<div class="input-group">
			<label>Confirm password</label>
			<input type="password" name="password_2">
		</div>
		<div class="input-group">
			<button type="submit" class="btn" name="reg_user">Register</button>
		</div>
		<p>
			Already a member? <a href="login.php">Sign in</a>
		</p>
		<p>
		<a href="../index.html">Back to main page</a>
		</p>
	</form>
</body>
</html>
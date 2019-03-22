{% extends 'base_file.py' %}

{% block title %}Rafael Cenzano - Raf{% endblock %}

{% block meta %}

	<!-- Facebook -->
	<meta property="og:url" content="https://www.rafaelcenzano.me/">

	<!-- Twitter -->
	<meta name="twitter:url" content="https://www.rafaelcenzano.me/">

{% endblock %}

{% block head_css %}

    <link rel="stylesheet" type="text/css" href={{ url_for('static', filename='css/main/home.css') }}>

	<link href='https://fonts.googleapis.com/css?family=Josefin+Sans' rel='stylesheet' type='text/css'>

	<link href='https://use.fontawesome.com/releases/v5.7.1/css/all.css' rel='stylesheet' type='text/css'>

{% endblock %}

{% block content %}

	<article class="color-changer">
  		<h1>RAFAEL CENZANO</h1>
		<img src="https://rafaelcenzano-com.herokuapp.com/static/img/profile.jpeg" alt="Rafael Cenzano's profile image" class="profile">
	</article>
	<div class="social-buttons">
  		<a href="#" class="social-buttons__button social-button social-button--facebook" aria-label="Facebook">
    		<span class="social-button__inner">
     			<i class="fab fa-facebook-f"></i>
    		</span>
  		</a>
  		<a href="#" class="social-buttons__button social-button social-button--linkedin" aria-label="LinkedIn">
    		<span class="social-button__inner">
     			<i class="fab fa-linkedin-in"></i>
    		</span>
  		</a>
  		<a href="#" class="social-buttons__button social-button social-button--github" aria-label="GitHub">
    		<span class="social-button__inner">
     			<i class="fab fa-github"></i>
    		</span>
  		</a>
	</div>

{% endblock %}

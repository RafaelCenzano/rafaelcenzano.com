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

	<link rel="stylesheet" type="text/css" href="https://fonts.googleapis.com/css?family=Ubuntu:regular,bold&subset=Latin">

{% endblock %}

{% block content %}

	<article class="color-changer">
  		<h1>RAFAEL CENZANO</h1>
		<img src={{ url_for('static', filename='img/profile.jpeg') }} alt="Rafael Cenzano's profile image" class="profile">
	</article>
	<div class="social-buttons">
  		<a href="https://www.facebook.com/profile.php?id=100008046498255" class="social-buttons__button social-button social-button--facebook" target="_blank" aria-label="Facebook">
    		<span class="social-button__inner">
     			<i class="fab fa-facebook-f"></i>
    		</span>
  		</a>
  		<a href="https://www.linkedin.com/in/rafael-cenzano/" class="social-buttons__button social-button social-button--linkedin" target="_blank" aria-label="LinkedIn">
    		<span class="social-button__inner">
     			<i class="fab fa-linkedin-in"></i>
    		</span>
  		</a>
  		<a href="https://github.com/RafaelCenzano" class="social-buttons__button social-button social-button--github" target="_blank" aria-label="GitHub">
    		<span class="social-button__inner">
     			<i class="fab fa-github"></i>
    		</span>
  		</a>
	</div>
	<div class="button-wrapper">
  		<a href="#"><button>Contact me !</button></a>
	</div>
	<div class="title-wrapper">
  		<u><h2>Projects<h2></u>
	</div>
	<div class="projects">
		<div class="project-base">
			<a href="https://www.rafaelcenzano.me/lowelldashboard" class="project-url">
        	    <h3 class="project-title">Lowell Dashboard</h3>
        	    <p class="project-description">
        	    	A website created using Flask App Builder. The website is a dashboard for student at Lowell High School.
                </p>
                <p class="project-description">
                	Includes resources like up to date news, pdf textbooks, and a place to post homework for a class to help connect students and relieve the stress of having to look far and wide for resources.
                </p>
       		</a>
       	</div>
       	<div class="project-base">
			<a href="https://www.rafaelcenzano.me/marvinvirtualassistant" class="project-url">
        	    <h3 class="project-title">Marvin Virtual Assistant</h3>
        	    <p class="project-description">
        	    	A virtual assistant in python that currently has 3 versions. This is a project that has tons of room to grow and will always be updated with hopes to have it be a open source project people want to join in.
        	    </p>
       		</a>
       	</div>
    </div>
    <footer>
        <p class="copyright">© 2019 Rafael Cenzano</p>
        <div class="source-wrapper">
            <a href="https://github.com/RafaelCenzano/rafaelcenzano.com">
                <p class="source">Source</p>
            </a>
        </div>
    </footer>

{% endblock %}

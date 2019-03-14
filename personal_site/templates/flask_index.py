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

	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

{% endblock %}

{% block content %}

	<!-- The social media icon bar -->
	<div class="icon-bar">
		<a href="#" class="github"><i class="fa fa-github" aria-hidden="true"></i></a>
		<a href="#" class="linkedin"><i class="fa fa-linkedin" aria-hidden="true"></i></a>
  		<a href="#" class="facebook"><i class="fa fa-facebook" aria-hidden="true"></i></a>

	</div>
    <h1>Rafael Cenzano</h1>
    <img src={{ url_for('static', filename='img/profile.jpeg') }} alt="Rafael Cenzano Profile Image" height="200" width="200">

{% endblock %}

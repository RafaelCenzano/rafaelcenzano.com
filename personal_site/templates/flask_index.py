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

{% endblock %}

{% block content %}

	<article class="color-changer">
  		<h1>RAFAEL CENZANO</h1>
		<img src={{ url_for('static', filename='img/profile.jpeg') }} alt="Rafael Cenzano's profile image" class="profile">
	</article>
	<h2>Projects</h1>

{% endblock %}

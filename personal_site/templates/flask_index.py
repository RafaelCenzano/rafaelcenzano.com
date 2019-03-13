{% extends 'base_file.py' %}

{% block title %}Rafael Cenzano{% endblock %}

{% block meta %}
	<!-- Facebook -->
	<meta property="og:url" content="http://rafaelcenzano.com/">
	<meta property="og:image" content="{{ url_for('static', filename='img/profile.jpeg') }}">
	<meta property="og:description" content="Personal website to display Rafael Cenzano's work">
	<meta property="og:title" content="Rafael Cenzano">
	<meta property="og:site_name" content="Rafael Cenzano's Personal website">
	<meta property="og:see_also" content="http://rafaelcenzano.com">

	<!-- Twitter -->
	<meta name="twitter:card" content="Rafael Cenzano's Personal website">
	<meta name="twitter:url" content="http://rafaelcenzano.com/">
	<meta name="twitter:title" content="Rafael Cenzano">
	<meta name="twitter:description" content="Personal website to display Rafael Cenzano's work">
	<meta name="twitter:image" content="{{ url_for('static', filename='img/profile.jpeg') }}">

	<!-- Google+ -->
	<meta itemprop="name" content="Rafael Cenzano">
	<meta itemprop="description" content="Personal website to display Rafael Cenzano's work">
	<meta itemprop="image" content="{{ url_for('static', filename='img/profile.jpeg') }}">
{% endblock %}

{% block head_css %}
    <link rel="stylesheet" type="text/css" href={{ url_for('static', filename='css/main/home.css') }}>
{% endblock %}

{% block content %}
  <h1>Rafael Cenzano</h1>
{% endblock %}

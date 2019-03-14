{% extends 'base_file.py' %}

{% block title %}My Experiences{% endblock %}

{% block meta %}

	<!-- Facebook -->
	<meta property="og:url" content="https://www.rafaelcenzano.me/resume">

	<!-- Twitter -->
	<meta name="twitter:url" content="https://www.rafaelcenzano.me/resume">

{% endblock %}

{% block head_css %}
    <link rel="stylesheet" type="text/css" href={{ url_for('static', filename='css/main/resume.css') }}>
{% endblock %}

{% block content %}
  <h1>Rafael Cenzano</h1>
{% endblock %}

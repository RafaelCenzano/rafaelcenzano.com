{% extends 'base_file.py' %}

{% block title %}Server Error{% endblock %}

{% block meta %}

	<!-- Facebook -->
	<meta property="og:url" content="https://www.rafaelcenzano.me/500">

	<!-- Twitter -->
	<meta name="twitter:url" content="https://www.rafaelcenzano.me/500">

{% endblock %}

{% block head_css %}

    <link rel="stylesheet" type="text/css" href={{ url_for('static', filename='css/main/500.css') }}>

{% endblock %}

{% block content %}
	<div class="title">
		<h1 id="spinner">SERVER</h1>
    	<h1 id="spinner">ERROR</h1>
	</div>
{% endblock %}

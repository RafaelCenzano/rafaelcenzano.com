{% extends 'base_file.py' %}

{% block title %}Message Sent!{% endblock %}

{% block meta %}

	<!-- Facebook -->
	<meta property="og:url" content="https://www.rafaelcenzano.me/contact">

	<!-- Twitter -->
	<meta name="twitter:url" content="https://www.rafaelcenzano.me/contact">

{% endblock %}

{% block head_css %}

    <link rel="stylesheet" type="text/css" href={{ url_for('static', filename='css/main/success.css') }}>

{% endblock %}

{% block content %}
    <h1>Success!</h1>
    <h2>Message sent</h2>
{% endblock %}

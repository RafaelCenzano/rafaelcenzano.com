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
{% endblock %}

{% block content %}
  <h1>Rafael Cenzano</h1>
{% endblock %}

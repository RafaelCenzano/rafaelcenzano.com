<!DOCTYPE html>
<html>
<head>
	<!-- Title -->
	<title>{% block title %}{% endblock %}</title>

	<!-- Meta Data -->
	<meta charset="utf-8">
	<meta name="robots" content="index,follow">
	<meta name="theme-color" content="#ffffff">
	<meta name="viewport" content="width=device-width,initial-scale=1">
	<meta name="keywords" content="Rafael Cenzano">
	<meta name="description" content="Website for Rafael Cenzano.">
	<meta name="msapplication-TileColor" content="#da532c">
	<link rel="author" href="https://www.rafaelcenzano.me">
	<link rel="canonical" href="https://www.rafaelcenzano.me">

	<!-- Favicon -->
	<link rel="apple-touch-icon" sizes="180x180" href="{{ url_for('static', filename='img/apple-touch-icon.png') }}">
	<link rel="icon" type="image/png" sizes="32x32" href="{{ url_for('static', filename='img/favicon-32x32.png') }}">
	<link rel="icon" type="image/png" sizes="16x16" href="{{ url_for('static', filename='img/favicon-16x16.png') }}">
	<link rel="manifest" href="{{ url_for('static', filename='img/site.webmanifest') }}">
	<link rel="mask-icon" href="{{ url_for('static', filename='img/safari-pinned-tab.svg') }}" color="#5bbad5">
	<meta name="msapplication-TileColor" content="#da532c">
	<meta name="theme-color" content="#ffffff">

	<!-- Facebook -->
	<meta property="og:image" content={{ url_for('static', filename='img/profile.jpeg') }}>
	<meta property="og:description" content="Personal website to display Rafael Cenzano's work">
	<meta property="og:title" content="Rafael Cenzano">
	<meta property="og:site_name" content="Rafael Cenzano's Personal website">
	<meta property="og:see_also" content="https://www.rafaelcenzano.me">

	<!-- Twitter -->
	<meta name="twitter:card" content="Rafael Cenzano's Personal website">
	<meta name="twitter:title" content="Rafael Cenzano">
	<meta name="twitter:description" content="Personal website to display Rafael Cenzano's work">
	<meta name="twitter:image" content={{ url_for('static', filename='img/profile.jpeg') }}>

	<!-- Google+ -->
	<meta itemprop="name" content="Rafael Cenzano">
	<meta itemprop="description" content="Personal website to display Rafael Cenzano's work">
	<meta itemprop="image" content={{ url_for('static', filename='img/profile.jpeg') }}>

	{% block meta %}
	{% endblock %}
    {% block head_css %}
    {% endblock %}
    {% block head_js %}
    {% endblock %}
</head>
<body>
    {% block content %}
    {% endblock %}
    {% block trailing_js %}
    {% endblock %}
</body>
</html>

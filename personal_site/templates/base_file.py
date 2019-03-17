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
	<meta name="description" content="Website for Lowell High School's Dev Club.">
	<meta name="msapplication-TileColor" content="#da532c">
	<link rel="author" href="https://www.rafaelcenzano.me">
	<link rel="canonical" href="https://www.rafaelcenzano.me">

	<!-- Favicon -->
	<link rel="apple-touch-icon" sizes="57x57" href={{ url_for('static', filename='img/apple-icon-57x57.png') }}>
	<link rel="apple-touch-icon" sizes="60x60" href={{ url_for('static', filename='img/apple-icon-60x60.png') }}>
	<link rel="apple-touch-icon" sizes="72x72" href={{ url_for('static', filename='img/apple-icon-72x72.png') }}>
	<link rel="apple-touch-icon" sizes="76x76" href={{ url_for('static', filename='img/apple-icon-76x76.png') }}>
	<link rel="apple-touch-icon" sizes="114x114" href={{ url_for('static', filename='img/apple-icon-114x114.png') }}>
	<link rel="apple-touch-icon" sizes="120x120" href={{ url_for('static', filename='img/apple-icon-120x120.png') }}>
	<link rel="apple-touch-icon" sizes="144x144" href={{ url_for('static', filename='img/apple-icon-144x144.png') }}>
	<link rel="apple-touch-icon" sizes="152x152" href={{ url_for('static', filename='img/apple-icon-152x152.png') }}>
	<link rel="apple-touch-icon" sizes="180x180" href={{ url_for('static', filename='img/apple-icon-180x180.png') }}>
	<link rel="icon" type="image/png" sizes="192x192"  href={{ url_for('static', filename='img/android-icon-192x192.png') }}>
	<link rel="icon" type="image/png" sizes="32x32" href={{ url_for('static', filename='img/favicon-32x32.png') }}>
	<link rel="icon" type="image/png" sizes="96x96" href={{ url_for('static', filename='img/favicon-96x96.png') }}>
	<link rel="icon" type="image/png" sizes="16x16" href={{ url_for('static', filename='img/favicon-16x16.png') }}>
	<link rel="manifest" href="/manifest.json">
	<meta name="msapplication-TileColor" content="#ffffff">
	<meta name="msapplication-TileImage" content={{ url_for('static', filename='img/ms-icon-144x144.png') }}>
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

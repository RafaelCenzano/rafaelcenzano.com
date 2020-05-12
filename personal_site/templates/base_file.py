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
	<link rel="author" href="https://rafaelcenzano.com">

	<!-- Favicon -->
	<link rel="icon" type="image/png" sizes="32x32" href="{{ url_for('static', filename='img/favicon-32x32.png') }}">
	<link rel="icon" type="image/png" sizes="96x96" href="{{ url_for('static', filename='img/favicon-96x96.png') }}">

	<!-- Apple Icon -->
	<link rel="apple-touch-icon" sizes="57x57"   href="{{ url_for('static', filename='img/apple-icon-57x57.png') }}">
	<link rel="apple-touch-icon" sizes="60x60"   href="{{ url_for('static', filename='img/apple-icon-60x60.png') }}">
	<link rel="apple-touch-icon" sizes="72x72"   href="{{ url_for('static', filename='img/apple-icon-72x72.png') }}">
	<link rel="apple-touch-icon" sizes="76x76"   href="{{ url_for('static', filename='img/apple-icon-76x76.png') }}">
	<link rel="apple-touch-icon" sizes="114x114" href="{{ url_for('static', filename='img/apple-icon-114x114.png') }}">
	<link rel="apple-touch-icon" sizes="120x120" href="{{ url_for('static', filename='img/apple-icon-120x120.png') }}">
	<link rel="apple-touch-icon" sizes="144x144" href="{{ url_for('static', filename='img/apple-icon-144x144.png') }}">
	<link rel="apple-touch-icon" sizes="152x152" href="{{ url_for('static', filename='img/apple-icon-152x152.png') }}">
	<link rel="apple-touch-icon" sizes="180x180" href="{{ url_for('static', filename='img/apple-icon-180x180.png') }}">

	<!-- Andriod Icon -->
	<link rel="icon" type="image/png" sizes="48x48"    href="{{ url_for('static', filename='img/android-icon-48x48.png') }}">
	<link rel="icon" type="image/png" sizes="72x72"    href="{{ url_for('static', filename='img/android-icon-72x72.png') }}">
	<link rel="icon" type="image/png" sizes="96x96"    href="{{ url_for('static', filename='img/android-icon-96x96.png') }}">
	<link rel="icon" type="image/png" sizes="144x144"  href="{{ url_for('static', filename='img/android-icon-144x144.png') }}">
	<link rel="icon" type="image/png" sizes="192x192"  href="{{ url_for('static', filename='img/android-icon-192x192.png') }}">
	<meta name="msapplication-TileColor" content="#da532c">
	<meta name="theme-color" content="#dddddd">

	<!-- Facebook -->
	<meta property="og:title" content="Rafael Cenzano">
	<meta property="og:site_name" content="Rafael Cenzano's Personal website">
	<meta property="og:description" content="Personal website to display Rafael Cenzano's work">
	<meta property="og:url" content="https://rafaelcenzano.com/">
	<meta property="og:image" content="{{ url_for('static', filename='img/rafael_profile_square.jpeg') }}">

	<!-- Twitter -->
	<meta name="twitter:title" content="Rafael Cenzano">
	<meta name="twitter:card" content="Rafael Cenzano's Personal website">
	<meta name="twitter:description" content="Personal website to display Rafael Cenzano's work">	
	<meta name="twitter:url" content="https://rafaelcenzano.com/">
	<meta name="twitter:image" content="{{ url_for('static', filename='img/rafael_profile_square.jpeg') }}">

	<!-- Google+ -->
	<meta itemprop="name" content="Rafael Cenzano">
	<meta itemprop="description" content="Personal website to display Rafael Cenzano's work">
	<meta itemprop="image" content="{{ url_for('static', filename='img/rafael_profile_square.jpeg') }}">

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

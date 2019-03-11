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

	<!-- Favicon -->
    <link rel="apple-touch-icon" sizes="180x180" href="{{ url_for('static', filename='img/apple-touch-icon.png') }}">
    <link rel="icon" type="image/png" sizes="32x32" href="{{ url_for('static', filename='img/favicon-32x32.png') }}">
    <link rel="icon" type="image/png" sizes="16x16" href="{{ url_for('static', filename='img/favicon-16x16.png') }}">
    <link rel="mask-icon" href="{{ url_for('static', filename='img/safari-pinned-tab.svg') }}" color="#5bbad5">

	<!-- Facebook -->
	<meta property="og:url" content="http://www.lowelldev.club">
	<meta property="og:image" content="/static/img/High_Resolution_dev_club_logo.png">
	<meta property="og:description" content="Website for Lowell High School's Dev Club.">
	<meta property="og:title" content="Rafael Cenzano">
	<meta property="og:site_name" content="Rafael Cenzano">
	<meta property="og:see_also" content="http://www.lowelldev.club">

	<!-- Twitter -->
	<meta name="twitter:card" content="Rafael Cenzano">
	<meta name="twitter:url" content="http://www.lowelldev.club">
	<meta name="twitter:title" content="Rafael Cenzano">
	<meta name="twitter:description" content="Website for Lowell High School's Dev Club.">
	<meta name="twitter:image" content="/static/img/High_Resolution_dev_club_logo.png">

	<!-- Google+ -->
	<meta itemprop="name" content="Rafael Cenzano">
	<meta itemprop="description" content="Website for Lowell High School's Dev Club.">
	<meta itemprop="image" content="/static/img/High_Resolution_dev_club_logo.png">

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

<!DOCTYPE html>
<html lang="en">
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
	<link rel="icon" type="image/png" sizes="32x32" href="https://rafael.sirv.com/Images/faivon.png?w=32&png.optimize=true">
	<link rel="icon" type="image/png" sizes="64x64" href="https://rafael.sirv.com/Images/faivon.png?w=64&png.optimize=true">
	<link rel="icon" type="image/png" sizes="96x96" href="https://rafael.sirv.com/Images/faivon.png?w=96&png.optimize=true">
	<link rel="icon" type="image/png" sizes="100x100" href="https://rafael.sirv.com/Images/faivon.png?w=100&png.optimize=true">
	<link rel="icon" type="image/png" sizes="200x200" href="https://rafael.sirv.com/Images/faivon.png?w=200&png.optimize=true">
	<link rel="icon" type="image/png" sizes="300x300" href="https://rafael.sirv.com/Images/faivon.png?w=300&png.optimize=true">
	<link rel="icon" type="image/png" sizes="400x400" href="https://rafael.sirv.com/Images/faivon.png?w=400&png.optimize=true">
	<link rel="icon" type="image/png" sizes="500x500" href="https://rafael.sirv.com/Images/faivon.png?w=500&png.optimize=true">
	<link rel="alternate icon" href="https://rafael.sirv.com/Images/favicon.ico">

	<!-- Apple Icon -->
	<link rel="apple-touch-icon" sizes="57x57"   href="https://rafael.sirv.com/Images/faivon.png?w=57&png.optimize=true">
	<link rel="apple-touch-icon" sizes="60x60"   href="https://rafael.sirv.com/Images/faivon.png?w=60&png.optimize=true">
	<link rel="apple-touch-icon" sizes="72x72"   href="https://rafael.sirv.com/Images/faivon.png?w=72&png.optimize=true">
	<link rel="apple-touch-icon" sizes="76x76"   href="https://rafael.sirv.com/Images/faivon.png?w=76&png.optimize=true">
	<link rel="apple-touch-icon" sizes="114x114" href="https://rafael.sirv.com/Images/faivon.png?w=114&png.optimize=true">
	<link rel="apple-touch-icon" sizes="120x120" href="https://rafael.sirv.com/Images/faivon.png?w=120&png.optimize=true">
	<link rel="apple-touch-icon" sizes="144x144" href="https://rafael.sirv.com/Images/faivon.png?w=144&png.optimize=true">
	<link rel="apple-touch-icon" sizes="152x152" href="https://rafael.sirv.com/Images/faivon.png?w=152&png.optimize=true">
	<link rel="apple-touch-icon" sizes="180x180" href="https://rafael.sirv.com/Images/faivon.png?w=180&png.optimize=true">

	<!-- Andriod Icon -->
	<link rel="icon" type="image/png" sizes="36x36"    href="https://rafael.sirv.com/Images/faivon.png?w=36&png.optimize=true">
	<link rel="icon" type="image/png" sizes="48x48"    href="https://rafael.sirv.com/Images/faivon.png?w=48&png.optimize=true">
	<link rel="icon" type="image/png" sizes="72x72"    href="https://rafael.sirv.com/Images/faivon.png?w=72&png.optimize=true">
	<link rel="icon" type="image/png" sizes="96x96"    href="https://rafael.sirv.com/Images/faivon.png?w=96&png.optimize=true">
	<link rel="icon" type="image/png" sizes="144x144"  href="https://rafael.sirv.com/Images/faivon.png?w=144&png.optimize=true">
	<link rel="icon" type="image/png" sizes="192x192"  href="https://rafael.sirv.com/Images/faivon.png?w=192&png.optimize=true">

	<!-- Facebook -->
	<meta property="og:title" content="Rafael Cenzano">
	<meta property="og:site_name" content="Rafael Cenzano's Personal website">
	<meta property="og:description" content="Personal website to display Rafael Cenzano's work">
	<meta property="og:url" content="https://rafaelcenzano.com/">
	<meta property="og:image" content="https://rafael.sirv.com/Images/rafael.jpeg">

	<!-- Twitter -->
	<meta name="twitter:title" content="Rafael Cenzano">
	<meta name="twitter:card" content="Rafael Cenzano's Personal website">
	<meta name="twitter:description" content="Personal website to display Rafael Cenzano's work">	
	<meta name="twitter:url" content="https://rafaelcenzano.com/">
	<meta name="twitter:image" content="https://rafael.sirv.com/Images/rafael.jpeg">

	<!-- Google+ -->
	<meta itemprop="name" content="Rafael Cenzano">
	<meta itemprop="description" content="Personal website to display Rafael Cenzano's work">
	<meta itemprop="image" content="https://rafael.sirv.com/Images/rafael.jpeg">

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

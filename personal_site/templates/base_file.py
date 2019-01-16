<!DOCTYPE html>
<html>
  <head>
    {% block head_meta %}
      <!-- Title & SEO -->
      <meta name="keywords" content="rafael,cenzano,rafael cenzano,san francisco,hackthefog,hack the fog,marvin virtual assistant,random coders">
      <meta name="image" content="{{ url_for('static', filename='img/profile.jpeg') }}">
      <title>Rafael Cenzano</title>
      <meta name="description" content="Lowell Help Forum News Page.">
      <meta charset='utf-8'>

      <!-- Viewport -->
      <meta name="viewport" content="width=device-width, initial-scale=1">

      <!-- Theming & Site Icons -->
      <link rel="apple-touch-icon" sizes="180x180" href="{{ url_for('static', filename='img/apple-touch-icon.png') }}">
      <link rel="icon" type="image/png" sizes="32x32" href="{{ url_for('static', filename='img/favicon-32x32.png') }}">
      <link rel="icon" type="image/png" sizes="16x16" href="{{ url_for('static', filename='img/favicon-16x16.png') }}">
      <link rel="mask-icon" href="{{ url_for('static', filename='img/safari-pinned-tab.svg') }}" color="#5bbad5">
      <meta name="msapplication-TileColor" content="#da532c">
      <meta name="theme-color" content="#ffffff">
    {% endblock %}
    {% block head_css %}
      <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/lib/bootstrap.min.css') }}">
    {% endblock %}
    {% block head_js %}{% endblock %}
  </head>
  <body>
    {% block content %}
    {% endblock %}
    {% block trailing_js %}
    {% endblock %}
  </body>
</html>

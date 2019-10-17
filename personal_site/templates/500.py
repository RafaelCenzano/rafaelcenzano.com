{% extends 'base_file.py' %}

{% block title %}Server Error{% endblock %}

{% block head_css %}

    <link rel="stylesheet" type="text/css" href={{ url_for('static', filename='css/main/500.css') }}>

{% endblock %}

{% block content %}
	<h1>500</h1>
{% endblock %}

{% extends 'base_file.py' %}

{% block title %}404 not found{% endblock %}

{% block head_css %}

    <link rel="stylesheet" type="text/css" href={{ url_for('static', filename='css/main/404.css') }}>

{% endblock %}

{% block content %}
	<div id="background-wrap">
   		<div class="x1">
        	<div class="cloud"></div>
    	</div>
    	<div class="x2">
        	<div class="cloud"></div>
    	</div>
    	<div class="x3">
        	<div class="cloud"></div>
    	</div>
    	<div class="x4">
        	<div class="cloud"></div>
    	</div>
    	<div class="x5">
        	<div class="cloud"></div>
    	</div>
        <div class="x6">
            <div class="cloud"></div>
        </div>
        <div class="x7">
            <div class="cloud"></div>
        </div>
        <div class="x8">
            <div class="cloud"></div>
        </div>
	</div>
	<h1>404</h1>
{% endblock %}

{% extends 'base_file.py' %}

{% block title %}Plasma Cube{% endblock %}

{% block head_css %}
<link href='http://fonts.googleapis.com/css?family=Open+Sans' rel='stylesheet' type='text/css'>
<link rel="stylesheet" href="{{ url_for('static', filename='css/apjava.min.css') }}">
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/home.min.css') }}">
{% endblock %}

{% block head_js %}
<script type="text/javascript" src="{{ url_for('static', filename='js/p5.min.js') }}"></script>
{% endblock %}

{% block content %}
		<header>
			<h1>Plasma Cube</h1>
		</header>
			<div class="button-wrapper center">
	        	<a href="{{ url_for('apjava') }}" class="back-other">Back</a>
	    	</div>
            <br>
			<section id="content">
				<canvas id="Lightning" data-processing-sources="{{ url_for('static', filename='lightning/Lightning.pde') }}">
				</canvas>
		    </section>
	    <div class="footer">
		    Created by Rafael for APCS A (Java) with Processing
		</div>
        {% include 'footer.py' %}
{% endblock %}

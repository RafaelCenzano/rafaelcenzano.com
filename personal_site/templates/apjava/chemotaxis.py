{% extends 'base_file.py' %}

{% block title %}Plague{% endblock %}

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
			<h1>The Plague</h1>
		</header>
			<div class="button-wrapper center">
	        	<a href="{{ url_for('apjava') }}" class="contact">Back</a>
	    	</div>
            <br>
			<section id="content">
				<canvas id="Chemotaxis" data-processing-sources="{{ url_for('static', filename='chemotaxis/Chemotaxis.pde') }}">
				</canvas>
		    </section>
	    <footer>
	    	The Plague always takes everything over...
	    	But a cure can restart its process until further mutations (Click)
	    	<br>
		    Created by Rafael for APCS A (Java) with Processing
		    <p class="copyright">© 2019 Rafael Cenzano</p>
            <div class="source-wrapper">
                <p>
                    <a href="https://github.com/RafaelCenzano/rafaelcenzano.com" class="source">Source</a>
                </p>
            </div>
	    </footer>
{% endblock %}

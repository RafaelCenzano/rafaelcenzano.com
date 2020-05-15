{% extends 'base_file.py' %}

{% block title %}U.S.S. Discovery{% endblock %}

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
			<h1>Starship Discovery</h1>
		</header>
		<div class="button-wrapper center">
        	<a href="{{ url_for('apjava') }}" class="back-other">Back</a>
    	</div>
    	<br>
		<section id="content">
			<canvas id="AsteroidsGame" data-processing-sources="{{ url_for('static', filename='asteroids/AsteroidsGame.pde') }} {{ url_for('static', filename='asteroids/Floater.pde') }}  {{ url_for('static', filename='asteroids/Spaceship.pde') }} {{ url_for('static', filename='asteroids/Star.pde') }} {{ url_for('static', filename='asteroids/Asteroid.pde') }} {{ url_for('static', filename='asteroids/Bullet.pde') }}">
			</canvas>
	    </section>
	    <div class="footer">
	    	1 - shooting projectiles<br>
	    	2 - hyperspace (there is a cooldown delay)<br>
	    	3 - turn left<br>
	    	4 - turn right<br>
	    	5 - accelerate<br>
	    	6 - hyperspeed (Multiplies speed)<br>
	    	7 - deccelerate to a stop<br>

	    	Black Alert! Black Alert! Black Alert! Black Alert!<br>
		    Created by Rafael for APCS A (Java) with Processing
		</div>
		{% include 'footer.py' %}
{% endblock %}

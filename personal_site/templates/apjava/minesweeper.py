{% extends 'base_file.py' %}

{% block title %}Minesweeper{% endblock %}

{% block head_css %}
<link href='http://fonts.googleapis.com/css?family=Open+Sans' rel='stylesheet' type='text/css'>
<link rel="stylesheet" href="{{ url_for('static', filename='css/apjava.min.css') }}">
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/home.min.css') }}">
{% endblock %}

{% block head_js %}
<script type="text/javascript" src="{{ url_for('static', filename='js/p5.min.js') }}"></script>
<script type="text/javascript" src="{{ url_for('static', filename='js/Guido.js') }}"></script>
{% endblock %}

{% block content %}
        <header>
            <h1>Mining but avoid the mines</h1>
        </header>
        <div class="button-wrapper center">
            <a href="{{ url_for('apjava') }}" class="back-other">Back</a>
        </div>
        <br>
        <section id="content">
            <canvas id="Minesweeper" data-processing-sources="{{ url_for('static', filename='minesweeper/Minesweeper.pde') }}">
            </canvas>
        </section>
        <div class="desc">
            Created by Rafael for APCS A (Java) with Processing
            <br>
            <a href="https://github.com/RafaelCenzano/Minesweeper" class="pdesource">Check out the code!</a>
        </div>
        {% include 'footer.py' %}
{% endblock %}

{% extends 'base_file.py' %}

{% block title %}Minesweeper{% endblock %}

{% block head_css %}
<link href='http://fonts.googleapis.com/css?family=Open+Sans' rel='stylesheet' type='text/css'>
<link rel="stylesheet" href="{{ url_for('static', filename='css/apjava.min.css') }}">
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/home.min.css') }}">
{% endblock %}

{% block head_js %}
<script type="text/javascript" src="{{ url_for('static', filename='js/p5.min.js') }}"></script>
<script type="text/javascript" src="{{ url_for('static', filename='js/guido.js') }}"></script>
{% endblock %}

{% block content %}
        <header>
            <h1>Mining but avoid the mines</h1>
        </header>
            <div class="button-wrapper center">
                <a href="{{ url_for('apjava') }}" class="contact">Back</a>
            </div>
            <br>
            <section id="content">
                <canvas id="Minesweeper" data-processing-sources="{{ url_for('static', filename='minesweeper/Minesweeper.pde') }}">
                </canvas>
            </section>
        <footer>
            Created by Rafael for APCS A (Java) with Processing
            <p class="copyright">© 2020 Rafael Cenzano</p>
            <div class="source-wrapper">
                <p>
                    <a href="https://github.com/RafaelCenzano/rafaelcenzano.com" class="source">Source</a>
                </p>
            </div>
        </footer>
{% endblock %}

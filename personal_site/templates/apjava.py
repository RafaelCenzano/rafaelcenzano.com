{% extends 'base_file.py' %}

{% block title %}Rafael Cenzano{% endblock %}

{% block head_css %}

    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/home.min.css') }}">

    <link href='https://use.fontawesome.com/releases/v5.7.1/css/all.css' rel='stylesheet' type='text/css'>

    <style type="text/css">
    @media (min-width:801px) {
      body {
        /* Fix background during scrolling */
        background-attachment: fixed;
        /* Use scalable background image */
        background-image: url("{{ url_for('static', filename='img/bkgrdhalf2.jpeg') }}");
        background-position: center center;
        background-attachment: fixed;
        -ms-background-size: cover;
        background-size: cover;
      }
    }
    </style>

{% endblock %}

{% block content %}

    <div class="body-wrapper">
        <article class="color-changer">
            <h1 class="top-title">AP JAVA</h1>
        </article>
        <br>
        <div class="button-wrapper center">
            <a href="{{ url_for('index') }}" class="contact">Home</a>
        </div>
        <br>
        <div class="experiences center things">
            <h4><a href="/apjava/asteroids" class="experience">Asteroids Game</a></h4>
            <p class="current-experience-description experience-description">
                <a class="experience-link" href="/apjava/asteroids">Semi-functional asteroids game. Includes movements, projectiles, and hyperspace.</a>
            </p>
        </div>
        <br>
        <div class="experiences center things">
            <h4><a href="/apjava/chemotaxis" class="experience">Chemotaxis</a></h4>
            <p class="current-experience-description experience-description">
                <a class="experience-link" href="/apjava/chemotaxis">Random walking particles that eventually overtake each other.</a>
            </p>
        </div>
        <br>
        <div class="experiences center things">
            <h4><a href="/apjava/originalfractal" class="experience">Custom Fractal</a></h4>
            <p class="current-experience-description experience-description">
                <a class="experience-link" href="/apjava/originalfractal">Random circles made recursively.</a>
            </p>
        </div>
        <br>
        <div class="experiences center things">
            <h4><a href="/apjava/dice" class="experience">Dice</a></h4>
            <p class="current-experience-description experience-description">
                <a class="experience-link" href="/apjava/dice">Object Oriented Dice utilizing 2D arrays and displaying many dice and the totals of your rolls.</a>
            </p>
        </div>
        <br>
        <div class="experiences center things">
            <h4><a href="/apjava/fractaltree" class="experience">Fractal Tree</a></h4>
            <p class="current-experience-description experience-description">
                <a class="experience-link" href="/apjava/fractaltree">Recursive fractal tree that uses random values to make the tree sway in the "wind".</a>
            </p>
        </div>
        <br>
        <div class="experiences center things">
            <h4><a href="/apjava/lightning" class="experience">Lightning</a></h4>
            <p class="current-experience-description experience-description">
                <a class="experience-link" href="/apjava/lightning">Random walking lines that create lightning to look like a plasma ball.</a>
            </p>
        </div>
        <br>
        <div class="experiences center things">
            <h4><a href="/apjava/minesweeper" class="experience">Minesweeper</a></h4>
            <p class="current-experience-description experience-description">
                <a class="experience-link" href="/apjava/tendron">Minesweeper game made with guido library. Contains Object Oriented code, recursion, and 2 dimensional arrays</a>
            </p>
        </div>
        <br>
        <div class="experiences center things">
            <h4><a href="/apjava/sierpinskitriangle" class="experience">Sierpinski Triangle</a></h4>
            <p class="current-experience-description experience-description">
                <a class="experience-link" href="/apjava/sierpinskitriangle">A simple recursive sierpinski triangle.</a>
            </p>
        </div>
        <br>
        <div class="experiences center things">
            <h4><a href="/apjava/starfield" class="experience">Star Field</a></h4>
            <p class="current-experience-description experience-description">
                <a class="experience-link" href="/apjava/starfield">Object Oriented program that utilizes Arraylists to create particles to make a warp effect.</a>
            </p>
        </div>
        <br>
        <div class="experiences center things">
            <h4><a href="/apjava/tendron" class="experience">Tendron</a></h4>
            <p class="current-experience-description experience-description">
                <a class="experience-link" href="/apjava/tendron">Recursive fractal tendril program.</a>
            </p>
        </div>
        <br>
        <footer>
            <p class="copyright">© 2020 Rafael Cenzano</p>
            <div class="source-wrapper">
                <p>
                    <a href="https://github.com/RafaelCenzano/rafaelcenzano.com" class="source">Source</a>
                </p>
            </div>
        </footer>
    </div>

{% endblock %}

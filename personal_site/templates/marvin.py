{% extends 'base_file.py' %}

{% block title %}Marvin{% endblock %}

{% block head_css %}

    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/home.min.css') }}">

    <style type="text/css">
    @media (min-width:950px) {
      body {
        /* Fix background during scrolling */
        background-attachment: fixed;
        /* Use scalable background image */
        background-image: url("{{ url_for('static', filename='img/bkgrdhalf3.jpeg') }}");
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
            <h1 class="top-title">Marvin</h1>
        </article>
        <br>
        <div class="button-wrapper center">
            <a href="{{ url_for('index') }}" class="back">Home</a>
        </div>
        <br>
        <div class="experiences center things">
            <h4><a href="https://github.com/Marvin-Virtual-Assistant" target="_blank" class="experience">MVA</a></h4>
            <p class="current-experience-description experience-description">
                <a class="experience-link" href="https://github.com/Marvin-Virtual-Assistant" target="_blank">Marvin Virtual Asssitant is a Github organization I own. I have brought some friends into the organization and they have helped with a few things through out the different versions of Marvin.</a>
            </p>
        </div>
        <br>
        <div class="experiences center things">
            <h4><a href="https://github.com/Marvin-Virtual-Assistant/Marvin-V4" target="_blank" class="experience">V4</a></h4>
            <p class="current-experience-description experience-description">
                <a class="experience-link" href="https://github.com/Marvin-Virtual-Assistant/Marvin-V4" target="_blank">Version 4.0 of Marvin. Version 4 has a Flask app for the GUI and utilizes more advanced coding techniques to make code more effiecient. It has been devloped a ton on ceratin features but there is still much work to be done to regain and refactor past features of Marvin projects.</a>
            </p>
        </div>
        <br>
        <div class="experiences center things">
            <h4><a href="https://github.com/Marvin-Virtual-Assistant/notebooks" target="_blank" class="experience">Notebooks</a></h4>
            <p class="current-experience-description experience-description">
                <a class="experience-link" href="https://github.com/Marvin-Virtual-Assistant/notebooks" target="_blank">Jupyter notebooks for Marvin version 4.0. I experiment and test code in jupyter notebooks which are published in a seperate repo to keep the repos cleaner and so testing and feature devlopment progress can be seen online.</a>
            </p>
        </div>
        <br>
        <div class="experiences center things">
            <h4><a href="https://github.com/Marvin-Virtual-Assistant/Marvin-v3-client" target="_blank" class="experience">V3 - client</a></h4>
            <p class="current-experience-description experience-description">
                <a class="experience-link" href="https://github.com/Marvin-Virtual-Assistant/Marvin-v3-client" target="_blank">Version 3.0 of Marvin for clients. I attempted to create a client version of marvin that could work with the server version to create a better experience but due to the server version not working out this version in turned failed because it was initially built to work with the server version.</a>
            </p>
        </div>
        <br>
        <div class="experiences center things">
            <h4><a href="https://github.com/Marvin-Virtual-Assistant/Marvin-v3-server" target="_blank" class="experience">V3 - server</a></h4>
            <p class="current-experience-description experience-description">
                <a class="experience-link" href="https://github.com/Marvin-Virtual-Assistant/Marvin-v3-server" target="_blank">Version 3.0 of Marvin in the cloud. I attempted to create flask app api that could be called by the client version but it was too slow and never worked like I had wished.</a>
            </p>
        </div>
        <br>
        <div class="experiences center things">
            <h4><a href="https://github.com/Marvin-Virtual-Assistant/MARVIN_2.0" target="_blank" class="experience">V2</a></h4>
            <p class="current-experience-description experience-description">
                <a class="experience-link" href="https://github.com/Marvin-Virtual-Assistant/MARVIN_2.0" target="_blank">Version 2.0 of Marvin. I refactored a huge amount of the code and created many new features. It was a great success and allowed me to learn new strategies for coding and python code. It is on the inefficient side due to putting together code from many different sources.</a>
            </p>
        </div>
        <br>
        <div class="experiences center things">
            <h4><a href="https://github.com/Marvin-Virtual-Assistant/Marvin" target="_blank" class="experience">V1</a></h4>
            <p class="current-experience-description experience-description">
                <a class="experience-link" href="https://github.com/Marvin-Virtual-Assistant/Marvin" target="_blank">My original marvin virtual assistant. It one of my <strong>first</strong> projects. It has simple python code allowing it to give users cool functions but due to my inexperience with coding at the time it is highly inefficient.</a>
            </p>
        </div>
        <br>
        {% include 'footer.py' %}
    </div>

{% endblock %}
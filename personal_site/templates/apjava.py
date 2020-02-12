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
    </div>

{% endblock %}

{% extends 'base_file.py' %}

{% block title %}Server Error{% endblock %}

{% block head_css %}

    <link rel="stylesheet" type="text/css" href={{ url_for('static', filename='css/500.css') }}>

{% endblock %}

{% block content %}
    <div class="body-wrapper">
        <article class="color-changer">
            <h1 class="top-title">500</h1>
        </article>
    </div>
{% endblock %}

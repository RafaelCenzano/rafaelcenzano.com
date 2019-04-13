{% extends 'base_file.py' %}

{% block title %}Contact Me{% endblock %}

{% block meta %}

	<!-- Facebook -->
	<meta property="og:url" content="https://www.rafaelcenzano.me/contact/">

	<!-- Twitter -->
	<meta name="twitter:url" content="https://www.rafaelcenzano.me/contact/">

{% endblock %}

{% block head_css %}

    <link rel="stylesheet" type="text/css" href={{ url_for('static', filename='css/main/contact.css') }}>
	
{% endblock %}

{% block content %}

    <h1>Contact Me</h1>
    <h2>Contact Form</h2>

    {% with messages = get_flashed_messages(with_categories=true) %}
    {% if messages %}
        <ul>
            {% for message in messages %}
            <li>{{ message[1] }}</li>
            {% endfor %}
        </ul>
    {% endif %}
    {% endwith %}

    <form action="" method="POST">
    {{ form.hidden_tag() }}
    {{ form.csrf }}
        <div class="input text">
            {{ form.name.label }}<br>
            {{ form.name }}
            <br>
            {{ form.email.label }}<br>
            {{ form.email }}
            <br>
            {{ form.message.label }}<br>
            {{ form.message }}
            <br>
        </div>
        <div class="input submit">
            <input type="submit" value="Submit">
        </div>
    </form>

{% endblock %}

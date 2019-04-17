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

    <form method="POST" action="/contact/">
        {{ form.hidden_tag() }}
        {{ form.name.label }}{{ form.name(size=20) }}
        <br/>
        {{ form.email.label }}{{ form.email(size=50) }}
        <br/>
        {{ form.message.label }}{{ form.message(size=300) }}
        <br/>
        <input type="submit" value="Submit">
    </form>

{% endblock %}

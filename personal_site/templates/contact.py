{% extends 'base_file.py' %}

{% block title %}Contact Me{% endblock %}

{% block meta %}

	<!-- Facebook -->
	<meta property="og:url" content="https://www.rafaelcenzano.me/contact">

	<!-- Twitter -->
	<meta name="twitter:url" content="https://www.rafaelcenzano.me/contact">

{% endblock %}

{% block head_css %}

    <link rel="stylesheet" type="text/css" href={{ url_for('static', filename='css/main/contact.css') }}>
	
{% endblock %}

{% block content %}
    <h1>Contact Me</h1>
    <h2 style = "text-align: center;">Contact Form</h2>

    {% for message in form.name.errors %}
        <div>{{ message }}</div>
    {% endfor %}

    {% for message in form.email.errors %}
        <div>{{ message }}</div>
    {% endfor %}

    <form action = "https://www.rafaelcenzano.me/contact" method = post>
       <fieldset>
          <legend>Contact Form</legend>
              {{ form.hidden_tag() }}

              <div style = font-size:20px; font-weight:bold; margin-left:150px;>
                  {{ form.name.label }}<br>
                  {{ form.name }}
              	  <br>
              	  {{ form.email.label }}<br>
                  {{ form.email }}
                  <br>
				  {{ form.message.label }}<br>
                  {{ form.message }}
                  <br>
                  {{ form.submit }}
            </div>

        </fieldset>
    </form>
{% endblock %}

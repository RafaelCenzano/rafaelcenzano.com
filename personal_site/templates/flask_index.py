{% extends 'base_file.py' %}

{% block title %}Rafael Cenzano{% endblock %}

{% block head_css %}

    <link rel="stylesheet" type="text/css" href={{ url_for('static', filename='css/home.min.css') }}>

	<link href='https://use.fontawesome.com/releases/v5.7.1/css/all.css' rel='stylesheet' type='text/css'>

    <style type="text/css">
    @media (min-width:801px) {
      body {
        /* Fix background during scrolling */
        background-attachment: fixed;
        /* Use scalable background image */
        background-image: url("{{ url_for('static', filename='img/bkgrd-smaller.jpeg') }}");
        background-image: url("{{ url_for('static', filename='img/bkgrd.jpeg') }}");
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
        <h1 class="top-title">RAFAEL</h1>
        <h1 class="top-title">CENZANO</h1>
        <img src={{ url_for('static', filename='img/rafael_profile_square.jpeg') }} class="profile">
    </article>

    <div class="social-buttons">
        <a href="https://www.facebook.com/profile.php?id=100008046498255" class="social-buttons__button social-button social-button--facebook" target="_blank" aria-label="Facebook">
            <span class="social-button__inner">
                <i class="fab fa-facebook-f"></i>
            </span>
        </a>
        <a href="https://www.linkedin.com/in/rafael-cenzano/" class="social-buttons__button social-button social-button--linkedin" target="_blank" aria-label="LinkedIn">
            <span class="social-button__inner">
                <i class="fab fa-linkedin-in"></i>
            </span>
        </a>
        <a href="https://github.com/RafaelCenzano" class="social-buttons__button social-button social-button--github" target="_blank" aria-label="GitHub">
            <span class="social-button__inner">
                <i class="fab fa-github"></i>
            </span>
        </a>
    </div>

    <div class="button-wrapper center">
        <a href="mailto:contact@rafaelcenzano.com" class="contact">Contact me!</a>
    </div>

    <div class="title-wrapper">
        <u><h2>Projects<h2></u>
    </div>

    <div class="projects things center">
        <div class="project-base">
            <a href="https://github.com/Marvin-Virtual-Assistant/Marvin-V4" target="_blank">
                <h3 class="project-title">Marvin Virtual Assistant</h3>
                <p class="project-description things-description">
                    A virtual assistant created in python that currently has 4 versions. This is a project that has tons of room to grow and will always be updated with hopes to have it be an open source project people want to contribute to.
                </p>
            </a>
        </div>
    </div>

    <div class="title-wrapper">
        <u><h2>Experiences<h2></u>
    </div>

    <div class="experiences center things">
        <h4><a href="https://www.hackthefog.com" target="_blank" class="experience">Hack The Fog (HTF)</a></h4>
        <p class="experience-description">Organized Hack The Fog the first high school hackathon in San Francisco and currently organizing Hack the Fog 2.0.</p>
        <p class="current-experience-description experience-description">
            <a class="experience-link" target="_blank" href="https://www.hackthefog.com">~ Currently Co-Lead Organizer and Director of Internal affairs ~</a>
        </p>
        <p class="current-experience-description experience-description">
            <a class="experience-link" target="_blank" href="https://www.hackthefog.com">~ Organizer 1 year 4 months ~</a>
        </p>
        <p class="current-experience-description experience-description">
            <a class="experience-link" target="_blank" href="https://www.hackthefog.com">~ Operations 6 months ~</a>
        </p>
        <p class="current-experience-description experience-description">
            <a class="experience-link chronicle" target="_blank" href="https://www.sfchronicle.com/bayarea/article/Hack-the-Fog-makes-history-as-San-12729895.php">HTF in a chronicle article!</a>
        </p>
    </div>
    <br>
    <div class="experiences center things">
        <h4><a href="https://www.lowelldev.club/" target="_blank" class="experience">Lowell Dev Club</a></h4>
        <p class="experience-description">Programming club at Lowell High School. Our mission is to make people interested in programming and have amazing experiences that stay with them for their whole life.</p>
        <p class="current-experience-description experience-description">
            <a class="experience-link" target="_blank" href="https://www.lowelldev.club">~ Co-Founder and Current Co-Leader ~</a>
        </p>
    </div>
    <br>
    <div class="experiences center things">
        <h4><a href="https://jcyc.org/jyl.htm" target="_blank" class="experience">Japantown Youth Leader (JYL)</a></h4>
        <p class="experience-description">Youth Leadership program in Japantown San Francisco. We go into the community and voulnteer to help the community as well as learn valuable leadership skills.</p>
        <p class="current-experience-description experience-description">
            <a class="experience-link" target="_blank" href="https://jcyc.org/jyl.htm">~ Japantown Youth Leader 2 years + Currently in program ~</a>
        </p>
        <p class="current-experience-description experience-description">
            <a class="experience-link" target="_blank" href="https://jcyc.org/jyl.htm">~ 224.5 volunteer hours total ~</a>
        </p>
    </div>
    <br>
    <div class="experiences center things">
        <h4><a href="#byte_lab_website_is_nonexsistant" class="experience">Byte Lab</a></h4>
        <p class="experience-description">Programming club at Lowell High School.</p>
        <p class="current-experience-description experience-description">
            <a class="experience-link" href="#byte_lab_website_is_nonexsistant">~ Club Secretary 1 year ~</a>
        </p>
        <p class="current-experience-description experience-description">
            <a class="experience-link" href="#byte_lab_website_is_nonexsistant">~ Club Member 1 year ~</a>
        </p>
    </div>
    <footer>
        <p class="copyright">© 2019 Rafael Cenzano</p>
        <div class="source-wrapper">
            <p>
                <a href="https://github.com/RafaelCenzano/rafaelcenzano.com" class="source">Source</a>
            </p>
        </div>
    </footer>
    </div>

{% endblock %}

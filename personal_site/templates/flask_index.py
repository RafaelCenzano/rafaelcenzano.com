{% extends 'base_file.py' %}

{% block title %}Rafael Cenzano{% endblock %}

{% block head_css %}

    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/home.min.css') }}">
    
    <style type="text/css">
    @media (min-width:950px) {
      body {
        /* Fix background during scrolling */
        background-attachment: fixed;
        /* Use scalable background image */
        background-image: url("https://rafael.sirv.com/Images/bkgrdhalf.jpeg?format=webp&q=85");
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
        <img class="profile" src="https://rafael.sirv.com/Images/rafael.jpeg?w=200&q=100" width="200" height="200" srcset="https://rafael.sirv.com/Images/rafael.jpeg?w=200&q=100 1x, https://rafael.sirv.com/Images/rafael.jpeg?w=400&q=100 2x" alt="Rafael Cenzano Profile Image" />
    </article>

    <div class="social-buttons">
        <a rel="noopener" href="https://www.facebook.com/profile.php?id=100008046498255" class="social-buttons__button social-button social-button--facebook" target="_blank" aria-label="Facebook">
            <span class="social-button__inner">
                <svg aria-hidden="true" focusable="false" data-prefix="fab" data-icon="facebook-f" class="svg-inline--fa fa-facebook-f fa-w-10" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 512"><path fill="currentColor" d="M279.14 288l14.22-92.66h-88.91v-60.13c0-25.35 12.42-50.06 52.24-50.06h40.42V6.26S260.43 0 225.36 0c-73.22 0-121.08 44.38-121.08 124.72v70.62H22.89V288h81.39v224h100.17V288z"></path></svg>
            </span>
        </a>
        <a rel="noopener" href="https://www.linkedin.com/in/rafael-cenzano/" class="social-buttons__button social-button social-button--linkedin" target="_blank" aria-label="LinkedIn">
            <span class="social-button__inner">
                <svg aria-hidden="true" focusable="false" data-prefix="fab" data-icon="linkedin-in" class="svg-inline--fa fa-linkedin-in fa-w-14" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><path fill="currentColor" d="M100.28 448H7.4V148.9h92.88zM53.79 108.1C24.09 108.1 0 83.5 0 53.8a53.79 53.79 0 0 1 107.58 0c0 29.7-24.1 54.3-53.79 54.3zM447.9 448h-92.68V302.4c0-34.7-.7-79.2-48.29-79.2-48.29 0-55.69 37.7-55.69 76.7V448h-92.78V148.9h89.08v40.8h1.3c12.4-23.5 42.69-48.3 87.88-48.3 94 0 111.28 61.9 111.28 142.3V448z"></path></svg>
            </span>
        </a>
        <a rel="noopener" href="https://github.com/RafaelCenzano" class="social-buttons__button social-button social-button--github" target="_blank" aria-label="GitHub">
            <span class="social-button__inner">
                <svg aria-hidden="true" focusable="false" data-prefix="fab" data-icon="github" class="svg-inline--fa fa-github fa-w-16" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 496 512"><path fill="currentColor" d="M165.9 397.4c0 2-2.3 3.6-5.2 3.6-3.3.3-5.6-1.3-5.6-3.6 0-2 2.3-3.6 5.2-3.6 3-.3 5.6 1.3 5.6 3.6zm-31.1-4.5c-.7 2 1.3 4.3 4.3 4.9 2.6 1 5.6 0 6.2-2s-1.3-4.3-4.3-5.2c-2.6-.7-5.5.3-6.2 2.3zm44.2-1.7c-2.9.7-4.9 2.6-4.6 4.9.3 2 2.9 3.3 5.9 2.6 2.9-.7 4.9-2.6 4.6-4.6-.3-1.9-3-3.2-5.9-2.9zM244.8 8C106.1 8 0 113.3 0 252c0 110.9 69.8 205.8 169.5 239.2 12.8 2.3 17.3-5.6 17.3-12.1 0-6.2-.3-40.4-.3-61.4 0 0-70 15-84.7-29.8 0 0-11.4-29.1-27.8-36.6 0 0-22.9-15.7 1.6-15.4 0 0 24.9 2 38.6 25.8 21.9 38.6 58.6 27.5 72.9 20.9 2.3-16 8.8-27.1 16-33.7-55.9-6.2-112.3-14.3-112.3-110.5 0-27.5 7.6-41.3 23.6-58.9-2.6-6.5-11.1-33.3 2.6-67.9 20.9-6.5 69 27 69 27 20-5.6 41.5-8.5 62.8-8.5s42.8 2.9 62.8 8.5c0 0 48.1-33.6 69-27 13.7 34.7 5.2 61.4 2.6 67.9 16 17.7 25.8 31.5 25.8 58.9 0 96.5-58.9 104.2-114.8 110.5 9.2 7.9 17 22.9 17 46.4 0 33.7-.3 75.4-.3 83.6 0 6.5 4.6 14.4 17.3 12.1C428.2 457.8 496 362.9 496 252 496 113.3 383.5 8 244.8 8zM97.2 352.9c-1.3 1-1 3.3.7 5.2 1.6 1.6 3.9 2.3 5.2 1 1.3-1 1-3.3-.7-5.2-1.6-1.6-3.9-2.3-5.2-1zm-10.8-8.1c-.7 1.3.3 2.9 2.3 3.9 1.6 1 3.6.7 4.3-.7.7-1.3-.3-2.9-2.3-3.9-2-.6-3.6-.3-4.3.7zm32.4 35.6c-1.6 1.3-1 4.3 1.3 6.2 2.3 2.3 5.2 2.6 6.5 1 1.3-1.3.7-4.3-1.3-6.2-2.2-2.3-5.2-2.6-6.5-1zm-11.4-14.7c-1.6 1-1.6 3.6 0 5.9 1.6 2.3 4.3 3.3 5.6 2.3 1.6-1.3 1.6-3.9 0-6.2-1.4-2.3-4-3.3-5.6-2z"></path></svg>
            </span>
        </a>
    </div>
    <br>
     <div class="experiences center things">
        <h4 class="experience">About me</h4>
        <p class="experience-description">I'm a Senior at Lowell Highschool and I love to code on my free time. I Co-Founded Co-Lead a coding club and I am a Co-Founder and Co-Director of a highschool hackathon. I have created many projects in python and processing (Java).</p>
    </div>

    <div class="button-wrapper center">
        <a href="mailto:contact@rafaelcenzano.com" class="contact">Contact me!</a>
    </div>

    <div class="title-wrapper">
        <u><h2>Projects<h2></u>
    </div>

    <div class="projects things center">
        <div class="project-base">
            <a rel="noopener" href="https://github.com/RafaelCenzano/jyl-site" target="_blank">
                <h3 class="project-title">JYL Toolbox</h3>
                <p class="project-description things-description">
                    A Flask app created to connect student leaders together and to provide a space for all members of JYL and adult leaders to share content and work together.
                </p>
            </a>
        </div>
        <div class="project-base">
            <a rel="noopener" href="https://github.com/RafaelCenzano/Corona-Virus-Email-Updater" target="_blank">
                <h3 class="project-title">Covid 19 Reporter</h3>
                <p class="project-description things-description">
                    A webscraper that scrapes from the CDC and The SF Chronicle to provide a daily email report containing data on case counts and death counts including changes in both. It displays the current day and the previous day's data on a table in the email.
                </p>
            </a>
        </div>
        <div class="project-base">
            <a href="{{ url_for('marvin') }}">
                <h3 class="project-title">Marvin Virtual Assistant</h3>
                <p class="project-description things-description">
                    A virtual assistant created in python that currently has 4 versions. It webscrapes and utilizes API's to give users data and useful functions.
                </p>
            </a>
        </div>
        <div class="project-base">
            <a rel="noopener" href="https://github.com/RafaelCenzano/PyStarter" target="_blank">
                <h3 class="project-title">Pystarter</h3>
                <p class="project-description things-description">
                    CLI tool to aid in starting a project for python and git devlopers. Available on PyPi and can be installed with: pip install pystarter
                </p>
            </a>
        </div>
        <div class="project-base">
            <a href="{{ url_for('apjava') }}">
                <h3 class="project-title">AP Java</h3>
                <p class="project-description things-description">
                    Projects created in Processing for APCS A (Java)
                </p>
            </a>
        </div>
    </div>

    <div class="title-wrapper">
        <u><h2>Experiences<h2></u>
    </div>

    <div class="experiences center things">
        <h4><a rel="noopener" href="https://www.hackthefog.com" target="_blank" class="experience">Hack The Fog (HTF)</a></h4>
        <p class="experience-description">Organized Hack The Fog the first high school hackathon in San Francisco and currently organizing Hack the Fog 2.0. Hosted Hack the Cloud an online hackathon in response to the pandemic.</p>
        <p class="current-experience-description experience-description">
            <a rel="noopener" class="experience-link" target="_blank" href="https://cloud.hackthefog.com">~ Co-Founder and Director of the Hack the Fog Organization ~</a>
        </p>
        <p class="current-experience-description experience-description">
            <a rel="noopener" class="experience-link" target="_blank" href="https://cloud.hackthefog.com">~ Currently Co-Director of Hack the Cloud (Online Hackathon) ~</a>
        </p>
        <p class="current-experience-description experience-description">
            <a rel="noopener" class="experience-link" target="_blank" href="https://www.hackthefog.com">~ Co-Lead Director and Director of Internal affairs for Hack the Fog 2.0 *Postponed* ~</a>
        </p>
        <p class="current-experience-description experience-description">
            <a rel="noopener" class="experience-link" target="_blank" href="https://www.hackthefog.com">~ Organizer 1 year 4 months ~</a>
        </p>
        <p class="current-experience-description experience-description">
            <a rel="noopener" class="experience-link" target="_blank" href="https://www.hackthefog.com">~ Operations 6 months ~</a>
        </p>
        <p class="current-experience-description experience-description">
            <a rel="noopener" class="experience-link chronicle" target="_blank" href="https://www.sfchronicle.com/bayarea/article/Hack-the-Fog-makes-history-as-San-12729895.php">HTF in a chronicle article!</a>
        </p>
    </div>
    <br>
    <div class="experiences center things">
        <h4><a rel="noopener" href="https://www.lowelldev.club/" target="_blank" class="experience">Lowell Dev Club</a></h4>
        <p class="experience-description">Programming club at Lowell High School. Our mission is to make people interested in programming and have amazing experiences that stay with them for their whole life.</p>
        <p class="current-experience-description experience-description">
            <a rel="noopener" class="experience-link" target="_blank" href="https://www.lowelldev.club">~ Co-Founder and Current Co-President ~</a>
        </p>
    </div>
    <br>
    <div class="experiences center things">
        <h4><a rel="noopener" href="#" target="_blank" class="experience">Empower.py</a></h4>
        <p class="experience-description">Online organization created to bring cs education to students with Python.</p>
        <p class="current-experience-description experience-description">
            <a rel="noopener" class="experience-link" target="_blank" href="#">~ Currently Director of Instruction ~</a>
        </p>
    </div>
    <br>
    <div class="experiences center things">
        <h4><a rel="noopener" href="https://jcyc.org/jyl.htm" target="_blank" class="experience">Japantown Youth Leader (JYL)</a></h4>
        <p class="experience-description">Youth Leadership program in Japantown San Francisco. We go into the community and voulnteer to help the community as well as learn valuable leadership skills.</p>
        <p class="current-experience-description experience-description">
            <a rel="noopener" class="experience-link" target="_blank" href="https://jcyc.org/jyl.htm">~ Japantown Youth Leader 2 years + Currently in program ~</a>
        </p>
        <p class="current-experience-description experience-description">
            <a rel="noopener" class="experience-link" target="_blank" href="https://jcyc.org/jyl.htm">~ 208.5 volunteer hours total ~</a>
        </p>
    </div>
    <br>
    <div class="experiences center things">
        <h4><a rel="noopener" target="_blank" href="https://bytelab.rafaelcenzano.com" class="experience">Byte Lab</a></h4>
        <p class="experience-description">Programming club at Lowell High School.</p>
        <p class="current-experience-description experience-description">
            <a target="_blank" class="experience-link" rel="noopener" href="https://bytelab.rafaelcenzano.com">~ Club Secretary 1 year ~</a>
        </p>
        <p class="current-experience-description experience-description">
            <a target="_blank" class="experience-link" rel="noopener" href="https://bytelab.rafaelcenzano.com">~ Club Member 1 year ~</a>
        </p>
    </div>
    {% include 'footer.py' %}
    </div>

{% endblock %}

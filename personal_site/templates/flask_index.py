{% extends 'base_file.py' %}

{% block title %}Rafael Cenzano - Raf{% endblock %}

{% block meta %}

	<!-- Facebook -->
	<meta property="og:url" content="https://www.rafaelcenzano.me/">

	<!-- Twitter -->
	<meta name="twitter:url" content="https://www.rafaelcenzano.me/">

{% endblock %}

{% block head_css %}

    <link rel="stylesheet" type="text/css" href={{ url_for('static', filename='css/main/home.css') }}>

	<link href='https://fonts.googleapis.com/css?family=Josefin+Sans' rel='stylesheet' type='text/css'>

	<link href='https://use.fontawesome.com/releases/v5.7.1/css/all.css' rel='stylesheet' type='text/css'>

	<link rel="stylesheet" type="text/css" href="https://fonts.googleapis.com/css?family=Ubuntu:regular,bold&subset=Latin">

{% endblock %}

{% block head_js %}

    <script src={{ url_for('static', filename='js/main/home.js') }}></script>

{% endblock %}

{% block content %}

	<article class="color-changer">
  		<h1 class="top-title">RAFAEL</h1>
        <h1 class="top-title">CENZANO</h1>
		<img src={{ url_for('static', filename='img/profile.jpeg') }} alt="Rafael Cenzano's profile image" class="profile">
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
        <a href="/contact/" class="contact">Contact me !</a>
    </div>
    <div class="title-wrapper">
        <u><h2>Projects<h2></u>
    </div>
    <div class="projects things center">
        <div class="project-base">
            <a href="/lowelldashboard">
                <h3 class="project-title">Lowell Dashboard</h3>
                <p class="project-description things-description">A website created using Flask App Builder. The website is a dashboard for students at Lowell High School in San Francisco.
                </p>
                <p class="project-description things-description">The website includes resources like up to date news, pdf textbooks, and a place to post homework for classes to help connect students and relieve the stress of having to look far and wide for resources.
                </p>
            </a>
        </div>
      <div class="project-base">
			<a href="/marvinvirtualassistant">
        	    <h3 class="project-title">Marvin Virtual Assistant</h3>
        	    <p class="project-description things-description">
        	    	A virtual assistant created in python that currently has 3 versions. This is a project that has tons of room to grow and will always be updated with hopes to have it be an open source project people want to contribute to.
        	    </p>
       		  </a>
       	</div>
    </div>
    <div class="title-wrapper">
        <u><h2>Experiences<h2></u>
    </div>
    <div class="experiences center things">
        <h4><a href="https://hackthefog.com/" target="_blank" class="experience">Hack The Fog</a></h4>
        <p class="experience-description">Organized Hack The Fog the first high school hackathon in San Francisco</p>
        <p class="current-experience-description experience-description">
        	<a class="experience-link" target="_blank" href="https://hackthefog.com">~ Currently organizing Hack The Fog 2.0 (Organizer) ~</a>
        </p>
        <p class="current-experience-description experience-description">
        	<a class="experience-link" target="_blank" href="https://www.sfchronicle.com/bayarea/article/Hack-the-Fog-makes-history-as-San-12729895.php">~ Organized Hack The Fog (Operations) ~</a
        </p>
        <p class="current-experience-description experience-description">
        	<a class="experience-link" target="_blank" href="https://www.sfchronicle.com/bayarea/article/Hack-the-Fog-makes-history-as-San-12729895.php">~ 1 year 7 months ~</a
        </p>
    </div>
    <br>
    <div class="experiences center things">
        <h4><a href="https://jcyc.org/jyl.htm" target="_blank" class="experience">Japantown Youth Leader (JYL)</a></h4>
        <p class="experience-description">Youth Leadership program in Japantown San Francisco. We go into the community and voulnteer to help the community.</p>
        <p class="current-experience-description experience-description">
        	<a class="experience-link" target="_blank" href="https://jcyc.org/jyl.htm">~ Japantown Youth Leader ~</a>
        </p>
        <p class="current-experience-description experience-description">
        	<a class="experience-link" target="_blank" href="https://jcyc.org/jyl.htm" id="jyl"></a>
        </p>
        <p class="current-experience-description experience-description">
            <a class="experience-link" target="_blank" href="https://jcyc.org/jyl.htm">~ 224.5 volunteer hours total ~</a>
        </p>
    </div>
    <br>
    <div class="experiences center things">
        <h4><a href="https://www.lowelldev.club/" target="_blank" class="experience">Dev Club</a></h4>
        <p class="experience-description">Programming club at Lowell High School. Our mission is to make people interested in programming and have amazing experiences that stay with them for their whole life.</p>
        <p class="current-experience-description experience-description">
        	<a class="experience-link" target="_blank" href="https://www.lowelldev.club">~ Founder and Co-Leader ~</a>
        </p>
    </div>
    <br>
    <div class="experiences center things">
        <h4><a href="https://www.bytelab.club/" target="_blank" class="experience">Byte Lab</a></h4>
        <p class="experience-description">Programming club at Lowell High School.</p>
        <p class="current-experience-description experience-description">
        	<a class="experience-link" target="_blank" href="https://www.bytelab.club/">~ Club Secretary ~</a>
        </p>
        <p class="current-experience-description experience-description">
        	<a class="experience-link" target="_blank" href="https://www.bytelab.club/">~ 2 years ~</a>
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

{% endblock %}

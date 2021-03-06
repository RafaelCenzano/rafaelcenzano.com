{% extends 'base_file.py' %}

{% block title %}Rafael Cenzano{% endblock %}

{% block head_css %}
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/home.min.css') }}">  
{% endblock %}

{% block content %}

    <div class="body-wrapper">
	<article class="color-changer">
        <div class="top-title"><h1>RAFAEL</h1></div>
        <div class="top-title second"><h1>CENZANO</h1></div>
        <img class="profile" src="https://rafael.sirv.com/Images/rafael.jpeg?w=300&q=100" 
            width="300" height="300" 
            srcset="https://rafael.sirv.com/Images/rafael.jpeg?w=300&q=100 1x,
                    https://rafael.sirv.com/Images/rafael.jpeg?w=450&q=100 1.5x,
                    https://rafael.sirv.com/Images/rafael.jpeg?w=600&q=100 2x,
                    https://rafael.sirv.com/Images/rafael.jpeg?w=750&q=100 2.5x,
                    https://rafael.sirv.com/Images/rafael.jpeg?w=900&q=100 3x"
            alt="Rafael Cenzano Profile Image" />
    </article>
    <div class="my-socials">
        <a rel="noopener" href="https://www.facebook.com/profile.php?id=100008046498255" class="social-icon my-facebook" target="_blank" aria-label="Facebook">
            <svg aria-hidden="true" focusable="false" data-prefix="fab" data-icon="facebook-f" class="svg-inline--fa fa-facebook-f fa-w-10" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 512"><path fill="currentColor" d="M279.14 288l14.22-92.66h-88.91v-60.13c0-25.35 12.42-50.06 52.24-50.06h40.42V6.26S260.43 0 225.36 0c-73.22 0-121.08 44.38-121.08 124.72v70.62H22.89V288h81.39v224h100.17V288z"></path></svg>
        </a>
        <a rel="noopener" href="https://www.linkedin.com/in/rafael-cenzano/" class="social-icon my-linkedin" target="_blank" aria-label="LinkedIn">
            <svg aria-hidden="true" focusable="false" data-prefix="fab" data-icon="linkedin-in" class="svg-inline--fa fa-linkedin-in fa-w-14" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><path fill="currentColor" d="M100.28 448H7.4V148.9h92.88zM53.79 108.1C24.09 108.1 0 83.5 0 53.8a53.79 53.79 0 0 1 107.58 0c0 29.7-24.1 54.3-53.79 54.3zM447.9 448h-92.68V302.4c0-34.7-.7-79.2-48.29-79.2-48.29 0-55.69 37.7-55.69 76.7V448h-92.78V148.9h89.08v40.8h1.3c12.4-23.5 42.69-48.3 87.88-48.3 94 0 111.28 61.9 111.28 142.3V448z"></path></svg>
        </a>
        <a rel="noopener" href="https://github.com/RafaelCenzano" class="social-icon my-github" target="_blank" aria-label="GitHub">
            <svg aria-hidden="true" focusable="false" data-prefix="fab" data-icon="github" class="svg-inline--fa fa-github fa-w-16" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 496 512"><path fill="currentColor" d="M165.9 397.4c0 2-2.3 3.6-5.2 3.6-3.3.3-5.6-1.3-5.6-3.6 0-2 2.3-3.6 5.2-3.6 3-.3 5.6 1.3 5.6 3.6zm-31.1-4.5c-.7 2 1.3 4.3 4.3 4.9 2.6 1 5.6 0 6.2-2s-1.3-4.3-4.3-5.2c-2.6-.7-5.5.3-6.2 2.3zm44.2-1.7c-2.9.7-4.9 2.6-4.6 4.9.3 2 2.9 3.3 5.9 2.6 2.9-.7 4.9-2.6 4.6-4.6-.3-1.9-3-3.2-5.9-2.9zM244.8 8C106.1 8 0 113.3 0 252c0 110.9 69.8 205.8 169.5 239.2 12.8 2.3 17.3-5.6 17.3-12.1 0-6.2-.3-40.4-.3-61.4 0 0-70 15-84.7-29.8 0 0-11.4-29.1-27.8-36.6 0 0-22.9-15.7 1.6-15.4 0 0 24.9 2 38.6 25.8 21.9 38.6 58.6 27.5 72.9 20.9 2.3-16 8.8-27.1 16-33.7-55.9-6.2-112.3-14.3-112.3-110.5 0-27.5 7.6-41.3 23.6-58.9-2.6-6.5-11.1-33.3 2.6-67.9 20.9-6.5 69 27 69 27 20-5.6 41.5-8.5 62.8-8.5s42.8 2.9 62.8 8.5c0 0 48.1-33.6 69-27 13.7 34.7 5.2 61.4 2.6 67.9 16 17.7 25.8 31.5 25.8 58.9 0 96.5-58.9 104.2-114.8 110.5 9.2 7.9 17 22.9 17 46.4 0 33.7-.3 75.4-.3 83.6 0 6.5 4.6 14.4 17.3 12.1C428.2 457.8 496 362.9 496 252 496 113.3 383.5 8 244.8 8zM97.2 352.9c-1.3 1-1 3.3.7 5.2 1.6 1.6 3.9 2.3 5.2 1 1.3-1 1-3.3-.7-5.2-1.6-1.6-3.9-2.3-5.2-1zm-10.8-8.1c-.7 1.3.3 2.9 2.3 3.9 1.6 1 3.6.7 4.3-.7.7-1.3-.3-2.9-2.3-3.9-2-.6-3.6-.3-4.3.7zm32.4 35.6c-1.6 1.3-1 4.3 1.3 6.2 2.3 2.3 5.2 2.6 6.5 1 1.3-1.3.7-4.3-1.3-6.2-2.2-2.3-5.2-2.6-6.5-1zm-11.4-14.7c-1.6 1-1.6 3.6 0 5.9 1.6 2.3 4.3 3.3 5.6 2.3 1.6-1.3 1.6-3.9 0-6.2-1.4-2.3-4-3.3-5.6-2z"></path></svg>
        </a>
    </div>
    <div id="webring-wrapper">
        <a rel="noopener" href="https://webring.hackclub.com/" id="previousBtn" class="webring-anchor" title="Previous">‹</a>
        <a rel="noopener" href="https://webring.hackclub.com/" class="webring-logo" title="Hack Club Webring" alt="Hack Club Webring"></a>
        <a rel="noopener" href="https://webring.hackclub.com/" id="nextBtn" class="webring-anchor" title="Next">›</a>
        <script src="https://webring.hackclub.com/public/embed.min.js"></script>
    </div>
    <div class="bio">
        <div class="columns"><div class="column is-narrow"><h2>About me</h2></div><div class="column"><div class="button-wrapper center"><a href="mailto:contact@rafaelcenzano.com" class="contact">Contact me!</a></div></div></div>
        <p>I'm a Hobby Programmer who plans to do Computer Science for my career. I Co-Founded Co-Lead a coding club and I am a Co-Founder and Co-Director of a highschool hackathon. I have created many projects in python, processing (Java), and HTML CSS.</p>
    </div>

    <div class="title-wrapper">
        <h2>Projects<h2>
    </div>
    <div class="columns is-multiline">
        <div class="column is-full">
            <div class="project-column">
                <a href="https://hackathon.rafaelcenzano.com">
                    <div class="project-container">
                        <div class="project-title"><h3>Hackathon Projects</h3></div>
                        <div class="img">
                            <img src="https://rafael.sirv.com/Images/hackathon.png?w=800&format=webp&webp.fallback=png&png.optimize=true"
                            srcset="https://rafael.sirv.com/Images/hackathon.png?w=800&format=webp&webp.fallback=png&png.optimize=true 1x,
                            https://rafael.sirv.com/Images/hackathon.png?w=1600&format=webp&webp.fallback=png&png.optimize=true 2x"
                            alt="Hackathon image" loading="lazy" />
                        </div>
                        <div class="project-description">
                            <p>Projects that I've worked on during various hackathons.</p>
                        </div>
                    </div>
                </a>
            </div>
        </div>
    </div>
    <div class="main-projects">
        <div class="columns is-multiline is-centered">
            <div class="column is-half">
                <a target="_blank" rel="noopener" href="https://github.com/RafaelCenzano/jyl-site">
                    <div class="project-container">
                        <div class="project-title"><h3>JYL Toolbox</h3></div>
                        <div class="img">
                            <img src="https://rafael.sirv.com/Images/jyltoolbox.png?w=800&format=webp&webp.fallback=png&png.optimize=true"
                            srcset="https://rafael.sirv.com/Images/jyltoolbox.png?w=800&format=webp&webp.fallback=png&png.optimize=true 1x,
                            https://rafael.sirv.com/Images/jyltoolbox.png?w=1600&format=webp&webp.fallback=png&png.optimize=true 2x"
                            alt="JYL Toolbox Image" loading="lazy" />
                        </div>
                        <div class="project-description">
                            <p>JYL Toolbox is a Flask website created for the Japantown Youth Leaders group. It was created to help connect students to leaders and to provide an easy online experience that improves the JYL experience for students and leaders alike.</p>
                        </div>
                    </div>
                </a>
            </div>
            <div class="column is-half">
                <a target="_blank" rel="noopener" href="https://github.com/RafaelCenzano/Corona-Virus-Email-Updater">
                    <div class="project-container">
                        <div class="project-title"><h3>Covid-19 Reporter</h3></div>
                        <div class="img">
                            <img src="https://rafael.sirv.com/Images/covid19reporter2.png?w=800&format=webp&webp.fallback=png&png.optimize=true"
                            srcset="https://rafael.sirv.com/Images/covid19reporter2.png?w=800&format=webp&webp.fallback=png&png.optimize=true 1x,
                            https://rafael.sirv.com/Images/covid19reporter2.png?w=1600&format=webp&webp.fallback=png&png.optimize=true 2x"
                            alt="JYL Toolbox Image" loading="lazy" />
                        </div>
                        <div class="project-description">
                            <p>A webscraper that scrapes from the CDC and The SF Chronicle to provide a daily email report containing data on case counts, death counts, and the difference in numbers from the previous day.</p>
                        </div>
                    </div>
                </a>
            </div>
            <div class="column is-half">
                <a target="_blank" rel="noopener" href="https://pypi.org/project/PyStarter/">
                    <div class="project-container">
                        <div class="project-title"><h3>PyStarter</h3></div>
                        <div class="img">
                            <img src="https://rafael.sirv.com/Images/pystarter.png?w=800&format=webp&webp.fallback=png&png.optimize=true"
                            srcset="https://rafael.sirv.com/Images/pystarter.png?w=800&format=webp&webp.fallback=png&png.optimize=true 1x,
                            https://rafael.sirv.com/Images/pystarter.png?w=1600&format=webp&webp.fallback=png&png.optimize=true 2x"
                            alt="JYL Toolbox Image" loading="lazy" />
                        </div>
                        <div class="project-description">
                            <p>Command Line tool to aid in starting a project for python and git devlopers. Available on PyPi and can be installed with: pip install pystarter</p>
                        </div>
                    </div>
                </a>
            </div>
            <div class="column is-half">
                <a href="{{ url_for('marvin') }}">
                    <div class="project-container">
                        <div class="project-title"><h3>Marvin Virtual Assistant</h3></div>
                        <div class="img">
                            <img src="https://rafael.sirv.com/Images/marvin.png?w=800&format=webp&webp.fallback=png&png.optimize=true"
                            srcset="https://rafael.sirv.com/Images/marvin.png?w=800&format=webp&webp.fallback=png&png.optimize=true 1x,
                            https://rafael.sirv.com/Images/marvin.png?w=1600&format=webp&webp.fallback=png&png.optimize=true 2x"
                            alt="Hackathon image" loading="lazy" />
                        </div>
                        <div class="project-description">
                            <p>A virtual assistant created in python that currently has 4 versions. It contains a webscraper and utilizes API's to give users data and useful functions.</p>
                        </div>
                    </div>
                </a>
            </div>
        </div>
    </div>
    <div class="columns is-multiline push">
        <div class="column is-full">
            <div class="project-column">
                <a href="{{ url_for('apjava') }}">
                    <div class="project-container">
                        <div class="project-title"><h3>AP CS A</h3></div>
                        <div class="img">
                            <img src="https://rafael.sirv.com/Images/apcs.jpg?w=800&format=webp&webp.fallback=jpg" width="800" height="450"
                            alt="AP Computer Science" loading="lazy" />
                        </div>
                        <div class="project-description">
                            <p>Projects created in Processing for APCS A (Java). The projects can be viewed right in the browser.</p>
                        </div>
                    </div>
                </a>
            </div>
        </div>
    </div>
    <div class="title-wrapper">
        <h2>Experiences<h2>
    </div>
    <div class="experiences">
        <div class="columns is-multiline is-centered">
            <div class="column is-full">
                <div class="experience-container">
                    <h3>Photon Commerce</h3>
                    <div class="columns is-centered is-vcentered is-mobile images">
                        <div class="column">
                            <div class="experience-img">
                                <img src="https://rafael.sirv.com/Images/photon-commerce.jpeg?h=200&format=webp&webp.fallback=jpg"
                                srcset="https://rafael.sirv.com/Images/photon-commerce.jpeg?h=200&format=webp&webp.fallback=jpg 1x,
                                https://rafael.sirv.com/Images/photon-commerce.jpeg?h=800&format=webp&webp.fallback=jpg 2x"
                                alt="Photon Commerce Logo" loading="lazy" />
                            </div>
                        </div>
                    </div>
                    <h4>Software Engineer Intern</h4>
                    <p class="experience-description">Photon Commerce is a fintech company with products using AI to digitize financial data.</p>
                    <div class="links">
                        <p><a target="_blank" rel="noopener" href="https://www.photoncommerce.com">photoncommerce.com</a></p>
                    </div>
                    <div class="positions">
                        <p>- Software Engineer Intern</p>
                    </div>
                </div>
            </div>
            <div class="column is-half">
                <div class="experience-container">
                    <h3>Hack the Fog</h3>
                    <div class="columns is-centered is-vcentered is-mobile images">
                        <div class="column">
                            <div class="experience-img">
                                <img src="https://rafael.sirv.com/Images/htf1.png?h=200&format=webp&webp.fallback=png&png.optimize=true"
                                srcset="https://rafael.sirv.com/Images/htf1.png?h=200&format=webp&webp.fallback=png&png.optimize=true 1x,
                                https://rafael.sirv.com/Images/htf1.png?h=800&format=webp&webp.fallback=png&png.optimize=true 2x"
                                alt="Hack the Fog 1.0 Logo" loading="lazy" />
                            </div>
                        </div>
                        <div class="column">
                            <div class="experience-img">
                                <img src="https://rafael.sirv.com/Images/htf2.png?h=200&format=webp&webp.fallback=png&png.optimize=true"
                                srcset="https://rafael.sirv.com/Images/htf2.png?h=200&format=webp&webp.fallback=png&png.optimize=true 1x,
                                https://rafael.sirv.com/Images/htf2.png?h=800&format=webp&webp.fallback=png&png.optimize=true 2x"
                                alt="Hack the Fog 2.0 Logo" loading="lazy" />
                            </div>
                        </div>
                        <div class="column">
                            <div class="experience-img">
                                <img src="https://rafael.sirv.com/Images/hackthecloudWhitetext.png?h=200&format=webp&webp.fallback=png&png.optimize=true"
                                srcset="https://rafael.sirv.com/Images/hackthecloudWhitetext.png?h=200&format=webp&webp.fallback=png&png.optimize=true 1x,
                                https://rafael.sirv.com/Images/hackthecloudWhitetext.png?h=800&format=webp&webp.fallback=png&png.optimize=true 2x"
                                alt="Hack the Cloud Logo" loading="lazy" />
                            </div>
                        </div>
                    </div>
                    <h4>Co-Founder and Director</h4>
                    <p class="experience-description">Hack the Fog (HTF) is a Non-Profit organization that I <strong>co-founded</strong>. In March 2018 HTF made history by hosting the <strong>first high school hackathon in San Francisco</strong>, HTF got featured in the SF Chronicle for this achievment. Since July 2019 HTF started organizing HTF 2.0, but due to Covid-19 is has been indefinitely postponed. In 3 months part of the HTF organization hosted <strong>Hack the Cloud, HTF's reaction Covid-19</strong> to bring the hackathon experience to highschoolers during the shelter in place.</p>
                    <div class="links">
                        <p><a target="_blank" rel="noopener" href="https://htf.hackthefog.com">htf.hackthefog.com</a></p>
                        <p><a target="_blank" rel="noopener" href="https://www.hackthefog.com">hackthefog.com</a></p>
                        <p><a target="_blank" rel="noopener" href="https://cloud.hackthefog.com">cloud.hackthefog.com</a></p>
                        <p><a target="_blank" rel="noopener" href="https://www.sfchronicle.com/bayarea/article/Hack-the-Fog-makes-history-as-San-12729895.php">sfchonicle.com</a></p>
                    </div>
                    <div class="positions">
                        <p>- Co-Director of Hack the Cloud (Hosted July 11th 2020)</p>
                        <p>- Co-Director and Director of Internal Affairs of Hack the Fog 2.0 (Postponed)</p>
                        <p>- Co-Founder and Organizer of Hack the Fog (Hosted March 3rd 2020)</p>
                    </div>
                </div>
            </div>
            <div class="column is-half">
                <div class="experience-container">
                    <h3>Lowell Dev Club</h3>
                    <div class="columns is-centered is-vcentered is-mobile images">
                        <div class="column">
                            <div class="experience-img">
                                <img src="https://rafael.sirv.com/Images/devclub.png?h=200&format=webp&webp.fallback=png&png.optimize=true"
                                srcset="https://rafael.sirv.com/Images/devclub.png?h=200&format=webp&webp.fallback=png&png.optimize=true 1x,
                                https://rafael.sirv.com/Images/devclub.png?h=800&format=webp&webp.fallback=png&png.optimize=true 2x"
                                alt="Lowell Dev Club Logo" loading="lazy" />
                            </div>
                        </div>
                    </div>
                    <h4>Co-Founder and Co-President</h4>
                    <p class="experience-description">Lowell Dev Club is a <strong>Hack Club</strong> at Lowell highschool. Dev Club was founded after ByteLab, the previous cs club at Lowell, ended and was created to improve on the weakness of ByteLab. We founded Dev Club to bring <strong>meaninful CS experiences and lessons</strong> to fellow students. We also wanted to <strong>prepare and connect students to CS experiences</strong> like Hackathons.</p>
                    <div class="links">
                        <p><a target="_blank" rel="noopener" href="https://www.lowelldev.club">www.lowelldev.club</a></p>
                        <p><a target="_blank" rel="noopener" href="https://hackclub.com">hackclub.com</a></p>
                    </div>
                    <div class="positions">
                        <p>- Co-Founder and Co-President Since May 2019</p>
                    </div>
                </div>
            </div>
            <div class="column is-half">
                <div class="experience-container">
                    <h3>Japantown Youth Leaders</h3>
                    <div class="columns is-centered is-vcentered is-mobile images">
                        <div class="column">
                            <div class="experience-img">
                                <img src="https://rafael.sirv.com/Images/jyl.png?h=200&format=webp&webp.fallback=png&png.optimize=true"
                                srcset="https://rafael.sirv.com/Images/jyl.png?h=200&format=webp&webp.fallback=png&png.optimize=true 1x,
                                https://rafael.sirv.com/Images/jyl.png?h=800&format=webp&webp.fallback=png&png.optimize=true 2x"
                                alt="Japantown Youth Leaders Logo" loading="lazy" />
                            </div>
                        </div>
                    </div>
                    <h4>Youth Leader</h4>
                    <p class="experience-description">Japantown Youth Leaders (JYL) is a youth leaders program through JCYC. Leaders <strong>volunteer throughout the year at various events in japantown and the city</strong>. Leaders have weekly meetings diving more in depth in skills  like leadership, public speaking, and volunteerism. I have <strong>volunteered 208.5 hours</strong> since I started JYL</p>
                    <div class="links">
                        <p><a target="_blank" rel="noopener" href="https://jcyc.org/jyl.htm">jcyc.org/jyl</a></p>
                    </div>
                    <div class="positions">
                        <p>- JYL toolbox creater and maintainer Since March 2020</p>
                        <p>- Youth Leader Since September 2017</p>
                    </div>
                </div>
            </div>
            <div class="column is-half">
                <div class="experience-container">
                    <h3>ByteLab</h3>
                    <div class="columns is-centered is-vcentered is-mobile images">
                        <div class="column">
                            <div class="experience-img">
                                <img src="https://rafael.sirv.com/Images/bytelab.png?h=200&format=webp&webp.fallback=png&png.optimize=true"
                                srcset="https://rafael.sirv.com/Images/bytelab.png?h=200&format=webp&webp.fallback=png&png.optimize=true 1x,
                                https://rafael.sirv.com/Images/bytelab.png?h=800&format=webp&webp.fallback=png&png.optimize=true 2x"
                                alt="Empowerpy Logo" loading="lazy" />
                            </div>
                        </div>
                    </div>
                    <h4>Club Secretary</h4>
                    <p class="experience-description">Bytelab was a coding club created to teach students how to become fullstack devlopers.</p>
                    <div class="links">
                        <p><a target="_blank" rel="noopener" href="https://bytelab.rafaelcenzano.com">bytelab.rafaelcenzano.com</a></p>
                    </div>
                    <div class="positions">
                        <p>- Club Secretary 2018-2019</p>
                        <p>- Club Member 2017-2019</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    {% include 'footer.py' %}
    </div>

{% endblock %}

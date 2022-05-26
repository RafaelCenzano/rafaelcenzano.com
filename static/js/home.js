var scroll = new SmoothScroll('a[href*="#"]');

const currentTheme = localStorage.getItem('theme');
const fullMoon = document.getElementById('fullMoon');
const openMoon = document.getElementById('openMoon');
if (currentTheme) {
  document.documentElement.setAttribute('data-theme', currentTheme);
  if (currentTheme === 'light') {
    openMoon.style = '';
    fullMoon.style = 'display:none;';
  }
} else {
  if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    localStorage.setItem('theme', 'dark');
    document.documentElement.setAttribute('data-theme', 'dark');
    openMoon.style = 'display:none;';
    fullMoon.style = '';
  } else if (window.matchMedia && window.mathMedia('(perfers-color-scheme: light)').matches) {
    localStorage.setItem('theme', 'light');
    document.documentElement.setAttribute('data-theme', 'light');
    openMoon.style = '';
    fullMoon.style = 'display:none;';
  } else {
    localStorage.setItem('theme', 'dark');
    document.documentElement.setAttribute('data-theme', 'dark');
    openMoon.style = 'display:none;';
    fullMoon.style = '';
  }
}

function switchTheme() {
  if (localStorage.getItem('theme') === 'dark') {
    document.documentElement.setAttribute('data-theme', 'light');
    localStorage.setItem('theme', 'light');
    openMoon.style = '';
    fullMoon.style = 'display:none;';
  } else {
    document.documentElement.setAttribute('data-theme', 'dark');
    localStorage.setItem('theme', 'dark');
    openMoon.style = 'display:none;';
    fullMoon.style = '';
  }
}
document.addEventListener('DOMContentLoaded', function() {
    const darkModeToggle = document.getElementById('darkModeToggle');
    const icon = darkModeToggle.querySelector('i');
    
    // Verifica preferência salva
    if (localStorage.getItem('darkMode') === 'enabled') {
      enableDarkMode();
    }
  
    // Evento de clique
    darkModeToggle.addEventListener('click', function() {
      if (document.body.classList.contains('dark-mode')) {
        disableDarkMode();
      } else {
        enableDarkMode();
      }
    });
  
    function enableDarkMode() {
        document.body.classList.add('dark-mode');
        
        // Elementos que frequentemente mantêm cores escuras
        document.querySelectorAll('.text-dark, .navbar-brand, .card, .list-group-item').forEach(el => {
          el.classList.add('dark-mode-element');
        });
        
        // Adiciona uma classe global ao html para maior especificidade
        document.documentElement.classList.add('dark-theme-active');
      }
  
    function disableDarkMode() {
      document.body.classList.remove('dark-mode');
      icon.classList.replace('bi-sun-fill', 'bi-moon-fill');
      localStorage.setItem('darkMode', 'disabled');
    }
  });
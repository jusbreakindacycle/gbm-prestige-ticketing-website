const navToggle = document.querySelector('[data-nav-toggle]');
const navMenu = document.querySelector('[data-nav-menu]');

if (navToggle && navMenu) {
  navToggle.addEventListener('click', () => {
    const isOpen = navMenu.classList.toggle('is-open');
    navToggle.setAttribute('aria-expanded', String(isOpen));
    navMenu.style.display = isOpen ? 'flex' : '';
    navMenu.style.flexDirection = isOpen ? 'column' : '';
    navMenu.style.position = isOpen ? 'absolute' : '';
    navMenu.style.top = isOpen ? '72px' : '';
    navMenu.style.right = isOpen ? '1rem' : '';
    navMenu.style.background = isOpen ? 'white' : '';
    navMenu.style.padding = isOpen ? '1rem' : '';
    navMenu.style.border = isOpen ? '1px solid rgba(15, 39, 71, 0.12)' : '';
    navMenu.style.borderRadius = isOpen ? '16px' : '';
    navMenu.style.boxShadow = isOpen ? '0 16px 45px rgba(15, 39, 71, 0.08)' : '';
  });
}

const faqItems = document.querySelectorAll('.faq-item');
faqItems.forEach((item) => {
  const button = item.querySelector('.faq-question');
  if (!button) return;
  button.addEventListener('click', () => {
    const isOpen = item.classList.contains('open');
    faqItems.forEach((entry) => {
      entry.classList.remove('open');
      const entryButton = entry.querySelector('.faq-question');
      if (entryButton) entryButton.setAttribute('aria-expanded', 'false');
    });
    if (!isOpen) {
      item.classList.add('open');
      button.setAttribute('aria-expanded', 'true');
    }
  });
});
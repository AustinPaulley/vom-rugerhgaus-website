document.addEventListener('DOMContentLoaded', () => {
  const slides = document.querySelector('.slides');
  const dots   = Array.from(document.querySelectorAll('.dot'));
  let current  = 0;
  const total  = dots.length;
  function goTo(i) {
    slides.style.transform = `translateX(-${i * 100}%)`;
    dots[current].classList.remove('active');
    dots[i].classList.add('active');
    current = i;
  }
  dots.forEach((dot, i) => dot.addEventListener('click', () => goTo(i)));
  setInterval(() => goTo((current + 1) % total), 5000);
  goTo(0);
});
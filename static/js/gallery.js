document.addEventListener('DOMContentLoaded', () => {
  const modal = document.getElementById('gallery-modal');
  const modalImg = document.getElementById('modal-img');
  const closeBtn = document.querySelector('.close-modal');
  document.querySelectorAll('.gallery-item').forEach(img => {
    img.addEventListener('click', () => {
      modalImg.src = img.src;
      modal.style.display = 'flex';
    });
  });
  closeBtn.addEventListener('click', () => {
    modal.style.display = 'none';
  });
  modal.addEventListener('click', e => {
    if (e.target === modal) modal.style.display = 'none';
  });
});
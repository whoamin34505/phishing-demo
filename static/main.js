document.getElementById('next').addEventListener('click', async () => {
  const phoneInput = document.getElementById('phone').value;
  const phone = '+7' + phoneInput.replace(/\D/g, '');
  const userAgent = navigator.userAgent;
  const now = new Date();
  const hours = now.getHours();
  const minutes = now.getMinutes();
  const seconds = now.getSeconds();
  console.log(`Текущее время: ${hours}:${minutes}:${seconds}`);

  try {
    const response = await fetch('http://localhost:5555/bot', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ phone, userAgent, hours, minutes, seconds })
    });

    if (response.ok) {
      console.log('Отправлено на сервер');
    } else {
      console.error('Ошибка сервера:', response.status);
    }
  } catch (error) {
    console.error('Ошибка при запросе:', error);
  }
});

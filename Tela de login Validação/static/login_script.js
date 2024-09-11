document.querySelector('.btn-login').addEventListener('click', () => {
  const user = document.getElementById('user').value;
  const password = document.getElementById('password').value;


 // Enviando os dados para o servidor
  fetch('http://localhost:5000/login', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      user: user,
      password: password
    })
  })
  .then(response => response.json())
  .then(data => {
    if (data.status === 'success') {
      alert(data.message);
    } else {
      alert(data.message);
    }
  })
  .catch(error => console.error('Erro:', error));
});


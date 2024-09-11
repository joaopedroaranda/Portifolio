document.getElementById('register-form').addEventListener('submit', (event) => {
    event.preventDefault(); // Impede o envio padrão do formulário

    const user = document.getElementById('user').value;
    const password = document.getElementById('password').value;
    const passwordConfirm = document.getElementById('confirm-password').value;

    // Enviando os dados para o servidor
    fetch('/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        user: user,
        password: password,
        password_confirm: passwordConfirm
      })
    })
    .then(response => response.json())
    .then(data => {
      if (data.status === 'success') {
        alert(data.message);
        // Redireciona para a página de login após o cadastro bem-sucedido
        window.location.href = '/';
      } else {
        alert(data.message);
      }
    })
    .catch(error => console.error('Erro:', error));
});

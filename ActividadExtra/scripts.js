document.getElementById('formularioRegistro').addEventListener('submit', function(event) {
  const nombre = document.getElementById('nombre').value.trim();
  const correo = document.getElementById('correo').value.trim();
  const contraseña = document.getElementById('contraseña').value.trim();

  if (!nombre || !correo || !contraseña) {
      alert('Por favor, completa todos los campos antes de enviar.');
      event.preventDefault(); // Evita el envío del formulario
      return;
  }

  if (contraseña.length < 6) {
      alert('La contraseña debe tener al menos 6 caracteres.');
      event.preventDefault();
      return;
  }

  alert('Formulario enviado correctamente.');
});

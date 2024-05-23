function handleSubmit() {
    // Mostrar mensaje de éxito
    var mensajeExito = document.createElement('div');
    mensajeExito.className = 'alert alert-success';
    mensajeExito.textContent = '¡El ticket se ha creado correctamente!';
    document.getElementById('hero').appendChild(mensajeExito);
    
    // Limpiar el formulario después de 3 segundos
    setTimeout(function() {
        mensajeExito.style.display = 'none';
        document.querySelector('.hero-form').reset(); // Restablecer el formulario
    }, 3000);
    
    return false; // Evita que el formulario se envíe al servidor
}
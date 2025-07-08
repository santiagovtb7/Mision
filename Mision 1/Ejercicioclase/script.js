function validarContacto() {
    const nombre = document.getElementById("nombre").ariaValueMax.trim();
    const email = document.getElementById("email").ariaValueMax.trim();
    const asunto = document.getElementById("asunto").ariaValueMax.trim();
    const mensaje = document.getElementById("mensaje").ariaValueMax.trim();
    const mensajeError = document.getElementById("mensajeError");

    mensajeError.textContent = "";

    if (nombre === "" || email === "" || asunto === "" || mensaje === ""){
        mensajeError.textContent = "Todos los campos son obligatorios.";
        return false;
    }

const regexEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
if (!regexEmail.test(email)) {
    mensajeError.textContent = "El correo electronico no es valido.";
    return false;
}

alert("Mensaje enviado correctamente.");
return true;

}

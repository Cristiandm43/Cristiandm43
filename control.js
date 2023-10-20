document.addEventListener("DOMContentLoaded", function () {
    const aplicarFiltrosButton = document.getElementById('aplicar-filtros-button');
    aplicarFiltrosButton.addEventListener('click', aplicarFiltros);

    function aplicarFiltros() {
        const modalidadSeleccionada = obtenerModalidadSeleccionada();
        const ciudadSeleccionada = obtenerCiudadSeleccionada();
        const salarioSeleccionado = obtenerSalarioSeleccionado();
        const listaTrabajos = document.querySelectorAll('.list-group-item');

        listaTrabajos.forEach(trabajo => {
            const modalidadTrabajo = trabajo.getAttribute('data-modalidad');
            const ciudadTrabajo = trabajo.getAttribute('data-ciudad');
            const salarioTrabajo = parseInt(trabajo.getAttribute('data-salario'));

            const modalidadCoincide = modalidadSeleccionada === 'todos' || modalidadTrabajo === modalidadSeleccionada;
            const ciudadCoincide = ciudadSeleccionada === 'todas' || ciudadTrabajo === ciudadSeleccionada;
            const salarioCoincide = (
                salarioSeleccionado === 'todos' ||
                (salarioSeleccionado === 'menos-de-1m' && salarioTrabajo < 1000000) ||
                (salarioSeleccionado === '1m-a-1.5m' && salarioTrabajo >= 1000000 && salarioTrabajo <= 1500000) ||
                (salarioSeleccionado === '1.5m-a-2.5m' && salarioTrabajo > 1500000 && salarioTrabajo <= 2500000) ||
                (salarioSeleccionado === 'mas-de-2.5m' && salarioTrabajo > 2500000)
            );

            if (modalidadCoincide && ciudadCoincide && salarioCoincide) {
                trabajo.style.display = 'block';
            } else {
                trabajo.style.display = 'none';
            }
        });
    }

    function obtenerModalidadSeleccionada() {
        const modalidadRadios = document.getElementsByName('modalidad');
        let modalidadSeleccionada = "";

        modalidadRadios.forEach(radio => {
            if (radio.checked) {
                modalidadSeleccionada = radio.value;
            }
        });

        return modalidadSeleccionada;
    }

    function obtenerCiudadSeleccionada() {
        const ciudadSelect = document.getElementById('ciudad');
        return ciudadSelect.value;
    }

    function obtenerSalarioSeleccionado() {
        const salarioRadios = document.querySelectorAll('.form-check-input[name="salario"]');
        let salarioSeleccionado = "";

        salarioRadios.forEach(radio => {
            if (radio.checked) {
                salarioSeleccionado = radio.value;
            }
        });

        return salarioSeleccionado;
    }

    // Agregar un evento de escucha a los radios de modalidad para activar el filtro
    const modalidadRadios = document.getElementsByName('modalidad');
    modalidadRadios.forEach(radio => {
        radio.addEventListener('change', aplicarFiltros);
    });

    // Agregar un evento de escucha al select de ciudad para activar el filtro
    const ciudadSelect = document.getElementById('ciudad');
    ciudadSelect.addEventListener('change', aplicarFiltros);

    // Agregar un evento de escucha a los checkboxes de salario para activar el filtro
    const salarioCheckboxes = document.querySelectorAll('.form-check-input[name="salario"]');
    salarioCheckboxes.forEach(checkbox => {
        checkbox.addEventListener('change', aplicarFiltros);
    });

    // Llamar a la función al cargar la página para mostrar todos los trabajos inicialmente
    aplicarFiltros();


// Obtener referencias a los elementos HTML y los formularios
const loginButton = document.getElementById("login-button");
const registerButton = document.getElementById("register-button");
const loginForm = document.getElementById("login-form");
const registerForm = document.getElementById("register-form");

// Mostrar el formulario de inicio de sesión cuando se hace clic en "Acceder a la cuenta"
loginButton.addEventListener("click", (e) => {
    e.stopPropagation(); // Evitar que el clic se propague al documento
    loginForm.style.display = "block";
    registerForm.style.display = "none";
});

// Mostrar el formulario de registro cuando se hace clic en "Registrarse"
registerButton.addEventListener("click", (e) => {
    e.stopPropagation(); // Evitar que el clic se propague al documento
    registerForm.style.display = "block";
    loginForm.style.display = "none";
});

// Controlador de clic en el documento para ocultar los formularios
document.addEventListener("click", () => {
    loginForm.style.display = "none";
    registerForm.style.display = "none";
});
    
});

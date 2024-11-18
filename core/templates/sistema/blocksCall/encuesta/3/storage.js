//  ---GUARDAR DATOS DE FORMULARIO EN LOCALSTORAGE---
document.addEventListener('DOMContentLoaded', function() {
    const nombreEncuesta = document.getElementById('nombreEncuesta');
    const descripcionEncuesta = document.getElementById('descripcionEncuesta');
    const fechaCreacion = document.getElementById('fechaCreacion');

    if (localStorage.getItem('nombre')) {
        nombreEncuesta.value = localStorage.getItem('nombre');
    }
    if (localStorage.getItem('descripcion')) {
        descripcionEncuesta.value = localStorage.getItem('descripcion');
    }
    if (localStorage.getItem('fecha')) {
        fechaCreacion.value = localStorage.getItem('fecha');
    }

    nombreEncuesta.addEventListener('input', function() {
        localStorage.setItem('nombre', nombreEncuesta.value);
    });
    descripcionEncuesta.addEventListener('input', function() {
        localStorage.setItem('descripcion', descripcionEncuesta.value);
    });
    fechaCreacion.addEventListener('input', function() {
        localStorage.setItem('fecha', fechaCreacion.value);
    });
});
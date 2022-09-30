document.getElementById('frm-buscar').addEventListener(
    'submit',(e)=>{
        e.preventDefault();
        let txt_busqueda = document.getElementById('txt-busqueda').value;
        location.href = `${window.location.href}search/${txt_busqueda}`;
    }
);

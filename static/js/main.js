document.getElementById('frm-buscar').addEventListener(
    'submit',(e)=>{
        e.preventDefault();
        buscar();
    }
);
function buscar(){
    let txt_busqueda = document.getElementById('txt-busqueda').value;
    if(txt_busqueda.trim() == ''){
        return;
    }
    location.href = `${window.location.href}search/${txt_busqueda}`;
}
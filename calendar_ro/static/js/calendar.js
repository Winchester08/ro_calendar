const mesesNombres = [
  "ENERO",
  "FEBRERO",
  "MARZO",
  "ABRIL",
  "MAYO",
  "JUNIO",
  "JULIO",
  "AGOSTO",
  "SEPTIEMBRE",
  "OCTUBRE",
  "NOVIEMBRE",
  "DICIEMBRE",
];

let fechaActual = new Date();
let mesActual = fechaActual.getMonth();
let añoActual = fechaActual.getFullYear();

// Ejemplo de eventos (puedes agregar los que quieras)
const eventos = {
  "2024-2-14": "Día de San Valentín",
  "2024-2-15": "Reunión importante",
  "2024-2-20": "Presentación proyecto",
  "2024-3-8": "Día Internacional de la Mujer",
  "2024-3-21": "Inicio de Primavera",
};

function renderizarCalendario() {
  const primerDia = new Date(añoActual, mesActual, 1);
  const ultimoDia = new Date(añoActual, mesActual + 1, 0);
  const diasMesAnterior = new Date(añoActual, mesActual, 0).getDate();

  const primerDiaSemana = primerDia.getDay();
  const ultimoDiaMes = ultimoDia.getDate();

  document.getElementById("mesNombre").textContent = mesesNombres[mesActual];
  document.getElementById("añoNumero").textContent = añoActual;

  const diasGrid = document.getElementById("diasGrid");
  diasGrid.innerHTML = "";

  // Días del mes anterior
  for (let i = primerDiaSemana - 1; i >= 0; i--) {
    const dia = diasMesAnterior - i;
    const divDia = crearDivDia(dia, "otro-mes");
    diasGrid.appendChild(divDia);
  }

  // Días del mes actual
  const hoy = new Date();
  for (let dia = 1; dia <= ultimoDiaMes; dia++) {
    const esHoy =
      dia === hoy.getDate() &&
      mesActual === hoy.getMonth() &&
      añoActual === hoy.getFullYear();

    const fechaKey = `${añoActual}-${mesActual + 1}-${dia}`;
    const tieneEvento = eventos.hasOwnProperty(fechaKey);

    const clases = [];
    if (esHoy) clases.push("hoy");
    if (tieneEvento) clases.push("tiene-evento");

    const divDia = crearDivDia(dia, clases.join(" "));
    diasGrid.appendChild(divDia);
  }

  // Días del mes siguiente
  const diasRestantes = 42 - diasGrid.children.length;
}

function crearDivDia(numero, clases) {
  
  const div = document.createElement("div");
  div.className = `dia ${clases}`;
  div.textContent = numero;

  const modal = document.getElementById("modal");
  
  const cierra = document.getElementById("cierra");
  

//aqui abrimos el modal 
div.addEventListener("click",  () => {
 modal.style.display = "flex";
 let diae = document.querySelector("#dia_e");
 document.getElementById("dia_e").value = numero
 //diae.textContent = numero;

//alert(numero);

});

cierra.addEventListener("click", () => {
  modal.style.display = "none";
})

document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape' ) {
    modal.style.display = "none";
  }

  modal.addEventListener("click", (e) => {
    if (e.target=== modal){
      modal.style.display = "none";
    }
  })
});

  return div;

  
}
document.getElementById("abrirm").addEventListener("click", function(){
  console.log("Abriendo elemento con boton")
    lastFocused = document.activeElement;
    overlay.classList.add('is-open');
  // Mueve el foco al botón de cerrar
    closeBtn.focus();
});



function cambiarMes(direccion) {
  mesActual += direccion;

  if (mesActual > 11) {
    mesActual = 0;
    añoActual++;
  } else if (mesActual < 0) {
    mesActual = 11;
    añoActual--;
  }

  renderizarCalendario();
}

document
  .getElementById("prevBtn")
  .addEventListener("click", () => cambiarMes(-1));
document
  .getElementById("nextBtn")
  .addEventListener("click", () => cambiarMes(1));

// Renderizar calendario inicial
renderizarCalendario();

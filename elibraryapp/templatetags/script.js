let cells = document.querySelectorAll('td');

for(let i=0; i < cells.length; i++) {
	cells[i].setAttribute('onclick', 'play(this)');
	cells[i].innerHTML = "";
}

function play(cell) {
	cell.innerHTML = "X";
}
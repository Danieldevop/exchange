function soles_to_usd() {
				let soles = document.getElementById("envias").value
				document.getElementById("recibes").value = soles * 3
			}

function usd_to_soles() {
	let usd = document.getElementById("recibes").value
	document.getElementById("envias").value = usd / 3
}
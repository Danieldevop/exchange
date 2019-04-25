function soles_to_usd() {
	let soles = document.getElementById("envias").value
	let operation = soles * 3
	let res = document.getElementById("recibes").value = operation.toFixed(2)

	if (res == 'NaN') {
		document.getElementById("recibes").value = "Valor Inválido"
	}
}

function usd_to_soles() {
	let usd = document.getElementById("recibes").value
	let operation = usd / 3
	let res = document.getElementById("envias").value = operation.toFixed(2)

	if (res == 'NaN') {
		document.getElementById("envias").value = "Valor Inválido"
	}
}

let soles =  document.getElementById("money1").innerHTML = `
	<div class="column is-two-thirds">
		<div class="control ">
			<input class="" id="envias" required="true" onkeyup="soles_to_usd();" type="text" value="" name="envias">
		</div>
	</div>
			
	<div class="money column">
		<div class="columns">
			<div class="column">
				<img src="https://storage.cloud.google.com/exchange-usd-peru/peru.svg?authuser=1&_ga=2.178088807.-354877498.1555388895" alt="peru">
			</div>
			<div class="column is-two-thirds">
				<p>SOLES</p>
			</div>
		</div>
	</div>
`

let dolars = document.getElementById("money2").innerHTML = `

	<div class="column is-two-thirds">
		<input class="" id="recibes" required="true" onkeyup="usd_to_soles();" type="text" value="" name="recibes">
	</div>
	<div class="money column">
		<div class="columns">
			<div class="column">
				<img src="https://storage.cloud.google.com/exchange-usd-peru/usd.svg?authuser=1&_ga=2.140453105.-354877498.1555388895" alt="usd">
			</div>
			<div class="column is-two-thirds">
				<p>DOLARES</p>
			</div>
		</div>
	</div>

`

var tryes = false;



function changeCoin() {

	console.log(tryes)

	if (tryes == true) {

		let soles =  document.getElementById("money1").innerHTML = `
			<div class="column is-two-thirds">
				<div class="control ">
					<input class="" id="envias" required="true" onkeyup="soles_to_usd();" type="text" value="" name="envias">
				</div>
			</div>
					
			<div class="money column">
				<div class="columns">
					<div class="column">
						<img src="https://storage.cloud.google.com/exchange-usd-peru/peru.svg?authuser=1&_ga=2.178088807.-354877498.1555388895" alt="peru">
					</div>
					<div class="column is-two-thirds">
						<p>SOLES</p>
					</div>
				</div>
			</div>
		`

		let dolars = document.getElementById("money2").innerHTML = `

			<div class="column is-two-thirds">
				<input class="" id="recibes" required="true" onkeyup="usd_to_soles();" type="text" value="" name="recibes">
			</div>
			<div class="money column">
				<div class="columns">
					<div class="column">
						<img src="https://storage.cloud.google.com/exchange-usd-peru/usd.svg?authuser=1&_ga=2.140453105.-354877498.1555388895" alt="usd">
					</div>
					<div class="column is-two-thirds">
						<p>DOLARES</p>
					</div>
				</div>
			</div>

		`

		let spin =document.getElementById("spin")
		spin.classList.remove("spin-btn")
		spin.classList.add("spin-reverse")


		tryes = false;

	} else {

		let dolares = document.getElementById("money2").innerHTML = `

			<div class="column is-two-thirds">
			<div class="control ">
				<input class="" id="envias" required="true" onkeyup="soles_to_usd();" type="text" value="" name="envias">
			</div>
		</div>
				
		<div class="money column">
			<div class="columns">
				<div class="column">
					<img src="https://storage.cloud.google.com/exchange-usd-peru/peru.svg?authuser=1&_ga=2.178088807.-354877498.1555388895" alt="peru">
				</div>
				<div class="column is-two-thirds">
					<p>SOLES</p>
				</div>
			</div>
		</div>

		`

		let soles =  document.getElementById("money1").innerHTML = `
			<div class="column is-two-thirds">
			<input class="" id="recibes" required="true" onkeyup="usd_to_soles();" type="text" value="" name="recibes">
		</div>
		<div class="money column">
			<div class="columns">
				<div class="column">
					<img src="https://storage.cloud.google.com/exchange-usd-peru/usd.svg?authuser=1&_ga=2.140453105.-354877498.1555388895" alt="usd">
				</div>
				<div class="column is-two-thirds">
					<p>DOLARES</p>
				</div>
			</div>
		</div>
		`

		var sheet = window.document.styleSheets[0];
		sheet.insertRule(`
			@keyframes spin {
	  			0% { transform: rotate(0deg); }
	  			100% { transform: rotate(360deg); }
			}

		`, sheet.cssRules.length);

		tryes = true;

	}

}


he = false;
function hello() {
	he = true;
	if (he) {
		console.log('hello');
	} else {
		console.log('mello');
	}
}

setTimeout(hello, 5000);

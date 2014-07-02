function changeWords () {
	var sadTemplate = [];
	sadTemplate["once"] = "FOREVER";
	sadTemplate["watch"] = "PEER";
	sadTemplate["end"] = "BEGIN";
	var originalText = document.getElementById("oriText").value;
	var textArray = originalText.split(" ");
	var changedText = "";
	for (i = 0; i < textArray.length; i++) {
		var oriWord = textArray[i];
		var word = sadTemplate[oriWord];
		if (word != undefined) {
			changedText = changedText + word + " ";
		} else {	
			changedText = changedText + oriWord + " ";
		}
	}
	alert("The changed text is: " + changedText);
}

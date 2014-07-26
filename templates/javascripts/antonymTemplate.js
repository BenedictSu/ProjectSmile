function antonymTemplate () {
	var antonymTemplate = [];
	antonymTemplate["once"] = "FOREVER";
	antonymTemplate["watch"] = "PEER";
	antonymTemplate["end"] = "BEGIN";
	var originalText = document.getElementById("oriText").value;
	var textArray = originalText.split(" ");
	var changedText = "";
	for (i = 0; i < textArray.length; i++) {
		var oriWord = textArray[i];
		var word = antonymTemplate[oriWord];
		if (word != undefined) {
			changedText = changedText + word + " ";
		} else {	
			changedText = changedText + oriWord + " ";
		}
	}
	alert("The changed text is: " + changedText);
}
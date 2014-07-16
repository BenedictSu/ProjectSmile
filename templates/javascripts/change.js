function changeWords (template) {
	if(template == ""){
		alert("You have not selected a template.");
	} else if(template == "sad"){
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
	} else if(template == "simple") {
		var r1 = "ANGRY";
		var r2 = "SAD";
		var r3 = "HAPPY";
		var database = {};
		database["enraged"] = r1;
		database["annoyed"] = r1;
		database["irritated"] = r1;
		database["furious"] = r1;
		database["outraged"] = r1;
		database["fierce"] = r1;
		database["mad"] = r1;
		database["troubled"] = r1;
		database["melancholic"] = r2;
		database["depressed"] = r2;
		database["crestfallen"] = r2;
		database["sorrowful"] = r2;
		database["bitter"] = r2;
		database["heartbroken"] = r2;
		database["dejected"] = r2;
		database["gloomy"] = r2;
		database["mournful"] = r2;
		database["forlorn"] = r2;
		database["cheerful"] = r3;
		database["delighted"] = r3;
		database["excited"] = r3;
		database["joyful"] = r3;
		database["joyous"] = r3;
		database["glad"] = r3;
		database["blissful"] = r3;
		database["gleeful"] = r3;
		database["contented"] = r3;
		database["jolly"] = r3;
		database["ecstatic"] = r3;
		database["elated"] = r3;
		database["overjoyed"] = r3;
		var originalText = document.getElementById("oriText").value;
		var textArray = originalText.split(" ");
		var changedText = "";
		for (i = 0; i < textArray.length; i++) {
			var oriWord = textArray[i];
			var word = database[oriWord];
			if (word != undefined) {
				changedText = changedText + word + " ";
			} else {	
				changedText = changedText + oriWord + " ";
			}
		}
		alert("The changed text is: " + changedText);
	}
}

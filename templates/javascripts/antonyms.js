function antonymTemplate() {
	var data = {};
	data["sad"] = "happy";
	data["happy"]="sad";
	data["long"]="short";
	data["short"]="long";
	data["angry"]="calm";
	data["calm"]="angry";
	data["pretty"]="ugly";
	data["ugly"]="pretty";
	data["thin"]="fat";
	data["fat"]="thin";
	data["clever"]="stupid";
	data["stupid"]="clever";
	data["hot"]="cold";
	data["cold"]="hot";
	data["difficult"]="easy";
	data["easy"]="difficult";
	data["courteous"]="rude";
	data["rude"]="courteous";
	data["win"]="lose";
	data["lose"]="win";
	data["pass"]="fail";
	data["fail"]="pass";
	data["big"]="small";
	data["small"]="big";
	data["expensive"]="cheap";
	data["cheap"]="expensive"
	data["slow"]="fast";
	data["fast"]="slow";
	data["deep"]="shallow";
	data["shallow"]="deep";
	data["here"]="there";
	data["there"]="here";
	data["high"]="low";
	data["low"]="high";
	data["old"]="young";
	data["young"]="old";
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

function changeWords (template) {
	var templateTable = {};
	templateTable[0] = function () {noTemplate();};
	templateTable[1] = function () {sadTemplate();};
	templateTable[2] = function () {simpleTemplate();};
	templateTable[template]();
}

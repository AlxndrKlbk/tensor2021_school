function sortNumberArray(arr){
	let result = arr.sort(function(a, b) {
  		return a - b;
		  });
	alert(result);
	return result;
}
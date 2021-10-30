function task21(arr){
	arr = addIsoDate(arr);
	let resArr = [];
	let val_keys;
	arr.map(function(wordbook){
		if(resArr.hasOwnProperty(wordbook['date'])){
			resArr[wordbook['date']] += wordbook['amount'];
		} else{
			resArr[wordbook['date']] = wordbook['amount']
		}
	});
	resArr = Object.fromEntries(Object.entries(resArr).map(([key,value])=>[value,key]));
	val_keys = Object.keys(resArr);
	val_keys = val_keys.map(Number);
	val_keys.sort(function(a, b) {
  		return a - b;
		  });
	val_keys.reverse();
	val_keys = val_keys.slice(0, 3);
	alert(val_keys);
	return findInObj(resArr, val_keys)
	//return resArr[val_keys.slice(0, 3)];
	}

function findInObj(wordbook, keys){
	let result = [];
	keys.map(function(val){
		result.push(wordbook[val])
	});
	return	result
}

function addIsoDate(arr){
	let resArr = [];
	arr.map(function(wordbook){
			isoStr = wordbook["year"] + "-" + wordbook["month"] + "-" + wordbook["day"];
			resArr.push({
				'date': isoStr,
				'type':wordbook['type'],
				'amount': wordbook["amount"]
			});
	});
	return resArr
};


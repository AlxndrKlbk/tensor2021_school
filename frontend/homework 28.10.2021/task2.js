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
};

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

function task22(year, month, arr){

	let result = [];
	result['replenishment'] = 0;
	result['withdrawal'] = 0;

	arr = arr.filter(function(item){
		return item['year'] === year && item['month'] === month;
	});

	arr = addIsoDate(arr);

	let balance = arr.reduce(function(prevVal, operation){
		if (operation['type'] === 'payment' || operation['type'] === 'withdrawal'){
			result['withdrawal'] += operation['amount']
		}else {
			result['replenishment'] += operation['amount']
		};
		
		result['date'] = operation['date'];
	}, 0);
	
	result['withdrawalRate'] = result['withdrawal'] / result['replenishment'] 
	result['monthBalance'] = result['replenishment'] - result['withdrawal']

	if(result['withdrawalRate'] < 0.15){
		result['rank'] = 'Золотой';
	}else if (result['withdrawalRate'] < 0.3){
		result['rank'] = 'Серебрянный';
	}else{
		result['rank'] = 'Бронзовый';
	};

	return result
};

function task23(arr){

	let uniq_dates = [];

	arr.reduce(function(prevVal, item){
		k_date = item['year'] + '-' + item['month'];
		
		if(! uniq_dates.hasOwnProperty(k_date)){
			uniq_dates.push({'year': item['year'], 'month': item['month']})
		}
	});

	let result = [];

	uniq_dates.map(function(item, i){
		result.push(task22(item['yearh'], item['month'], arr))
		
		if (i > 0){
			result[i]['totalBalance'] = result[i-1]['totalBalance'] + result[i]['monthBalance']
		}else{
			result[i]['totalBalance'] = result[i]['monthBalance']
		};

	});

	return result
};
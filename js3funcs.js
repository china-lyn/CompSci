// Q1
function canDriveCar(user,car){
    if (user['age'] >= 18){
        return true;
    }
    else if (car['engineSze' < 1000]){
        return true;
    }
    else{
        return false;
    }
}

let user = {'name':'John Doe', 'age':21}
let car = {'engineSze':1200, 'name':'Manzda 3'}

console.log(canDriveCar(user, car));

// Q2
function areAllNumbersEven(n1,n2,n3,n4,n5){
    if (n1%2 == 0 && n2%2 == 0 && n3%2 == 0 && n4%2 == 0 && n5%2 == 0){
        return true;
    }
    else{
        return false;
    }
}

console.log(areAllNumbersEven(29,4,18,6,8));

// Q3
function getBiggestNumberInArrays(numbers1, numbers2){
    let num = 0;
    let numb = 0;
    for (let n = 0;n < numbers1.length; n++){
        if (numbers1[n] > num){
            num = numbers1[n];
        }
    }
    for (let x = 0;x < numbers2.length; x++){
        if (numbers2[x] > numb){
            numb = numbers2[x];
        }
    }
    if (num>numb){
        return num;
    }
    else{
        return numb;
    }
}

let numbers1 = [32,45,666,34,5,7];
let numbers2 = [222,3,77,54,21,44];
let maxnum = getBiggestNumberInArrays(numbers1, numbers2);
console.log('The maximum number is', maxnum);
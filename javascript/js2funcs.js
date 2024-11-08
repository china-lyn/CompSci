// Q1
function minutesToHours(mins){
    let hours = mins / 60;
    return hours;
}
let m = 120;
let ans = minutesToHours(m);
console.log(m, 'mins is', ans, 'hours');

// Q2
function averageOf4Numbers(n1, n2, n3, n4){
    let sum = n1 + n2 + n3 + n4;
    let avg = sum / 4;
    return avg;
}
let average = averageOf4Numbers(3,6,33,7);
console.log('The average is', average);

// Q3
function getGasolineAmount(kmtod, avglitres){
    let km = kmtod * 2;
    let consump = km / 100;
    let gas = consump * avglitres;
    return gas;
}
let gasneeded = getGasolineAmount(200,10);
console.log('Total amnt of gas needed for the entire round trip is',gasneeded);

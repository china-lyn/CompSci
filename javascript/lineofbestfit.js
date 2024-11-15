function Mean(values){
    sum = 0
    for (x in values){
        sum += values[x]
    }
    let mean = sum / values.length;
    return mean;
}
 
let pairs = [[8,3], [2,10], [11,3], [6,6], [5,8], [4,12], [12,1], [9,4], [6,9], [1,14]];
 
let xs = [];
let ys = [];
 
for (pos in pairs){ // this sorts the x's into a list of x's and same fro y's
    let pair = pairs[pos]
    console.log(pairs[pos]);
    xs.push(pair[0]);
    ys.push(pair[1]);
}
 
let xmean = Mean(xs);
let ymean = Mean(ys);
 
let numerator = 0;
let denom = 0;
 
for (x in xs){ // getting the brackets to multiply and add to find slope
    let xbrackets = xs[x] - xmean;
    let ybrackets = ys[x] - ymean;
    let multiplied = xbrackets * ybrackets;
    let squared = xbrackets ** 2;
    numerator += multiplied;
    denom += squared;
}
console.log(numerator);
let M = (numerator / denom).toFixed(1); // slope
//console.log(M);
let B = (ymean - (M * xmean)).toFixed(0); // y-intercept
//console.log(B);
 
console.log('y =', M+'x','+',B); // final equation
 
//for (pair in Object.entries(pairs)){
//    console.log(Object.entries(pairs))
//    xs.push(Object.entries(pairs[0]));
//    ys.push(Object.entries(pairs[1]));
//}
//console.log('xs= ', xs,'ys = ', ys, Mean(xs), Mean(ys));

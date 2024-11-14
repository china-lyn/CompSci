// Q1 a)
function standardDeviation(list){
    let sum = 0;
    let N = list.length;
    for (let num = 0;num < list.length; num++){
       sum += list[num] 
    }
    let mean = sum / N;
    let summation = 0;
    for (value in list){
        let brackets = (list[value] - mean) ** 2;
        summation += brackets;
    }
    let ans = Math.sqrt(summation / (N-1));
    console.log('Mean =', mean.toFixed(2));
    return ans;
}
 
let list1 = [20,21,19,22,21,20,19,20,21,20];
let list2 = [303,299,306,298,304,307,299,302,305,299,300];
let list3 = [15.3,14.9,15.1,15.2,14.8,14.7,15.1,14.8,15.0,15.0];
let list4 = [87, 89, 84, 88, 89, 87, 86, 87, 86, 87];
 
let lists = [list1, list2, list3, list4];
 
for (i in lists){
    let sd = standardDeviation(lists[i]);
    console.log('SD =', sd.toFixed(2));
    console.log();
}
 
 
//let list2 = [303,299,306,298,304,307,299,302,305,299,300];
//let m2, sd2 = standardDeviation(list2);
//console.log('b) Mean =', m2, 'SD =', sd2);
 
//let m3, sd3 = standardDeviation(list3);
//console.log('c) Mean =', m3, 'SD =', sd3);
 
//let m4, sd4 = standardDeviation(list4);
//console.log('d) Mean =', m4, 'SD =', sd4)

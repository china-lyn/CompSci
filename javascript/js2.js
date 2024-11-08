// Q1
for (let i = 0; i < 21; i = i + 1){
    console.log(i);
}

// Q2
for (let i = 3; i < 30; i = i + 2){
   console.log(i);
}

// Q3
for (let i = 12; i > -15; i = i - 2){
   console.log(i);
}

// Q4
for (let i = 50; i > 20; i = i - 1){
   if (i%3 == 0){
       console.log(i);
   }
}

// Q5
let num = -3;
if (num > 0){
   console.log(num, 'is positive!');
}
else if (num < 0){
   console.log(num, 'is negative :(');
}

// Q6
let number = 6;
if (number%2 == 0){
   console.log(number, 'is even');
}
else{
   console.log(number, 'is odd');
}

// Q7
let n1 = 34;
let n2 = 29;
if (n1 > n2){
   console.log(n1, 'is greater than', n2);
}
else{
   console.log(n2, 'is greater than', n1);
}

// Q8
let ngrade = 10;
let agrade = '';
if (ngrade == 10){
   agrade = 'A';
}
else if (ngrade == 9){
   agrade = 'B';
}
else if (ngrade == 8){
   agrade = 'C';
}
else if (ngrade == 7){
   agrade = 'D';
}
else if (ngrade == 6){
   agrade = 'E';
}
else{
   agrade = 'F';
}
console.log(ngrade, 'is a', agrade);

// Q9
let age = 43;
let tprice = 0;
if (age < 13){
   tprice = 5;
}
else if (age < 19 && age > 12){
   tprice = 10;
}
else if (age < 61 && age > 18){
   tprice = 20;
}
else{
   tprice = 15;
}
console.log('Ticket price for age', age, 'is', tprice);

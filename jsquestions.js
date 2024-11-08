// Q1
let var1 = 2
let var2 = 12
let var3 = 33;
console.log(var1, var2, var3)
let Var1 = var1 + var2;
let Var2 = var2 + var3;
console.log(Var1, Var2, var3);
 
// Q2
let n = 7;
let num = n+1;
let numb =  n+2;
console.log(n, num, numb);
 
// Q3
let rad = 4;
let PI = 3.14
let area = PI * (rad**2)
console.log(area);
 
// Q4
let bse = 22
let h = 8;
let trianglearea = 0.5 / (bse*h)
console.log(trianglearea)
 
// Q5
let n1 = 2;
console.log(n1);
console.log(n1**2);
console.log(n1**3);
console.log(n1**4);
 
// Q6
let height = 100; // in cm
let foot = 2.54 * 12; // 2.54 cm in 1 inch and 12 inches in 1 foot
console.log(height / foot); 
let convert = (height / foot).toFixed(2); // rounds to 2 dec places
console.log(convert);

// Q7
let sphererad = 16
let volume = (4/3) * PI * (sphererad**3)
console.log(volume)
 
// Q8
let name = 'China';
let age = 18;
let years = 100 - age;
let result = years + 2024;
console.log('Hello', name, 'you will turn 100 in the year', result);
 
// Q9
let mass = 2;
let speedoflight = (3 * (10**8))**2;
let energy = mass * (speedoflight)**2;
console.log('Energy = ', energy)
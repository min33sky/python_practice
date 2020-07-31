let str1 = 'ab';
let str2 = 'basd';
let str3 = '';

console.log([str1, str2, str3].sort((a, b) => b.length - a.length));

let array = [1, 2, 3, 4, 5];

for (const [key, value] of array.entries()) {
  console.log(key, value);
}

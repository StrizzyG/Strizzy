// Din første JavaScript Kode
console.log('Hello, World!');

// Variabler
let name = 'John';
const age = 30;
var isStudent = true;

console.log(name, age, isStudent);

// Ændre HTML Indhold
function changeText() {
    document.getElementById('demo').innerHTML = 'Teksten er ændret!';
}

// Event Listeners
document.getElementById('myButton').addEventListener('click', function() {
    alert('Button clicked!');
});

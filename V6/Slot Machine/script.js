spin = document.querySelector('.spin');
autoSpin = document.querySelector('.auto-spin');

moneySpent = document.querySelector('.money-spent');
moneyEarned = document.querySelector('.money-earned');

a = document.querySelector('.a');
b = document.querySelector('.b');
c = document.querySelector('.c');

spin.addEventListener("click", function() {
  spinSlot();
});
autoSpin.addEventListener("click", function() {
  
});

symbols = ['🍒','💎','🔔','🍉','⭐','🍇','7️⃣','🥇','🥈','🥉']

function spinSlot() {
  for (let i = 0; i < 10; i++) {
    setTimeout(function() {
      let s1 = symbols[Math.floor(Math.random() * symbols.length)];
      let s2 = symbols[Math.floor(Math.random() * symbols.length)];
      let s3 = symbols[Math.floor(Math.random() * symbols.length)];

      a.innerText = s1
      b.innerText = s2
      c.innerText = s3
    }, 100 * i)
  }
}
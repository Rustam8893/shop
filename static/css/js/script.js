document.querySelectorAll('.glass-card').forEach(card => {
    card.addEventListener('mousemove', (e) => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;

        // Blob (shaffof nuqta) sichqoncha bilan birga harakatlanishi uchun
        const blob = card.querySelector('.liquid-blob');
        blob.style.transform = `translate(${x - 40}px, ${y - 40}px)`;
        blob.style.background = "rgba(0, 122, 255, 0.2)";
    });

    card.addEventListener('mouseleave', () => {
        const blob = card.querySelector('.liquid-blob');
        blob.style.transform = `translate(0, 0)`;
        blob.style.background = "rgba(0, 122, 255, 0.1)";
    });
});



// Counter (Sanoq) funksiyasi
const plus = document.querySelector(".plus");
const minus = document.querySelector(".minus");
const countInput = document.getElementById("product-count");

plus.addEventListener("click", () => {
    countInput.value = parseInt(countInput.value) + 1;
});

minus.addEventListener("click", () => {
    if (countInput.value > 1) {
        countInput.value = parseInt(countInput.value) - 1;
    }
});

// Tugma uchun Liquid Effect
const btn = document.querySelector(".buy-now-btn");
btn.addEventListener("click", function(e) {
    let x = e.clientX - e.target.offsetLeft;
    let y = e.clientY - e.target.offsetTop;
    
    let ripple = document.createElement("span");
    ripple.style.left = x + "px";
    ripple.style.top = y + "px";
    ripple.classList.add("ripple-effect"); // CSS-da ripple stili qo'shish kerak
    
    this.appendChild(ripple);
    
    setTimeout(() => {
        ripple.remove();
    }, 600);
});

// Sichqoncha harakatiga qarab blobni siljitish
document.addEventListener('mousemove', (e) => {
    const blob = document.querySelector('.liquid-bg-blob');
    const x = e.clientX / 50;
    const y = e.clientY / 50;
    blob.style.transform = `translate(${x}px, ${y}px)`;
});


document.addEventListener('DOMContentLoaded', () => {
    
    // 1. Home Page: Savatga qo'shish tugmasi effekti
    const addButtons = document.querySelectorAll('.add-btn');
    
    addButtons.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault(); // Sahifa yangilanib ketmasligi uchun
            
            // Tugmani vaqtincha o'zgartirish
            const originalIcon = btn.innerHTML;
            btn.style.background = '#4ade80'; // Yashil rang
            btn.innerHTML = '✓';
            
            // 1.5 sekunddan keyin qaytarish
            setTimeout(() => {
                btn.style.background = '#38bdf8';
                btn.innerHTML = originalIcon;
            }, 1500);
            
            // Bu yerda AJAX orqali savatga qo'shish funksiyasini yozishingiz mumkin
        });
    });

    // 2. Product Detail: Rasm uchun interaktiv effekt
    const productDetailImg = document.querySelector('.image-section img');
    if (productDetailImg) {
        productDetailImg.addEventListener('mouseover', () => {
            productDetailImg.style.transform = 'scale(1.1) rotate(2deg)';
        });
        
        productDetailImg.addEventListener('mouseout', () => {
            productDetailImg.style.transform = 'scale(1) rotate(0deg)';
        });
    }

    // 3. Scroll animatsiyasi (Kartalar paydo bo'lishi)
    const cards = document.querySelectorAll('.glass-card');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, { threshold: 0.1 });

    cards.forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'all 0.6s ease-out';
        observer.observe(card);
    });
});


document.addEventListener('DOMContentLoaded', function() {
    
    // 1. Miqdorni boshqarish (Plus/Minus)
    const qtyInput = document.getElementById('product-qty');
    const plusBtn = document.querySelector('.plus');
    const minusBtn = document.querySelector('.minus');

    if (qtyInput) {
        plusBtn.addEventListener('click', () => {
            let val = parseInt(qtyInput.value);
            if (val < qtyInput.max) qtyInput.value = val + 1;
        });

        minusBtn.addEventListener('click', () => {
            let val = parseInt(qtyInput.value);
            if (val > 1) qtyInput.value = val - 1;
        });
    }

    // 2. Rasmga Zoom effekti
    const mainImg = document.querySelector('.image-section img');
    if (mainImg) {
        mainImg.addEventListener('mousemove', (e) => {
            const { left, top, width, height } = mainImg.getBoundingClientRect();
            const x = ((e.pageX - left) / width) * 100;
            const y = ((e.pageY - top) / height) * 100;
            
            mainImg.style.transformOrigin = `${x}% ${y}%`;
            mainImg.style.transform = "scale(1.5)";
        });

        mainImg.addEventListener('mouseleave', () => {
            mainImg.style.transform = "scale(1)";
            mainImg.style.transformOrigin = "center center";
        });
    }

    // 3. Savatga qo'shish animatsiyasi
    const cartBtn = document.getElementById('add-to-cart-btn');
    if (cartBtn) {
        cartBtn.addEventListener('click', function() {
            this.innerHTML = '<span class="loader"></span> Yuklanmoqda...';
            this.style.opacity = '0.7';
            this.disabled = true;

            // Simulyatsiya (AJAX o'rniga)
            setTimeout(() => {
                this.innerHTML = 'Qo\'shildi ✓';
                this.style.backgroundColor = '#22c55e'; // Yashil rang
                this.style.opacity = '1';
                
                setTimeout(() => {
                    this.innerHTML = 'Savatga qo\'shish';
                    this.style.backgroundColor = ''; // Asl rangga qaytish
                    this.disabled = false;
                }, 2000);
            }, 8000);
        });
    }

    // 4. Sevimlilar (Heart) tugmasi
    const favBtn = document.getElementById('fav-btn');
    if (favBtn) {
        favBtn.addEventListener('click', function() {
            this.classList.toggle('active');
            if (this.classList.contains('active')) {
                this.innerHTML = '♥';
                this.style.color = '#ef4444';
                this.style.transform = 'scale(1.2)';
            } else {
                this.innerHTML = '♡';
                this.style.color = '';
                this.style.transform = 'scale(1)';
            }
        });
    }
});
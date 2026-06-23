// ---------- Data ----------
const products = [
  { name: "Halden Ceramic Vase", category: "Decor", price: 48, tag: "New", img: "images/product-vase.png" },
  { name: "Linen Throw Pillow", category: "Textiles", price: 36, tag: "Bestseller", img: "images/product-pillow.png" },
  { name: "Woven Seagrass Basket", category: "Storage", price: 54, tag: null, img: "images/product-basket.png" },
  { name: "Stoneware Mug, Set of 2", category: "Kitchen", price: 32, tag: "Limited", img: "images/product-mug.png" },
  { name: "Matte Bud Vase", category: "Decor", price: 28, tag: null, img: "images/product-vase.png" },
  { name: "Terracotta Cushion", category: "Textiles", price: 42, tag: "New", img: "images/product-pillow.png" },
  { name: "Rattan Storage Tray", category: "Storage", price: 38, tag: null, img: "images/product-basket.png" },
  { name: "Sage Stoneware Bowl", category: "Kitchen", price: 26, tag: "Bestseller", img: "images/product-mug.png" },
];

const PER_PAGE = 4;
let shown = 0;

const categories = [
  { name: "Living", count: "32 pieces", img: "images/category-living.png" },
  { name: "Kitchen", count: "48 pieces", img: "images/category-kitchen.png" },
  { name: "Decor", count: "26 pieces", img: "images/category-decor.png" },
];

// ---------- Render products ----------
const productGrid = document.getElementById("productGrid");
const loadMoreBtn = document.getElementById("loadMoreBtn");

function productCard(p) {
  return `
    <article class="product reveal">
      <div class="product__media">
        ${p.tag ? `<span class="product__tag">${p.tag}</span>` : ""}
        <img src="${p.img}" alt="${p.name}" loading="lazy" />
      </div>
      <div class="product__body">
        <span class="product__cat">${p.category}</span>
        <h3 class="product__name">${p.name}</h3>
        <div class="product__foot">
          <span class="product__price">$${p.price}</span>
          <button class="product__add" data-name="${p.name}">Add to cart</button>
        </div>
      </div>
    </article>`;
}

function renderMore() {
  const next = products.slice(shown, shown + PER_PAGE);
  next.forEach((p) => {
    productGrid.insertAdjacentHTML("beforeend", productCard(p));
    io.observe(productGrid.lastElementChild);
  });
  shown += next.length;
  if (shown >= products.length) {
    loadMoreBtn.textContent = "All products loaded";
    loadMoreBtn.disabled = true;
  }
}

loadMoreBtn.addEventListener("click", renderMore);

// ---------- Render categories ----------
const categoryGrid = document.getElementById("categoryGrid");
categoryGrid.innerHTML = categories
  .map(
    (c) => `
    <a href="#featured" class="category reveal">
      <img src="${c.img}" alt="${c.name} collection" loading="lazy" />
      <div class="category__body">
        <span class="category__count">${c.count}</span>
        <span class="category__name">${c.name}</span>
      </div>
    </a>`
  )
  .join("");

// ---------- Cart ----------
let cartCount = 0;
const cartCountEl = document.getElementById("cartCount");
const toast = document.getElementById("toast");
let toastTimer;

function showToast(message) {
  toast.textContent = message;
  toast.classList.add("show");
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => toast.classList.remove("show"), 2200);
}

productGrid.addEventListener("click", (e) => {
  const btn = e.target.closest(".product__add");
  if (!btn) return;
  cartCount += 1;
  cartCountEl.textContent = cartCount;
  showToast(`Added “${btn.dataset.name}” to your cart`);
});

document.getElementById("cartBtn").addEventListener("click", () => {
  showToast(cartCount === 0 ? "Your cart is empty" : `${cartCount} item${cartCount > 1 ? "s" : ""} in your cart`);
});

// ---------- Mobile menu ----------
const header = document.getElementById("header");
const menuBtn = document.getElementById("menuBtn");
const mobileNav = document.getElementById("mobileNav");

menuBtn.addEventListener("click", () => {
  const open = mobileNav.classList.toggle("open");
  header.classList.toggle("menu-open", open);
  menuBtn.setAttribute("aria-expanded", String(open));
});
mobileNav.querySelectorAll("a").forEach((a) =>
  a.addEventListener("click", () => {
    mobileNav.classList.remove("open");
    header.classList.remove("menu-open");
    menuBtn.setAttribute("aria-expanded", "false");
  })
);

// ---------- Header scroll state ----------
window.addEventListener("scroll", () => {
  header.classList.toggle("is-scrolled", window.scrollY > 8);
}, { passive: true });

// ---------- Newsletter ----------
const form = document.getElementById("newsletterForm");
const emailInput = document.getElementById("emailInput");
const note = document.getElementById("newsletterNote");

form.addEventListener("submit", (e) => {
  e.preventDefault();
  const value = emailInput.value.trim();
  const valid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
  if (!valid) {
    note.textContent = "Please enter a valid email address.";
    return;
  }
  note.textContent = "Thanks for subscribing — welcome to Atelier.";
  emailInput.value = "";
});

// ---------- Marquee: duplicate for seamless loop ----------
const track = document.getElementById("marqueeTrack");
track.innerHTML += track.innerHTML;

// ---------- Reveal on scroll ----------
const io = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("in");
        io.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.12 }
);
document.querySelectorAll(".reveal").forEach((el) => io.observe(el));

// ---------- Initial products (after io is defined) ----------
renderMore();

// ---------- Footer year ----------
document.getElementById("year").textContent = new Date().getFullYear();

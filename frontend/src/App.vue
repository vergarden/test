<script setup>
import { useRoute } from 'vue-router'

const route = useRoute()
const pages = [
  { key: 'intro', label: '自我介绍', icon: '01', path: '/intro' },
  { key: 'guestbook', label: '留言板', icon: '02', path: '/guestbook' },
  { key: 'contact', label: '联系方式', icon: '03', path: '/contact' },
]
</script>

<template>
  <div class="app-shell">
    <div class="top-band"></div>

    <header class="nav-header">
      <div class="nav-inner">
        <router-link to="/intro" class="site-brand" style="text-decoration:none;">
          <div class="brand-box">
            <span class="brand-letter">V</span>
          </div>
          <div>
            <h1 class="brand-title">类我空间</h1>
            <p class="brand-sub">VERGARDEN</p>
          </div>
        </router-link>
        <nav class="nav-links">
          <router-link
            v-for="p in pages"
            :key="p.key"
            :to="p.path"
            :class="['nav-btn', { active: route.path === p.path }]"
          >
            <span class="nav-num">{{ p.icon }}</span>
            <span class="nav-label">{{ p.label }}</span>
          </router-link>
        </nav>
      </div>
      <div class="nav-stripe-bar">
        <div class="stripe-seg red"></div>
        <div class="stripe-seg black"></div>
        <div class="stripe-seg yellow"></div>
        <div class="stripe-seg black"></div>
        <div class="stripe-seg red"></div>
      </div>
    </header>

    <main class="page-main">
      <router-view />
    </main>

    <footer class="page-footer">
      <div class="footer-stripe"></div>
      <div class="footer-inner">
        <div class="footer-brand">
          <span class="badge red" style="border-color:var(--black-3);">SINCE 2024</span>
        </div>
        <p class="footer-text">类我空间 &copy; VERGARDEN</p>
        <div class="footer-angles">
          <span class="angle-bracket">&lt;/&gt;</span>
        </div>
      </div>
    </footer>
  </div>
</template>

<style>
/* ====== Top Band ====== */
.top-band {
  height:6px;
  background:repeating-linear-gradient(
    90deg, var(--red) 0px, var(--red) 30px,
    var(--black) 30px, var(--black) 40px
  );
}

/* ====== Header ====== */
.nav-header {
  position:sticky; top:0; z-index:100;
  background:var(--white);
}

.nav-inner {
  max-width:1100px; margin:0 auto;
  padding:0.75rem 1.5rem;
  display:flex; justify-content:space-between; align-items:center;
  flex-wrap:wrap; gap:1rem;
}

.site-brand { display:flex; align-items:center; gap:0.75rem; cursor:pointer; }

.brand-box {
  width:48px; height:48px; background:var(--red);
  border:3px solid var(--black);
  display:flex; align-items:center; justify-content:center;
  transform:rotate(5deg); transition:transform 0.2s;
  position:relative;
}
.brand-box::after {
  content:""; position:absolute;
  top:-6px; left:-6px; width:100%; height:100%;
  border:1px solid var(--black); z-index:-1;
}
.site-brand:hover .brand-box { transform:rotate(0deg); }

.brand-letter { color:var(--white); font-size:1.75rem; font-weight:900; }
.brand-title { font-size:1.25rem; text-transform:uppercase; letter-spacing:0.08em; line-height:1; color:var(--black); }
.brand-sub { font-family:var(--mono); font-size:0.625rem; letter-spacing:0.15em; color:var(--red); text-transform:uppercase; }

.nav-links { display:flex; gap:0.5rem; }

.nav-btn {
  display:flex; align-items:center; gap:0.5rem;
  padding:0.6rem 1.2rem;
  border:2px solid var(--black);
  background:var(--white); color:var(--black);
  font-family:var(--sans); font-size:0.8125rem; font-weight:700;
  text-transform:uppercase; letter-spacing:0.04em;
  cursor:pointer; transition:all 0.12s;
  text-decoration:none;
  position:relative;
}
.nav-btn:hover { background:var(--cream); }
.nav-btn.active { background:var(--red); color:var(--white); border-color:var(--red-dark); }
.nav-btn.active::after {
  content:""; position:absolute;
  bottom:-8px; left:50%; transform:translateX(-50%);
  width:0; height:0;
  border-left:6px solid transparent;
  border-right:6px solid transparent;
  border-top:6px solid var(--red);
}
.nav-num { font-family:var(--mono); font-size:0.6875rem; opacity:0.7; }

.nav-stripe-bar { display:flex; height:6px; }
.stripe-seg { flex:1; }
.stripe-seg.red { background:var(--red); }
.stripe-seg.black { background:var(--black); }
.stripe-seg.yellow { background:var(--yellow); }

/* ====== Main ====== */
.page-main { flex:1; }

/* ====== Footer ====== */
.page-footer { margin-top:3rem; border-top:3px solid var(--black); }
.footer-stripe {
  height:4px;
  background:repeating-linear-gradient(
    90deg, var(--red) 0px, var(--red) 40px,
    var(--yellow) 40px, var(--yellow) 60px,
    var(--black) 60px, var(--black) 80px
  );
}
.footer-inner {
  max-width:1100px; margin:0 auto;
  padding:1.5rem;
  display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:1rem;
}
.footer-text { font-size:0.8125rem; color:var(--gray); font-family:var(--mono); letter-spacing:0.03em; }
.footer-angles { opacity:0.4; }

/* ====== Responsive ====== */
@media (max-width:640px) {
  .nav-inner { flex-direction:column; align-items:stretch; padding:0.5rem 0.75rem; }
  .site-brand { justify-content:center; }
  .nav-links { justify-content:center; }
  .nav-btn { flex:1; justify-content:center; padding:0.5rem 0.75rem; font-size:0.6875rem; }
  .nav-label { display:none; }
  .nav-num { display:inline; }
  .footer-inner { flex-direction:column; text-align:center; }
}
</style>



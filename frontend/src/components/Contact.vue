<template>
  <div class="contact page-container">
    <!-- ====== 构成主义装饰元素 ====== -->
    <!-- 大圆 -->
    <div class="circle-decor red" style="width:200px;height:200px;top:-50px;right:-60px;opacity:0.07;"></div>
    <div class="circle-decor outline" style="width:140px;height:140px;bottom:150px;right:30px;opacity:0.1;"></div>
    <div class="circle-decor black" style="width:60px;height:60px;top:200px;left:40px;opacity:0.06;"></div>
    <div class="circle-decor yellow" style="width:45px;height:45px;bottom:300px;left:20%;opacity:0.08;"></div>
    <div class="circle-decor red" style="width:25px;height:25px;top:450px;right:15%;opacity:0.12;"></div>

    <!-- 长方形 -->
    <div class="rect-decor black" style="width:20px;height:180px;bottom:100px;left:0;opacity:0.06;"></div>
    <div class="rect-decor red-outline" style="width:220px;height:120px;top:200px;left:-50px;opacity:0.07;"></div>
    <div class="rect-decor red" style="width:35px;height:100px;bottom:200px;right:5%;opacity:0.06;"></div>
    <div class="rect-decor outline" style="width:150px;height:80px;top:350px;right:0;opacity:0.08;"></div>

    <!-- 斜线条纹 -->
    <div class="diagonal-stripe" style="width:100%;height:14px;bottom:0;left:0;opacity:0.03;"></div>
    <div class="diagonal-stripe red" style="width:5px;height:180px;top:150px;right:12%;opacity:0.06;transform:skewY(-12deg);"></div>
    <div class="diagonal-stripe" style="width:4px;height:160px;bottom:100px;left:8%;opacity:0.05;transform:skewY(8deg);"></div>

    <!-- 网格叠层 -->
    <div class="grid-overlay"></div>

    <!-- Header -->
    <div class="section-block" style="text-align:center;overflow:hidden;">
      <div class="corner-accent tl"></div>
      <div class="corner-accent br"></div>
      <div class="circle-decor outline" style="width:35px;height:35px;top:1rem;right:1rem;opacity:0.06;"></div>

      <div class="badge red" style="margin-bottom:0.75rem;">CONTACT</div>
      <h1>联系我</h1>
      <div class="construct-divider" style="max-width:160px;margin:0.75rem auto;"></div>
      <p style="font-size:1.05rem;max-width:500px;margin:0 auto;color:var(--black-3);">
        如果你想和我说说话，这些是最快的方式。
      </p>
    </div>

    <!-- Contact cards -->
    <div class="contact-grid">
      <div class="section-block" style="margin-bottom:0;">
        <div class="corner-accent tl"></div>
        <div class="corner-accent br"></div>
        <!-- 内部装饰 -->
        <div class="rect-decor red" style="width:3px;height:50px;top:1.5rem;right:1rem;opacity:0.1;"></div>
        <div class="circle-decor black" style="width:15px;height:15px;bottom:1rem;left:1rem;opacity:0.06;"></div>

        <div class="ct-icon"><span class="badge red" style="font-size:1rem;">@</span></div>
        <div style="display:flex;justify-content:space-between;align-items:flex-start;">
          <h3>电子邮箱</h3>
          <span class="angle-bracket" style="font-size:0.9rem;opacity:0.4;">[ MAIL ]</span>
        </div>
        <p style="font-family:var(--mono);font-size:0.9375rem;word-break:break-all;padding:0.75rem 0;border-top:2px solid var(--black);border-bottom:2px solid var(--black);margin:0.75rem 0;">
          asdfghjkl2008311<span style="color:var(--red);font-weight:700;">@</span>163.com
        </p>
        <div style="display:flex;gap:0.5rem;align-items:center;">
          <span class="badge outline" style="border-color:var(--red);color:var(--red);font-size:0.625rem;">PREFERRED</span>
          <span style="font-size:0.75rem;color:var(--gray);">工作联系优先使用邮件</span>
        </div>
        <!-- 装饰点 -->
        <div style="margin-top:1rem;display:flex;gap:4px;">
          <div style="width:6px;height:6px;background:var(--red);"></div>
          <div style="width:6px;height:6px;background:var(--black);"></div>
        </div>
      </div>

      <div class="section-block" style="margin-bottom:0;">
        <div class="corner-accent tr"></div>
        <div class="corner-accent bl"></div>
        <!-- 内部装饰 -->
        <div class="rect-decor black" style="width:80%;height:2px;bottom:2rem;left:10%;opacity:0.04;"></div>
        <div class="circle-decor red" style="width:12px;height:12px;top:1rem;left:1rem;opacity:0.08;"></div>

        <div class="ct-icon"><span class="badge red" style="font-size:1rem;">S</span></div>
        <div style="display:flex;justify-content:space-between;align-items:flex-start;">
          <h3>社交平台</h3>
          <span class="angle-bracket" style="font-size:0.9rem;opacity:0.4;">[ SOCIAL ]</span>
        </div>
        <div class="soc-item">
          <div class="soc-icon-box">S</div>
          <div>
            <strong style="font-size:0.875rem;">Steam</strong>
            <a :href="steamUrl" target="_blank" class="soc-link">{{ steamUrl }}</a>
          </div>
          <span class="badge outline" style="border-color:var(--red);color:var(--red);font-size:0.625rem;margin-left:auto;">ONLINE</span>
        </div>
      </div>
    </div>

    <div class="construct-divider"></div>

    <!-- Mail form -->
    <div class="section-block offset-right">
      <div class="corner-accent tr"></div>
      <div class="corner-accent bl"></div>
      <!-- 内部装饰 -->
      <div class="circle-decor outline" style="width:40px;height:40px;bottom:1rem;right:1rem;opacity:0.06;"></div>
      <div class="rect-decor red" style="width:4px;height:30px;top:1rem;left:1rem;opacity:0.1;"></div>

      <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;">
        <h2 style="margin-bottom:1rem;">发送邮件</h2>
        <span class="angle-bracket" style="font-size:1.2rem;">[ SEND ]</span>
      </div>
      <form @submit.prevent="sendMail">
        <div class="form-row-2">
          <div class="form-group">
            <label style="display:block;font-weight:700;font-size:0.8125rem;text-transform:uppercase;letter-spacing:0.05em;margin-bottom:0.4rem;font-family:var(--mono);">你的名字</label>
            <input v-model="mailForm.name" class="input-construct" placeholder="称呼" required />
          </div>
          <div class="form-group">
            <label style="display:block;font-weight:700;font-size:0.8125rem;text-transform:uppercase;letter-spacing:0.05em;margin-bottom:0.4rem;font-family:var(--mono);">你的邮箱</label>
            <input v-model="mailForm.email" class="input-construct" type="email" placeholder="you@example.com" required />
          </div>
        </div>
        <div class="form-group" style="margin-bottom:1rem;">
          <label style="display:block;font-weight:700;font-size:0.8125rem;text-transform:uppercase;letter-spacing:0.05em;margin-bottom:0.4rem;font-family:var(--mono);">主题</label>
          <input v-model="mailForm.subject" class="input-construct" placeholder="邮件主题" />
        </div>
        <div class="form-group" style="margin-bottom:1rem;">
          <label style="display:block;font-weight:700;font-size:0.8125rem;text-transform:uppercase;letter-spacing:0.05em;margin-bottom:0.4rem;font-family:var(--mono);">内容</label>
          <textarea v-model="mailForm.body" class="input-construct" placeholder="说点什么……" required style="min-height:120px;"></textarea>
        </div>
        <button type="submit" class="btn-construct"><span>&#8594;</span> 发送</button>
      </form>
      <p v-if="mailSent" style="margin-top:1rem;padding:0.75rem;background:var(--black);color:var(--white);font-family:var(--mono);font-size:0.875rem;border-left:4px solid var(--yellow);">
        [系统] 消息已提交！（数据已保存到数据库）
      </p>
    </div>

    <!-- Footer note -->
    <div class="section-block" style="background:var(--black);text-align:center;overflow:hidden;">
      <div class="grid-overlay" style="opacity:0.06;background-image:linear-gradient(rgba(255,255,255,0.05) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,0.05) 1px,transparent 1px);"></div>
      <div class="circle-decor outline" style="width:80px;height:80px;top:-20px;right:-20px;z-index:-1;border-color:rgba(255,255,255,0.05);"></div>
      <div class="rect-decor red" style="width:50px;height:50px;bottom:-15px;left:-15px;z-index:-1;opacity:0.08;transform:rotate(45deg);"></div>
      <p style="color:var(--white);font-family:var(--mono);font-size:0.8125rem;letter-spacing:0.05em;">
        &copy; 2024-2026 VERGARDEN &mdash; 构成之美，就在最简洁的形式中。
      </p>
      <div style="margin-top:0.75rem;display:flex;justify-content:center;gap:0.5rem;">
        <span class="badge outline" style="border-color:var(--gray);color:var(--gray);font-size:0.625rem;">CONSTRUCTIVISM</span>
        <span class="badge outline" style="border-color:var(--gray);color:var(--gray);font-size:0.625rem;">MINIMAL</span>
      </div>
      <!-- 底部装饰方块 -->
      <div style="margin-top:1.25rem;display:flex;justify-content:center;gap:6px;">
        <div style="width:8px;height:8px;background:var(--red);transform:rotate(45deg);"></div>
        <div style="width:8px;height:8px;background:var(--yellow);transform:rotate(45deg);"></div>
        <div style="width:8px;height:8px;background:var(--white);transform:rotate(45deg);opacity:0.3;"></div>
      </div>
    </div>

    <!-- 底部装饰条 -->
    <div style="margin-top:1.5rem;display:flex;gap:4px;justify-content:center;">
      <div style="width:20px;height:4px;background:var(--red);"></div>
      <div style="width:20px;height:4px;background:var(--black);"></div>
      <div style="width:20px;height:4px;background:var(--yellow);"></div>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'

const steamUrl = 'https://steamcommunity.com/id/vergarden/'

const mailForm = reactive({ name: '', email: '', subject: '', body: '' })
const mailSent = ref(false)

async function sendMail() {
  if (!mailForm.name || !mailForm.email || !mailForm.body) return
  const res = await fetch('/api/emailsending/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      name: mailForm.name,
      email: mailForm.email,
      subject: mailForm.subject,
      body: mailForm.body,
    }),
  })
  if (res.ok) {
    mailSent.value = true
    mailForm.name = ''; mailForm.email = ''; mailForm.subject = ''; mailForm.body = ''
    setTimeout(() => { mailSent.value = false }, 5000)
  }
}
</script>

<style scoped>
.contact-grid {
  display:grid; grid-template-columns:1fr 1fr; gap:1.5rem;
}
.ct-icon { margin-bottom:0.75rem; }
.soc-item {
  display:flex; align-items:center; gap:0.75rem;
  padding:0.5rem 0;
  border-bottom:1px solid var(--gray-light);
}
.soc-item:last-child { border-bottom:none; }
.soc-icon-box {
  width:32px; height:32px; flex-shrink:0;
  background:var(--black); color:var(--white);
  display:flex; align-items:center; justify-content:center;
  font-weight:900; font-size:0.875rem;
}
.soc-link {
  font-size:0.75rem; color:var(--gray);
  font-family:var(--mono);
  word-break:break-all;
  text-decoration:none;
  border-bottom:1px dashed var(--gray-light);
  transition:color 0.15s;
}
.soc-link:hover { color:var(--red); border-bottom-color:var(--red); }
.form-row-2 { display:grid; grid-template-columns:1fr 1fr; gap:1rem; }
.form-group { margin-bottom:1rem; }
@media (max-width:768px) {
  .contact-grid { grid-template-columns:1fr; }
  .form-row-2 { grid-template-columns:1fr; }
}
</style>



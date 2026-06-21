<template>
  <div class="guestbook page-container">
    <div class="circle-decor red" style="width:200px;height:200px;top:-40px;right:-60px;opacity:0.08;"></div>
    <div class="circle-decor outline" style="width:140px;height:140px;bottom:120px;right:40px;opacity:0.1;"></div>
    <div class="circle-decor black" style="width:70px;height:70px;top:160px;left:50px;opacity:0.06;"></div>
    <div class="circle-decor yellow" style="width:40px;height:40px;bottom:250px;left:15%;opacity:0.08;"></div>
    <div class="rect-decor outline" style="width:280px;height:180px;top:80px;right:-30px;opacity:0.08;"></div>
    <div class="rect-decor black" style="width:15px;height:160px;bottom:150px;right:5%;opacity:0.06;"></div>
    <div class="diagonal-stripe red" style="width:100%;height:12px;top:0;left:0;opacity:0.04;"></div>
    <div class="grid-overlay"></div>

    <div class="section-block" style="text-align:center;overflow:hidden;">
      <div class="corner-accent tl"></div>
      <div class="corner-accent br"></div>
      <div class="badge red" style="margin-bottom:0.75rem;">GUESTBOOK</div>
      <h1 class="gb-title">留下你的足迹</h1>
      <div class="construct-divider" style="max-width:200px;margin:0.75rem auto;"></div>
      <p class="gb-sub">如果你有什么想说的，欢迎在这里留言。</p>
    </div>

    <div class="section-block offset-right">
      <div class="corner-accent tr"></div>
      <div class="corner-accent bl"></div>
      <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;">
        <h2 style="margin-bottom:1rem;">写留言</h2>
        <span class="angle-bracket" style="font-size:1.2rem;">[ NEW ]</span>
      </div>
      <form @submit.prevent="submitMsg">
        <div style="display:flex;gap:1rem;flex-wrap:wrap;">
          <div style="flex:1;min-width:200px;">
            <label style="display:block;font-weight:700;font-size:0.8125rem;text-transform:uppercase;letter-spacing:0.05em;margin-bottom:0.4rem;font-family:var(--mono);">昵称</label>
            <input v-model="form.name" class="input-construct" placeholder="你的名字" required />
          </div>
          <div style="flex:2;min-width:300px;">
            <label style="display:block;font-weight:700;font-size:0.8125rem;text-transform:uppercase;letter-spacing:0.05em;margin-bottom:0.4rem;font-family:var(--mono);">留言</label>
            <textarea v-model="form.message" class="input-construct" placeholder="说点什么……" required></textarea>
          </div>
        </div>
        <button type="submit" class="btn-construct" style="margin-top:1rem;"><span>&#8594;</span> 发送留言</button>
      </form>
    </div>

    <div class="construct-divider"></div>

    <div class="section-block">
      <div class="corner-accent tl"></div>
      <div class="corner-accent br"></div>
      <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;">
        <h2 style="margin-bottom:0;">留言展示</h2>
        <div style="display:flex;gap:0.5rem;align-items:center;">
          <span class="badge black">{{ messages.length }} / {{ totalCount }} 条</span>
          <button @click="refreshMessages" class="btn-construct" style="padding:0.3rem 0.75rem;font-size:0.75rem;" :disabled="refreshing">
            <span style="display:inline-block;" :class="{ spinning: refreshing }">&#8635;</span> 刷新
          </button>
          <span class="angle-bracket" style="font-size:1rem;opacity:0.4;">[ LIST ]</span>
        </div>
      </div>

      <div v-if="messages.length === 0" style="text-align:center;padding:3rem;color:var(--gray);font-family:var(--mono);">
        <div style="font-size:2.5rem;font-weight:900;color:var(--gray-light);margin-bottom:0.5rem;">. . .</div>
        暂无留言。
      </div>

      <div v-for="(msg, i) in messages" :key="i" class="msg-item">
        <div style="position:relative;">
          <div class="msg-avatar">{{ msg.nickname.charAt(0) }}</div>
          <div class="circle-decor red" style="width:52px;height:52px;top:-4px;left:-4px;opacity:0.1;z-index:0;"></div>
        </div>
        <div style="flex:1;">
          <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;">
            <div style="display:flex;align-items:center;gap:0.5rem;">
              <strong>{{ msg.nickname }}</strong>
              <span class="badge outline" style="font-size:0.625rem;border-width:1px;padding:0.125rem 0.5rem;border-color:var(--gray-light);color:var(--gray);">#{{ i + 1 }}</span>
            </div>
            <span class="msg-date">{{ msg.created_at ? msg.created_at.slice(0,10) : "" }}</span>
          </div>
          <p style="margin-top:0.3rem;">{{ msg.message }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue'

const form = reactive({ name: '', message: '' })
const messages = ref([])
const totalCount = ref(0)
const refreshing = ref(false)

onMounted(() => {
  fetchMessages()
  fetchTotalCount()
})

async function fetchMessages() {
  const res = await fetch("/api/boardsaying/")
  if (res.ok) messages.value = await res.json()
}

async function fetchTotalCount() {
  const res = await fetch("/api/boardsaying/count/")
  if (res.ok) {
    const data = await res.json()
    totalCount.value = data.count
  }
}

async function refreshMessages() {
  refreshing.value = true
  await fetchMessages()
  refreshing.value = false
}

async function submitMsg() {
  if (!form.name.trim() || !form.message.trim()) return
  const res = await fetch("/api/boardsaying/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ nickname: form.name, message: form.message }),
  })
  if (res.ok) {
    form.name = ""
    form.message = ""
    await fetchMessages()
    await fetchTotalCount()
  }
}
</script>

<style scoped>
.gb-title { font-size:clamp(2rem,5vw,3.5rem); margin-bottom:0.25rem; }
.gb-sub { font-size:1.05rem; max-width:500px; margin:0 auto; color:var(--black-3); }
.msg-item { padding:1.25rem 0; border-bottom:2px solid var(--black); display:flex; gap:1rem; align-items:flex-start; }
.msg-item:last-child { border-bottom:none; }
.msg-avatar { width:44px; height:44px; flex-shrink:0; background:var(--red); color:var(--white); display:flex; align-items:center; justify-content:center; font-weight:900; font-size:1.125rem; border:2px solid var(--black); position:relative; z-index:1; }
.msg-date { font-size:0.75rem; color:var(--gray); font-family:var(--mono); }
.spinning { animation: spin 0.8s linear infinite; }
@keyframes spin { from { transform:rotate(0deg); } to { transform:rotate(360deg); } }
</style>
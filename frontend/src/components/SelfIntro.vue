

<template>
  <div class="self-intro page-container">
    <!-- ====== 构成主义装饰元素 ====== -->
    <!-- 大圆 -->
    <div class="circle-decor red" style="width:260px;height:260px;top:-60px;right:-80px;opacity:0.08;"></div>
    <div class="circle-decor black" style="width:160px;height:160px;top:180px;right:60px;opacity:0.06;"></div>
    <div class="circle-decor outline" style="width:120px;height:120px;bottom:200px;right:20px;opacity:0.12;"></div>
    <div class="circle-decor red" style="width:80px;height:80px;bottom:100px;left:30px;opacity:0.1;"></div>
    <div class="circle-decor black" style="width:40px;height:40px;top:120px;left:40px;opacity:0.08;"></div>
    <div class="circle-decor yellow" style="width:50px;height:50px;top:350px;left:10%;opacity:0.1;"></div>

    <!-- 长方形 -->
    <div class="rect-decor red" style="width:30px;height:200px;top:250px;right:0;opacity:0.08;"></div>
    <div class="rect-decor black" style="width:20px;height:120px;top:400px;left:0;opacity:0.07;"></div>
    <div class="rect-decor outline" style="width:180px;height:100px;bottom:50px;right:10%;opacity:0.1;"></div>
    <div class="rect-decor red-outline" style="width:100px;height:100px;top:500px;left:5%;opacity:0.08;"></div>
    <div class="rect-decor black" style="width:50%;height:4px;top:50%;left:25%;opacity:0.04;transform:rotate(-3deg);"></div>

    <!-- 斜线条纹 -->
    <div class="diagonal-stripe" style="width:100%;height:20px;top:0;left:0;opacity:0.04;"></div>
    <div class="diagonal-stripe red" style="width:8px;height:300px;bottom:100px;right:15%;opacity:0.08;transform:skewY(-15deg);"></div>
    <div class="diagonal-stripe" style="width:6px;height:250px;top:200px;left:8%;opacity:0.06;transform:skewY(10deg);"></div>

    <!-- 网格叠层 -->
    <div class="grid-overlay"></div>

    <!-- Hero -->
    <div class="intro-hero section-block">
      <div class="corner-accent tl"></div>
      <div class="corner-accent br"></div>
      <div class="avatar-wrap">
        <div class="avatar-box">
          <span>V</span>
          <div class="circle-decor red-outline" style="width:180px;height:180px;top:-14px;left:-14px;"></div>
        </div>
        <div class="badge yellow" style="position:absolute;bottom:-12px;right:-12px;">SINCE 2024</div>
        <div class="photo-frame" style="width:60px;height:60px;position:absolute;top:20px;right:-20px;display:flex;align-items:center;justify-content:center;background:var(--yellow);font-weight:900;font-size:1.5rem;color:var(--black);transform:rotate(12deg);">
          AI
        </div>
        <!-- 额外装饰 -->
        <div class="rect-decor red" style="width:40px;height:40px;bottom:0;left:-30px;opacity:0.2;transform:rotate(45deg);"></div>
      </div>
      <div class="hero-text">
        <div class="badge red" style="margin-bottom:1rem;">1！5！</div>
        <h1>VERGARDEN</h1>
        <p class="hero-tags">/ AI Overdoser / 全职幻想家 / 现居幻想乡 /</p>
        <p class="hero-desc">我不擅长精通什么，但擅长让别人以为我精通什么。</p>
        
      </div>
    </div>

    <div class="diagonal-cut"></div>

    <!-- About -->
    <div class="section-block offset-right">
      <div class="corner-accent tr"></div>
      <div class="corner-accent bl"></div>
      <!-- 内部装饰 -->
      <div class="circle-decor outline" style="width:60px;height:60px;bottom:20px;right:20px;opacity:0.08;"></div>
      <div class="rect-decor black" style="width:80%;height:2px;top:3.5rem;left:10%;opacity:0.05;"></div>

      <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;">
        <h2>关于我</h2>
        <span class="angle-bracket" style="font-size:1.2rem;opacity:0.5;">[ ABOUT ]</span>
      </div>
      <div class="about-grid">
        <div>
          <p>Vergarden，现居幻想乡。AI Overdoser，一个只会使用新质生产力的飞舞。作为全职幻想家，职业内容是在脑子里跑项目——从不开工，从不延期。</p>
          <p style="margin-top:1rem;">每天都会拷打AI ，问一些我自己也答不上来的问题，然后假装那是在"探索技术边界"。擅长把简单的事搞复杂，再把复杂的搞砸，最后甩锅给 prompt 没写对。</p>
          <p style="margin-top:1rem;">信奉"只要别人认为我懂了，那我就懂了"的唯心信条。履历上写满了还没开始做的项目，自我介绍里充满了还没学会的技能——但你说的时候要自信。</p>
        </div>
        <div class="skills-col">
          <!-- 竖线装饰 -->
          <div class="rect-decor red" style="width:4px;height:30px;top:-8px;left:-3px;opacity:0.3;"></div>
          <div class="badge red" style="margin-bottom:1rem;">SKILLS</div>
          <div style="display:flex;flex-wrap:wrap;gap:0.5rem;margin-bottom:1.5rem;">
            <span class="badge black">摆烂</span>
            <span class="badge black">帮倒忙</span>
            <span class="badge black">糊弄别人</span>
            <span class="badge black" style="opacity:0.6;">（真的很擅长）</span>
          </div>
          <div class="badge red" style="margin-bottom:1rem;">INTERESTS</div>
          <div style="display:flex;flex-wrap:wrap;gap:0.5rem;">
            <span class="badge white">爽吃</span>
            <span class="badge white">爽睡</span>
            <span class="badge white">爽玩卡拉彼丘</span>
          </div>
          <div style="margin-top:1.5rem;height:4px;background:repeating-linear-gradient(90deg,var(--black) 0px,var(--black) 20px,transparent 20px,transparent 30px);"></div>
          <!-- 底部装饰方块 -->
          <div style="margin-top:1rem;display:flex;gap:6px;">
            <div style="width:10px;height:10px;background:var(--red);"></div>
            <div style="width:10px;height:10px;background:var(--black);"></div>
            <div style="width:10px;height:10px;background:var(--yellow);"></div>
          </div>
        </div>
      </div>
    </div>

    <div class="construct-divider"></div>

    <!-- Philosophy -->
    <div class="section-block" style="background:var(--black);color:var(--white);overflow:hidden;">
      <div class="rect-decor red" style="width:80px;height:200%;top:-50%;right:-20px;transform:rotate(20deg);z-index:-1;"></div>
      <!-- 更多背景装饰 -->
      <div class="rect-decor red-outline" style="width:150px;height:150px;bottom:-40px;left:-30px;z-index:-1;border-color:rgba(255,255,255,0.06);"></div>
      <div class="circle-decor outline" style="width:200px;height:200px;top:-60px;right:-40px;z-index:-1;border-color:rgba(255,255,255,0.05);"></div>
      <div class="grid-overlay" style="opacity:0.08;background-image:linear-gradient(rgba(255,255,255,0.04) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,0.04) 1px,transparent 1px);"></div>

      <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;">
        <div class="badge yellow" style="margin-bottom:1rem;border-color:var(--white);">PHILOSOPHY</div>
        <span class="angle-bracket" style="color:var(--gray);font-size:1.2rem;">[ 核心理念 ]</span>
      </div>
      <blockquote class="phil-quote">"我不擅长精通什么，但擅长让别人以为我精通什么。"</blockquote>
      <p style="color:var(--cream);margin-top:0.75rem;font-size:0.9rem;font-family:var(--mono);letter-spacing:0.03em;">
        实力不是核心生产力，印象才是。你不需要真的会，只需要让别人觉得你会。
      </p>
      <div style="margin-top:1.5rem;display:flex;gap:1rem;flex-wrap:wrap;">
        <span class="badge outline" style="border-color:var(--white);color:var(--white);">FAKE IT</span>
        <span class="badge outline" style="border-color:var(--white);color:var(--white);">TILL YOU</span>
        <span class="badge outline" style="border-color:var(--white);color:var(--white);">MAKE IT</span>
      </div>
      <!-- 底部小方块装饰 -->
      <div style="margin-top:1.5rem;display:flex;gap:8px;">
        <div style="width:8px;height:8px;background:var(--red);transform:rotate(45deg);"></div>
        <div style="width:8px;height:8px;background:var(--yellow);transform:rotate(45deg);"></div>
        <div style="width:8px;height:8px;background:var(--white);transform:rotate(45deg);opacity:0.3;"></div>
      </div>
    </div>

    <!-- 底部装饰条 -->
    <div style="margin-top:2rem;display:flex;gap:6px;justify-content:center;">
      <div style="width:30px;height:6px;background:var(--red);"></div>
      <div style="width:30px;height:6px;background:var(--black);"></div>
      <div style="width:30px;height:6px;background:var(--yellow);"></div>
      <div style="width:30px;height:6px;background:var(--black);"></div>
      <div style="width:30px;height:6px;background:var(--red);"></div>
    </div>

    <div class="zigzag"></div>
  </div>
</template>



<script setup>
// clean
</script>

<style scoped>
.intro-hero { display:flex; gap:2.5rem; align-items:center; flex-wrap:wrap; overflow:hidden; }
.intro-hero h1 { font-size:clamp(2.8rem,7vw,5rem); letter-spacing:-0.04em; margin-bottom:0.25rem; }
.avatar-wrap { flex-shrink:0; position:relative; }
.avatar-box { width:160px; height:160px; border:4px solid var(--black); display:flex; align-items:center; justify-content:center; background:var(--red); color:var(--white); font-size:4rem; font-weight:900; position:relative; }
.hero-text { flex:1; min-width:240px; }
.hero-tags { font-family:var(--mono); font-size:1.125rem; color:var(--red); margin-bottom:1rem; letter-spacing:0.05em; }
.hero-desc { font-size:1.0625rem; max-width:540px; font-weight:600; }
.about-grid { display:grid; grid-template-columns:1fr 1fr; gap:2rem; }
.skills-col { border-left:3px solid var(--black); padding-left:2rem; position:relative; }
.phil-quote { font-size:1.25rem; font-style:italic; font-weight:700; padding:1rem 0; border-left:4px solid var(--red); padding-left:1.5rem; color:var(--white); }
@media (max-width:768px) {
  .intro-hero { flex-direction:column; text-align:center; }
  .about-grid { grid-template-columns:1fr; }
  .skills-col { border-left:none; padding-left:0; border-top:3px solid var(--black); padding-top:1.5rem; margin-top:1rem; }
}
</style>



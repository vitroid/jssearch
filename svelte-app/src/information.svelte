<script>
    import { project } from "./jscc71.svelte";

</script>
<div class="post">
    <h1 class="post-title">{project.title}</h1>
    <p class="intro">
        <a class="lk" href="http://jsccc71.com/top/" target="_blank">オンデマンド配信、発表および視聴方法に関する案内など</a>
    </p>
    <div class="intro">（錯体化学会の特設サイトに飛びます）</div>
    <div class="intro">
        <span class="zm">ZOOM</span>
        <span class="rm">REMO</span>ボタンでZoom(口頭発表)・Remo(ポスター)会場に入れます.
    </div>
    <div class="intro">Remo Reference Manual <a class="lk" href="http://www.sakutai.jp/cms/wp-content/uploads/2020/07/RemoManual_JP_20200804_v1_1.pdf" target="_blank">日本語</a> <a class="lk" href="http://www.sakutai.jp/cms/wp-content/uploads/2020/07/RemoManual_EN_20200804_v1_1.pdf" target="_blank">English</a></div>

    <p class="intro">懇親会・交流会</p>
    <div class="intro"><a class="rm" href="https://live.remo.co/e/71remo-1a">REMO1</a>オンライン懇親会 ⽇時：9⽉19⽇（日）18:00-</div>
</div>

<style>
    div.post {
  margin: 2px;
}
h1.post-title {
  padding: 10px;
  text-align: center;
  background-color: #fff;
}
p.intro {
  padding: 5px;
  text-align: center;
  font-size: 120%;
  font-weight: bold;
}
div.intro {
  text-align: center;
}
/*囲み=リンク*/
.zm{
  border-radius: 5px 5px 5px;
  border: 1px solid blue;
  color: blue;
  font-size: 90%;
  background-color: #cacaff;
  padding: 2px;
  text-decoration: none;
}

.rm{
  border-radius: 5px 5px 5px;
  border: 1px solid red;
  color: red;
  font-size: 90%;
  background-color: #ffcaca;
  padding: 2px;
  text-decoration: none;
}

</style>
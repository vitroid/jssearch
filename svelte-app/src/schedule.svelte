<script>
    import PosterTable from "./postertable.svelte";

    function range(a,b){
        let c = new Set();
        for(let i=a; i<=b; i++){
            c.add(i);
        }
        return c;
    }

    const poster1 = [ { label:"PA1-", items:range(1,74) },
                      { label:"PB1-", items:range(1,15) },
                      { label:"PC1-", items:range(1,16) },
                      { label:"PD1-", items:range(1,14) },
                      { label:"PE1-", items:range(1,10) },
                      { label:"PF1-", items:range(1,42) } ];

</script>
<div class="tabs">
    <input id="day1_tab" type="radio" name="tab_item" checked />
    <label class="tab_item" for="day1_tab">Sep. 16</label>
    <input id="day2_tab" type="radio" name="tab_item">
    <label class="tab_item" for="day2_tab">Sep. 17</label>
    <input id="day3_tab" type="radio" name="tab_item">
    <label class="tab_item" for="day3_tab">Sep. 18</label>
    <input id="day4_tab" type="radio" name="tab_item">
    <label class="tab_item" for="day4_tab">Sep. 19</label>
    <input id="ad_tab" type="radio" name="tab_item">
    <label class="tab_item" for="ad_tab">協賛企業</label>
    <div class="tab_content" id="day1_content">
        <div class="ttpanel" id=day1_panel>
            <PosterTable title={"test poster 1"} sessions={poster1} on:search />
        </div>
    </div>
    <div class="tab_content" id="day2_content"><div class="ttpanel" id=day2_panel></div></div>
    <div class="tab_content" id="day3_content"><div class="ttpanel" id=day3_panel></div></div>
    <div class="tab_content" id="day4_content"><div class="ttpanel" id=day4_panel></div></div>
    <div class="tab_content" id="ad_content"><div class="ttpanel" id=ad_panel></div>
    <div class="credit">jssearch build 33 Copyright (c) 2020 by Masakazu Matsumoto</div></div>
</div>


<style>
    /* tabs using CSS https://bagelee.com/design/css/create_tabs_using_only_css/ */

    /* using */
    /*タブ切り替え全体のスタイル*/
    div.tabs {
    margin-top: 50px;
    padding-bottom: 40px;
    background-color: #fff;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
    max-width: 700px;
    margin: 0 auto;
    }

    /* using */
    label.tab_item:hover {
    opacity: 0.75;
    }

    /*ラジオボタンを全て消す*/
    /* using */
    input[name="tab_item"] {
    display: none;
    }

    /* using */
    /*タブ切り替えの中身のスタイル*/
    div.tab_content {
    display: none;
    padding: 10px 10px 0;
    clear: both;
    overflow: hidden;
    }



    /*選択されているタブのスタイルを変える*/
    div.tabs input:checked + .tab_item {
    background-color: #5ab4bd;
    color: #fff;
    }

    /* using */
    div.ttpanel {
        display: flex;
        flex-wrap: wrap;
    }

    div.credit {
        font-size: 80%;
        color: #888;
        text-align: center;
    }


    /* https://allabout.co.jp/gm/gc/459917/3/ */
/*タブのスタイル*/
.tab_item {
  width: calc(100%/5); /* 5 tabs 2021 */
  height: 50px;
  border-bottom: 3px solid #5ab4bd;
  background-color: #d9d9d9;
  line-height: 50px;
  font-size: 16px;
  text-align: center;
  color: #565656;
  display: block;
  float: left;
  text-align: center;
  font-weight: bold;
  transition: all 0.2s ease;
}

/*選択されているタブのコンテンツのみを表示*/
#day1_tab:checked ~ #day1_content,
#day2_tab:checked ~ #day2_content,
#day3_tab:checked ~ #day3_content,
#day4_tab:checked ~ #day4_content,
#ad_tab:checked ~ #ad_content {
  display: block;
}

</style>
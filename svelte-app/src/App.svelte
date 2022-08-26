<script>
	// import { data } from "./index.svelte";
	// import { bin1, bin2, sc } from "./jscc71.svelte";
	import SearchBox from "./searchbox.svelte";
	// import Information from "./information.svelte";
	import Schedule from "./schedule.svelte";
	import ShortCuts from "./shortcuts.svelte";

	let search = "";
    function searchHandler(event){
		search = event.detail.text;
    }
</script>

<body>
	<div class="wrap">
		<!-- <Information /> -->

		<h2>要旨集検索</h2>
		<div class="search">
			<ShortCuts on:search={searchHandler} />
			<ul>
				<li>発表番号、題目、キーワード、研究場所、発表者名にて検索が可能です.</li>
				<li>正規表現が使えます.</li>
				<li>画像クリックでPDFが開きます.</li>
				<li>表示は申込データに基づいており、表示のタイトルおよび著者の一部が要旨とは異なる場合があります.</li>
			</ul>

			<SearchBox search={search}/>
			<p>興味のある講演番号を押すと、下の表に青い印が付きます. 聴講スケジュールを決めるのにご活用下さい.</p>
		</div>
		<Schedule on:search={searchHandler} />
		<!-- tabs using CSS https://bagelee.com/design/css/create_tabs_using_only_css/ -->

		<!-- <script src="index.js"></script>
		<script src="ads.js"></script>
		<script src="zoom.js"></script>
		<script src="remo.js"></script>
		<script src="jscc71.js"></script>
		<script src="search.js"></script> -->
		<noscript>
			<p>注意: この検索機能は JavaScript を使用しています。</p>
		</noscript>

	</div>
</body>

<style>
	p {
		padding: 0px 5;
	}
	body{
		font-family: Helvetica, Ariel, sans-serif;
		font-size: 10pt;
	}
	div.wrap{
		max-width: 750px;
		background-color:#f0f0f0;
		margin: 0 auto;
	}
	h2 {
		padding: 10px;
		text-align: center;
		background-color: #fff;
	}
	div.search {
		margin: 10px;
	}
</style>

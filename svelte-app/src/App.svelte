<script>
    import { _ } from 'svelte-i18n';
    import LocaleSelector from './localeselector.svelte';
    import Schedule from "./schedule.svelte";
    import SearchBox from "./searchbox.svelte";
    import ShortCuts from "./shortcuts.svelte";

    // Set the current locale to en-US
    // locale.set('ja')
    // setupI18n({ withLocale: 'en' });

    let search = "";
    function searchHandler(event){
        search = event.detail.text;
    }


</script>

<body>
	<div class="wrap">
        <div class="banner">
            <div>
                <a href="http://www.sakuto72-kyudai.net" target="_blank" >
                    錯体化学会 第72回討論会
                </a>
            </div>
            <div class="right">
                <LocaleSelector />
            </div>
        </div>
		<h2>{$_("SEARCH")}</h2>
		<div class="search">
			<ShortCuts on:search={searchHandler} />
			<ul>
				<li>{$_("hint1")}</li>
				<li>{$_("hint2")}</li>
				<li>{$_("hint3")}</li>
				<li>{$_("hint4")}</li>
			</ul>

			<SearchBox search={search}/>
            <p>{$_("hint5")}</p>
		</div>
		<Schedule on:search={searchHandler} />
		<noscript>
			<p>{$_("usingjs")}</p>
		</noscript>

	</div>
</body>

<style>
    .banner {
        background-color: #4169E1;
        display: flex;
        justify-content: space-between;
        padding: 10px;
    }
	a {
		padding: 0px 5;
        font-size: 150%;
        color: white;
        text-decoration: none;
    }
    a:link, a:visited {
        color: white;
    }
    a:hover {
        opacity: 75%;
        transition-duration: 500ms;
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
        margin: 0;
		text-align: center;
		background-color: #fff;
	}
	div.search {
		margin: 10px;
	}
</style>

<script lang="ts">
    import { ads } from './ads.js';
</script>

<div class="wrap">
    <div class="container">
        {#each ads as ad, i}
        <div class="panel">
            <div class="pair">
                <a href={ad.pdf} target="_blank" ><img src={ad.tn} alt={ad.tn} /></a>
            </div>
            <div class="pair">
                {#each ad.sp as sp}
                <a href={sp.url} target="_blank">{sp.name}</a><br />
                {/each}
            </div>
        </div>
        {/each}
    </div>
</div>

<style>
    .wrap {
        margin: 5px auto 5px auto;

    }
    .container {
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
    }
    .panel {
        display: flex;
        flex-direction: column;
        margin: 5px;
        padding: 10px;
        border: 1px solid #888;
        background-color: white;
        border-radius: 10px;
    }
    .pair {
        text-align: center;
    }
</style>
